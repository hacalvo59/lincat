// ============================================================================
// LINCAT Industrial Ecosystem - Panel CNC (Slint UI)
// Author: Hugo Alberto Calvo
// Component Type: UI / PANEL CNC
// Description:
//     Interfaz gráfica industrial para controlar el motor LINCAT:
//         - START / PAUSE / RESUME / STOP
//         - Estado del driver y streaming
//         - Posición X/Y/Z en tiempo real
//         - Consola de log industrial
//     Este panel se comunica con el motor LINCAT (Rust) mediante
//     PanelControl, BufferCNC, StreamingCNC y MonitorCNC.
// ============================================================================

use slint::SharedString;
slint::include_modules!();

use lincat_engine::cnc::panel_control::PanelControl;
use lincat_engine::cnc::buffer_cnc::BufferCNC;

fn main() {
    // -------------------------------
    // Crear panel LINCAT (motor real)
    // -------------------------------
    let mut panel = PanelControl::new(10, 20);

    // Cargar G-code de prueba
    let gcode = "G1 X10 Y10\nG1 X20 Y5\nG1 X30 Y15\n";
    let mut buffer = BufferCNC::new(1024);
    for linea in gcode.lines() {
        buffer.push(linea.to_string()).unwrap();
    }

    // -------------------------------
    // Crear UI Slint
    // -------------------------------
    let ui = LincatPanel::new().unwrap();

    ui.set_driver_state("IDLE".into());
    ui.set_streaming_state("IDLE".into());
    ui.set_position("X0.000 Y0.000 Z0.000".into());
    ui.set_log_text("LINCAT Panel iniciado...\n".into());

    let ui_handle = ui.as_weak();

    // -------------------------------
    // START
    // -------------------------------
    ui.on_start_clicked(move || {
        if let Some(ui) = ui_handle.upgrade() {
            let mut log = ui.get_log_text().to_string();
            log.push_str("START enviado a LINCAT\n");
            ui.set_log_text(log.into());

            // Ejecutar motor LINCAT
            panel.start(&mut buffer);

            ui.set_driver_state(format!("{:?}", panel.driver.estado).into());
            ui.set_streaming_state(format!("{:?}", panel.streaming.estado).into());

            ui.set_position(format!(
                "X{:.3} Y{:.3} Z{:.3}",
                panel.monitor.x,
                panel.monitor.y,
                panel.monitor.z
            ).into());
        }
    });

    // -------------------------------
    // PAUSE
    // -------------------------------
    let ui_handle = ui.as_weak();
    ui.on_pause_clicked(move || {
        if let Some(ui) = ui_handle.upgrade() {
            panel.pause();

            let mut log = ui.get_log_text().to_string();
            log.push_str("PAUSE enviado a LINCAT\n");
            ui.set_log_text(log.into());

            ui.set_streaming_state(format!("{:?}", panel.streaming.estado).into());
        }
    });

    // -------------------------------
    // RESUME
    // -------------------------------
    let ui_handle = ui.as_weak();
    ui.on_resume_clicked(move || {
        if let Some(ui) = ui_handle.upgrade() {
            panel.resume();

            let mut log = ui.get_log_text().to_string();
            log.push_str("RESUME enviado a LINCAT\n");
            ui.set_log_text(log.into());

            ui.set_streaming_state(format!("{:?}", panel.streaming.estado).into());
        }
    });

    // -------------------------------
    // STOP
    // -------------------------------
