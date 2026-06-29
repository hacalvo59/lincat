14\_estados\_cnc.md

Estados Técnicos del Módulo CNC‑CAT

1. Propósito del Documento

Definir los estados técnicos del módulo CNC‑CAT dentro del ecosistema LINCAT.

Incluye estados, transiciones, señales asociadas, condiciones de entrada y salida, y estructuras técnicas necesarias para el funcionamiento del camino CNC.


2. Alcance Técnico

Este documento describe:


estados CNC,


transiciones permitidas,


señales asociadas,


condiciones de habilitación,


dependencias técnicas,


estructuras de estado.


No incluye visión conceptual ni arquitectura general.


3. Estados Técnicos CNC‑CAT

3.1 Estado Idle

Sistema inicial sin habilitación de movimiento.


Servo deshabilitado.


Spindle deshabilitado.


No hay trayectoria cargada.


3.2 Estado Ready

Sistema preparado para movimiento.


Servo habilitado.


Spindle opcionalmente habilitado.


Trayectoria cargada.


Estados FLOW verificados.


3.3 Estado Homing

Proceso técnico de referencia de ejes.


Movimiento controlado hacia sensores de home.


Límites activos.


Servo habilitado.


3.4 Estado Running

Ejecución activa de trayectoria CNC.


Interpolación activa.


Servo habilitado.


Spindle según programa.


Sincronización con FLOW.


3.5 Estado Paused

Ejecución detenida temporalmente.


Servo habilitado.


Spindle opcionalmente detenido.


Trayectoria retenida.


3.6 Estado Stopped

Ejecución detenida por comando.


Servo deshabilitado.


Spindle detenido.


Trayectoria cancelada.


3.7 Estado Error

Fallo técnico detectado.


Servo deshabilitado.


Spindle detenido.


Movimiento bloqueado.


Requiere reset técnico.


4. Transiciones Técnicas Permitidas

4.1 Transiciones normales

Idle → Ready


Ready → Homing


Homing → Ready


Ready → Running


Running → Paused


Paused → Running


Running → Stopped


Paused → Stopped


Stopped → Ready


4.2 Transiciones por fallo

Any → Error


Error → Idle (tras reset técnico)


5. Señales Asociadas a Estados

5.1 Señales de habilitación

servo\_enabled


spindle\_enabled


motion\_ready


flow\_ready


safety\_ok


5.2 Señales de ejecución

interp\_active


block\_running


sync\_spindle\_motion


sync\_probe\_motion


5.3 Señales de fallo

axis\_fault\[N\]


spindle\_fault


limit\_triggered\[N\]


probe\_fault


flow\_alarm


safety\_alarm


6. Condiciones Técnicas de Entrada y Salida

6.1 Entrada a Ready

Servo habilitado.


Spindle sin fallos.


Estados FLOW activos:


VacuumReady


AirReady


LubeReady


SafetyOk


ProcessReady


6.2 Entrada a Running

Trayectoria cargada.


Interpolador activo.


Servo habilitado.


Spindle según programa.


Estados FLOW estables.


6.3 Entrada a Error

Cualquier fallo crítico:


límites,


spindle,


servo,


seguridad,


FLOW.


7. Estructuras Técnicas de Estado

7.1 Estructura CNC\_State

Código

struct CNC\_State \{

    int state;

    bool servo\_enabled;

    bool spindle\_enabled;

    bool homing\_active;

    bool running\_active;

    bool paused;

    bool error;

\}

7.2 Estructura CNC\_Faults

Código

struct CNC\_Faults \{

    bool axis\_fault\[AXES\];

    bool spindle\_fault;

    bool limit\_min\[AXES\];

    bool limit\_max\[AXES\];

    bool probe\_fault;

    bool safety\_fault;

    bool flow\_fault;

\}

7.3 Estructura CNC\_Execution

Código

struct CNC\_Execution \{

    bool interp\_active;

    int current\_block;

    float target\_pos\[AXES\];

    float feed;

    float spindle\_speed;

\}

8. Dependencias Técnicas

Los estados CNC dependen de:


interfaces CNC


interfaces FLOW


señales PLC/IO


EtherCAT — drives y módulos.


Seguridad — enclavamientos y zonas seguras.


9. Principios Técnicos

Estados determinísticos.


Transiciones claras y seguras.


Independencia modular.


Integración mediante señales.


Expansión sin romper estados existentes.
