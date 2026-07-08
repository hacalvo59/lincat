11\_interfaces\_cnc.md

Interfaces Técnicas del Módulo CNC‑CAT

1. Propósito del Documento

Definir las interfaces técnicas del módulo CNC‑CAT dentro del ecosistema LINCAT.

Incluye señales, estados, estructuras, entradas, salidas y dependencias técnicas necesarias para el funcionamiento del camino CNC.


2. Alcance Técnico

Este documento describe:


interfaces internas CNC‑CAT,


interfaces externas hacia FLOW, PLC, IO y EtherCAT,


señales técnicas,


estados técnicos,


estructuras de datos,


dependencias de ejecución.


No incluye visión conceptual ni arquitectura general.


3. Interfaces Internas CNC‑CAT

Interfaces internas utilizadas por el motor CNC:


3.1 Interfaz de Interpolación

interp\_input — bloque G‑code procesado.


interp\_output — trayectoria interpolada.


feed\_target — velocidad objetivo.


path\_segment — segmento de trayectoria.


3.2 Interfaz de Servo

servo\_enable — habilitación de servo.


axis\_target\_pos\[N\] — posición objetivo por eje.


axis\_target\_vel\[N\] — velocidad objetivo por eje.


axis\_feedback\_pos\[N\] — posición real.


axis\_feedback\_vel\[N\] — velocidad real.


3.3 Interfaz de Spindle

spindle\_enable


spindle\_speed\_cmd


spindle\_speed\_feedback


spindle\_direction


3.4 Interfaz de Herramientas

tool\_number


tool\_length


tool\_radius


tool\_offset\_active


4. Interfaces Externas CNC‑CAT

Interfaces hacia otros módulos del ecosistema.


4.1 Interfaz CNC → FLOW

CNC‑CAT consume estados auxiliares:


VacuumReady


AirReady


LubeReady


SafetyOk


ProcessReady


4.2 Interfaz CNC → PLC

CNC‑CAT consume señales PLC:


plc\_servo\_enable


plc\_spindle\_enable


plc\_tool\_change\_ready


plc\_probe\_ready


plc\_cycle\_start


plc\_cycle\_stop


4.3 Interfaz CNC → IO

CNC‑CAT consume IO físico:


limit\_min\[N\]


limit\_max\[N\]


probe\_signal


estop\_signal


door\_signal


spindle\_fault


axis\_fault\[N\]


4.4 Interfaz CNC → EtherCAT

CNC‑CAT consume datos EtherCAT:


drive\_pos\[N\]


drive\_vel\[N\]


drive\_status\[N\]


drive\_fault\[N\]


spindle\_drive\_status


5. Señales Técnicas CNC‑CAT

Listado técnico de señales internas y externas.


5.1 Señales de Movimiento

cmd\_pos\[N\]


cmd\_vel\[N\]


cmd\_acc\[N\]


cmd\_jerk\[N\]


5.2 Señales de Estado

CNC\_State


Idle


Ready


Homing


Running


Paused


Stopped


Error


5.3 Señales de Sincronización

sync\_spindle\_motion


sync\_probe\_motion


sync\_tool\_change


6. Estructuras Técnicas

6.1 Estructura de Bloque CNC

Código

struct CNC\_Block \{

    int block\_id;

    float target\_pos\[AXES\];

    float feed;

    float spindle\_speed;

    int tool;

    int motion\_type;

\}

6.2 Estructura de Estado CNC

Código

struct CNC\_State \{

    int state;

    bool servo\_enabled;

    bool spindle\_enabled;

    bool tool\_loaded;

    bool flow\_ready;

\}

6.3 Estructura de Feedback

Código

struct CNC\_Feedback \{

    float pos\[AXES\];

    float vel\[AXES\];

    float spindle\_speed;

    bool limits\[AXES\]\[2\];

\}

7. Dependencias Técnicas

CNC‑CAT depende técnicamente de:


FLOW — estados auxiliares.


PLC — habilitaciones y enclavamientos.


IO — señales físicas.


EtherCAT — drives y módulos.


Seguridad — enclavamientos y estados seguros.


8. Principios Técnicos

Interfaces claras y estables.


Señales determinísticas.


Estados bien definidos.


Independencia modular.


Integración mediante señales y estructuras.


Expansión sin romper interfaces existentes.


9. Estado del Documento

Documento técnico oficial.

Base para implementación del módulo CNC‑CAT.
