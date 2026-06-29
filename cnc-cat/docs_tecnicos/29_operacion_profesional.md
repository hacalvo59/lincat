29\_operacion\_profesional.md

Manual Técnico de Operación Profesional — Ecosistema LINCAT

1. Propósito del Documento

Definir los criterios, modos, protocolos y responsabilidades para operar profesionalmente una máquina CNC industrial basada en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual establece las reglas de operación certificada, los límites técnicos y los procedimientos de uso seguro y eficiente.


2. Alcance

Este documento cubre:


operación profesional CNC‑CAT,


operación profesional FLOW,


operación profesional PLC/IO,


operación profesional EtherCAT,


operación profesional de seguridad industrial,


operación profesional del spindle,


operación profesional de herramientas,


operación profesional del modo REAL,


operación profesional del proceso industrial,


criterios de operación segura,


responsabilidades del operario.


No cubre instalación, mantenimiento ni diagnóstico.


3. Roles y Responsabilidades

3.1 Operario profesional

ejecutar programas CNC,


verificar estados FLOW,


validar seguridad,


supervisar spindle y herramientas,


detener operación ante fallos.


3.2 Técnico industrial

validar parámetros,


supervisar EtherCAT,


revisar IO,


autorizar operación en modo REAL.


3.3 Supervisor

aprobar producción,


validar certificación,


autorizar cambios de proceso.


4. Condiciones Previas de Operación

4.1 Máquina

EtherCAT online,


FLOW operativo,


seguridad estable,


CNC‑CAT en estado Ready.


4.2 Entorno

temperatura 15–30 °C,


humedad \< 70 %,


ausencia de vibraciones externas.


4.3 Operario

EPI obligatorio,


formación certificada,


conocimiento de enclavamientos.


5. Operación Profesional CNC‑CAT

5.1 Estados CNC

Idle → Ready → Homing → Running → Paused → Stopped → Error.


5.2 Reglas de operación

homing obligatorio antes de Running,


spindle habilitado solo con seguridad estable,


feed dentro de parámetros,


offsets de herramienta verificados.


5.3 Señales críticas

servo\_enabled,


spindle\_enabled,


interp\_active,


axis\_fault\[N\],


spindle\_fault.


5.4 Programas CNC

solo G-code validado,


sin macros no certificadas,


sin movimientos fuera de límites.


6. Operación Profesional FLOW

6.1 Estados auxiliares

VacuumReady,


AirReady,


LubeReady,


HydraulicReady,


CoolantReady,


SafetyOk,


ProcessReady.


6.2 Reglas de operación

FLOW debe estar Ready antes de Running CNC,


sensores dentro de rango,


actuadores operativos,


sin alarmas FLOW.


6.3 Señales críticas

vacuum\_level,


air\_pressure,


lube\_flow,


hydraulic\_pressure,


coolant\_level.


7. Operación Profesional PLC/IO

7.1 Entradas críticas

estop,


door,


probe,


limit\_min/max,


axis\_fault,


spindle\_fault.


7.2 Salidas críticas

servo\_enable,


spindle\_enable,


tool\_change,


probe\_enable.


7.3 Reglas de operación

ninguna entrada crítica puede estar en fallo,


salidas deben corresponder al estado CNC,


analógicos dentro de rango.


8. Operación Profesional EtherCAT

8.1 Requisitos

todos los slaves online,


sincronización DC estable,


drives sin fallos,


FSoE operativo.


8.2 Señales críticas

drive\_pos\[N\],


drive\_vel\[N\],


drive\_fault\[N\],


safe\_channel\_ok.


8.3 Reglas de operación

ciclo determinístico 1000 µs,


watchdog activo,


sin jitter excesivo.


9. Operación Profesional de Seguridad Industrial

9.1 Estados

SafetyOk,


SafetyFault,


SafetyLock.


9.2 Reglas de operación

SafetyOk obligatorio para Running,


SafetyLock bloquea movimiento,


SafetyFault requiere intervención técnica.


9.3 Elementos críticos

enclavamiento de puerta,


zona segura,


parada segura,


relés de seguridad.


10. Operación Profesional del Spindle

10.1 Requisitos

velocidad dentro de tolerancia,


dirección correcta,


feedback estable.


10.2 Límites

velocidad máxima certificada,


torque dentro de rango,


vibración dentro de límites.


10.3 Reglas de operación

habilitar solo con seguridad estable,


detener ante vibración excesiva,


validar refrigerante.


11. Operación Profesional de Herramientas

11.1 Requisitos

offsets verificados,


herramienta correcta,


sujeción segura.


11.2 Reglas

cambio de herramienta solo en estado Stopped,


validación de longitud y radio,


verificación de desgaste.


12. Operación Profesional del Modo REAL

12.1 Requisitos

EtherCAT online,


FLOW operativo,


seguridad estable,


CNC Ready.


12.2 Parámetros

sync\_cycle\_us: 1000,


servo\_timeout\_ms: 200,


sensor\_poll\_ms: 20,


safe\_check\_ms: 10.


12.3 Reglas

no operar con alarmas,


no operar con fallos de seguridad,


no operar con fallos de FLOW.


13. Operación Profesional del Proceso Industrial

13.1 Requisitos

proceso definido,


actuadores operativos,


sensores dentro de rango.


13.2 Reglas

secuencia FLOW debe ser estable,


CNC debe consumir estados auxiliares,


no se permite operación con alarmas.


14. Criterios de Operación Segura

14.1 Crítico

afecta seguridad,


afecta movimiento,


afecta spindle.


14.2 Alto

afecta precisión,


afecta proceso FLOW.


14.3 Medio

afecta estabilidad.


14.4 Bajo

afecta eficiencia.


15. Estado del Documento

Manual técnico oficial.

Base para operación profesional del ecosistema LINCAT.
