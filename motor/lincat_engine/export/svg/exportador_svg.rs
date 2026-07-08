// ============================================================================
// LINCAT Industrial Engine - Exportador SVG
// Author: Hugo Alberto Calvo
// Component Type: EXPORT / SVG
// Description:
//     Convierte resultados HF/MF/LF en un SVG 2D industrial.
//     Soporta:
//         - LINE → <line>
//         - ARC  → <path> con A
//         - HELICE → <path> polilínea 2D (proyección XY)
// ============================================================================

use serde_json::Value;

pub struct ExportadorSVG {
    pub width: f64,
    pub height: f64,
    pub stroke_width: f64,
    pub stroke_color: String,
    pub background: String,
}

impl ExportadorSVG {
    pub fn new(width: f64, height: f64) -> Self {
        Self {
            width,
            height,
            stroke_width: 1.5,
            stroke_color: "#00FF88".to_string(),
            background: "#111111".to_string(),
        }
    }

    pub fn exportar(&self, resultados: &[Value]) -> String {
        let mut svg = String::new();

        svg.push_str(&format!(
            r#"<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <rect x="0" y="0" width="{w}" height="{h}" fill="{bg}" />
"#,
            w = self.width,
            h = self.height,
            bg = self.background
        ));

        for res in resultados {
            let modulo = res["modulo"].as_str().unwrap_or("");

            match modulo {
                "HF Lineal" => svg.push_str(&self.exportar_linea(res)),
                "HF Arcos" => svg.push_str(&self.exportar_arco(res)),
                "HF Helicoidal" => svg.push_str(&self.exportar_helice(res)),
                _ => {}
            }
        }

        svg.push_str("</svg>\n");
        svg
    }

    // LINE → <line>
    fn exportar_linea(&self, res: &Value) -> String {
        let x0 = res["input"]["x0"].as_f64().unwrap_or(0.0);
        let y0 = res["input"]["y0"].as_f64().unwrap_or(0.0);
        let x1 = res["input"]["x1"].as_f64().unwrap_or(0.0);
        let y1 = res["input"]["y1"].as_f64().unwrap_or(0.0);

        format!(
            r#"<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" />
"#,
            x0 = x0,
            y0 = self.height - y0,
            x1 = x1,
            y1 = self.height - y1,
            c = self.stroke_color,
            sw = self.stroke_width
        )
    }

    // ARC → <path d="M ... A ...">
    fn exportar_arco(&self, res: &Value) -> String {
        let cx = res["resultado"]["centro"]["cx"].as_f64().unwrap_or(0.0);
        let cy = res["resultado"]["centro"]["cy"].as_f64().unwrap_or(0.0);
        let radio = res["resultado"]["radio"].as_f64().unwrap_or(0.0);

        let ang_i = res["resultado"]["angulo_inicio"].as_f64().unwrap_or(0.0);
        let ang_f = res["resultado"]["angulo_fin"].as_f64().unwrap_or(0.0);

        let x0 = cx + radio * ang_i.cos();
        let y0 = cy + radio * ang_i.sin();
        let x1 = cx + radio * ang_f.cos();
        let y1 = cy + radio * ang_f.sin();

        let large_arc = if (ang_f - ang_i).abs() > std::f64::consts::PI { 1 } else { 0 };
        let sweep = if ang_f > ang_i { 1 } else { 0 };

        format!(
            r#"<path d="M {x0} {y0} A {r} {r} 0 {la} {sw} {x1} {y1}" fill="none" stroke="{c}" stroke-width="{swid}" />
"#,
            x0 = x0,
            y0 = self.height - y0,
            x1 = x1,
            y1 = self.height - y1,
            r = radio,
            la = large_arc,
            sw = sweep,
            c = self.stroke_color,
            swid = self.stroke_width
        )
    }

    // HELICE → polilínea 2D (proyección XY)
    fn exportar_helice(&self, res: &Value) -> String {
        let puntos = res["resultado"]["trayectoria"]
            .as_array()
            .unwrap_or(&vec![]);

        if puntos.is_empty() {
            return String::new();
        }

        let mut d = String::from("M ");

        for (i, p) in puntos.iter().enumerate() {
            let x = p["x"].as_f64().unwrap_or(0.0);
            let y = p["y"].as_f64().unwrap_or(0.0);

            if i == 0 {
                d.push_str(&format!("{x} {y}", x = x, y = self.height - y));
            } else {
                d.push_str(&format!(" L {x} {y}", x = x, y = self.height - y));
            }
        }

        format!(
            r#"<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" />
"#,
            d = d,
            c = self.stroke_color,
            sw = self.stroke_width
        )
    }
}
