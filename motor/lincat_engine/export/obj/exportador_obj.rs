// ============================================================================
// LINCAT Industrial Engine - Exportador OBJ
// Author: Hugo Alberto Calvo
// Component Type: EXPORT / OBJ
// Description:
//     Convierte resultados HF/MF/LF en un OBJ 3D industrial.
//     Representación:
//         - Líneas → barra 3D triangulada
//         - Arcos → discretización + barra 3D triangulada
//         - Helicoidales → polilínea 3D triangulada
// ============================================================================

use serde_json::Value;

pub struct ExportadorOBJ {
    pub nombre: String,
    pub grosor: f64,   // grosor del trazo en mm
}

impl ExportadorOBJ {
    pub fn new(nombre: &str, grosor: f64) -> Self {
        Self {
            nombre: nombre.to_string(),
            grosor,
        }
    }

    /// Exporta una lista de resultados del motor a un OBJ ASCII.
    pub fn exportar(&self, resultados: &[Value]) -> String {
        let mut obj = String::new();
        obj.push_str(&format!("# OBJ generado por LINCAT: {}\n", self.nombre));

        let mut vertices: Vec<(f64, f64, f64)> = Vec::new();
        let mut caras: Vec<(usize, usize, usize)> = Vec::new();

        for res in resultados {
            let modulo = res["modulo"].as_str().unwrap_or("");

            match modulo {
                "HF Lineal" => self.exportar_linea(res, &mut vertices, &mut caras),
                "HF Arcos" => self.exportar_arco(res, &mut vertices, &mut caras),
                "HF Helicoidal" => self.exportar_helice(res, &mut vertices, &mut caras),
                _ => {}
            }
        }

        // Escribir vértices
        for (x, y, z) in &vertices {
            obj.push_str(&format!("v {} {} {}\n", x, y, z));
        }

        // Escribir caras
        for (a, b, c) in &caras {
            obj.push_str(&format!("f {} {} {}\n", a, b, c));
        }

        obj
    }

    // ============================================================
    // LÍNEA → barra 3D triangulada
    // ============================================================
    fn exportar_linea(
        &self,
        res: &Value,
        vertices: &mut Vec<(f64, f64, f64)>,
        caras: &mut Vec<(usize, usize, usize)>
    ) {
        let x0 = res["input"]["x0"].as_f64().unwrap_or(0.0);
        let y0 = res["input"]["y0"].as_f64().unwrap_or(0.0);
        let x1 = res["input"]["x1"].as_f64().unwrap_or(0.0);
        let y1 = res["input"]["y1"].as_f64().unwrap_or(0.0);

        let g = self.grosor;

        let p1 = (x0, y0, 0.0);
        let p2 = (x1, y1, 0.0);
        let p3 = (x1, y1, g);
        let p4 = (x0, y0, g);

        let base = vertices.len() + 1;

        vertices.push(p1);
        vertices.push(p2);
        vertices.push(p3);
        vertices.push(p4);

        caras.push((base, base + 1, base + 2));
        caras.push((base, base + 2, base + 3));
    }

    // ============================================================
    // ARCO → discretización + barra 3D triangulada
    // ============================================================
    fn exportar_arco(
        &self,
        res: &Value,
        vertices: &mut Vec<(f64, f64, f64)>,
        caras: &mut Vec<(usize, usize, usize)>
    ) {
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

            let base = vertices.len() + 1;

            vertices.push(p1);
            vertices.push(p2);
            vertices.push(p3);
            vertices.push(p4);

            caras.push((base, base + 1, base + 2));
            caras.push((base, base + 2, base + 3));
        }
    }

    // ============================================================
    // HELICE → polilínea 3D triangulada
    // ============================================================
    fn exportar_helice(
        &self,
        res: &Value,
        vertices: &mut Vec<(f64, f64, f64)>,
        caras: &mut Vec<(usize, usize, usize)>
    ) {
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

            let base = vertices.len() + 1;

            vertices.push(p1a);
            vertices.push(p2a);
            vertices.push(p3a);
            vertices.push(p4a);

            caras.push((base, base + 1, base + 2));
            caras.push((base, base + 2, base + 3));
        }
    }
}
