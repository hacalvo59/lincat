// ============================================================================
// LINCAT Industrial Engine - Module: HF Helicoidal
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: MODULO / HIGH FREQUENCY
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Módulo HF para generación de trayectorias helicoidales industriales
//     (arco G2/G3 + avance en Z).
//
// Responsibilities:
//     - Procesar tareas HF de tipo "helicoidal".
//     - Calcular geometría circular + avance axial.
//     - Producir parámetros industriales para postprocesador G-code.
//     - Mantener determinismo y bajo tiempo de respuesta.
//
// Contracts:
//     Input:  TaskIn (JSON Entrada).
//     Output: serde_json::Value (resultado geométrico helicoidal).
//     Tipo:   HF.
// ============================================================================

use serde_json::json;
use crate::lincat_engine::modulos::contratos::{ModuloEjecutable, TipoModulo};
use crate::lincat_engine::json::entrada::TaskIn;

/// Módulo HF Helicoidal.
pub struct ModuloHFHelicoidal;

impl ModuloHFHelicoidal {
    pub fn new() -> Self {
        Self
    }
}

impl ModuloEjecutable for ModuloHFHelicoidal {
    fn tipo(&self) -> TipoModulo {
        TipoModulo::HF
    }

    fn ejecutar(&self, entrada: &TaskIn) -> serde_json::Value {
        // Parámetros básicos
        let x0 = entrada.x0.unwrap_or(0.0);
        let y0 = entrada.y0.unwrap_or(0.0);
        let z0 = entrada.z0.unwrap_or(0.0);

        let x1 = entrada.x1.unwrap_or(0.0);
        let y1 = entrada.y1.unwrap_or(0.0);
        let z1 = entrada.z1.unwrap_or(z0);

        let cx = entrada.cx.unwrap_or(0.0);
        let cy = entrada.cy.unwrap_or(0.0);

        let pitch = entrada.pitch.unwrap_or(0.0); // avance por vuelta
        let vueltas = entrada.vueltas.unwrap_or(1.0);

        // Radio
        let dx0 = x0 - cx;
        let dy0 = y0 - cy;
        let radio = (dx0 * dx0 + dy0 * dy0).sqrt();

        // Ángulos
        let ang0 = dy0.atan2(dx0);
        let ang1 = (y1 - cy).atan2(x1 - cx);
        let delta_ang = ang1 - ang0;

        // Longitud arco y avance Z
        let longitud_arco = radio * delta_ang.abs();
        let delta_z = z1 - z0;

        // Pitch efectivo si no viene definido
        let pitch_eff = if pitch == 0.0 && vueltas != 0.0 {
            delta_z / vueltas
        } else {
            pitch
        };

        json!({
            "modulo": "HF Helicoidal",
            "descripcion": "Trayectoria helicoidal G2/G3 + Z",
            "input": {
                "x0": x0, "y0": y0, "z0": z0,
                "x1": x1, "y1": y1, "z1": z1,
                "cx": cx, "cy": cy,
                "pitch": pitch,
                "vueltas": vueltas
            },
            "resultado": {
                "centro": { "cx": cx, "cy": cy },
                "radio": radio,
                "angulo_inicio": ang0,
                "angulo_fin": ang1,
                "delta_angulo": delta_ang,
                "longitud_arco": longitud_arco,
                "delta_z": delta_z,
                "pitch_efectivo": pitch_eff,
                "tipo_gcode": if delta_ang >= 0.0 { "G3" } else { "G2" }
            }
        })
    }
}
