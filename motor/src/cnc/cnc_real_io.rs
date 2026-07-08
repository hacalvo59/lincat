// ============================================================================
// LINCAT Industrial Engine - CNC Real I/O Layer
// Author: Hugo Alberto Calvo
// Component Type: CNC / REAL I/O
// Description:
//     Orquesta el flujo completo hacia una máquina CNC real:
//     - BufferCNC
//     - DriverCNCReal (Serial/TCP)
//     - StreamingCNC
//     - PanelControl
//     - MonitorCNC
// ============================================================================

use crate::lincat_engine::cnc::buffer_cnc::BufferCNC;
use crate::lincat_engine::cnc::driver_cnc_real::{DriverCNCReal, CanalCNC};
use crate::lincat_engine::cnc::streaming_cnc::StreamingCNC;
use crate::lincat_engine::cnc::monitor_cnc::MonitorCNC;

pub struct CNCRealIO<C: CanalCNC> {
    pub buffer: BufferCNC,
    pub driver: DriverCNCReal<C>,
    pub streaming: StreamingCNC,
    pub monitor: MonitorCNC,
}

impl<C: CanalCNC> CNCRealIO<C> {
    pub fn new(canal: C, capacidad_buffer: usize, delay_stream_ms: u64, delay_driver_ms: u64) -> Self {
        Self {
            buffer: BufferCNC::new(capacidad_buffer),
            driver: DriverCNCReal::new(canal),
            streaming: StreamingCNC::new(delay_stream_ms),
            monitor: MonitorCNC::new(),
        }
    }

    /// Carga G-code en el buffer CNC.
    pub fn cargar_programa(&mut self, gcode: &str) {
        for linea in gcode.lines() {
            let _ = self.buffer.push(linea.to_string());
        }
    }

    /// Conecta al driver real.
    pub fn conectar(&mut self) -> Result<(), String> {
        self.driver.conectar()
    }

    /// Ejecuta el programa CNC real.
    pub fn ejecutar(&mut self) -> Result<(), String> {
        self.streaming.transmitir(
            &mut self.buffer,
            &mut self.driver,
            |line| {
                self.monitor.actualizar_posicion(line);
                let _ = self.driver.enviar_linea(line);
                println!("{}", self.monitor.render_estado(
                    line,
                    self.driver.estado,
                    self.streaming.estado
                ));
            },
            || println!("** CNC REAL: PAUSADO **"),
            || println!("** CNC REAL: FINALIZADO **"),
        );

        Ok(())
    }

    /// Pausa transmisión.
    pub fn pausar(&mut self) {
        self.streaming.pausar();
    }

    /// Reanuda transmisión.
    pub fn reanudar(&mut self) {
        self.streaming.reanudar();
    }

    /// Desconecta del driver real.
    pub fn desconectar(&mut self) -> Result<(), String> {
        self.driver.desconectar()
    }
}
