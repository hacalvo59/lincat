// ============================================================================
// LINCAT Industrial Engine - Module: tick
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: BUS / TIME
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Tick industrial del ciclo T: contador determinista del motor.
//
// Responsibilities:
//     - Mantener el índice de ciclo actual.
//     - Mantener el offset temporal dentro del CycleT.
//     - Avanzar ciclos de forma determinista.
//     - Proveer base temporal al BUS Ida/Vuelta y al Scheduler.
//
// Contracts:
//     Input:  CycleT (duración del ciclo).
//     Output: Tick actualizado.
//     Qtime:  HF / MF / LF según ventanas.
//     Core:   Multi-core.
//
// Notes:
//     - Offset siempre dentro del rango del CycleT.
//     - Avance determinista, sin saltos.
//     - No memoria compartida.
// ============================================================================

use crate::lincat_engine::bus::CycleT;

#[derive(Debug, Clone, Copy)]
pub struct Tick {
    /// Número de ciclo global (contador industrial).
    pub cycle_index: u64,
    /// Offset actual dentro del ciclo, en nanosegundos.
    pub offset_ns: u64,
}

impl Tick {
    /// Crea un tick inicial en el ciclo 0, offset 0.
    pub fn initial() -> Self {
        Self {
            cycle_index: 0,
            offset_ns: 0,
        }
    }

    /// Avanza el offset dentro del ciclo.
    /// Si se supera la duración del CycleT, se pasa al siguiente ciclo.
    pub fn advance(&mut self, cycle: &CycleT, delta_ns: u64) {
        self.offset_ns += delta_ns;

        if self.offset_ns >= cycle.duration_ns {
            self.next_cycle();
        }
    }

    /// Avanza al siguiente ciclo y resetea el offset.
    pub fn next_cycle(&mut self) {
        self.cycle_index += 1;
        self.offset_ns = 0;
    }

    /// Verifica si el offset actual es válido dentro del CycleT.
    pub fn is_valid(&self, cycle: &CycleT) -> bool {
        self.offset_ns <= cycle.duration_ns
    }
}
