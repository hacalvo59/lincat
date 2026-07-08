// ============================================================================
// LINCAT Industrial Engine - Simulador CNC 3D (wireframe ASCII)
// Author: Hugo Alberto Calvo
// Component Type: CNC / SIMULADOR 3D
// Description:
//     Proyecta trayectoria CNC (X,Y,Z) a vista 3D isométrica en ASCII.
// ============================================================================

use crate::lincat_engine::cnc::buffer_cnc::BufferCNC;

#[derive(Debug, Clone)]
pub struct SimuladorCNC3D {
    ancho: usize,
    alto: usize,
    matriz: Vec<Vec<char>>,
}

impl SimuladorCNC3D {
    pub fn new(ancho: usize, alto: usize) -> Self {
        Self {
            ancho,
            alto,
            matriz: vec![vec!['.'; ancho]; alto],
        }
    }

    fn marcar_iso(&mut self, x: f64, y: f64, z: f64) {
        // proyección isométrica simple
        let sx = x - y;
        let sy = (x + y) * 0.5 - z;

        let ix = sx.round() as isize;
        let iy = sy.round() as isize;

        if ix >= 0 && iy >= 0 && (ix as usize) < self.ancho && (iy as usize) < self.alto {
            self.matriz[iy as usize][ix as usize] = '#';
        }
    }

    fn procesar_gcode(&mut self, linea: &str) {
        let mut x = None;
        let mut y = None;
        let mut z = Some(0.0);

        for token in linea.split_whitespace() {
            if token.starts_with('X') {
                x = token[1..].parse::<f64>().ok();
            } else if token.starts_with('Y') {
                y = token[1..].parse::<f64>().ok();
            } else if token.starts_with('Z') {
                z = token[1..].parse::<f64>().ok();
            }
        }

        if let (Some(px), Some(py), Some(pz)) = (x, y, z) {
            self.marcar_iso(px, py, pz);
        }
    }

    pub fn simular(&mut self, buffer: &mut BufferCNC) {
        while let Some(linea) = buffer.pop() {
            if linea.starts_with('G') {
                self.procesar_gcode(&linea);
            }
        }
    }

    pub fn render(&self) -> String {
        self.matriz
            .iter()
            .rev()
            .map(|fila| fila.iter().collect::<String>())
            .collect::<Vec<String>>()
            .join("\n")
    }
}
