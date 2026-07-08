// ============================================================================
// LINCAT Industrial Engine - Module: bus_interno
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: BUS
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Núcleo del BUS interno: ciclo maestro (CycleT), ticks y mapa de núcleos.
//
// Responsibilities:
//     - Definir el ciclo industrial de tiempo (CycleT).
//     - Gestionar ticks dentro del ciclo.
//     - Mantener el mapa de núcleos y sus ventanas QtimeSlot.
//     - Proveer base temporal al BUS Ida/Vuelta y al scheduler.
//
// Contracts:
//     Input:  Configuración de tiempo y núcleos.
//     Output: Estructuras de ciclo, ticks y mapa de núcleos.
//     Qtime:  HF / MF / LF (según ventanas configuradas).
//     Core:   Multi-core, según CoreMap.
//
// Notes:
//     - Ejecución determinista dentro de QtimeSlot.
//     - Sin memoria compartida entre núcleos.
//     - El BUS es el único canal de coordinación.
// ============================================================================

use std::time::Duration;

/// Identificador de núcleo lógico del motor.
pub type CoreId = u8;

/// Representa una ventana de tiempo dentro de un CycleT para un núcleo.
#[derive(Debug, Clone)]
pub struct QtimeSlot {
    pub core_id: CoreId,
    pub start_offset_ns: u64,
    pub end_offset_ns: u64,
    // Más adelante: modo HF/MF/LF, TaskId asignado, etc.
}

/// Representa un ciclo industrial de tiempo (T) del motor LINCAT.
#[derive(Debug, Clone)]
pub struct CycleT {
    /// Duración total del ciclo en nanosegundos.
    pub duration_ns: u64,
    /// Ventanas de tiempo por núcleo dentro del ciclo.
    pub slots: Vec<QtimeSlot>,
}

/// Tick interno del BUS: posición actual dentro del CycleT.
#[derive(Debug, Clone, Copy)]
pub struct Tick {
    /// Número de ciclo (contador global).
    pub cycle_index: u64,
    /// Offset actual dentro del ciclo, en nanosegundos.
    pub offset_ns: u64,
}

/// Mapa de núcleos y sus ventanas temporales.
#[derive(Debug, Clone)]
pub struct CoreMap {
    pub cores: Vec<CoreId>,
    pub slots: Vec<QtimeSlot>,
}

impl CycleT {
    /// Crea un nuevo ciclo T con duración fija y sin ventanas aún.
    pub fn new(duration: Duration) -> Self {
        Self {
            duration_ns: duration.as_nanos() as u64,
            slots: Vec::new(),
        }
    }

    /// Asigna una ventana QtimeSlot a este ciclo.
    pub fn add_slot(&mut self, slot: QtimeSlot) {
        // Más adelante: validaciones de solapamiento, rango, etc.
        self.slots.push(slot);
    }
}

impl Tick {
    /// Crea un tick inicial en el ciclo 0, offset 0.
    pub fn initial() -> Self {
        Self {
            cycle_index: 0,
            offset_ns: 0,
        }
    }

    /// Avanza al siguiente ciclo, reseteando el offset.
    pub fn next_cycle(&mut self, _cycle: &CycleT) {
        self.cycle_index += 1;
        self.offset_ns = 0;
    }
}

impl CoreMap {
    /// Crea un mapa de núcleos vacío.
    pub fn new(cores: Vec<CoreId>) -> Self {
        Self {
            cores,
            slots: Vec::new(),
        }
    }

    /// Registra una ventana para un núcleo.
    pub fn register_slot(&mut self, slot: QtimeSlot) {
        self.slots.push(slot);
    }
}
