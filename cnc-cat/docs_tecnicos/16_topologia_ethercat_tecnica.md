16\_topologia\_ethercat\_tecnica.md

Topología Técnica EtherCAT del Ecosistema LINCAT

1. Propósito del Documento

Definir la topología técnica EtherCAT utilizada por los módulos CNC‑CAT, FLOW, PLC e IO dentro del ecosistema LINCAT.

Incluye estructura del bus, orden de slaves, tipos de módulos, canales, señales y dependencias técnicas.


2. Alcance Técnico

Este documento describe:


estructura técnica del bus EtherCAT,


orden técnico de slaves,


módulos IO,


drives de ejes,


drive de spindle,


módulos FSoE,


canales seguros,


señales técnicas asociadas.


No incluye wiring físico ni direcciones reales de fábrica.


3. Estructura Técnica del Bus EtherCAT

3.1 Master EtherCAT

ECAT\_MASTER\_0


Controlador principal del bus.


Responsable del ciclo determinístico.


Provee sincronización DC.


3.2 Cadena de Slaves

La cadena técnica se organiza de forma lineal:


Drive Eje X


Drive Eje Y


Drive Eje Z


Drive Spindle


Módulo IO Digital 1


Módulo IO Digital 2


Módulo IO Analógico 1


Módulo IO Analógico 2


Módulo FSoE 1


Módulo FSoE 2


4. Drives Técnicos

4.1 Drive de Eje (por cada eje)

drive\_axis\[N\]


Canal de posición.


Canal de velocidad.


Canal de estado.


Canal de fallo.


Canal seguro (FSoE).


4.2 Drive de Spindle

drive\_spindle


Canal de velocidad.


Canal de dirección.


Canal de estado.


Canal de fallo.


Canal seguro (FSoE).


5. Módulos IO Técnicos

5.1 IO Digital

io\_digital\_1


16 entradas digitales.


16 salidas digitales.


io\_digital\_2


16 entradas digitales.


16 salidas digitales.


5.2 IO Analógico

io\_analog\_1


8 entradas analógicas.


8 salidas analógicas.


io\_analog\_2


8 entradas analógicas.


8 salidas analógicas.


6. Módulos de Seguridad FSoE

6.1 FSoE 1

safe\_in\[8\]


safe\_out\[8\]


safe\_status


safe\_fault


6.2 FSoE 2

safe\_in\[8\]


safe\_out\[8\]


safe\_status


safe\_fault


7. Señales Técnicas EtherCAT

7.1 Señales de Drive

drive\_pos\[N\]


drive\_vel\[N\]


drive\_status\[N\]


drive\_fault\[N\]


drive\_safe\[N\]


7.2 Señales de Spindle

spindle\_speed\_cmd


spindle\_speed\_feedback


spindle\_status


spindle\_fault


spindle\_safe


7.3 Señales IO Digital

din\[N\]


dout\[N\]


7.4 Señales IO Analógico

ain\[N\]


aout\[N\]


7.5 Señales FSoE

sin\[N\]


sout\[N\]


safe\_channel\_ok


safe\_channel\_fault


8. Estructuras Técnicas EtherCAT

8.1 Estructura de Slave

Código

struct ECAT\_Slave \{

    int id;

    int type;

    bool online;

    bool fault;

    bool safe\_ok;

\}

8.2 Estructura de Drive

Código

struct ECAT\_Drive \{

    float pos;

    float vel;

    int status;

    bool fault;

    bool safe\_ok;

\}

8.3 Estructura IO

Código

struct ECAT\_IO \{

    bool din\[64\];

    bool dout\[64\];

    float ain\[32\];

    float aout\[32\];

\}

8.4 Estructura FSoE

Código

struct ECAT\_FSOE \{

    bool sin\[16\];

    bool sout\[16\];

    bool safe\_ok;

    bool safe\_fault;

\}

9. Dependencias Técnicas

La topología EtherCAT se integra con:


interfaces CNC


interfaces FLOW


señales PLC/IO


Seguridad — enclavamientos y canales seguros.


Componentes industriales — sensores y actuadores.


10. Principios Técnicos

Topología determinística.


Orden de slaves estable.


Modularidad extrema.


Integración mediante canales EtherCAT.


Expansión sin romper estructura existente.


11. Estado del Documento

Documento técnico oficial.

Base para implementación EtherCAT en LINCAT.
