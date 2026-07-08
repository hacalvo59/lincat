// ============================================================================
// LINCAT Industrial Engine - Module: core_map
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: BUS / CORE MAP
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Mapa industrial de núcleos y sus ventanas QtimeSlot.
//
// Responsibilities:
//     - Registrar núcleos disponibles del motor.
//     - Asociar ventanas QtimeSlot a cada núcleo.
//     - Proveer estructura determinista para el BUS Interno y el Scheduler.
//
// Contracts:
//     Input:  Lista de núcleos y ventanas.
//     Output: Mapa determinista de núcleos y sus QtimeSlots.
//     Qtime:  HF / MF / LF según configuración.
//     Core:   Multi-core.
//
// Notes:
//     - No memoria compartida.
//     - No solapamiento de ventanas.
//     - Determinismo absoluto.
// ============================================================================

use crate::lincat_engine::bus::{CoreId, QtimeSlot};

#[derive(Debug, Clone)]
pub struct CoreMap {
    /// Lista de núcleos disponibles.
    pub cores: Vec<CoreId>,
    /// Ventanas QtimeSlot asociadas a los núcleos.
    pub slots: Vec<QtimeSlot>,
}

impl CoreMap {
    /// Crea un mapa de núcleos vacío con la lista de cores.
    pub fn new(cores: Vec<CoreId>) -> Self {
        Self {
            cores,
            slots: Vec::new(),
        }
    }

    /// Registra una ventana QtimeSlot para un núcleo.
    pub fn register_slot(&mut self, slot: QtimeSlot) {
        // Más adelante: validación de solapamiento y rango.
        self.slots.push(slot);
    }

    /// Obtiene todas las ventanas asociadas a un núcleo.
    pub fn get_slots_for_core(&self, core_id: CoreId) -> Vec<&QtimeSlot> {
        self.slots
            .iter()
            .filter(|slot| slot.core_id == core_id)
            .collect()
    }

    /// Verifica si un núcleo existe en el mapa.
    pub fn has_core(&self, core_id: CoreId) -> bool {
        self.cores.contains(&core_id)
    }
}
