43\_arquitectura\_global\_CNC\_CAT.md

Arquitectura global del motor CNC‑CAT

1. Propósito del documento

Definir la arquitectura global del motor CNC‑CAT: capas internas, módulos, modelos de estado, modelos de señal, integración con LINCAT (UI), integración con FLOW, PLC/IO, EtherCAT, seguridad y entornos REAL/SIM, usando una Motion API única.


2. Visión general del sistema

2.1 Capas principales

UI LINCAT


Motion API


Motor CNC‑CAT


FLOW industrial


PLC/IO + EtherCAT + Seguridad


REAL / SIM


2.2 Diagrama lógico

text

\[ Usuario \]

    ↓

\[ UI LINCAT \]

    ↓

\[ Motion API \]

    ↓

\[ Motor CNC‑CAT \]

    ↓

\[ FLOW / PLC-IO / EtherCAT / Seguridad \]

    ↓

\[ REAL / SIM \]

3. Capas internas del motor CNC‑CAT

3.1 Interp Layer (Interpolación)

Responsabilidad: generar trayectorias (lineales, circulares, spline).


Entradas: bloques de programa, límites, estados de máquina.


Salidas: consignas de posición/velocidad por eje.


3.2 Servo Layer

Responsabilidad: cerrar lazo de posición/velocidad.


Entradas: consignas de interpolación, feedback de drives.


Salidas: órdenes de movimiento a EtherCAT/drives.


3.3 Spindle Layer

Responsabilidad: control de velocidad, dirección y estado del husillo.


Entradas: comandos de programa, estados de seguridad.


Salidas: consignas de velocidad y estado a variador.


3.4 Tool Layer

Responsabilidad: gestión de herramientas y offsets.


Entradas: tabla de herramientas, comandos de cambio/compensación.


Salidas: offsets aplicados a interpolación y estados de herramienta.


3.5 State Layer

Responsabilidad: estados globales del motor.


Estados: Idle, Ready, Homing, Running, Paused, Stopped, Error.


3.6 Fault Layer

Responsabilidad: gestión de fallos determinísticos.


Tipos: fallos de eje, spindle, interpolación, seguridad, comunicación.


4. Modelo de estado global CNC‑CAT

yaml

CNC\_State:

  mode: Idle/Ready/Homing/Running/Paused/Stopped/Error

  program:

    loaded: bool

    name: string

    line\_current: int

    line\_total: int

  axes:

    - id: X/Y/Z/...

      pos: float

      vel: float

      fault: bool

  spindle:

    speed\_cmd: float

    speed\_fb: float

    direction: CW/CCW

    enabled: bool

    fault: bool

  tools:

    current\_tool: int

    offset\_len: float

    offset\_rad: float

  safety:

    safety\_ok: bool

    safety\_fault: bool

    safety\_lock: bool

5. Modelo de señal global CNC‑CAT

5.1 Señales internas críticas

Movimiento:


servo\_enable


axis\_pos\[N\]


axis\_vel\[N\]


axis\_fault\[N\]


Spindle:


spindle\_enable


spindle\_speed\_cmd


spindle\_speed\_fb


spindle\_fault


Interpolación:


interp\_active


block\_done


program\_end


Seguridad:


safety\_ok


safety\_fault


safety\_lock


6. Motion API global CNC‑CAT

La Motion API es el contrato único entre UI LINCAT y el motor CNC‑CAT.


6.1 Comandos principales

Carga y control de programa


CNC\_LoadProgram(path)


CNC\_Start()


CNC\_Pause()


CNC\_Resume()


CNC\_Stop()


Movimiento directo


CNC\_CommandMove(axis, pos, vel)


CNC\_Jog(axis, vel)


Herramientas


CNC\_SetTool(tool\_id)


CNC\_SetToolOffset(tool\_id, len, rad)


Estado y fallos


CNC\_GetState()


CNC\_GetFaults()


CNC\_ResetFaults()


7. Integración con FLOW, PLC/IO, EtherCAT y seguridad

7.1 CNC‑CAT ↔ FLOW

CNC‑CAT consume estados auxiliares:


VacuumReady, AirReady, LubeReady, HydraulicReady, CoolantReady.


FLOW garantiza condiciones industriales antes de CNC\_Start().


7.2 CNC‑CAT ↔ PLC/IO

Entradas críticas: estop, door, limits, probe.


Salidas: cycle\_start, cycle\_stop, señales de estado.


7.3 CNC‑CAT ↔ EtherCAT

Consumo de feedback de drives (posición, velocidad, estado).


Emisión de consignas determinísticas a cada eje y al spindle.


Sincronización con ciclo DC (p.ej. 1000 µs).


7.4 CNC‑CAT ↔ Seguridad

Estados: SafetyOk, SafetyFault, SafetyLock.


El motor no ejecuta movimiento si SafetyOk == false.


8. Arquitectura REAL / SIM

8.1 Principio de equivalencia

Misma Motion API.


Mismo modelo de estado.


Mismo modelo de señal.


Diferente origen de datos (hardware vs simulación).


8.2 Configuración REAL

yaml

real\_cnc\_cat.yaml:

  ecat:

    cycle\_us: 1000

    slaves: \[...\]

  axes:

    - id: X

      limits: \[...\]

      drive\_id: ...

  spindle:

    drive\_id: ...

  safety:

    fsoe\_channels: \[...\]

8.3 Configuración SIM

yaml

sim\_cnc\_cat.yaml:

  simulate\_motion: true

  axes:

    - id: X

      model: ideal

  spindle:

    model: ideal

  noise:

    pos\_mm: 0.01

    vel\_mm\_s: 0.1

9. Integración con UI LINCAT

9.1 Principio

La UI solo ve la Motion API, nunca el hardware.


9.2 Flujo

El usuario actúa en LINCAT.


LINCAT llama a la Motion API.


CNC‑CAT ejecuta sobre REAL o SIM.


CNC‑CAT devuelve estado y eventos.


LINCAT actualiza DRO, alarmas, paneles.


10. Criterios de diseño global CNC‑CAT

Determinismo: ciclo de control estable y reproducible.


Modularidad: capas internas independientes (interp, servo, spindle, tools, state, fault).


Escalabilidad: posibilidad de añadir ejes, herramientas, procesos.


Interoperabilidad: integración limpia con FLOW, PLC/IO, EtherCAT, seguridad.


Simulación/Real equivalentes: misma API, mismo modelo de estado.


11. Estado del documento

Documento técnico oficial.

Base de la arquitectura global del motor CNC‑CAT dentro del ecosistema LINCAT.
