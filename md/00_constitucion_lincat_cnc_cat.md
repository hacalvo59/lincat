# 00 – Constitución del ecosistema LINCAT / CNC‑CAT

## 1. Filosofía general

- **Libertad:**  
El ecosistema LINCAT / CNC‑CAT es libre y abierto, bajo licencia GPLv3.

- **Estándar mundial:**  
El objetivo es construir un estándar industrial, modular y claro, accesible para cualquiera que respete las normas.

- **Independencia:**  
El motor CNC‑CAT, la lógica PLC y la UI LINCAT son propios, no dependen de motores de terceros, sean libres o no.

- **Descendencia:**  
Todo se diseña de arriba hacia abajo: visión → arquitectura → módulos → interfaces → implementación.  
No se programan “parches”; se construyen bloques completos y coherentes.


## 2. Nombre y identidad del proyecto

- **Nombre obligatorio:**  
Cualquier uso, fork o derivado debe mantener explícitamente los nombres:

  - `LINCAT`

  - `CNC‑CAT`

- **Reconocimiento mínimo:**  
En toda documentación, UI o presentación técnica debe aparecer la referencia al ecosistema original LINCAT / CNC‑CAT.


## 3. Normas de modificación y aportes

- **Documento previo obligatorio (`.md`):**  
Antes de cambiar código, arquitectura o normas, se debe crear un archivo `.md` que contenga:

  - **Qué se modifica.**

  - **Por qué se modifica.**

  - **Qué problema resuelve.**

  - **Cómo se implementa.**

  - **Qué impacto tiene en otros módulos.**

- **Coherencia con normas existentes:**  
Ningún cambio puede contradecir las normas ya definidas sin una justificación clara y un rediseño descendente del bloque afectado.

- **Estilo limpio y prolijo:**  
Toda propuesta debe ser:

  - clara,

  - ordenada,

  - modular,

  - fácil de entender,

  - alineada con la filosofía industrial del proyecto.


## 4. Normas de programación y lógica

- **Modularidad estricta:**  
Cada módulo (CNC‑CAT, PLC, EtherCAT, Motion, UI, SIM/REAL, etc.) debe tener:

  - responsabilidades claras,

  - interfaces definidas,

  - límites precisos.

- **Separación SIM / REAL:**  
Toda funcionalidad que interactúe con hardware debe tener una contraparte de simulación, con la misma interfaz, para pruebas seguras.

- **Determinismo y seguridad:**  
Las decisiones de diseño deben priorizar:

  - comportamiento determinista,

  - seguridad de operación,

  - trazabilidad de estados.


## 5. Gobernanza del ecosistema

- **El proyecto es de todos:**  
LINCAT / CNC‑CAT pertenece a la comunidad que lo construye y lo respeta.

- **Visión fundacional:**  
La visión original (libre, independiente, modular, estándar mundial) no puede ser eliminada ni ocultada.

- **Responsabilidad ética:**  
Quien aporte al proyecto acepta:

  - respetar la filosofía,

  - no romper el estándar por capricho,

  - documentar cada cambio,

  - pensar en el impacto a largo plazo.


## 6. Espíritu del proyecto

LINCAT / CNC‑CAT no es solo código:

- es una forma de trabajar,

- una forma de pensar,

- una forma de documentar,

- una forma de compartir.

Todo se hace:

- **bajo las mismas normas**,

- **con la misma filosofía descendente**,

- **limpio**,

- **prolijo**,

- **paso a paso**,

- como queremos que lo hagan quienes se sumen al estándar.

