36\_ingenieria\_planta.md

Manual Técnico de Ingeniería de Planta — Ecosistema LINCAT

1. Propósito del Documento

Definir los criterios, estándares, estructuras, responsabilidades y protocolos de ingeniería de planta industrial para instalaciones que operan máquinas CNC basadas en LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual garantiza que la planta cumple requisitos de infraestructura, ingeniería, seguridad, calidad, mantenimiento, producción y trazabilidad.


2. Alcance

Este documento cubre:


ingeniería de infraestructura,


ingeniería mecánica,


ingeniería eléctrica,


ingeniería electrónica,


ingeniería EtherCAT,


ingeniería de seguridad industrial,


ingeniería FLOW,


ingeniería CNC‑CAT,


ingeniería de procesos,


ingeniería de calidad,


ingeniería de mantenimiento,


ingeniería de producción,


ingeniería de documentación,


ingeniería de trazabilidad.


No cubre operación diaria ni certificación de planta.


3. Ingeniería de Infraestructura

3.1 Entorno industrial

temperatura 15–30 °C,


humedad \< 70 %,


ventilación adecuada,


iluminación certificada,


ausencia de vibraciones externas.


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


4. Ingeniería Mecánica

4.1 Estructura

rigidez mínima 1.5× respecto a deflexión admisible,


materiales certificados,


análisis de vibración.


4.2 Guiado lineal

clase H o superior,


lubricación compatible FLOW,


alineación \< 0.02 mm.


4.3 Husillos / Correas

backlash \< 0.03 mm,


precarga P3,


tensión controlada.


5. Ingeniería Eléctrica

5.1 Alimentación

líneas dedicadas,


caída de tensión \< 5 %,


protección industrial.


5.2 Gabinetes

IP54 mínimo,


ventilación forzada,


separación potencia/control.


5.3 Aislamiento

control \> 1 MΩ,


potencia \> 10 MΩ.


6. Ingeniería Electrónica

6.1 Drives

EtherCAT nativo,


feedback estable,


parámetros certificados.


6.2 IO

módulos digitales y analógicos certificados,


FSoE operativo.


6.3 Spindle

variador certificado,


feedback de velocidad,


vibración dentro de límites.


7. Ingeniería EtherCAT

7.1 Topología

Master → Drives → IO → FSoE,


sin bifurcaciones,


cable CAT6 industrial.


7.2 Sincronización

ciclo DC 1000 µs,


jitter dentro de tolerancia.


7.3 Slaves

todos online,


sin slave\_fault.


8. Ingeniería de Seguridad Industrial

8.1 Elementos críticos

enclavamiento de puerta,


zona segura,


parada segura,


relés de seguridad,


sensores seguros.


8.2 Estados

SafetyOk,


SafetyFault,


SafetyLock.


8.3 Normativas

cumplimiento de normativa europea,


documentación de seguridad,


auditoría de seguridad.


9. Ingeniería FLOW

9.1 Sensores industriales

vacío, aire, lubricación, hidráulica, refrigerante.


9.2 Actuadores industriales

válvulas, bombas, contactores.


9.3 Estados auxiliares

VacuumReady, AirReady, LubeReady, HydraulicReady, CoolantReady, SafetyOk, ProcessReady.


10. Ingeniería CNC‑CAT

10.1 Interpolación

precisión lineal \< 0.05 mm,


precisión circular \< 0.07 mm.


10.2 Servo

estabilidad de posición,


ausencia de vibración.


10.3 Spindle

velocidad dentro de tolerancia,


dirección correcta.


10.4 Herramientas

offsets verificados,


repetibilidad certificada.


11. Ingeniería de Procesos Industriales

11.1 Secuencias FLOW

ejecución estable,


sensores dentro de rango,


actuadores operativos.


11.2 Integración CNC ↔ FLOW

consumo correcto de estados auxiliares,


sincronización estable.


11.3 Integración completa

CNC ↔ FLOW ↔ PLC/IO ↔ EtherCAT ↔ Seguridad.


12. Ingeniería de Calidad Industrial

12.1 Dimensional

tolerancias certificadas,


repetibilidad de lote.


12.2 Geométrica

paralelismo,


perpendicularidad,


planitud.


12.3 Superficial

rugosidad certificada.


12.4 Documentación

registro de calidad,


informes de producción.


13. Ingeniería de Mantenimiento

13.1 Mantenimiento mecánico

alineación,


backlash,


vibración.


13.2 Mantenimiento eléctrico

aislamiento,


protección.


13.3 Mantenimiento electrónico

drives,


IO,


FSoE.


13.4 Mantenimiento CNC‑CAT

interpolación,


servo,


spindle.


14. Ingeniería de Producción

14.1 Validación de máquina

homing,


FLOW,


seguridad,


EtherCAT.


14.2 Validación de proceso

material,


herramientas,


parámetros CNC,


secuencia FLOW.


14.3 Control de calidad

dimensional,


geométrico,


superficial.


15. Ingeniería de Documentación

15.1 Documentación obligatoria

planos mecánicos,


planos eléctricos,


topología EtherCAT,


mapa PLC/IO,


parámetros CNC‑CAT,


parámetros FLOW,


manuales técnicos.


15.2 Trazabilidad

mantenimiento,


producción,


auditorías,


calibraciones.


16. Ingeniería de Trazabilidad

16.1 Registros obligatorios

mantenimiento,


producción,


auditorías,


calibraciones,


fallos.


16.2 Formato

YAML técnico,


informes de trazabilidad.


16.3 Conservación

mínimo 15 años.


17. Estado del Documento

Manual técnico oficial.

Base para ingeniería de planta industrial en el ecosistema LINCAT.
