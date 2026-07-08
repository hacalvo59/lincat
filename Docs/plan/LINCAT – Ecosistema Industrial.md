# LINCAT – Ecosistema Industrial

Versión: 1.0  
Fecha: 2026-07-08  
Autor: Hugo Alberto Calvo

## 1. Identidad del Proyecto

LINCAT no es un CNC.  
LINCAT es un ecosistema industrial completo para automatización:

- CNC

- CAM

- Flujo industrial

- Bus multihilo

- Simulación

- Panel de control

- Motores geométricos

- Drivers

- Protocolos

- Scheduler

- Integración de máquinas

Todo bajo una filosofía: limpieza, modularidad, precisión y arquitectura industrial.

## 2. Tecnologías Base

- **Rust**: motor industrial, CNC, CAM, geometría, multihilo.

- **Slint**: interfaz gráfica CNC.

- **QTime**: base temporal para el bus multihilo.

- **Sin Python heredado**: todo lo viejo queda fuera del ecosistema.

## 3. Módulos del Ecosistema

- **lincat-engine** → motor geométrico + CNC + CAM + simulación.

- **lincat-panel** → UI Slint.

- **lincat-bus** → mensajería multihilo con QTime.

- **lincat-flow** → flujo industrial, estados, scheduler.

- **lincat-cam** → trayectorias, interpolaciones, G-code.

- **lincat-cnc** → driver, buffer, monitor, simulador.

- **docs** → documentación industrial.

Cada módulo es un “lego industrial”: independiente, limpio, reemplazable.

## 4. Filosofía de Diseño

- Separación estricta entre motor y UI.

- Multihilo seguro con Rust.

- Geometría determinista sin ruido numérico.

- Trayectorias puras y modulares.

- Exportadores limpios (G0/G1/G2/G3 + Z + helicoidal).

- Simulación integrada.

- Documentación viva.

- Arquitectura clara y mantenible.

## 5. Objetivo Final

Construir un ecosistema CNC/CAM industrial moderno, seguro, modular, nativo Linux, con arquitectura profesional y crecimiento sostenido.

