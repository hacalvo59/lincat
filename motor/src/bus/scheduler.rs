// ============================================================================
// LINCAT Industrial Engine - Module: scheduler
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: BUS / SCHEDULER
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Scheduler industrial del motor LINCAT. Decide qué módulo HF/MF/LF se
//     ejecuta en cada ventana QtimeSlot del CycleT.
//
// Responsibilities:
//     - Seleccionar módulo según tipo de tarea.
//     - Asignar módulo a núcleo y ventana.
//     - Garantizar determinismo en la selección.
//     - Integrarse con BUS Ida → Interno → Vuelta.
//
// Contracts:
//     Input:  TaskPrepared (núcleo, ventana, ciclo).
//     Output: Referencia a módulo ejecutable.
//     Qtime:  HF / MF / LF según ventana.
//     Core:   Multi-core.
//
// Notes:
//     - No ejecuta: solo decide.
//     - No JSON aquí.
//     - Determinismo absoluto.
// ============================================================================

use crate::lincat_engine::bus::bus_ida::TaskPrepared;
use crate::lincat_engine::modulos::contratos::{ModuloEjecutable, TipoModulo};

/// Scheduler industrial del motor.
pub struct Scheduler<'a> {
    /// Módulos disponibles en el motor.
    pub modulos: Vec<&'a dyn ModuloEjecutable>,
}

impl<'a> Scheduler<'a> {
    /// Crea un scheduler con la lista de módulos disponibles.
    pub fn new(modulos: Vec<&'a dyn ModuloEjecutable>) -> Self {
        Self { modulos }
    }

    /// Selecciona el módulo adecuado para la tarea preparada.
    pub fn seleccionar_modulo(
        &self,
        tarea: &TaskPrepared,
    ) -> Option<&'a dyn ModuloEjecutable> {
        let tipo = tarea.payload.tipo_modulo?;

        // Selección determinista: primer módulo que coincida con el tipo.
        for modulo in &self.modulos {
            if modulo.tipo() == tipo {
                return Some(*modulo);
            }
        }

        None
    }
}
