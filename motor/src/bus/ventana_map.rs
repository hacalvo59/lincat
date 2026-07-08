// ============================================================================
// LINCAT Industrial Engine - Module: ventana_map
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: BUS / TIME LAYOUT
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Generador industrial de ventanas QtimeSlot por núcleo dentro de un CycleT.
//
// Responsibilities:
//     - Definir el layout temporal por núcleo.
//     - Generar QtimeSlot para cada core.
//     - Integrarse con CoreMap y CycleT.
//     - Proveer base temporal al Scheduler y BUS Ida.
//
// Contracts:
//     Input:  duración de ciclo, lista de núcleos, política de reparto.
//     Output: Vec<QtimeSlot> y/o CoreMap poblado.
//     Qtime:  HF / MF / LF según configuración.
//     Core:   Multi-core.
//
// Notes:
//     - Política inicial: reparto uniforme.
//     - Más adelante: políticas HF/MF/LF específicas.
// ============================================================================

use std::time::Duration;

use crate::lincat_engine::bus::{CoreId, QtimeSlot, CycleT, CoreMap};

/// Política simple de reparto uniforme de ventanas.
pub fn generar_ventanas_uniformes(
    duration: Duration,
    cores: Vec<CoreId>,
) -> (CycleT, CoreMap) {
    let mut cycle = CycleT::new(duration);
    let mut core_map = CoreMap::new(cores.clone());

    let total_ns = cycle.duration_ns;
    let num_cores = cores.len() as u64;
    let slot_ns = if num_cores > 0 {
        total_ns / num_cores
    } else {
        0
    };

    let mut offset = 0u64;

    for core_id in cores {
        let start = offset;
        let end = (offset + slot_ns).min(total_ns);

        let slot = QtimeSlot {
            core_id,
            start_offset_ns: start,
            end_offset_ns: end,
        };

        cycle.add_slot(slot.clone());
        core_map.register_slot(slot);

        offset = end;
    }

    (cycle, core_map)
}
