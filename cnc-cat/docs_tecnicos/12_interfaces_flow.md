12\_interfaces\_flow.md

Interfaces Técnicas del Módulo LINCAT‑FLOW

1. Propósito del Documento

Definir las interfaces técnicas del módulo FLOW dentro del ecosistema LINCAT.

Incluye señales industriales, estados auxiliares, entradas, salidas, estructuras y dependencias técnicas necesarias para el funcionamiento del camino FLOW.


2. Alcance Técnico

Este documento describe:


interfaces internas FLOW,


interfaces externas hacia CNC‑CAT, PLC, IO y EtherCAT,


señales industriales,


estados auxiliares,


estructuras técnicas,


dependencias de ejecución.


No incluye visión conceptual ni arquitectura general.


3. Interfaces Internas FLOW

Interfaces internas utilizadas por el motor industrial FLOW.


3.1 Interfaz de Servicios Industriales

vacuum\_sensor


air\_pressure\_sensor


lube\_flow\_sensor


hydraulic\_pressure\_sensor


coolant\_level\_sensor


3.2 Interfaz de Actuadores Industriales

vacuum\_valve\_cmd


air\_valve\_cmd


lube\_pump\_cmd


hydraulic\_pump\_cmd


coolant\_pump\_cmd


3.3 Interfaz de Alarmas Industriales

vacuum\_alarm


air\_alarm


lube\_alarm


hydraulic\_alarm


coolant\_alarm


4. Interfaces Externas FLOW

Interfaces hacia otros módulos del ecosistema.


4.1 Interfaz FLOW → CNC‑CAT

FLOW provee estados auxiliares:


VacuumReady


AirReady


LubeReady


HydraulicReady


CoolantReady


SafetyOk


ProcessReady


4.2 Interfaz FLOW → PLC

FLOW define señales que PLC ejecuta:


plc\_vacuum\_enable


plc\_air\_enable


plc\_lube\_enable


plc\_hydraulic\_enable


plc\_coolant\_enable


plc\_process\_step


plc\_alarm\_reset


4.3 Interfaz FLOW → IO

FLOW utiliza IO físico:


digital\_in\[N\]


digital\_out\[N\]


analog\_in\[N\]


analog\_out\[N\]


safe\_in\[N\]


safe\_out\[N\]


4.4 Interfaz FLOW → EtherCAT

FLOW consume datos EtherCAT:


slave\_status\[N\]


slave\_fault\[N\]


safe\_channel\_status\[N\]


safe\_channel\_fault\[N\]


io\_module\_status\[N\]


5. Señales Técnicas FLOW

Listado técnico de señales internas y externas.


5.1 Señales de Servicios Industriales

vacuum\_level


air\_pressure


lube\_flow


hydraulic\_pressure


coolant\_level


5.2 Señales de Actuación

cmd\_vacuum\_on


cmd\_air\_on


cmd\_lube\_on


cmd\_hydraulic\_on


cmd\_coolant\_on


5.3 Señales de Seguridad

door\_closed


zone\_clear


estop\_released


safe\_motion\_ready


safety\_channel\_ok


5.4 Señales de Proceso

process\_step


process\_ready


process\_alarm


process\_complete


6. Estados Auxiliares FLOW

Estados técnicos generados por FLOW y consumidos por CNC‑CAT.


Código

struct FLOW\_AuxStates \{

    bool VacuumReady;

    bool AirReady;

    bool LubeReady;

    bool HydraulicReady;

    bool CoolantReady;

    bool SafetyOk;

    bool ProcessReady;

\}

7. Estructuras Técnicas FLOW

7.1 Estructura de Componente Industrial

Código

struct FLOW\_Component \{

    int id;

    int type;

    float sensor\_value;

    bool actuator\_cmd;

    bool alarm;

    bool ready;

\}

7.2 Estructura de Estado FLOW

Código

struct FLOW\_State \{

    bool vacuum\_ok;

    bool air\_ok;

    bool lube\_ok;

    bool hydraulic\_ok;

    bool coolant\_ok;

    bool safety\_ok;

    bool process\_ok;

\}

7.3 Estructura de Señales IO

Código

struct FLOW\_IO \{

    bool din\[64\];

    bool dout\[64\];

    float ain\[32\];

    float aout\[32\];

    bool sin\[16\];

    bool sout\[16\];

\}

8. Dependencias Técnicas

FLOW depende técnicamente de:


PLC — ejecución de lógica industrial.


IO — señales físicas.


EtherCAT — módulos industriales y seguridad.


Seguridad — enclavamientos y zonas seguras.


Componentes industriales — sensores y actuadores.


CNC‑CAT depende de FLOW para habilitación segura.


9. Principios Técnicos

Interfaces industriales claras.


Estados auxiliares determinísticos.


Señales estables y reproducibles.


Modularidad extrema.


Integración mediante señales y estructuras.


Expansión sin romper interfaces existentes.


10. Estado del Documento

Documento técnico oficial.

Base para implementación del módulo FLOW.
