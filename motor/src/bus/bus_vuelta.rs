// ============================================================================
// LINCAT Industrial Engine - Module: bus_vuelta
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: BUS / OUTPUT CHANNEL
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Canal de salida del motor industrial LINCAT. Recibe resultados de los
//     módulos ejecutados y los empaqueta para JSON Salida.
//
// Responsibilities:
//     - Recibir resultados desde BUS Interno.
//     - Asociar resultado con núcleo, ventana y ciclo.
//     - Empaquetar estructura determinista para JSON Salida.
//     - Garantizar salida ordenada y sin ambigüedad.
//
// Contracts:
//     Input:  Resultado de módulo ejecutado (TaskResult).
//     Output: TaskOut → JSON Salida.
//     Qtime:  HF / MF / LF según ventana ejecutada.
//     Core:   Núcleo donde se ejecutó.
//
// Notes:
//     - No ejecución aquí: solo salida.
//     - No memoria compartida.
//     - Determinismo absoluto.
// ============================================================================

use crate::lincat_engine::bus::{CoreId, QtimeSlot};
use crate::lincat_engine::json::salida::TaskOut;

/// Resultado interno del motor, producido por un módulo HF/MF/LF.
#[derive(Debug, Clone)]
pub struct TaskResult {
    pub core_id: CoreId,
    pub slot: QtimeSlot,
    pub cycle_index: u64,
    pub payload: serde_json::Value, // resultado geométrico o industrial
}

/// BUS Vuelta: canal de salida del motor.
pub struct BusVuelta;

impl BusVuelta {
    /// Recibe un resultado interno y lo convierte en TaskOut para JSON Salida.
    pub fn empaquetar_salida(result: TaskResult) -> TaskOut {
        TaskOut {
            core_id: result.core_id,
            slot_info: serde_json::json!({
                "core": result.slot.core_id,
                "start_ns": result.slot.start_offset_ns,
                "end_ns": result.slot.end_offset_ns
            }),
            cycle_index: result.cycle_index,
            output: result.payload,
        }
    }
}
