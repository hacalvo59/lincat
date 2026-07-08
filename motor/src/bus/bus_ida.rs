// ============================================================================
// LINCAT Industrial Engine - Module: bus_ida
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: BUS / INPUT CHANNEL
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Canal de entrada del motor industrial LINCAT. Recibe tareas, valida,
//     asigna núcleo y prepara la ejecución determinista dentro del CycleT.
//
// Responsibilities:
//     - Recibir tareas desde JSON Entrada.
//     - Validar estructura y parámetros.
//     - Asignar núcleo según CoreMap.
//     - Preparar ejecución determinista dentro de QtimeSlot.
//     - Entregar tareas al BUS Interno.
//
// Contracts:
//     Input:  JSON Entrada → TaskIn.
//     Output: TaskPrepared para BUS Interno.
//     Qtime:  HF / MF / LF según tipo de tarea.
//     Core:   Asignado vía CoreMap.
//
// Notes:
//     - No ejecución aquí: solo preparación.
//     - No memoria compartida.
//     - Determinismo absoluto.
// ============================================================================

use crate::lincat_engine::bus::{CoreId, CoreMap, QtimeSlot, Tick};
use crate::lincat_engine::json::entrada::TaskIn;

/// Tarea preparada para ejecución determinista dentro del motor.
#[derive(Debug, Clone)]
pub struct TaskPrepared {
    pub core_id: CoreId,
    pub slot: QtimeSlot,
    pub payload: TaskIn,
    pub cycle_index: u64,
}

/// BUS Ida: canal de entrada del motor.
pub struct BusIda<'a> {
    core_map: &'a CoreMap,
}

impl<'a> BusIda<'a> {
    /// Crea un BUS Ida con referencia al CoreMap.
    pub fn new(core_map: &'a CoreMap) -> Self {
        Self { core_map }
    }

    /// Recibe una tarea desde JSON Entrada y la prepara para el motor.
    pub fn preparar_tarea(
        &self,
        tarea: TaskIn,
        tick: &Tick,
    ) -> Option<TaskPrepared> {
        // 1. Validar núcleo solicitado
        let core_id = tarea.core_id?;
        if !self.core_map.has_core(core_id) {
            return None; // núcleo inexistente
        }

        // 2. Obtener ventanas del núcleo
        let slots = self.core_map.get_slots_for_core(core_id);
        if slots.is_empty() {
            return None; // núcleo sin ventanas
        }

        // 3. Seleccionar ventana determinista (por ahora: primera)
        let slot = slots[0].clone();

        // 4. Construir tarea preparada
        Some(TaskPrepared {
            core_id,
            slot,
            payload: tarea,
            cycle_index: tick.cycle_index,
        })
    }
}
