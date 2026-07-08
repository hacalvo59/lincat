// ============================================================================
// LINCAT Industrial Engine - Module: Streaming CNC
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: CNC / STREAMING
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Transmite G-code desde el BufferCNC hacia un driver CNC (virtual o real)
//     con control de flujo, pausa, reanudación y callbacks industriales.
//
// Responsibilities:
//     - Leer líneas del buffer CNC.
//     - Enviarlas al driver CNC.
//     - Controlar velocidad de transmisión.
//     - Permitir pausa/reanudación.
//     - Emitir eventos industriales (on_line, on_pause, on_finish).
// ============================================================================

use std::time::Duration;
use std::thread::sleep;

use crate::lincat_engine::cnc::buffer_cnc::BufferCNC;
use crate::lincat_engine::cnc::driver_cnc_virtual::{DriverCNCVirtual, EstadoDriver};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum EstadoStreaming {
    Idle,
    Streaming,
    Paused,
    Finished,
}

pub struct StreamingCNC {
    pub estado: EstadoStreaming,
    pub delay_transmision: Duration,
}

impl StreamingCNC {
    pub fn new(delay_ms: u64) -> Self {
        Self {
            estado: EstadoStreaming::Idle,
            delay_transmision: Duration::from_millis(delay_ms),
        }
    }

    /// Inicia transmisión CNC hacia el driver.
    pub fn transmitir(
        &mut self,
        buffer: &mut BufferCNC,
        driver: &mut DriverCNCVirtual,
        mut on_line: impl FnMut(&str),
        mut on_pause: impl FnMut(),
        mut on_finish: impl FnMut(),
    ) {
        self.estado = EstadoStreaming::Streaming;
        driver.estado = EstadoDriver::Running;

        while let Some(linea) = buffer.pop() {
            // Si está pausado, esperar
            while self.estado == EstadoStreaming::Paused {
                on_pause();
                sleep(Duration::from_millis(50));
            }

            // Enviar línea al driver
            on_line(&linea);
            println!("[STREAMING] → {}", linea);

            // Simular ejecución en driver
            sleep(driver.delay_por_linea);

            // Delay de transmisión
            sleep(self.delay_transmision);
        }

        self.estado = EstadoStreaming::Finished;
        driver.estado = EstadoDriver::Finished;

        on_finish();
    }

    /// Pausar transmisión
    pub fn pausar(&mut self) {
        if self.estado == EstadoStreaming::Streaming {
            self.estado = EstadoStreaming::Paused;
        }
    }

    /// Reanudar transmisión
    pub fn reanudar(&mut self) {
        if self.estado == EstadoStreaming::Paused {
            self.estado = EstadoStreaming::Streaming;
        }
    }
}
