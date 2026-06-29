23\_integracion\_tecnica.md

Integración Técnica Completa del Ecosistema LINCAT

1. Propósito del Documento

Definir la integración técnica entre los módulos CNC‑CAT, FLOW, PLC/IO, EtherCAT, Seguridad, SIM y REAL dentro del ecosistema LINCAT.

Incluye señales, estados, dependencias, sincronización, flujo de datos y estructuras industriales.


2. Alcance Técnico

Este documento describe:


integración CNC ↔ FLOW,


integración CNC ↔ PLC/IO,


integración FLOW ↔ PLC/IO,


integración con EtherCAT,


integración de seguridad,


integración SIM ↔ REAL,


sincronización industrial,


flujo técnico de datos.


No incluye visión conceptual ni arquitectura general.


3. Integración CNC ↔ FLOW

3.1 Señales FLOW consumidas por CNC

VacuumReady


AirReady


LubeReady


HydraulicReady


CoolantReady


SafetyOk


ProcessReady


3.2 Señales CNC dependientes de FLOW

motion\_ready


servo\_enable


spindle\_enable


interp\_active


3.3 API utilizada

CNC\_CheckFlowReady


FLOW\_GetAuxStates


4. Integración CNC ↔ PLC/IO

4.1 Señales PLC consumidas por CNC

plc\_servo\_enable


plc\_spindle\_enable


plc\_tool\_change\_ready


plc\_probe\_ready


plc\_cycle\_start


plc\_cycle\_stop


4.2 Señales IO consumidas por CNC

limit\_min\[N\]


limit\_max\[N\]


probe\_signal


estop\_signal


door\_signal


axis\_fault\[N\]


spindle\_fault


4.3 API utilizada

CNC\_GetAxisFeedback


CNC\_GetFaults


5. Integración FLOW ↔ PLC/IO

5.1 Señales PLC ejecutadas por FLOW

plc\_vacuum\_enable


plc\_air\_enable


plc\_lube\_enable


plc\_hydraulic\_enable


plc\_coolant\_enable


plc\_alarm\_reset


5.2 Señales IO consumidas por FLOW

digital\_in\[N\]


analog\_in\[N\]


safe\_in\[N\]


5.3 API utilizada

FLOW\_ReadSensor


FLOW\_ActuatorOn


6. Integración con EtherCAT

6.1 Drives CNC

drive\_pos\[N\]


drive\_vel\[N\]


drive\_status\[N\]


drive\_fault\[N\]


drive\_safe\[N\]


6.2 IO EtherCAT

din\[N\]


dout\[N\]


ain\[N\]


aout\[N\]


6.3 FSoE

sin\[N\]


sout\[N\]


safe\_channel\_ok


safe\_channel\_fault


6.4 Topología utilizada

topología EtherCAT técnica


7. Integración de Seguridad

7.1 Señales de seguridad

door\_closed


zone\_clear


estop\_released


safe\_motion\_ready


7.2 Estados de seguridad

SafetyOk


SafetyFault


SafetyLock


7.3 Módulos FSoE

safe\_in\[N\]


safe\_out\[N\]


7.4 API utilizada

FLOW\_GetSafetyStatus


CNC\_GetFaults


8. Integración SIM ↔ REAL

8.1 Equivalencia técnica

mismas señales,


mismos estados,


mismas estructuras,


misma API,


diferencia: origen de señales.


8.2 Archivos YAML utilizados

sim.yaml


real.yaml


8.3 Estructuras utilizadas

SIM\_CNC, REAL\_CNC


SIM\_FLOW, REAL\_FLOW


SIM\_IO, REAL\_IO


SIM\_ECAT, REAL\_ECAT


9. Sincronización Industrial

9.1 Sincronización CNC ↔ EtherCAT

ciclo DC EtherCAT,


feedback determinístico,


actualización de drives.


9.2 Sincronización FLOW ↔ IO

lectura periódica de sensores,


actualización de actuadores.


9.3 Sincronización Seguridad

verificación continua de canales seguros.


9.4 Parámetros técnicos

Código

sync:

  ethercat\_cycle\_us: 1000

  cnc\_feedback\_ms: 5

  flow\_poll\_ms: 20

  safety\_check\_ms: 10

10. Flujo Técnico de Datos

10.1 Flujo CNC

Código

G-code → Interpolador → Drives → Feedback → CNC\_State

10.2 Flujo FLOW

Código

Sensores → FLOW\_State → Actuadores → AuxStates → CNC

10.3 Flujo IO

Código

IO físico → PLC → FLOW/CNC → EtherCAT → Hardware

10.4 Flujo Seguridad

Código

FSoE → SafetyState → FLOW/CNC → Bloqueos

11. Dependencias Técnicas

La integración técnica depende de:


interfaces CNC


interfaces FLOW


señales PLC/IO


estados CNC


estados FLOW


topología EtherCAT técnica


componentes industriales técnicos


API CNC‑CAT


API FLOW


simulación técnica


REAL técnico


YAML técnico


12. Principios Técnicos

Integración determinística.


Señales estables.


Estados reproducibles.


Modularidad extrema.


Expansión sin romper estructura existente.


13. Estado del Documento

Documento técnico oficial.

Base para integración completa del ecosistema LINCAT.
