34\_certificacion\_planta.md

Manual Técnico de Certificación de Planta — Ecosistema LINCAT

1. Propósito del Documento

Definir los criterios, requisitos, auditorías, verificaciones, documentación y protocolos necesarios para obtener la certificación industrial de planta que opera máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual garantiza que la planta cumple estándares de seguridad, calidad, trazabilidad, estabilidad, infraestructura y operación profesional.


2. Alcance

Este documento cubre:


requisitos de infraestructura,


requisitos eléctricos y electrónicos,


requisitos de seguridad industrial,


requisitos de calidad,


requisitos de documentación,


auditorías internas y externas,


certificación de procesos,


certificación de producción,


certificación de mantenimiento,


certificación de trazabilidad,


criterios de aceptación,


emisión del certificado de planta.


No cubre instalación de máquinas ni operación diaria.


3. Requisitos de Infraestructura

3.1 Entorno industrial

temperatura 15–30 °C,


humedad \< 70 %,


ventilación adecuada,


ausencia de vibraciones externas,


iluminación certificada.


3.2 Distribución de planta

zonas de producción,


zonas de seguridad,


zonas de mantenimiento,


zonas de almacenamiento,


zonas de auditoría.


3.3 Suelo industrial

nivelación \< 0.1 mm/m,


resistencia mecánica certificada,


aislamiento de vibraciones.


4. Requisitos Eléctricos de Planta

4.1 Alimentación

líneas dedicadas,


caída de tensión \< 5 %,


protección industrial.


4.2 Gabinetes eléctricos

IP54 mínimo,


ventilación forzada,


separación potencia/control.


4.3 Aislamiento

control \> 1 MΩ,


potencia \> 10 MΩ.


5. Requisitos Electrónicos de Planta

5.1 Drives

EtherCAT nativo,


feedback estable,


parámetros certificados.


5.2 IO

módulos digitales y analógicos certificados,


FSoE operativo.


5.3 Spindle

variador certificado,


feedback de velocidad,


vibración dentro de límites.


6. Requisitos EtherCAT de Planta

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


7. Requisitos de Seguridad Industrial

7.1 Elementos críticos

enclavamiento de puerta,


zona segura,


parada segura,


relés de seguridad,


sensores seguros.


7.2 Estados

SafetyOk,


SafetyFault,


SafetyLock.


7.3 Normativas

cumplimiento de normativa europea,


documentación de seguridad,


auditoría de seguridad.


8. Requisitos FLOW de Planta

8.1 Sensores industriales

vacío, aire, lubricación, hidráulica, refrigerante.


8.2 Actuadores industriales

válvulas, bombas, contactores.


8.3 Estados auxiliares

VacuumReady, AirReady, LubeReady, HydraulicReady, CoolantReady, SafetyOk, ProcessReady.


9. Requisitos CNC‑CAT de Planta

9.1 Interpolación

precisión lineal \< 0.05 mm,


precisión circular \< 0.07 mm.


9.2 Servo

estabilidad de posición,


ausencia de vibración.


9.3 Spindle

velocidad dentro de tolerancia,


dirección correcta.


9.4 Herramientas

offsets verificados,


repetibilidad certificada.


10. Requisitos de Calidad Industrial

10.1 Dimensional

tolerancias certificadas,


repetibilidad de lote.


10.2 Geométrica

paralelismo,


perpendicularidad,


planitud.


10.3 Superficial

rugosidad certificada.


10.4 Documentación

registro de calidad,


informes de producción.


11. Requisitos de Documentación Industrial

11.1 Documentación obligatoria

planos mecánicos,


planos eléctricos,


topología EtherCAT,


mapa PLC/IO,


parámetros CNC‑CAT,


parámetros FLOW,


manuales técnicos.


11.2 Trazabilidad

mantenimiento,


producción,


auditorías,


calibraciones.


12. Auditorías de Planta

12.1 Auditoría mecánica

alineación,


backlash,


vibración.


12.2 Auditoría eléctrica

aislamiento,


protección.


12.3 Auditoría electrónica

drives,


IO,


FSoE.


12.4 Auditoría EtherCAT

slaves,


sincronización.


12.5 Auditoría FLOW

sensores,


actuadores.


12.6 Auditoría CNC‑CAT

interpolación,


servo,


spindle.


12.7 Auditoría de documentación

trazabilidad,


registros,


informes.


13. Criterios de Aceptación

13.1 Crítico

afecta seguridad,


afecta movimiento,


afecta spindle.


13.2 Alto

afecta precisión,


afecta FLOW.


13.3 Medio

afecta estabilidad.


13.4 Bajo

afecta eficiencia.


14. Emisión del Certificado de Planta

14.1 Requisitos

auditorías aprobadas,


documentación completa,


trazabilidad verificada,


calidad certificada,


seguridad estable.


14.2 Contenido del certificado

identificación de planta,


módulos certificados,


fecha,


versión del sistema,


firma del auditor,


firma del supervisor.


15. Estado del Documento

Manual técnico oficial.

Base para certificación industrial de planta en el ecosistema LINCAT.
