// ============================================================================
// LINCAT Industrial Engine - Module: Driver CNC Virtual
// Author: Hugo Alberto Calvo
// Component Type: CNC / DRIVER VIRTUAL
// Description:
//     Simula una máquina CNC consumiendo líneas desde el BufferCNC.
// ============================================================================

use std::time::Duration;
use std::thread::sleep;

use crate::lincat_engine::cnc::buffer_cnc::BufferCNC;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum EstadoDriver {
    Idle,
    Running,
    Finished,
}

pub struct DriverCNCVirtual {
    pub estado: EstadoDriver,
    pub delay_por_linea: Duration,
}

impl DriverCNCVirtual {
    pub fn new(delay_ms: u64) -> Self {
        Self {
            estado: EstadoDriver::Idle,
            delay_por_linea: Duration::from_millis(delay_ms),
        }
    }

    /// Ejecuta el programa contenido en el buffer, línea por línea.
    pub fn ejecutar(&mut self, buffer: &mut BufferCNC) {
        self.estado = EstadoDriver::Running;

        while let Some(linea) = buffer.pop() {
            println!("[CNC VIRTUAL] Ejecutando: {}", linea);
            sleep(self.delay_por_linea);
        }

        self.estado = EstadoDriver::Finished;
        println!("[CNC VIRTUAL] Programa finalizado.");
    }
}
