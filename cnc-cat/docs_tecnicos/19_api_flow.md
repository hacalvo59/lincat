19\_api\_flow.md

API Técnica del Módulo LINCAT‑FLOW

1. Propósito del Documento

Definir la API técnica del módulo FLOW dentro del ecosistema LINCAT.

Incluye funciones, métodos, estructuras, parámetros, retornos y señales asociadas para control de servicios industriales, sensores, actuadores, estados auxiliares, seguridad y procesos.


2. Alcance Técnico

Este documento describe:


API de servicios industriales,


API de sensores,


API de actuadores,


API de estados auxiliares,


API de seguridad,


API de proceso industrial,


estructuras técnicas,


parámetros y retornos.


No incluye visión conceptual ni arquitectura general.


3. API de Servicios Industriales

3.1 FLOW\_Init()

Inicializa el módulo FLOW.


Código

bool FLOW\_Init();

3.2 FLOW\_EnableService()

Habilita un servicio industrial.


Código

bool FLOW\_EnableService(int service\_id);

Servicios: vacío, aire, lubricación, hidráulica, refrigerante.


3.3 FLOW\_DisableService()

Deshabilita un servicio industrial.


Código

bool FLOW\_DisableService(int service\_id);

3.4 FLOW\_GetServiceStatus()

Obtiene estado técnico del servicio.


Código

bool FLOW\_GetServiceStatus(int service\_id, bool\* ready, bool\* alarm);

4. API de Sensores Industriales

4.1 FLOW\_ReadSensor()

Lee un sensor industrial.


Código

bool FLOW\_ReadSensor(int sensor\_id, float\* value);

4.2 FLOW\_GetSensorAlarm()

Obtiene estado de alarma del sensor.


Código

bool FLOW\_GetSensorAlarm(int sensor\_id, bool\* alarm);

4.3 FLOW\_GetSensorRange()

Obtiene rango técnico del sensor.


Código

bool FLOW\_GetSensorRange(int sensor\_id, float\* min, float\* max);

5. API de Actuadores Industriales

5.1 FLOW\_ActuatorOn()

Activa un actuador industrial.


Código

bool FLOW\_ActuatorOn(int actuator\_id);

5.2 FLOW\_ActuatorOff()

Desactiva un actuador industrial.


Código

bool FLOW\_ActuatorOff(int actuator\_id);

5.3 FLOW\_GetActuatorStatus()

Obtiene estado técnico del actuador.


Código

bool FLOW\_GetActuatorStatus(int actuator\_id, bool\* active, bool\* fault);

6. API de Estados Auxiliares

6.1 FLOW\_GetAuxStates()

Obtiene estados auxiliares completos.


Código

bool FLOW\_GetAuxStates(FLOW\_AuxStates\* aux);

6.2 FLOW\_CheckAuxReady()

Verifica si todos los estados auxiliares están listos.


Código

bool FLOW\_CheckAuxReady();

6.3 FLOW\_WaitAuxReady()

Bloquea hasta que FLOW esté listo.


Código

bool FLOW\_WaitAuxReady();

7. API de Seguridad Industrial

7.1 FLOW\_GetSafetyStatus()

Obtiene estado de seguridad.


Código

bool FLOW\_GetSafetyStatus(bool\* safety\_ok);

7.2 FLOW\_GetSafetyFaults()

Obtiene fallos de seguridad.


Código

bool FLOW\_GetSafetyFaults(FLOW\_Faults\* faults);

7.3 FLOW\_ResetSafety()

Resetea fallos de seguridad.


Código

bool FLOW\_ResetSafety();

8. API de Proceso Industrial

8.1 FLOW\_StartProcess()

Inicia proceso industrial.


Código

bool FLOW\_StartProcess(int process\_id);

8.2 FLOW\_StopProcess()

Detiene proceso industrial.


Código

bool FLOW\_StopProcess();

8.3 FLOW\_GetProcessStatus()

Obtiene estado técnico del proceso.


Código

bool FLOW\_GetProcessStatus(FLOW\_Process\* process);

8.4 FLOW\_SetProcessStep()

Define paso técnico del proceso.


Código

bool FLOW\_SetProcessStep(int step);

9. Estructuras Técnicas

9.1 FLOW\_AuxStates

Código

struct FLOW\_AuxStates \{

    bool VacuumReady;

    bool AirReady;

    bool LubeReady;

    bool HydraulicReady;

    bool CoolantReady;

    bool SafetyOk;

    bool ProcessReady;

\};

9.2 FLOW\_Faults

Código

struct FLOW\_Faults \{

    bool vacuum\_alarm;

    bool air\_alarm;

    bool lube\_alarm;

    bool hydraulic\_alarm;

    bool coolant\_alarm;

    bool safety\_alarm;

\};

9.3 FLOW\_Process

Código

struct FLOW\_Process \{

    int step;

    bool ready;

    bool complete;

    bool alarm;

\};

10. Dependencias Técnicas

La API FLOW se integra con:


interfaces FLOW


señales PLC/IO


estados FLOW


topología EtherCAT técnica


Componentes industriales — sensores y actuadores.


Seguridad — enclavamientos y canales seguros.


CNC‑CAT — consumo de estados auxiliares.


11. Principios Técnicos

API determinística.


Funciones estables.


Modularidad extrema.


Integración mediante señales y estructuras.


Expansión sin romper API existente.


12. Estado del Documento

Documento técnico oficial.

Base para implementación del módulo FLOW.
