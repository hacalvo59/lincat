// ============================================================================
// LINCAT Industrial Engine - Module: Postprocesador G-code Arcos
// Author: Hugo Alberto Calvo
// Component Type: POST / GCODE
// Description:
//     Convierte geometría de arco (HF Arcos) en G2/G3 industrial.
// ============================================================================

use serde_json::Value;

pub struct PostGcodeArcos;

impl PostGcodeArcos {
    pub fn new() -> Self {
        Self
    }

    /// Convierte payload HF Arcos en G-code G2/G3.
    pub fn generar(&self, payload: &Value) -> String {
        let res = &payload["resultado"];

        let cx = res["centro"]["cx"].as_f64().unwrap_or(0.0);
        let cy = res["centro"]["cy"].as_f64().unwrap_or(0.0);

        let x1 = payload["input"]["x1"].as_f64().unwrap_or(0.0);
        let y1 = payload["input"]["y1"].as_f64().unwrap_or(0.0);

        let x0 = payload["input"]["x0"].as_f64().unwrap_or(0.0);
        let y0 = payload["input"]["y0"].as_f64().unwrap_or(0.0);

        let i = cx - x0;
        let j = cy - y0;

        let tipo = res["tipo_gcode"].as_str().unwrap_or("G2");

        format!(
            "{tipo} X{:.3} Y{:.3} I{:.3} J{:.3}",
            x1, y1, i, j
        )
    }
}
