32\_auditoria\_industrial.md

Manual Técnico de Auditoría Industrial — Ecosistema LINCAT

1. Propósito del Documento

Definir los criterios, protocolos, métricas, evidencias y responsabilidades necesarias para realizar auditorías industriales certificadas en máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual garantiza que la máquina cumple estándares de calidad, seguridad, estabilidad, documentación y trazabilidad industrial.


2. Alcance

Este documento cubre:


auditoría mecánica,


auditoría eléctrica,


auditoría electrónica,


auditoría EtherCAT,


auditoría de seguridad industrial,


auditoría FLOW,


auditoría CNC‑CAT,


auditoría de documentación,


auditoría de proceso,


criterios de aceptación,


emisión del informe de auditoría.


No cubre instalación, mantenimiento ni operación.


3. Auditoría Mecánica

3.1 Precisión geométrica

paralelismo \< 0.02 mm,


perpendicularidad \< 0.03 mm,


planitud \< 0.1 mm/m.


3.2 Repetibilidad

homing \< 0.02 mm,


herramienta \< 0.03 mm.


3.3 Backlash

backlash \< 0.03 mm por eje.


3.4 Vibración

RMS \< 0.05 mm,


sin resonancias críticas.


3.5 Evidencias

mediciones,


gráficos,


FFT,


espectrogramas.


4. Auditoría Eléctrica

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


4.4 Evidencias

mediciones,


fotos de gabinete,


registros de protección.


5. Auditoría Electrónica

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


5.4 Evidencias

logs,


capturas de señales,


registros de fallos.


6. Auditoría EtherCAT

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


6.4 Evidencias

topología EtherCAT,


logs DC,


registros de slaves.


7. Auditoría de Seguridad Industrial

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


7.4 Evidencias

registros FSoE,


pruebas de enclavamiento,


capturas de señales seguras.


8. Auditoría FLOW

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


8.4 Evidencias

capturas de sensores,


registros de actuadores,


logs FLOW.


9. Auditoría CNC‑CAT

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


9.5 Evidencias

capturas CNC,


registros de interpolación,


logs de servo.


10. Auditoría de Documentación

10.1 Documentación obligatoria

planos mecánicos,


planos eléctricos,


topología EtherCAT,


mapa PLC/IO,


parámetros CNC‑CAT,


parámetros FLOW,


manuales técnicos.


10.2 Trazabilidad

registro de mantenimiento,


registro de diagnósticos,


registro de calibraciones,


registro de auditorías.


10.3 Evidencias

documentos,


firmas,


versiones.


11. Auditoría de Proceso Industrial

11.1 Secuencias FLOW

ejecución estable,


sensores dentro de rango,


actuadores operativos.


11.2 Integración CNC ↔ FLOW

consumo correcto de estados auxiliares,


sincronización estable.


11.3 Integración completa

CNC ↔ FLOW ↔ PLC/IO ↔ EtherCAT ↔ Seguridad.


11.4 Evidencias

logs de proceso,


capturas de estados,


registros de integración.


12. Criterios de Aceptación

12.1 Crítico

afecta seguridad,


afecta movimiento,


afecta spindle.


12.2 Alto

afecta precisión,


afecta FLOW.


12.3 Medio

afecta estabilidad.


12.4 Bajo

afecta eficiencia.


13. Informe Final de Auditoría

13.1 Contenido

resumen ejecutivo,


módulos auditados,


fallos detectados,


severidad,


recomendaciones,


acciones correctivas.


13.2 Emisión

firma del auditor,


firma del supervisor,


registro en trazabilidad,


versión del informe.


14. Estado del Documento

Manual técnico oficial.

Base para auditoría industrial del ecosistema LINCAT.
