// ============================================================================
// LINCAT Industrial Engine - Module: Buffer CNC
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: CNC / BUFFER
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Buffer industrial para almacenar líneas G-code generadas por el motor
//     LINCAT antes de ser enviadas a la máquina CNC.
//
// Responsibilities:
//     - Almacenar G-code en orden determinista.
//     - Permitir push/pop seguro.
//     - Controlar overflow.
//     - Proveer estado industrial (Ready, Empty, Full).
//     - Integrarse con exportadores y drivers CNC.
//
// Contracts:
//     Input:  String (línea G-code).
//     Output: String (línea G-code).
// ============================================================================

use std::collections::VecDeque;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum BufferEstado {
    Empty,
    Ready,
    Full,
}

pub struct BufferCNC {
    capacidad: usize,
    cola: VecDeque<String>,
}

impl BufferCNC {
    /// Crea un buffer CNC con capacidad fija.
    pub fn new(capacidad: usize) -> Self {
        Self {
            capacidad,
            cola: VecDeque::with_capacity(capacidad),
        }
    }

    /// Estado industrial del buffer.
    pub fn estado(&self) -> BufferEstado {
        if self.cola.is_empty() {
            BufferEstado::Empty
        } else if self.cola.len() >= self.capacidad {
            BufferEstado::Full
        } else {
            BufferEstado::Ready
        }
    }

    /// Inserta una línea G-code en el buffer.
    pub fn push(&mut self, linea: String) -> Result<(), &'static str> {
        if self.cola.len() >= self.capacidad {
            return Err("Buffer CNC lleno");
        }
        self.cola.push_back(linea);
        Ok(())
    }

    /// Extrae la siguiente línea G-code.
    pub fn pop(&mut self) -> Option<String> {
        self.cola.pop_front()
    }

    /// Cantidad de líneas almacenadas.
    pub fn len(&self) -> usize {
        self.cola.len()
    }

    /// Limpia el buffer.
    pub fn clear(&mut self) {
        self.cola.clear();
    }

    /// Exporta todo el contenido como un programa CNC completo.
    pub fn exportar_programa(&self) -> String {
        self.cola
            .iter()
            .map(|l| l.clone())
            .collect::<Vec<String>>()
            .join("\n")
    }
}
