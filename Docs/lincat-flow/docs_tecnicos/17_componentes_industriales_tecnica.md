17\_componentes\_industriales\_tecnica.md

Componentes Industriales Técnicos del Ecosistema LINCAT

1. Propósito del Documento

Definir los componentes industriales técnicos utilizados por el módulo FLOW dentro del ecosistema LINCAT.

Incluye sensores, actuadores, parámetros técnicos, señales asociadas, estructuras y dependencias industriales.


2. Alcance Técnico

Este documento describe:


componentes eléctricos,


componentes neumáticos,


componentes hidráulicos,


sensores industriales,


actuadores industriales,


módulos EtherCAT,


parámetros técnicos,


estructuras de datos.


No incluye visión conceptual ni wiring físico.


3. Componentes Eléctricos Técnicos

3.1 Sensores Eléctricos

sensor\_voltage


sensor\_current


sensor\_temp\_electric


sensor\_contact\_state


3.2 Actuadores Eléctricos

relay\_cmd


contactor\_cmd


pump\_electric\_cmd


aux\_motor\_cmd


3.3 Señales Técnicas

voltage\_level


current\_level


electric\_alarm


electric\_ready


4. Componentes Neumáticos Técnicos

4.1 Sensores Neumáticos

sensor\_air\_pressure


sensor\_air\_flow


sensor\_air\_regulator


4.2 Actuadores Neumáticos

air\_valve\_cmd


air\_regulator\_cmd


air\_actuator\_cmd


4.3 Señales Técnicas

air\_pressure


air\_flow


air\_alarm


air\_ready


5. Componentes Hidráulicos Técnicos

5.1 Sensores Hidráulicos

sensor\_hyd\_pressure


sensor\_hyd\_flow


sensor\_hyd\_temp


5.2 Actuadores Hidráulicos

hyd\_pump\_cmd


hyd\_valve\_cmd


hyd\_actuator\_cmd


5.3 Señales Técnicas

hyd\_pressure


hyd\_flow


hyd\_alarm


hyd\_ready


6. Sensores Industriales Técnicos

6.1 Sensores de Nivel

sensor\_level\_low


sensor\_level\_high


6.2 Sensores de Temperatura

sensor\_temp\_process


sensor\_temp\_machine


6.3 Sensores de Flujo

sensor\_flow\_in


sensor\_flow\_out


6.4 Sensores de Vacío

sensor\_vacuum\_level


sensor\_vacuum\_stability


6.5 Señales Técnicas

level\_value


temp\_value


flow\_value


vacuum\_value


sensor\_alarm


7. Actuadores Industriales Técnicos

7.1 Actuadores de Válvulas

valve\_open\_cmd


valve\_close\_cmd


7.2 Actuadores de Bombas

pump\_start\_cmd


pump\_stop\_cmd


7.3 Actuadores Eléctricos

relay\_cmd


contactor\_cmd


7.4 Señales Técnicas

actuator\_state


actuator\_fault


actuator\_ready


8. Módulos EtherCAT Técnicos

8.1 IO Digital

din\[N\]


dout\[N\]


8.2 IO Analógico

ain\[N\]


aout\[N\]


8.3 Módulos FSoE

sin\[N\]


sout\[N\]


safe\_ok


safe\_fault


8.4 Señales Técnicas

slave\_status


slave\_fault


safe\_channel\_ok


safe\_channel\_fault


9. Parámetros Técnicos de Componentes

9.1 Parámetros de Sensores

Código

struct SensorParams \{

    float min\_value;

    float max\_value;

    float nominal\_value;

    float tolerance;

    bool alarm\_on\_fault;

\}

9.2 Parámetros de Actuadores

Código

struct ActuatorParams \{

    bool requires\_enable;

    float response\_time\_ms;

    float power\_rating;

    bool safe\_required;

\}

9.3 Parámetros de Módulos EtherCAT

Código

struct EtherCATModule \{

    int id;

    int type;

    int channels;

    bool safe\_capable;

\}

10. Estructuras Técnicas de Componentes

10.1 Estructura de Componente Industrial

Código

struct IndustrialComponent \{

    int id;

    int type;

    float sensor\_value;

    bool actuator\_cmd;

    bool ready;

    bool alarm;

\}

10.2 Estructura de Estado Industrial

Código

struct IndustrialState \{

    bool vacuum\_ok;

    bool air\_ok;

    bool lube\_ok;

    bool hydraulic\_ok;

    bool coolant\_ok;

    bool safety\_ok;

\}

11. Dependencias Técnicas

Los componentes industriales se integran con:


interfaces FLOW


señales PLC/IO


topología EtherCAT técnica


Seguridad — enclavamientos y canales seguros.


CNC‑CAT — consumo de estados auxiliares.


12. Principios Técnicos

Componentes industriales determinísticos.


Señales claras y reproducibles.


Modularidad extrema.


Integración mediante IO y EtherCAT.


Expansión sin romper estructura existente.


13. Estado del Documento

Documento técnico oficial.

Base para implementación industrial del módulo FLOW.
