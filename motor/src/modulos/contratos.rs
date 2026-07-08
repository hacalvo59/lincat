// ============================================================================
// LINCAT Industrial Engine - Module: contratos
// Author: Hugo Alberto Calvo
// Architecture: Deterministic Multi-Core V12
// Component Type: MODULOS / CONTRACTS
// Version: 0.1.0
// Stability: Experimental
// Description:
//     Contratos industriales para módulos HF/MF/LF del motor LINCAT.
//
// Responsibilities:
//     - Definir interfaz común para todos los módulos.
//     - Garantizar compatibilidad con BUS Ida / Interno / Vuelta.
//     - Proveer tipo de módulo para el scheduler.
//     - Asegurar determinismo en ejecución.
//
// Contracts:
//     Input:  TaskIn (JSON Entrada).
//     Output: serde_json::Value (resultado industrial).
//     Tipo:   HF / MF / LF.
//
// Notes:
//     - No lógica aquí: solo contratos.
//     - Módulos reales se implementan en carpetas HF/MF/LF.
// ============================================================================

use serde_json::Value;

/// Tipos de módulo industrial.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum TipoModulo {
    HF, // High Frequency
    MF, // Medium Frequency
    LF, // Low Frequency
}

/// Contrato que todos los módulos deben implementar.
pub trait ModuloEjecutable {
    /// Tipo del módulo (HF/MF/LF).
    fn tipo(&self) -> TipoModulo;

    /// Ejecución industrial del módulo.
    fn ejecutar(&self, entrada: &crate::lincat_engine::json::entrada::TaskIn) -> Value;
}
