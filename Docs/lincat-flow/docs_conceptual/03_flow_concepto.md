03\_flow\_concepto.md

Concepto del Módulo LINCAT‑FLOW

1. Propósito del Módulo

LINCAT‑FLOW es el módulo encargado de representar, organizar y controlar los servicios industriales de la máquina.

Define el comportamiento funcional del sistema y provee los estados auxiliares necesarios para habilitar el movimiento seguro en CNC‑CAT.


Incluye:


vacío,


aire comprimido,


lubricación,


sensores industriales,


válvulas,


relés,


contactores,


enclavamientos,


seguridad,


estados de proceso.


2. Alcance Conceptual

FLOW representa el camino industrial de la máquina.

Su función es modelar todos los elementos que no pertenecen al movimiento CNC pero que son esenciales para el funcionamiento real.


Incluye:


componentes eléctricos, neumáticos e hidráulicos,


estados de habilitación,


condiciones de seguridad,


alarmas,


secuencias de proceso,


topología EtherCAT completa,


lógica conceptual de PLC.


No incluye interpolación, servo, spindle ni herramientas.

Esos elementos pertenecen a CNC‑CAT.


3. Rol dentro del Ecosistema LINCAT

FLOW es el segundo corazón del ecosistema.

Su rol es:


representar los servicios industriales,


generar estados auxiliares,


definir condiciones de habilitación,


modelar la topología EtherCAT,


proveer señales a PLC e IO,


exponer estados a CNC‑CAT.


FLOW no ejecuta movimiento.

FLOW habilita el movimiento.


4. Dependencias Conceptuales

FLOW depende de:


PLC — ejecución de lógica industrial.


IO — entradas y salidas físicas.


EtherCAT — topología y comunicación con módulos.


Base de datos industrial — definición de componentes.


Seguridad — enclavamientos y zonas seguras.


FLOW provee estados a CNC‑CAT, pero no depende de él.


5. Camino FLOW

El camino FLOW incluye:


modelado de componentes,


estados de proceso,


enclavamientos,


condiciones de habilitación,


alarmas,


secuencias industriales,


seguridad,


topología EtherCAT.


Este camino opera de forma independiente del camino CNC.


6. Estados Conceptuales de FLOW

FLOW define estados auxiliares como:


VacuumReady


AirReady


LubeReady


SafetyOk


ProcessReady


Estos estados se combinan con los estados internos del CNC para habilitar movimiento seguro.


7. Integración Conceptual con CNC‑CAT

FLOW expone señales y estados que CNC‑CAT consume:


habilitación de ejes,


habilitación de spindle,


condiciones de inicio de ciclo,


enclavamientos de seguridad,


estados de proceso.


La integración es conceptual; los detalles técnicos se documentan por separado.


8. Integración Conceptual con PLC e IO

PLC ejecuta la lógica generada conceptualmente por FLOW.

IO representa las señales físicas de sensores y actuadores.


FLOW define:


qué sensores existen,


qué actuadores existen,


qué estados deben generarse,


qué alarmas deben activarse.


PLC e IO implementan esa lógica en hardware o simulación.


9. Integración Conceptual con EtherCAT

FLOW representa la topología EtherCAT completa:


master,


slaves,


módulos IO,


sensores,


actuadores,


seguridad FSoE.


FLOW organiza la máquina como un mapa industrial.

CNC‑CAT utiliza solo los elementos relevantes para movimiento.


10. Principios Conceptuales del Módulo

Representación industrial completa.


Modularidad extrema.


Independencia funcional.


Integración mediante estados auxiliares.


Descendencia conceptual.


Expansión sin modificar la arquitectura base.


11. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica del módulo FLOW.
