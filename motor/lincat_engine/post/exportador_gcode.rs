// ============================================================================
// LINCAT Industrial Engine - Module: Exportador G-code
// Author: Hugo Alberto Calvo
// Component Type: POST / EXPORT
// Description:
//     Orquesta postprocesadores (lineal, arcos, helicoidal) y genera
//     un programa G-code completo.
// ============================================================================

use serde_json::Value;

use crate::lincat_engine::post::gcode_arcos::PostGcodeArcos;
use crate::lincat_engine::post::gcode_helicoidal::PostGcodeHelicoidal;

pub struct ExportadorGcode {
    post_arcos: PostGcodeArcos,
    post_helicoidal: PostGcodeHelicoidal,
    // más adelante: post_lineal, post_rapidos, etc.
}

impl ExportadorGcode {
    pub fn new() -> Self {
        Self {
            post_arcos: PostGcodeArcos::new(),
            post_helicoidal: PostGcodeHelicoidal::new(),
        }
    }

    /// Recibe una lista de resultados del motor y genera G-code.
    pub fn exportar(&self, resultados: &[Value]) -> String {
        let mut lines = Vec::new();

        // Header básico
        lines.push(String::from("%"));
        lines.push(String::from("G90 G21")); // absoluto, mm

        for res in resultados {
            let modulo = res["modulo"].as_str().unwrap_or("");

            let line = match modulo {
                "HF Arcos" => self.post_arcos.generar(res),
                "HF Helicoidal" => self.post_helicoidal.generar(res),
                // más adelante: "HF Lineal" => ...
                _ => String::from("; desconocido / no procesado"),
            };

            lines.push(line);
        }

        // Footer básico
        lines.push(String::from("M30"));
        lines.push(String::from("%"));

        lines.join("\n")
    }
}
