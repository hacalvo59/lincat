// ============================================================================
// LINCAT Industrial Engine - Module: HF Arcos
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: MODULO / HIGH FREQUENCY
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Módulo HF para generación de arcos industriales. Ejecutado dentro de
//     ventanas QtimeSlot de alta frecuencia del CycleT.
//
// Responsibilities:
//     - Procesar tareas HF de tipo "arco".
//     - Calcular geometría circular (centro, radio, ángulos).
//     - Producir puntos industriales para G2/G3.
//     - Mantener determinismo y bajo tiempo de respuesta.
//
// Contracts:
//     Input:  TaskIn (JSON Entrada).
//     Output: serde_json::Value (resultado geométrico).
//     Tipo:   HF.
//
// Notes:
//     - Este módulo es real y produce geometría útil.
//     - Se integra con el postprocesador G-code.
// ============================================================================

use serde_json::json;
use crate::lincat_engine::modulos::contratos::{ModuloEjecutable, TipoModulo};
use crate::lincat_engine::json::entrada::TaskIn;

/// Módulo HF de Arcos.
pub struct ModuloHFArcos;

impl ModuloHFArcos {
    pub fn new() -> Self {
        Self
    }
}

impl ModuloEjecutable for ModuloHFArcos {
    fn tipo(&self) -> TipoModulo {
        TipoModulo::HF
    }

    fn ejecutar(&self, entrada: &TaskIn) -> serde_json::Value {
        // Extraer parámetros geométricos desde JSON Entrada
        let x0 = entrada.x0.unwrap_or(0.0);
        let y0 = entrada.y0.unwrap_or(0.0);
        let x1 = entrada.x1.unwrap_or(0.0);
        let y1 = entrada.y1.unwrap_or(0.0);
        let cx = entrada.cx.unwrap_or(0.0);
        let cy = entrada.cy.unwrap_or(0.0);

        // Cálculo del radio
        let dx = x0 - cx;
        let dy = y0 - cy;
        let radio = (dx * dx + dy * dy).sqrt();

        // Ángulos del arco
        let ang0 = dy.atan2(dx);
        let ang1 = (y1 - cy).atan2(x1 - cx);

        // Longitud del arco
        let delta_ang = ang1 - ang0;
        let longitud = radio * delta_ang.abs();

        // Resultado industrial
        json!({
            "modulo": "HF Arcos",
            "descripcion": "Generación geométrica de arco circular",
            "input": {
                "x0": x0, "y0": y0,
                "x1": x1, "y1": y1,
                "cx": cx, "cy": cy
            },
            "resultado": {
                "centro": { "cx": cx, "cy": cy },
                "radio": radio,
                "angulo_inicio": ang0,
                "angulo_fin": ang1,
                "longitud": longitud,
                "tipo_gcode": if delta_ang >= 0.0 { "G3" } else { "G2" }
            }
        })
    }
}
