// ============================================================================
// LINCAT Industrial Engine - Module: JSON Salida
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: JSON / OUTPUT
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Estructuras de salida del motor industrial LINCAT. Reciben TaskOut desde
//     BUS Vuelta y se convierten en JSON final para el exterior.
//
// Responsibilities:
//     - Representar resultados industriales del motor.
//     - Mantener estructura determinista y ordenada.
//     - Ser consumido por exportadores (G-code, DXF, etc).
//
// Contracts:
//     Input:  TaskOut (núcleo, ventana, ciclo, payload).
//     Output: JSON industrial.
// ============================================================================

use serde::{Serialize, Deserialize};
use serde_json::Value;

use crate::lincat_engine::bus::{CoreId};

/// Estructura de salida del motor.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TaskOut {
    pub core_id: CoreId,
    pub slot_info: Value,
    pub cycle_index: u64,
    pub output: Value,
}

/// JSON Salida completo del motor.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct JsonSalida {
    pub motor: String,
    pub version: String,
    pub resultados: Vec<TaskOut>,
}

impl JsonSalida {
    pub fn new() -> Self {
        Self {
            motor: "LINCAT Industrial Engine".to_string(),
            version: "0.1.0".to_string(),
            resultados: Vec::new(),
        }
    }

    pub fn agregar(&mut self, task: TaskOut) {
        self.resultados.push(task);
    }

    pub fn como_json(&self) -> Value {
        serde_json::json!({
            "motor": self.motor,
            "version": self.version,
            "resultados": self.resultados
        })
    }
}
