// ============================================================================
// LINCAT Industrial Engine - Driver CNC Real (Serial/TCP Abstracción)
// Author: Hugo Alberto Calvo
// Component Type: CNC / DRIVER REAL
// Description:
//     Capa industrial para enviar G-code a una máquina real mediante
//     un canal genérico (serial, TCP, etc.).
//     NOTA: aquí se define la abstracción; la implementación concreta
//     depende del entorno (libs de serial, sockets, etc.).
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum EstadoDriverReal {
    Desconectado,
    Conectado,
    Error,
}

pub trait CanalCNC {
    fn conectar(&mut self) -> Result<(), String>;
    fn enviar_linea(&mut self, linea: &str) -> Result<(), String>;
    fn desconectar(&mut self) -> Result<(), String>;
}

/// Implementación dummy para pruebas (no habla con hardware real).
pub struct CanalDummy {
    pub nombre: String,
    pub conectado: bool,
}

impl CanalDummy {
    pub fn new(nombre: &str) -> Self {
        Self {
            nombre: nombre.to_string(),
            conectado: false,
        }
    }
}

impl CanalCNC for CanalDummy {
    fn conectar(&mut self) -> Result<(), String> {
        self.conectado = true;
        println!("[CANAL DUMMY] Conectado a '{}'", self.nombre);
        Ok(())
    }

    fn enviar_linea(&mut self, linea: &str) -> Result<(), String> {
        if !self.conectado {
            return Err("Canal no conectado".into());
        }
        println!("[CANAL DUMMY] → {}", linea);
        Ok(())
    }

    fn desconectar(&mut self) -> Result<(), String> {
        self.conectado = false;
        println!("[CANAL DUMMY] Desconectado de '{}'", self.nombre);
        Ok(())
    }
}

pub struct DriverCNCReal<C: CanalCNC> {
    pub estado: EstadoDriverReal,
    pub canal: C,
}

impl<C: CanalCNC> DriverCNCReal<C> {
    pub fn new(canal: C) -> Self {
        Self {
            estado: EstadoDriverReal::Desconectado,
            canal,
        }
    }

    pub fn conectar(&mut self) -> Result<(), String> {
        self.canal.conectar()?;
        self.estado = EstadoDriverReal::Conectado;
        Ok(())
    }

    pub fn enviar_linea(&mut self, linea: &str) -> Result<(), String> {
        self.canal.enviar_linea(linea)
    }

    pub fn desconectar(&mut self) -> Result<(), String> {
        self.canal.desconectar()?;
        self.estado = EstadoDriverReal::Desconectado;
        Ok(())
    }
}
