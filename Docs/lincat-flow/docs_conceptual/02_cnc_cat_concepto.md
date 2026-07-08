02\_cnc\_cat\_concepto.md

Concepto del Módulo CNC‑CAT

1. Propósito del Módulo

CNC‑CAT es el motor de movimiento del ecosistema LINCAT.

Define el comportamiento cinemático de la máquina y ejecuta las funciones esenciales de control numérico:


interpolación,


servo,


ejes,


spindle,


herramientas,


sondas,


límites.


Su función es garantizar movimiento preciso, seguro y determinístico.


2. Alcance Conceptual

CNC‑CAT representa el camino CNC de la máquina.

Incluye:


planificación de trayectoria,


ejecución de bloques,


control de velocidad y aceleración,


gestión de estados de movimiento,


control de spindle,


gestión de herramientas,


homing y límites,


sondas y offsets.


No incluye servicios industriales, lógica PLC ni topología EtherCAT completa.

Esos elementos pertenecen a otros módulos del ecosistema.


3. Rol dentro del Ecosistema LINCAT

CNC‑CAT es uno de los dos corazones del sistema.

Su rol es:


ejecutar movimiento,


interpretar G‑code,


coordinar servo y spindle,


interactuar con Motion,


consumir estados auxiliares de FLOW,


integrarse con PLC e IO mediante señales definidas.


CNC‑CAT no controla servicios industriales.

Depende de FLOW para habilitar movimiento seguro.


4. Dependencias Conceptuales

CNC‑CAT depende de:


Motion — control de servo y cinemática.


PLC — lógica de habilitación y enclavamientos.


IO — entradas y salidas relevantes para movimiento.


FLOW — estados auxiliares (vacío, aire, lubricación, seguridad).


EtherCAT — comunicación con drives y módulos IO.


Estas dependencias se integran mediante interfaces claras y definidas.


5. Camino CNC

El camino CNC incluye:


interpolación lineal y circular,


control de velocidad,


planificación de bloques,


ejecución determinística,


sincronización con spindle,


gestión de herramientas,


sondas y offsets,


homing y límites.


Este camino opera de forma independiente del camino FLOW.


6. Estados Conceptuales del CNC

CNC‑CAT define estados internos como:


Idle


Ready


Homing


Running


Paused


Stopped


Error


Estos estados se combinan con los estados auxiliares provenientes de FLOW para habilitar movimiento seguro.


7. Integración Conceptual con FLOW

FLOW provee estados auxiliares:


VacuumReady


AirReady


LubeReady


SafetyOk


ProcessReady


CNC‑CAT los consume como condiciones previas para:


habilitar ejes,


arrancar spindle,


iniciar ciclo,


ejecutar cambios de herramienta.


La integración es conceptual; los detalles técnicos se documentan por separado.


8. Integración Conceptual con PLC e IO

PLC ejecuta la lógica industrial.

IO representa las señales físicas.


CNC‑CAT consume:


límites,


sondas,


habilitaciones,


enclavamientos,


señales de spindle,


señales de herramientas.


No genera lógica PLC.

No gestiona IO industrial.

Solo utiliza las señales necesarias para movimiento.


9. Integración Conceptual con EtherCAT

EtherCAT provee:


drives,


módulos IO,


sensores,


actuadores.


CNC‑CAT utiliza únicamente:


drives de ejes,


drive de spindle,


IO relevante para movimiento.


La topología completa se documenta en FLOW.


10. Principios Conceptuales del Módulo

Independencia funcional.


Modularidad extrema.


Integración mediante interfaces.


Descendencia conceptual.


No rompe otros módulos.


Expansión sin modificar la arquitectura base.


11. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica del módulo CNC‑CAT.
