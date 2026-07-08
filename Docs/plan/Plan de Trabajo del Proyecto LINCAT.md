# Plan de Trabajo del Proyecto LINCAT

Versión: 1.0  
Fecha: 2026-07-08

## 1. Estado Actual

- Motor Rust (lincat-engine) subido y a salvo.

- UI Slint (lincat-panel) subido y separada.

- Documentación limpia.

- Código heredado descartado.

- Repo en estado industrial inicial.

## 2. Orden de Construcción

### Etapa 1 — Núcleo geométrico (COMPLETADO)

- Vector3D, Matriz3x3

- Transformaciones 3D

- Distancias, ángulos, intersecciones

- Normalizaciones y tolerancias

### Etapa 2 — Trayectorias (EN PROCESO)

- Lineal

- Circular

- Helicoidal

- Spline

- Offset

- Interpolaciones

### Etapa 3 — CAM

- Generador G-code

- Setup G-code

- Export helicoidal G2/G3 + Z

- Postprocesadores industriales

### Etapa 4 — CNC

- Driver

- Buffer

- Monitor

- Simulador CNC

- Estados y control

### Etapa 5 — Bus Industrial (PENDIENTE)

- lincat-bus

- Mensajería ida/vuelta

- QTime

- Scheduler

- Operaciones

- Multihilo seguro

### Etapa 6 — Flow Industrial (PENDIENTE)

- lincat-flow

- Estados del sistema

- Flujo de trabajo

- Integración con bus

### Etapa 7 — Panel CNC (EN PROCESO)

- Slint UI

- Pantallas

- Componentes

- Temas

- Integración con motor

## 3. Cómo saber dónde estamos

Cada commit debe indicar:

- Módulo afectado

- Etapa del plan

- Avance concreto

Ejemplo: “CAM: agrego export helicoidal G2/G3 + Z (Etapa 3)”

## 4. Cómo seguir

Siempre avanzar módulo por módulo.  
Nunca mezclar UI con motor.  
Nunca mezclar CNC con CAM.  
Nunca mezclar Flow con Bus.  
Documentar cada decisión arquitectónica.

