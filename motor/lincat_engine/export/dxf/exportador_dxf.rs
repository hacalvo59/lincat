// ============================================================================
// LINCAT Industrial Engine - Exportador DXF
// Author: Hugo Alberto Calvo
// Component Type: EXPORT / DXF
// Description:
//     Convierte resultados HF/MF/LF en entidades DXF industriales.
//     Soporta:
//         - LINE
//         - ARC
//         - LWPOLYLINE (opcional)
//         - HELIX (representada como polilínea 3D)
// ============================================================================

use serde_json::Value;

pub struct ExportadorDXF {
    pub capa: String,
}

impl ExportadorDXF {
    pub fn new(capa: &str) -> Self {
        Self {
            capa: capa.to_string(),
        }
    }

    /// Exporta una lista de resultados del motor a un DXF completo.
    pub fn exportar(&self, resultados: &[Value]) -> String {
        let mut dxf = String::new();

        // ---------------------------------------------------------
        // HEADER DXF
        // ---------------------------------------------------------
        dxf.push_str("0\nSECTION\n2\nHEADER\n0\nENDSEC\n");

        // ---------------------------------------------------------
        // TABLES DXF
        // ---------------------------------------------------------
        dxf.push_str("0\nSECTION\n2\nTABLES\n0\nENDSEC\n");

        // ---------------------------------------------------------
        // ENTITIES DXF
        // ---------------------------------------------------------
        dxf.push_str("0\nSECTION\n2\nENTITIES\n");

        for res in resultados {
            let modulo = res["modulo"].as_str().unwrap_or("");

            match modulo {
                "HF Arcos" => dxf.push_str(&self.exportar_arco(res)),
                "HF Helicoidal" => dxf.push_str(&self.exportar_helice(res)),
                "HF Lineal" => dxf.push_str(&self.exportar_linea(res)),
                _ => {
                    dxf.push_str("0\nTEXT\n8\nINFO\n10\n0\n20\n0\n1\nMODULO DESCONOCIDO\n");
                }
            }
        }

        // ---------------------------------------------------------
        // END ENTITIES
        // ---------------------------------------------------------
        dxf.push_str("0\nENDSEC\n0\nEOF\n");

        dxf
    }

    // ============================================================
    // EXPORTAR LÍNEA
    // ============================================================
    fn exportar_linea(&self, res: &Value) -> String {
        let x0 = res["input"]["x0"].as_f64().unwrap_or(0.0);
        let y0 = res["input"]["y0"].as_f64().unwrap_or(0.0);
        let x1 = res["input"]["x1"].as_f64().unwrap_or(0.0);
        let y1 = res["input"]["y1"].as_f64().unwrap_or(0.0);

        format!(
            "0\nLINE\n8\n{}\n10\n{}\n20\n{}\n11\n{}\n21\n{}\n",
            self.capa, x0, y0, x1, y1
        )
    }

    // ============================================================
    // EXPORTAR ARCO
    // ============================================================
    fn exportar_arco(&self, res: &Value) -> String {
        let cx = res["resultado"]["centro"]["cx"].as_f64().unwrap_or(0.0);
        let cy = res["resultado"]["centro"]["cy"].as_f64().unwrap_or(0.0);
        let radio = res["resultado"]["radio"].as_f64().unwrap_or(0.0);

        let ang_i = res["resultado"]["angulo_inicio"].as_f64().unwrap_or(0.0).to_degrees();
        let ang_f = res["resultado"]["angulo_fin"].as_f64().unwrap_or(0.0).to_degrees();

        format!(
            "0\nARC\n8\n{}\n10\n{}\n20\n{}\n40\n{}\n50\n{}\n51\n{}\n",
            self.capa, cx, cy, radio, ang_i, ang_f
        )
    }

    // ============================================================
    // EXPORTAR HELICE (polilínea 3D)
    // ============================================================
    fn exportar_helice(&self, res: &Value) -> String {
        let puntos = res["resultado"]["trayectoria"]
            .as_array()
            .unwrap_or(&vec![]);

        let mut out = String::new();
        out.push_str("0\nPOLYLINE\n8\n");
        out.push_str(&self.capa);
        out.push_str("\n66\n1\n70\n8\n");

        for p in puntos {
            let x = p["x"].as_f64().unwrap_or(0.0);
            let y = p["y"].as_f64().unwrap_or(0.0);
            let z = p["z"].as_f64().unwrap_or(0.0);

            out.push_str(&format!("0\nVERTEX\n8\n{}\n10\n{}\n20\n{}\n30\n{}\n",
                                  self.capa, x, y, z));
        }

        out.push_str("0\nSEQEND\n");

        out
    }
}
