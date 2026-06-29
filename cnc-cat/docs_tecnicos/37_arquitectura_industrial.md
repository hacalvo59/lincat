37\_arquitectura\_industrial.md

Manual Técnico de Arquitectura Industrial — Ecosistema LINCAT

1. Propósito del Documento

Definir la arquitectura industrial completa para plantas que operan máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual establece la estructura jerárquica, los módulos, las capas, las interconexiones, los flujos de datos, los estándares y los criterios de diseño industrial.


2. Alcance

Este documento cubre:


arquitectura física,


arquitectura eléctrica,


arquitectura electrónica,


arquitectura EtherCAT,


arquitectura de seguridad industrial,


arquitectura FLOW,


arquitectura CNC‑CAT,


arquitectura de procesos,


arquitectura de calidad,


arquitectura de mantenimiento,


arquitectura de producción,


arquitectura de documentación,


arquitectura de trazabilidad,


arquitectura de planta.


No cubre operación diaria ni certificación.


3. Arquitectura Física de Planta

3.1 Distribución industrial

zona de producción,


zona de seguridad,


zona de mantenimiento,


zona de almacenamiento,


zona de auditoría.


3.2 Infraestructura

suelo nivelado \< 0.1 mm/m,


aislamiento de vibraciones,


iluminación certificada,


ventilación industrial.


3.3 Flujo físico

entrada de material,


proceso CNC,


inspección,


salida de producción.


4. Arquitectura Eléctrica

4.1 Alimentación

líneas dedicadas,


caída de tensión \< 5 %,


protección industrial.


4.2 Gabinetes

IP54 mínimo,


ventilación forzada,


separación potencia/control.


4.3 Cableado

señal blindada,


potencia certificada,


seguridad dedicada.


5. Arquitectura Electrónica

5.1 Drives

EtherCAT nativo,


feedback estable,


parámetros certificados.


5.2 IO

módulos digitales y analógicos,


FSoE operativo.


5.3 Spindle

variador certificado,


feedback de velocidad.


6. Arquitectura EtherCAT

6.1 Topología

Master → Drives → IO → FSoE,


sin bifurcaciones,


cable CAT6 industrial.


6.2 Sincronización

ciclo DC 1000 µs,


jitter dentro de tolerancia.


6.3 Slaves

todos online,


sin slave\_fault.


7. Arquitectura de Seguridad Industrial

7.1 Elementos críticos

enclavamiento de puerta,


zona segura,


parada segura,


relés de seguridad.


7.2 Estados

SafetyOk,


SafetyFault,


SafetyLock.


7.3 Integración

FSoE ↔ IO seguro ↔ CNC‑CAT ↔ FLOW.


8. Arquitectura FLOW

8.1 Sensores

vacío,


aire,


lubricación,


hidráulica,


refrigerante.


8.2 Actuadores

válvulas,


bombas,


contactores.


8.3 Estados auxiliares

VacuumReady, AirReady, LubeReady, HydraulicReady, CoolantReady, SafetyOk, ProcessReady.


9. Arquitectura CNC‑CAT

9.1 Capas CNC

interpolación,


servo,


spindle,


herramientas.


9.2 Señales críticas

servo\_enabled,


spindle\_enabled,


interp\_active.


9.3 Integración

CNC ↔ EtherCAT ↔ FLOW ↔ Seguridad.


10. Arquitectura de Procesos Industriales

10.1 Secuencias FLOW

sensores → estados → actuadores.


10.2 Secuencias CNC

homing → interpolación → spindle → herramientas.


10.3 Integración completa

CNC ↔ FLOW ↔ PLC/IO ↔ EtherCAT ↔ Seguridad.


11. Arquitectura de Calidad Industrial

11.1 Dimensional

tolerancias certificadas.


11.2 Geométrica

paralelismo,


perpendicularidad,


planitud.


11.3 Superficial

rugosidad certificada.


11.4 Documentación

informes de calidad.


12. Arquitectura de Mantenimiento

12.1 Mecánico

alineación,


backlash,


vibración.


12.2 Eléctrico

aislamiento,


protección.


12.3 Electrónico

drives,


IO,


FSoE.


12.4 CNC‑CAT

interpolación,


servo,


spindle.


13. Arquitectura de Producción

13.1 Validación de máquina

homing,


FLOW,


seguridad,


EtherCAT.


13.2 Validación de proceso

material,


herramientas,


parámetros CNC.


13.3 Control de calidad

dimensional,


geométrico,


superficial.


14. Arquitectura de Documentación

14.1 Documentación obligatoria

planos mecánicos,


planos eléctricos,


topología EtherCAT,


mapa PLC/IO,


parámetros CNC‑CAT,


parámetros FLOW.


14.2 Repositorio

versionado,


trazabilidad,


control de acceso.


15. Arquitectura de Trazabilidad

15.1 Registros

mantenimiento,


producción,


auditorías,


calibraciones.


15.2 Formato

YAML técnico,


informes.


15.3 Conservación

mínimo 15 años.


16. Arquitectura de Planta Completa

16.1 Capas

infraestructura,


mecánica,


eléctrica,


electrónica,


EtherCAT,


seguridad,


FLOW,


CNC‑CAT,


procesos,


calidad,


mantenimiento,


producción,


documentación,


trazabilidad.


16.2 Interconexión

cada capa depende de la anterior,


cada capa alimenta la siguiente,


arquitectura modular y escalable.


17. Estado del Documento

Manual técnico oficial.

Base para arquitectura industrial del ecosistema LINCAT.
