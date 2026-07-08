// ============================================================================
// LINCAT Industrial Engine - MAIN
// Autor: Hugo Alberto Calvo
// Arquitectura: Deterministic Multi-Core V12
// Descripción:
//     Punto de entrada del motor industrial LINCAT.
//     - Crea CycleT y ventanas.
//     - Registra módulos HF/MF/LF.
//     - Ejecuta tareas industriales.
//     - Produce JSON Salida.
//     - Exporta G-code.
// ============================================================================

mod lincat_engine;
mod cnc;
mod bus;
mod cam;
mod modulos;
mod ops;
mod protocolo;
mod scheduler;
mod sim;

use std::time::Duration;

use lincat_engine::bus::bus_ida::TaskPrepared;
use lincat_engine::bus::scheduler::Scheduler;
use lincat_engine::json::entrada::TaskIn;
use lincat_engine::json::salida::{JsonSalida};
use lincat_engine::post::exportador_gcode::ExportadorGcode;

// Módulos HF
use lincat_engine::modulos::hf::modulo_hf_arcos::ModuloHFArcos;
use lincat_engine::modulos::hf::modulo_hf_helicoidal::ModuloHFHelicoidal;

// Ventanas
use lincat_engine::bus::ventana_map::generar_ventanas_uniformes;
use lincat_engine::bus::CoreId;

fn main() {
    println!("=== LINCAT Industrial Engine V12 ===");

    // ---------------------------------------------------------
    // 1. Crear CycleT + ventanas por núcleo
    // ---------------------------------------------------------
    let duration = Duration::from_millis(10); // ciclo de 10ms
    let cores = vec![CoreId(0), CoreId(1)];

    let (cycle, core_map) = generar_ventanas_uniformes(duration, cores);

    println!("CycleT generado con {} ventanas.", cycle.slots.len());

    // ---------------------------------------------------------
    // 2. Registrar módulos HF/MF/LF
    // ---------------------------------------------------------
    let modulo_arcos = ModuloHFArcos::new();
    let modulo_helicoidal = ModuloHFHelicoidal::new();

    let scheduler = Scheduler::new(vec![
        &modulo_arcos,
        &modulo_helicoidal,
    ]);

    // ---------------------------------------------------------
    // 3. Crear tareas industriales (TaskIn)
    // ---------------------------------------------------------
    let tarea_arco = TaskIn {
        tipo_modulo: Some(lincat_engine::modulos::contratos::TipoModulo::HF),
        x0: Some(0.0),
        y0: Some(10.0),
        x1: Some(10.0),
        y1: Some(0.0),
        cx: Some(0.0),
        cy: Some(0.0),
        z0: None,
        z1: None,
        pitch: None,
        vueltas: None,
    };

    let tarea_helice = TaskIn {
        tipo_modulo: Some(lincat_engine::modulos::contratos::TipoModulo::HF),
        x0: Some(10.0),
        y0: Some(0.0),
        z0: Some(0.0),
        x1: Some(0.0),
        y1: Some(10.0),
        z1: Some(-20.0),
        cx: Some(0.0),
        cy: Some(0.0),
        pitch: Some(5.0),
        vueltas: Some(4.0),
    };

    // ---------------------------------------------------------
    // 4. BUS Ida → preparar tareas
    // ---------------------------------------------------------
    let prepared_arco = TaskPrepared::new(0, cycle.slots[0].clone(), tarea_arco);
    let prepared_helice = TaskPrepared::new(1, cycle.slots[1].clone(), tarea_helice);

    // ---------------------------------------------------------
    // 5. Scheduler → seleccionar módulo
    // ---------------------------------------------------------
    let modulo_a = scheduler.seleccionar_modulo(&prepared_arco).unwrap();
    let modulo_h = scheduler.seleccionar_modulo(&prepared_helice).unwrap();

    // ---------------------------------------------------------
    // 6. BUS Interno → ejecutar módulos
    // ---------------------------------------------------------
    let resultado_arco = modulo_a.ejecutar(&prepared_arco.payload);
    let resultado_helice = modulo_h.ejecutar(&prepared_helice.payload);

    // ---------------------------------------------------------
    // 7. BUS Vuelta → empaquetar TaskOut
    // ---------------------------------------------------------
    let mut salida = JsonSalida::new();

    salida.agregar(lincat_engine::bus::bus_vuelta::BusVuelta::empaquetar_salida(
        lincat_engine::bus::bus_vuelta::TaskResult {
            core_id: prepared_arco.core_id,
            slot: prepared_arco.slot.clone(),
            cycle_index: 0,
            payload: resultado_arco,
        }
    ));

    salida.agregar(lincat_engine::bus::bus_vuelta::BusVuelta::empaquetar_salida(
        lincat_engine::bus::bus_vuelta::TaskResult {
            core_id: prepared_helice.core_id,
            slot: prepared_helice.slot.clone(),
            cycle_index: 0,
            payload: resultado_helice,
        }
    ));

    // ---------------------------------------------------------
    // 8. Exportador G-code → generar programa CNC
    // ---------------------------------------------------------
    let exportador = ExportadorGcode::new();
    let gcode = exportador.exportar(&salida.resultados);

    println!("=== G-code generado ===");
    println!("{}", gcode);

    // ---------------------------------------------------------
    // 9. JSON Salida final
    // ---------------------------------------------------------
    let json_final = salida.como_json();
    println!("=== JSON Salida ===");
    println!("{}", json_final);
}
