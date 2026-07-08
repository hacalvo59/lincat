// ============================================================================
// LINCAT Industrial Engine - Module: Simulador CNC 2D
// Author: Hugo Alberto Calvo
// Component Type: CNC / SIMULADOR
// Description:
//     Simula visualmente (2D) la trayectoria ejecutada por el Driver CNC Virtual.
//     No usa gráficos reales: genera una matriz ASCII industrial.
// ============================================================================

use crate::lincat_engine::cnc::buffer_cnc::BufferCNC;

#[derive(Debug, Clone)]
pub struct SimuladorCNC {
    ancho: usize,
    alto: usize,
    matriz: Vec<Vec<char>>,
}

impl SimuladorCNC {
    pub fn new(ancho: usize, alto: usize) -> Self {
        Self {
            ancho,
            alto,
            matriz: vec![vec!['.'; ancho]; alto],
        }
    }

    /// Marca un punto en la matriz (coordenadas CNC → ASCII)
    fn marcar(&mut self, x: f64, y: f64) {
        let ix = x.round() as isize;
        let iy = y.round() as isize;

        if ix >= 0 && iy >= 0 && (ix as usize) < self.ancho && (iy as usize) < self.alto {
            self.matriz[iy as usize][ix as usize] = '#';
        }
    }

    /// Procesa un programa CNC completo desde el buffer.
    pub fn simular(&mut self, buffer: &mut BufferCNC) {
        while let Some(linea) = buffer.pop() {
            if linea.starts_with('G') {
                self.procesar_gcode(&linea);
            }
        }
    }

    /// Procesa una línea G-code simple (G1, G2, G3).
    fn procesar_gcode(&mut self, linea: &str) {
        let mut x = None;
        let mut y = None;

        for token in linea.split_whitespace() {
            if token.starts_with('X') {
                x = token[1..].parse::<f64>().ok();
            } else if token.starts_with('Y') {
                y = token[1..].parse::<f64>().ok();
            }
        }

        if let (Some(px), Some(py)) = (x, y) {
            self.marcar(px, py);
        }
    }

    /// Devuelve la simulación ASCII completa.
    pub fn render(&self) -> String {
        self.matriz
            .iter()
            .rev()
            .map(|fila| fila.iter().collect::<String>())
            .collect::<Vec<String>>()
            .join("\n")
    }
}
