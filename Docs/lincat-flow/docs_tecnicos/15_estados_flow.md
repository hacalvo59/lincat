15\_estados\_flow.md

Estados Técnicos del Módulo LINCAT‑FLOW

1. Propósito del Documento

Definir los estados técnicos del módulo FLOW dentro del ecosistema LINCAT.

Incluye estados industriales, transiciones, señales asociadas, condiciones de habilitación y estructuras técnicas necesarias para el funcionamiento del camino FLOW.


2. Alcance Técnico

Este documento describe:


estados FLOW,


transiciones permitidas,


señales industriales asociadas,


condiciones de entrada y salida,


dependencias técnicas,


estructuras de estado.


No incluye visión conceptual ni arquitectura general.


3. Estados Técnicos FLOW

3.1 Estado FlowIdle

Sistema industrial sin habilitación.


Actuadores desactivados.


Sensores activos.


Sin estados auxiliares generados.


3.2 Estado FlowInit

Inicialización industrial.


Validación de sensores.


Validación de actuadores.


Verificación de seguridad.


3.3 Estado FlowReady

Servicios industriales disponibles.


Vacío listo.


Aire listo.


Lubricación lista.


Hidráulica lista.


Refrigerante listo.


Seguridad estable.


3.4 Estado FlowProcess

Proceso industrial activo.


Secuencias industriales ejecutándose.


Actuadores activos.


Sensores monitoreando condiciones.


3.5 Estado FlowWarning

Advertencia industrial no crítica.


Parámetros fuera de rango leve.


No bloquea movimiento CNC.


Requiere atención.


3.6 Estado FlowAlarm

Fallo industrial crítico.


Parámetros fuera de rango severo.


Actuadores deshabilitados.


Bloqueo de movimiento CNC.


3.7 Estado FlowSafetyLock

Bloqueo de seguridad.


Puerta abierta.


Zona insegura.


Canal seguro en fallo.


Movimiento CNC bloqueado.


4. Transiciones Técnicas Permitidas

4.1 Transiciones normales

FlowIdle → FlowInit


FlowInit → FlowReady


FlowReady → FlowProcess


FlowProcess → FlowReady


FlowReady → FlowWarning


FlowWarning → FlowReady


4.2 Transiciones por fallo

Any → FlowAlarm


Any → FlowSafetyLock


FlowAlarm → FlowIdle (tras reset técnico)


FlowSafetyLock → FlowIdle (tras restablecer seguridad)


5. Señales Asociadas a Estados FLOW

5.1 Señales de servicios industriales

vacuum\_ok


air\_ok


lube\_ok


hydraulic\_ok


coolant\_ok


5.2 Señales de seguridad

door\_closed


zone\_clear


estop\_released


safe\_channel\_ok


5.3 Señales de proceso

process\_step


process\_ready


process\_alarm


process\_complete


5.4 Señales de fallo

vacuum\_alarm


air\_alarm


lube\_alarm


hydraulic\_alarm


coolant\_alarm


safety\_alarm


6. Condiciones Técnicas de Entrada y Salida

6.1 Entrada a FlowReady

Sensores válidos.


Actuadores sin fallos.


Seguridad estable.


Estados industriales:


VacuumReady


AirReady


LubeReady


HydraulicReady


CoolantReady


SafetyOk


6.2 Entrada a FlowProcess

Secuencia industrial activa.


Actuadores habilitados.


Sensores dentro de rango.


Seguridad estable.


6.3 Entrada a FlowAlarm

Fallo crítico en cualquier servicio industrial.


Fallo de seguridad.


Fallo de proceso.


7. Estructuras Técnicas de Estado

7.1 Estructura FLOW\_State

Código

struct FLOW\_State \{

    int state;

    bool vacuum\_ok;

    bool air\_ok;

    bool lube\_ok;

    bool hydraulic\_ok;

    bool coolant\_ok;

    bool safety\_ok;

    bool process\_ok;

\}

7.2 Estructura FLOW\_Faults

Código

struct FLOW\_Faults \{

    bool vacuum\_alarm;

    bool air\_alarm;

    bool lube\_alarm;

    bool hydraulic\_alarm;

    bool coolant\_alarm;

    bool safety\_alarm;

\}

7.3 Estructura FLOW\_Process

Código

struct FLOW\_Process \{

    int step;

    bool ready;

    bool complete;

    bool alarm;

\}

8. Dependencias Técnicas

Los estados FLOW dependen de:


interfaces FLOW


señales PLC/IO


EtherCAT — módulos industriales y seguridad.


Seguridad — enclavamientos y zonas seguras.


Componentes industriales — sensores y actuadores.


CNC‑CAT depende de FLOW para habilitación segura.


9. Principios Técnicos

Estados industriales determinísticos.


Transiciones claras y seguras.


Modularidad extrema.


Integración mediante señales.


Expansión sin romper estados existentes.


10. Estado del Documento

Documento técnico oficial.

Base para implementación del módulo FLOW.
