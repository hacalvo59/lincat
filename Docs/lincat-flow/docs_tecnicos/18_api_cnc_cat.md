18\_api\_cnc\_cat.md

API Técnica del Módulo CNC‑CAT

1. Propósito del Documento

Definir la API técnica del módulo CNC‑CAT dentro del ecosistema LINCAT.

Incluye funciones, métodos, estructuras, parámetros, retornos y señales asociadas para control de movimiento, interpolación, servo, spindle, herramientas y estados.


2. Alcance Técnico

Este documento describe:


API de movimiento,


API de interpolación,


API de servo,


API de spindle,


API de herramientas,


API de estados,


API de sincronización,


estructuras técnicas,


parámetros y retornos.


No incluye visión conceptual ni arquitectura general.


3. API de Movimiento CNC

3.1 CNC\_LoadProgram()

Carga un programa CNC en memoria.


Código

bool CNC\_LoadProgram(const char\* path);

Retorno: true si el programa es válido.


3.2 CNC\_Start()

Inicia la ejecución del programa CNC.


Código

bool CNC\_Start();

Requiere: Ready, FLOW habilitado, seguridad estable.


3.3 CNC\_Pause()

Pausa la ejecución.


Código

bool CNC\_Pause();

3.4 CNC\_Resume()

Reanuda la ejecución.


Código

bool CNC\_Resume();

3.5 CNC\_Stop()

Detiene la ejecución.


Código

bool CNC\_Stop();

3.6 CNC\_JogAxis()

Movimiento manual por eje.


Código

bool CNC\_JogAxis(int axis, float velocity);

3.7 CNC\_MoveTo()

Movimiento absoluto.


Código

bool CNC\_MoveTo(float target\_pos\[AXES\], float feed);

3.8 CNC\_MoveRel()

Movimiento relativo.


Código

bool CNC\_MoveRel(float delta\_pos\[AXES\], float feed);

4. API de Interpolación

4.1 CNC\_SetFeed()

Define velocidad de avance.


Código

bool CNC\_SetFeed(float feed);

4.2 CNC\_SetRapid()

Activa modo rápido.


Código

bool CNC\_SetRapid();

4.3 CNC\_SetMotionType()

Define tipo de movimiento.


Código

bool CNC\_SetMotionType(int type);

Tipos: lineal, circular, helicoidal.


5. API de Servo

5.1 CNC\_ServoEnable()

Habilita servo.


Código

bool CNC\_ServoEnable();

5.2 CNC\_ServoDisable()

Deshabilita servo.


Código

bool CNC\_ServoDisable();

5.3 CNC\_GetAxisFeedback()

Obtiene feedback de eje.


Código

bool CNC\_GetAxisFeedback(int axis, float\* pos, float\* vel);

6. API de Spindle

6.1 CNC\_SpindleOn()

Activa spindle.


Código

bool CNC\_SpindleOn(float speed, int direction);

6.2 CNC\_SpindleOff()

Detiene spindle.


Código

bool CNC\_SpindleOff();

6.3 CNC\_GetSpindleFeedback()

Obtiene velocidad real.


Código

bool CNC\_GetSpindleFeedback(float\* speed);

7. API de Herramientas

7.1 CNC\_ToolChange()

Cambio de herramienta.


Código

bool CNC\_ToolChange(int tool\_number);

7.2 CNC\_SetToolOffset()

Define offset de herramienta.


Código

bool CNC\_SetToolOffset(float length, float radius);

7.3 CNC\_GetToolInfo()

Obtiene información de herramienta.


Código

bool CNC\_GetToolInfo(int\* tool\_number, float\* length, float\* radius);

8. API de Estados

8.1 CNC\_GetState()

Obtiene estado CNC.


Código

int CNC\_GetState();

Estados: Idle, Ready, Homing, Running, Paused, Stopped, Error.


8.2 CNC\_GetFaults()

Obtiene fallos activos.


Código

bool CNC\_GetFaults(CNC\_Faults\* faults);

8.3 CNC\_ResetFaults()

Resetea fallos.


Código

bool CNC\_ResetFaults();

9. API de Sincronización FLOW

9.1 CNC\_CheckFlowReady()

Verifica estados auxiliares FLOW.


Código

bool CNC\_CheckFlowReady(FLOW\_AuxStates\* aux);

9.2 CNC\_WaitFlowReady()

Bloquea hasta que FLOW esté listo.


Código

bool CNC\_WaitFlowReady();

10. Estructuras Técnicas

10.1 CNC\_State

Código

struct CNC\_State \{

    int state;

    bool servo\_enabled;

    bool spindle\_enabled;

    bool homing\_active;

    bool running\_active;

    bool paused;

    bool error;

\};

10.2 CNC\_Faults

Código

struct CNC\_Faults \{

    bool axis\_fault\[AXES\];

    bool spindle\_fault;

    bool limit\_min\[AXES\];

    bool limit\_max\[AXES\];

    bool probe\_fault;

    bool safety\_fault;

    bool flow\_fault;

\};

10.3 CNC\_Feedback

Código

struct CNC\_Feedback \{

    float pos\[AXES\];

    float vel\[AXES\];

    float spindle\_speed;

\};

11. Dependencias Técnicas

La API CNC‑CAT se integra con:


interfaces CNC


interfaces FLOW


señales PLC/IO


estados CNC


EtherCAT — drives y módulos.


Seguridad — enclavamientos y zonas seguras.


12. Principios Técnicos

API determinística.


Funciones estables.


Modularidad extrema.


Integración mediante señales y estructuras.


Expansión sin romper API existente.


13. Estado del Documento

Documento técnico oficial.

Base para implementación del módulo CNC‑CAT.
