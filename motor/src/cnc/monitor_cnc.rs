// ============================================================================
// LINCAT Industrial Engine - Module: Monitor CNC Tiempo Real
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: CNC / MONITOR
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Monitor industrial que observa el streaming CNC, el driver y la
//     trayectoria ejecutada, mostrando estado en tiempo real.
//
// Responsibilities:
//     - Mostrar línea actual.
//     - Mostrar estado del driver.
//     - Mostrar estado del streaming.
//     - Mostrar posición actual (X,Y,Z).
//     - Integrarse con simuladores 2D/3D.
// ============================================================================

use crate::lincat_engine::cnc::driver_cnc_virtual::{DriverCNCVirtual, EstadoDriver};
use crate::lincat_engine::cnc::streaming_cnc::EstadoStreaming;

#[derive(Debug, Clone)]
pub struct MonitorCNC {
    pub x: f64,
    pub y: f64,
    pub z: f64,
}

impl MonitorCNC {
    pub fn new() -> Self {
        Self { x: 0.0, y: 0.0, z: 0.0 }
    }

    /// Actualiza posición según línea G-code.
    pub fn actualizar_posicion(&mut self, linea: &str) {
        for token in linea.split_whitespace() {
            if token.starts_with('X') {
                self.x = token[1..].parse::<f64>().unwrap_or(self.x);
            } else if token.starts_with('Y') {
                self.y = token[1..].parse::<f64>().unwrap_or(self.y);
            } else if token.starts_with('Z') {
                self.z = token[1..].parse::<f64>().unwrap_or(self.z);
            }
        }
    }

    /// Renderiza estado industrial del monitor.
    pub fn render_estado(
        &self,
        linea_actual: &str,
        estado_driver: EstadoDriver,
        estado_streaming: EstadoStreaming,
    ) -> String {
        format!(
            "\n=== MONITOR CNC LINCAT ===\n\
             Línea actual: {linea_actual}\n\
             Driver: {:?}\n\
             Streaming: {:?}\n\
             Posición: X{:.3} Y{:.3} Z{:.3}\n\
             ===========================\n",
            estado_driver,
            estado_streaming,
            self.x,
            self.y,
            self.z
        )
    }
}
