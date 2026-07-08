// ============================================================================
// LINCAT Industrial Engine - Module: Postprocesador G-code Helicoidal
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: POST / GCODE
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Convierte geometría helicoidal industrial en G-code G2/G3 + Z.
//
// Responsibilities:
//     - Recibir payload del módulo HF Helicoidal.
//     - Generar comando G2/G3 con I/J y avance en Z.
//     - Mantener determinismo y formato CNC estándar.
//     - Producir string G-code listo para exportar.
//
// Contracts:
//     Input:  serde_json::Value (resultado HF Helicoidal).
//     Output: String (G-code).
// ============================================================================

use serde_json::Value;

pub struct PostGcodeHelicoidal;

impl PostGcodeHelicoidal {
    pub fn new() -> Self {
        Self
    }

    /// Convierte payload HF Helicoidal en G-code industrial.
    pub fn generar(&self, payload: &Value) -> String {
        // Extraer datos del JSON HF Helicoidal
        let res = &payload["resultado"];

        let cx = res["centro"]["cx"].as_f64().unwrap_or(0.0);
        let cy = res["centro"]["cy"].as_f64().unwrap_or(0.0);

        let x1 = payload["input"]["x1"].as_f64().unwrap_or(0.0);
        let y1 = payload["input"]["y1"].as_f64().unwrap_or(0.0);
        let z1 = payload["input"]["z1"].as_f64().unwrap_or(0.0);

        let x0 = payload["input"]["x0"].as_f64().unwrap_or(0.0);
        let y0 = payload["input"]["y0"].as_f64().unwrap_or(0.0);

        // I/J relativos
        let i = cx - x0;
        let j = cy - y0;

        // Tipo G2/G3
        let tipo = res["tipo_gcode"].as_str().unwrap_or("G2");

        // Construcción del comando helicoidal
        format!(
            "{tipo} X{:.3} Y{:.3} Z{:.3} I{:.3} J{:.3}",
            x1, y1, z1, i, j
        )
    }
}
