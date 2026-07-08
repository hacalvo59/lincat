// ============================================================================
// LINCAT Industrial Engine - Exportador STL
// Author: Hugo Alberto Calvo
// Component Type: EXPORT / STL
// Description:
//     Convierte resultados HF/MF/LF en un STL ASCII industrial.
//     Representación:
//         - Líneas → segmentos triangulados
//         - Arcos → segmentos triangulados
//         - Helicoidales → malla 3D triangulada
// ============================================================================

use serde_json::Value;

pub struct ExportadorSTL {
    pub nombre: String,
    pub grosor: f64,   // grosor del trazo en mm
}

impl ExportadorSTL {
    pub fn new(nombre: &str, grosor: f64) -> Self {
        Self {
            nombre: nombre.to_string(),
            grosor,
        }
    }

    /// Exporta una lista de resultados del motor a un STL ASCII.
    pub fn exportar(&self, resultados: &[Value]) -> String {
        let mut stl = String::new();

        stl.push_str(&format!("solid {}\n", self.nombre));

        for res in resultados {
            let modulo = res["modulo"].as_str().unwrap_or("");

            match modulo {
                "HF Lineal" => self.exportar_linea(res, &mut stl),
                "HF Arcos" => self.exportar_arco(res, &mut stl),
                "HF Helicoidal" => self.exportar_helice(res, &mut stl),
                _ => {}
            }
        }

        stl.push_str("endsolid\n");
        stl
    }

    // ============================================================
    // LÍNEA → 2 triángulos (rectángulo extruido)
    // ============================================================
    fn exportar_linea(&self, res: &Value, stl: &mut String) {
        let x0 = res["input"]["x0"].as_f64().unwrap_or(0.0);
        let y0 = res["input"]["y0"].as_f64().unwrap_or(0.0);
        let x1 = res["input"]["x1"].as_f64().unwrap_or(0.0);
        let y1 = res["input"]["y1"].as_f64().unwrap_or(0.0);

        let z = 0.0;
        let g = self.grosor;

        // Representación simple: rectángulo extruido en Z
        let p1 = (x0, y0, z);
        let p2 = (x1, y1, z);
        let p3 = (x1, y1, z + g);
        let p4 = (x0, y0, z + g);

        self.triangulo(stl, p1, p2, p3);
        self.triangulo(stl, p1, p3, p4);
    }

    // ============================================================
    // ARCO → discretización en segmentos triangulados
    // ============================================================
    fn exportar_arco(&self, res: &Value, stl: &mut String) {
        let cx = res["resultado"]["centro"]["cx"].as_f64().unwrap_or(0.0);
        let cy = res["resultado"]["centro"]["cy"].as_f64().unwrap_or(0.0);
        let radio = res["resultado"]["radio"].as_f64().unwrap_or(0.0);

        let ang_i = res["resultado"]["angulo_inicio"].as_f64().unwrap_or(0.0);
        let ang_f = res["resultado"]["angulo_fin"].as_f64().unwrap_or(0.0);

        let pasos = 32;
        let g = self.grosor;

        for i in 0..pasos {
            let t0 = ang_i + (ang_f - ang_i) * (i as f64 / pasos as f64);
            let t1 = ang_i + (ang_f - ang_i) * ((i + 1) as f64 / pasos as f64);

            let x0 = cx + radio * t0.cos();
            let y0 = cy + radio * t0.sin();
            let x1 = cx + radio * t1.cos();
            let y1 = cy + radio * t1.sin();

            let p1 = (x0, y0, 0.0);
            let p2 = (x1, y1, 0.0);
            let p3 = (x1, y1, g);
            let p4 = (x0, y0, g);

            self.triangulo(stl, p1, p2, p3);
            self.triangulo(stl, p1, p3, p4);
        }
    }

    // ============================================================
    // HELICE → polilínea 3D triangulada
    // ============================================================
    fn exportar_helice(&self, res: &Value, stl: &mut String) {
        let puntos = res["resultado"]["trayectoria"]
            .as_array()
            .unwrap_or(&vec![]);

        let g = self.grosor;

        for i in 0..(puntos.len().saturating_sub(1)) {
            let p0 = &puntos[i];
            let p1 = &puntos[i + 1];

            let x0 = p0["x"].as_f64().unwrap_or(0.0);
            let y0 = p0["y"].as_f64().unwrap_or(0.0);
            let z0 = p0["z"].as_f64().unwrap_or(0.0);

            let x1 = p1["x"].as_f64().unwrap_or(0.0);
            let y1 = p1["y"].as_f64().unwrap_or(0.0);
            let z1 = p1["z"].as_f64().unwrap_or(0.0);

            let p1a = (x0, y0, z0);
            let p2a = (x1, y1, z1);
            let p3a = (x1, y1, z1 + g);
            let p4a = (x0, y0, z0 + g);

            self.triangulo(stl, p1a, p2a, p3a);
            self.triangulo(stl, p1a, p3a, p4a);
        }
    }

    // ============================================================
    // TRIÁNGULO STL ASCII
    // ============================================================
    fn triangulo(
        &self,
        stl: &mut String,
        p1: (f64, f64, f64),
        p2: (f64, f64, f64),
        p3: (f64, f64, f64),
    ) {
        stl.push_str("  facet normal 0 0 0\n");
        stl.push_str("    outer loop\n");
        stl.push_str(&format!("      vertex {} {} {}\n", p1.0, p1.1, p1.2));
        stl.push_str(&format!("      vertex {} {} {}\n", p2.0, p2.1, p2.2));
        stl.push_str(&format!("      vertex {} {} {}\n", p3.0, p3.1, p3.2));
        stl.push_str("    endloop\n");
        stl.push_str("  endfacet\n");
    }
}
