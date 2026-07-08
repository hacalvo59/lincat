// ============================================================================
// LINCAT Industrial Engine - Panel de Control CNC
// Author: Hugo Alberto Calvo
// Component Type: CNC / PANEL CONTROL
// Description:
//     Interfaz industrial para controlar el flujo CNC LINCAT.
//     - Start / Pause / Resume / Stop
//     - Estado del driver
//     - Estado del streaming
//     - Posición actual
//     - Integración con simuladores 2D/3D
// ============================================================================

use crate::lincat_engine::cnc::streaming_cnc::{StreamingCNC, EstadoStreaming};
use crate::lincat_engine::cnc::driver_cnc_virtual::{DriverCNCVirtual, EstadoDriver};
use crate::lincat_engine::cnc::monitor_cnc::MonitorCNC;
use crate::lincat_engine::cnc::buffer_cnc::BufferCNC;

pub struct PanelControl {
    pub monitor: MonitorCNC,
    pub streaming: StreamingCNC,
    pub driver: DriverCNCVirtual,
}

impl PanelControl {
    pub fn new(delay_stream_ms: u64, delay_driver_ms: u64) -> Self {
        Self {
            monitor: MonitorCNC::new(),
            streaming: StreamingCNC::new(delay_stream_ms),
            driver: DriverCNCVirtual::new(delay_driver_ms),
        }
    }

    /// Inicia el programa CNC desde el buffer.
    pub fn start(&mut self, buffer: &mut BufferCNC) {
        println!("=== PANEL LINCAT: START ===");

        self.streaming.transmitir(
            buffer,
            &mut self.driver,
            |line| {
                self.monitor.actualizar_posicion(line);
                println!("{}", self.monitor.render_estado(
                    line,
                    self.driver.estado,
                    self.streaming.estado
                ));
            },
            || println!("** PANEL: PAUSADO **"),
            || println!("** PANEL: PROGRAMA FINALIZADO **"),
        );
    }

    /// Pausa el streaming CNC.
    pub fn pause(&mut self) {
        println!("=== PANEL LINCAT: PAUSE ===");
        self.streaming.pausar();
    }

    /// Reanuda el streaming CNC.
    pub fn resume(&mut self) {
        println!("=== PANEL LINCAT: RESUME ===");
        self.streaming.reanudar();
    }

    /// Detiene el driver y el streaming.
    pub fn stop(&mut self) {
        println!("=== PANEL LINCAT: STOP ===");
        self.streaming.estado = EstadoStreaming::Finished;
        self.driver.estado = EstadoDriver::Finished;
    }

    /// Renderiza estado general del panel.
    pub fn estado(&self) -> String {
        format!(
            "\n=== PANEL DE CONTROL LINCAT ===\n\
             Driver: {:?}\n\
             Streaming: {:?}\n\
             Posición: X{:.3} Y{:.3} Z{:.3}\n\
             =================================\n",
            self.driver.estado,
            self.streaming.estado,
            self.monitor.x,
            self.monitor.y,
            self.monitor.z
        )
    }
}
