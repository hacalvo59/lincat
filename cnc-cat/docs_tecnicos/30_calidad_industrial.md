30\_calidad\_industrial.md

Manual Técnico de Calidad Industrial — Ecosistema LINCAT

1. Propósito del Documento

Establecer los criterios, métricas, protocolos y procedimientos necesarios para asegurar la calidad industrial certificada en máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual define estándares de precisión, estabilidad, repetibilidad, seguridad, documentación y auditoría.


2. Alcance

Este documento cubre:


calidad mecánica,


calidad eléctrica,


calidad electrónica,


calidad EtherCAT,


calidad de seguridad industrial,


calidad FLOW,


calidad CNC‑CAT,


calidad de proceso,


calidad de documentación,


auditorías internas y externas.


No cubre instalación ni mantenimiento.


3. Calidad Mecánica

3.1 Precisión geométrica

paralelismo \< 0.02 mm,


perpendicularidad \< 0.03 mm,


planitud \< 0.1 mm/m.


3.2 Repetibilidad

repetibilidad de homing \< 0.02 mm,


repetibilidad de herramienta \< 0.03 mm.


3.3 Backlash

backlash \< 0.03 mm por eje.


3.4 Vibración

RMS \< 0.05 mm,


sin resonancias críticas.


4. Calidad Eléctrica

4.1 Alimentación

caída de tensión \< 5 %,


ruido eléctrico dentro de tolerancia.


4.2 Aislamiento

control \> 1 MΩ,


potencia \> 10 MΩ.


4.3 Gabinete

IP54 mínimo,


ventilación adecuada,


separación potencia/control.


5. Calidad Electrónica

5.1 Drives

feedback estable,


torque dentro de rango,


homing repetible.


5.2 Spindle

velocidad real dentro de ±3 %,


vibración dentro de límites,


potencia estable.


5.3 IO

entradas digitales sin rebotes,


salidas digitales estables,


analógicos calibrados.


6. Calidad EtherCAT

6.1 Slaves

todos online,


sin slave\_fault,


sincronización DC estable.


6.2 Drives

drive\_safe activo,


watchdog operativo,


ciclo determinístico 1000 µs.


6.3 FSoE

canales seguros estables,


sin safe\_channel\_fault.


7. Calidad de Seguridad Industrial

7.1 Estados

SafetyOk estable,


sin SafetyFault,


sin SafetyLock inesperado.


7.2 Elementos críticos

enclavamiento de puerta,


zona segura,


parada segura,


relés de seguridad.


7.3 Tiempos

tiempo de respuesta dentro de norma,


verificación periódica de sensores seguros.


8. Calidad FLOW

8.1 Sensores

vacío dentro de rango,


presión de aire estable,


flujo de lubricación correcto,


hidráulica estable,


nivel de refrigerante adecuado.


8.2 Actuadores

válvulas con respuesta certificada,


bombas con caudal dentro de tolerancia.


8.3 Estados auxiliares

VacuumReady, AirReady, LubeReady, HydraulicReady, CoolantReady, SafetyOk, ProcessReady.


9. Calidad CNC‑CAT

9.1 Interpolación

precisión lineal \< 0.05 mm,


precisión circular \< 0.07 mm.


9.2 Servo

estabilidad de posición,


ausencia de vibración,


respuesta dentro de parámetros.


9.3 Spindle

velocidad dentro de tolerancia,


dirección correcta,


feedback estable.


9.4 Herramientas

offsets verificados,


repetibilidad certificada.


10. Calidad de Proceso Industrial

10.1 Secuencias FLOW

ejecución estable,


sensores dentro de rango,


actuadores operativos.


10.2 Integración CNC ↔ FLOW

consumo correcto de estados auxiliares,


sincronización estable.


10.3 Integración completa

CNC ↔ FLOW ↔ PLC/IO ↔ EtherCAT ↔ Seguridad.


11. Calidad de Documentación

11.1 Documentación obligatoria

planos mecánicos,


planos eléctricos,


topología EtherCAT,


mapa PLC/IO,


parámetros CNC‑CAT,


parámetros FLOW,


manuales técnicos.


11.2 Trazabilidad

registro de mantenimiento,


registro de diagnósticos,


registro de calibraciones,


registro de auditorías.


12. Auditorías de Calidad

12.1 Auditoría interna

revisión mensual,


verificación de tolerancias,


validación de seguridad.


12.2 Auditoría externa

certificación anual,


verificación de documentación,


validación de parámetros.


12.3 Auditoría de proceso

análisis de producción,


análisis de estabilidad,


análisis de repetibilidad.


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


14. Estado del Documento

Manual técnico oficial.

Base para calidad industrial del ecosistema LINCAT.
