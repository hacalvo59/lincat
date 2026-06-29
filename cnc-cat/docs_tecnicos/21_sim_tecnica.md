21\_sim\_tecnica.md

Simulación Técnica del Ecosistema LINCAT

1. Propósito del Documento

Definir la simulación técnica utilizada por los módulos CNC‑CAT, FLOW, PLC, IO y EtherCAT dentro del ecosistema LINCAT.

Incluye señales simuladas, modelos, estructuras, parámetros, equivalencias y dependencias industriales.


2. Alcance Técnico

Este documento describe:


simulación CNC,


simulación FLOW,


simulación IO,


simulación EtherCAT,


simulación de seguridad,


parámetros técnicos,


estructuras de simulación.


No incluye visión conceptual ni arquitectura general.


3. Simulación Técnica CNC

3.1 Feedback de Ejes

Código

sim\_cnc:

  axis\_feedback:

    noise: 0.01

    update\_rate\_ms: 5

3.2 Feedback de Spindle

Código

sim\_cnc:

  spindle\_feedback:

    noise: 5

    update\_rate\_ms: 10

3.3 Movimiento Simulado

trayectoria interpolada generada sin hardware,


posición simulada = posición objetivo + ruido,


velocidad simulada = velocidad objetivo + ruido.


3.4 Señales Simuladas CNC

sim\_axis\_pos\[N\]


sim\_axis\_vel\[N\]


sim\_spindle\_speed


sim\_limit\_min\[N\]


sim\_limit\_max\[N\]


sim\_probe\_signal


4. Simulación Técnica FLOW

4.1 Sensores Industriales Simulados

Código

sim\_flow:

  sensors:

    vacuum\_noise: 0.05

    air\_noise: 0.05

    lube\_noise: 0.05

    hydraulic\_noise: 0.05

    coolant\_noise: 0.05

4.2 Actuadores Industriales Simulados

Código

sim\_flow:

  actuators:

    delay\_ms: 50

4.3 Estados Auxiliares Simulados

VacuumReady


AirReady


LubeReady


HydraulicReady


CoolantReady


SafetyOk


ProcessReady


4.4 Señales Simuladas FLOW

sim\_vacuum\_level


sim\_air\_pressure


sim\_lube\_flow


sim\_hydraulic\_pressure


sim\_coolant\_level


5. Simulación Técnica IO

5.1 IO Digital Simulado

Código

sim\_io:

  digital:

    update\_rate\_ms: 2

Señales:


sim\_din\[N\]


sim\_dout\[N\]


5.2 IO Analógico Simulado

Código

sim\_io:

  analog:

    noise: 0.02

    update\_rate\_ms: 5

Señales:


sim\_ain\[N\]


sim\_aout\[N\]


5.3 IO Seguro Simulado

Código

sim\_io:

  safe:

    stable: true

Señales:


sim\_sin\[N\]


sim\_sout\[N\]


6. Simulación Técnica EtherCAT

6.1 Slaves Simulados

Código

sim\_ethercat:

  slaves:

    online: true

    fault\_probability: 0.0

6.2 Drives Simulados

Código

sim\_ethercat:

  drives:

    pos\_noise: 0.01

    vel\_noise: 0.02

Señales:


sim\_drive\_pos\[N\]


sim\_drive\_vel\[N\]


sim\_drive\_status\[N\]


sim\_drive\_fault\[N\]


6.3 FSoE Simulado

Código

sim\_ethercat:

  fsoe:

    safe\_ok: true

    fault\_probability: 0.0

Señales:


sim\_safe\_in\[N\]


sim\_safe\_out\[N\]


sim\_safe\_ok


7. Simulación Técnica de Seguridad

7.1 Señales Simuladas de Seguridad

sim\_door\_closed


sim\_zone\_clear


sim\_estop\_released


sim\_safe\_motion\_ready


7.2 Estados Simulados de Seguridad

Código

sim\_safety:

  stable: true

  alarm\_probability: 0.0

8. Estructuras Técnicas de Simulación

8.1 Estructura de Simulación CNC

Código

struct SIM\_CNC \{

    float axis\_pos\[AXES\];

    float axis\_vel\[AXES\];

    float spindle\_speed;

    bool limits\_min\[AXES\];

    bool limits\_max\[AXES\];

    bool probe;

\};

8.2 Estructura de Simulación FLOW

Código

struct SIM\_FLOW \{

    float vacuum;

    float air;

    float lube;

    float hydraulic;

    float coolant;

    bool ready;

\};

8.3 Estructura de Simulación IO

Código

struct SIM\_IO \{

    bool din\[128\];

    bool dout\[128\];

    float ain\[64\];

    float aout\[64\];

    bool sin\[32\];

    bool sout\[32\];

\};

8.4 Estructura de Simulación EtherCAT

Código

struct SIM\_ECAT \{

    float drive\_pos\[AXES\];

    float drive\_vel\[AXES\];

    bool drive\_fault\[AXES\];

    bool safe\_ok;

\};

9. Equivalencia Técnica SIM ↔ REAL

mismas señales,


mismos estados,


mismas estructuras,


misma API,


mismo flujo de datos,


diferencia: origen de señales.


10. Dependencias Técnicas

La simulación técnica se integra con:


interfaces CNC


interfaces FLOW


señales PLC/IO


topología EtherCAT técnica


API CNC‑CAT


API FLOW


YAML técnico


11. Principios Técnicos

Simulación determinística.


Señales reproducibles.


Equivalencia completa con modo REAL.


Modularidad extrema.


Expansión sin romper estructura existente.


12. Estado del Documento

Documento técnico oficial.

Base para implementación del modo SIM en LINCAT.
