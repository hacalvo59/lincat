22\_real\_tecnica.md

Modo REAL Técnico del Ecosistema LINCAT

1. Propósito del Documento

Definir el modo REAL técnico utilizado por los módulos CNC‑CAT, FLOW, PLC, IO y EtherCAT dentro del ecosistema LINCAT.

Incluye señales físicas, parámetros de hardware, estructuras, dependencias y comportamiento determinístico del sistema sobre hardware real.


2. Alcance Técnico

Este documento describe:


modo REAL CNC,


modo REAL FLOW,


modo REAL IO,


modo REAL EtherCAT,


modo REAL seguridad,


parámetros técnicos,


estructuras de hardware.


No incluye visión conceptual ni arquitectura general.


3. Modo REAL CNC

3.1 Feedback de Ejes (Hardware)

drive\_pos\[N\] — posición real del drive.


drive\_vel\[N\] — velocidad real del drive.


drive\_status\[N\] — estado del drive.


drive\_fault\[N\] — fallo del drive.


drive\_safe\[N\] — canal seguro.


3.2 Feedback de Spindle (Hardware)

spindle\_speed\_feedback


spindle\_status


spindle\_fault


spindle\_safe


3.3 Movimiento REAL

trayectoria interpolada enviada a drives,


posición real = feedback EtherCAT,


velocidad real = feedback EtherCAT.


3.4 Señales CNC en modo REAL

axis\_feedback\_pos\[N\]


axis\_feedback\_vel\[N\]


spindle\_feedback


limit\_min\[N\]


limit\_max\[N\]


probe\_signal


4. Modo REAL FLOW

4.1 Sensores Industriales (Hardware)

sensor\_vacuum\_level


sensor\_air\_pressure


sensor\_lube\_flow


sensor\_hyd\_pressure


sensor\_coolant\_level


4.2 Actuadores Industriales (Hardware)

vacuum\_valve\_cmd


air\_valve\_cmd


lube\_pump\_cmd


hyd\_pump\_cmd


coolant\_pump\_cmd


4.3 Estados Auxiliares en modo REAL

VacuumReady


AirReady


LubeReady


HydraulicReady


CoolantReady


SafetyOk


ProcessReady


4.4 Señales FLOW en modo REAL

vacuum\_level


air\_pressure


lube\_flow


hydraulic\_pressure


coolant\_level


5. Modo REAL IO

5.1 IO Digital (Hardware)

din\[N\] — entradas digitales reales.


dout\[N\] — salidas digitales reales.


5.2 IO Analógico (Hardware)

ain\[N\] — entradas analógicas reales.


aout\[N\] — salidas analógicas reales.


5.3 IO Seguro (Hardware)

sin\[N\] — entradas seguras reales.


sout\[N\] — salidas seguras reales.


6. Modo REAL EtherCAT

6.1 Slaves en modo REAL

slave\_status\[N\]


slave\_fault\[N\]


slave\_online\[N\]


slave\_safe\_ok\[N\]


6.2 Drives en modo REAL

drive\_pos\[N\]


drive\_vel\[N\]


drive\_status\[N\]


drive\_fault\[N\]


drive\_safe\[N\]


6.3 FSoE en modo REAL

safe\_in\[N\]


safe\_out\[N\]


safe\_channel\_ok


safe\_channel\_fault


7. Modo REAL Seguridad

7.1 Señales de Seguridad (Hardware)

door\_closed


zone\_clear


estop\_released


safe\_motion\_ready


7.2 Estados de Seguridad (Hardware)

SafetyOk


SafetyFault


SafetyLock


8. Parámetros Técnicos del Modo REAL

8.1 Parámetros CNC

Código

real\_cnc:

  servo\_timeout\_ms: 200

  spindle\_timeout\_ms: 300

  feedback\_rate\_ms: 5

8.2 Parámetros FLOW

Código

real\_flow:

  sensor\_poll\_ms: 20

  actuator\_response\_ms: 10

8.3 Parámetros EtherCAT

Código

real\_ethercat:

  sync\_cycle\_us: 1000

  watchdog\_ms: 50

8.4 Parámetros Seguridad

Código

real\_safety:

  debounce\_ms: 5

  safe\_check\_ms: 10

9. Estructuras Técnicas del Modo REAL

9.1 Estructura CNC REAL

Código

struct REAL\_CNC \{

    float axis\_pos\[AXES\];

    float axis\_vel\[AXES\];

    float spindle\_speed;

    bool limits\_min\[AXES\];

    bool limits\_max\[AXES\];

    bool probe;

\};

9.2 Estructura FLOW REAL

Código

struct REAL\_FLOW \{

    float vacuum;

    float air;

    float lube;

    float hydraulic;

    float coolant;

    bool ready;

\};

9.3 Estructura IO REAL

Código

struct REAL\_IO \{

    bool din\[128\];

    bool dout\[128\];

    float ain\[64\];

    float aout\[64\];

    bool sin\[32\];

    bool sout\[32\];

\};

9.4 Estructura EtherCAT REAL

Código

struct REAL\_ECAT \{

    float drive\_pos\[AXES\];

    float drive\_vel\[AXES\];

    bool drive\_fault\[AXES\];

    bool safe\_ok;

\};

10. Equivalencia Técnica SIM ↔ REAL

mismas señales,


mismos estados,


mismas estructuras,


misma API,


diferencia: origen de señales (simuladas vs hardware).


11. Dependencias Técnicas

El modo REAL se integra con:


interfaces CNC


interfaces FLOW


señales PLC/IO


topología EtherCAT técnica


componentes industriales técnicos


API CNC‑CAT


API FLOW


simulación técnica


YAML técnico


12. Principios Técnicos

Modo REAL determinístico.


Señales físicas reproducibles.


Integración completa con EtherCAT.


Modularidad extrema.


Expansión sin romper estructura existente.


13. Estado del Documento

Documento técnico oficial.

Base para implementación del modo REAL en LINCAT.
