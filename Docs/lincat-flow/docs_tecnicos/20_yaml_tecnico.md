20\_yaml\_tecnico.md

Estructuras YAML Técnicas del Ecosistema LINCAT

1. Propósito del Documento

Definir las estructuras YAML técnicas utilizadas por los módulos CNC‑CAT, FLOW, PLC, IO y EtherCAT dentro del ecosistema LINCAT.

Incluye configuraciones, parámetros, estados, señales, topologías y dependencias industriales.


2. Alcance Técnico

Este documento describe:


YAML de configuración CNC,


YAML de configuración FLOW,


YAML de IO,


YAML de EtherCAT,


YAML de seguridad,


YAML de componentes industriales,


YAML de simulación y modo REAL.


No incluye visión conceptual ni arquitectura general.


3. YAML de Configuración CNC

3.1 cnc.yaml

Código

cnc:

  axes: 3

  homing:

    sequence: \[X, Y, Z\]

    velocity: 200

    accel: 300

  spindle:

    max\_speed: 12000

    min\_speed: 500

  feed:

    default: 1500

    rapid: true

4. YAML de Configuración FLOW

4.1 flow.yaml

Código

flow:

  vacuum:

    min\_level: -0.6

    max\_level: -0.9

    alarm\_threshold: -0.5

  air:

    min\_pressure: 5.0

    max\_pressure: 8.0

    alarm\_threshold: 4.5

  lube:

    min\_flow: 0.2

    max\_flow: 1.0

  hydraulic:

    min\_pressure: 80

    max\_pressure: 120

  coolant:

    min\_level: 20

    max\_level: 100

5. YAML de IO

5.1 io.yaml

Código

io:

  digital\_in:

    - di\_estop

    - di\_door

    - di\_probe

    - di\_limit\_min\_x

    - di\_limit\_max\_x

    - di\_limit\_min\_y

    - di\_limit\_max\_y

    - di\_limit\_min\_z

    - di\_limit\_max\_z


  digital\_out:

    - do\_servo\_enable

    - do\_spindle\_enable

    - do\_tool\_change

    - do\_probe\_enable


  analog\_in:

    - ai\_air\_pressure

    - ai\_vacuum\_level

    - ai\_lube\_flow

    - ai\_hydraulic\_pressure

    - ai\_coolant\_level


  analog\_out:

    - ao\_spindle\_speed\_cmd

    - ao\_axis\_vel\_cmd\_x

    - ao\_axis\_vel\_cmd\_y

    - ao\_axis\_vel\_cmd\_z

6. YAML de EtherCAT

6.1 ethercat.yaml

Código

ethercat:

  master: ECAT\_MASTER\_0

  slaves:

    - id: 1

      type: drive\_axis

      axis: X

    - id: 2

      type: drive\_axis

      axis: Y

    - id: 3

      type: drive\_axis

      axis: Z

    - id: 4

      type: drive\_spindle

    - id: 5

      type: io\_digital

      channels: 32

    - id: 6

      type: io\_analog

      channels: 16

    - id: 7

      type: fsoe

      safe\_channels: 8

7. YAML de Seguridad

7.1 safety.yaml

Código

safety:

  door:

    sensor: sin\_door\_safe

    lock: lock\_door

  zone:

    sensor: sin\_zone\_safe

    lock: lock\_zone

  estop:

    sensor: sin\_estop\_safe

  spindle:

    safe\_channel: sin\_spindle\_safe

  motion:

    safe\_channel: sin\_drive\_safe

8. YAML de Componentes Industriales

8.1 components.yaml

Código

components:

  vacuum:

    sensor: sensor\_vacuum\_level

    actuator: vacuum\_valve\_cmd

    ready\_threshold: -0.7


  air:

    sensor: sensor\_air\_pressure

    actuator: air\_valve\_cmd

    ready\_threshold: 6.0


  lube:

    sensor: sensor\_lube\_flow

    actuator: lube\_pump\_cmd

    ready\_threshold: 0.3


  hydraulic:

    sensor: sensor\_hyd\_pressure

    actuator: hyd\_pump\_cmd

    ready\_threshold: 90


  coolant:

    sensor: sensor\_coolant\_level

    actuator: coolant\_pump\_cmd

    ready\_threshold: 30

9. YAML de Simulación

9.1 sim.yaml

Código

sim:

  enabled: true

  cnc:

    feedback\_noise: 0.01

    spindle\_noise: 5

  flow:

    sensor\_noise: 0.05

    actuator\_delay\_ms: 50

10. YAML de Modo REAL

10.1 real.yaml

Código

real:

  enabled: true

  ethercat:

    sync\_cycle\_us: 1000

  cnc:

    servo\_timeout\_ms: 200

  flow:

    sensor\_poll\_ms: 20

11. Dependencias Técnicas

Las estructuras YAML se integran con:


interfaces CNC


interfaces FLOW


señales PLC/IO


topología EtherCAT técnica


componentes industriales técnicos


API CNC‑CAT


API FLOW


12. Principios Técnicos

YAML determinístico.


Estructuras estables.


Modularidad extrema.


Integración mediante archivos de configuración.


Expansión sin romper estructuras existentes.


13. Estado del Documento

Documento técnico oficial.

Base para configuración del ecosistema LINCAT.
