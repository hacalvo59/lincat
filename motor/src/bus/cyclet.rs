// ============================================================================
// LINCAT Industrial Engine - Module: cyclet
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: BUS / TIME CORE
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Define el ciclo maestro de tiempo (CycleT) del motor industrial LINCAT.
//
// Responsibilities:
//     - Representar el ciclo industrial T.
//     - Gestionar duración, ventanas y validaciones.
//     - Servir como base temporal para BUS Interno, Ida, Vuelta y Scheduler.
//
// Contracts:
//     Input:  Configuración de duración y ventanas.
//     Output: Estructura CycleT lista para asignar QtimeSlots.
//     Qtime:  HF / MF / LF según ventanas.
//     Core:   Multi-core.
//
// Notes:
//     - Determinismo absoluto.
//     - No memoria compartida.
//     - No improvisación temporal.
// ============================================================================

use std::time::Duration;
use crate::lincat_engine::bus::QtimeSlot;

#[derive(Debug, Clone)]
pub struct CycleT {
    /// Duración total del ciclo en nanosegundos.
    pub duration_ns: u64,
    /// Ventanas de tiempo por núcleo dentro del ciclo.
    pub slots: Vec<QtimeSlot>,
}

impl CycleT {
    /// Crea un nuevo ciclo T con duración fija.
    pub fn new(duration: Duration) -> Self {
        Self {
            duration_ns: duration.as_nanos() as u64,
            slots: Vec::new(),
        }
    }

    /// Agrega una ventana QtimeSlot al ciclo.
    pub fn add_slot(&mut self, slot: QtimeSlot) {
        // Más adelante: validaciones de solapamiento, rango, etc.
        self.slots.push(slot);
    }

    /// Verifica si un offset está dentro del ciclo.
    pub fn is_valid_offset(&self, offset_ns: u64) -> bool {
        offset_ns <= self.duration_ns
    }
}
