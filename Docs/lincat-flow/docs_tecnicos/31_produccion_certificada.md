31\_produccion\_certificada.md

Manual Técnico de Producción Certificada — Ecosistema LINCAT

1. Propósito del Documento

Definir los criterios, protocolos, controles, verificaciones y documentación necesarios para ejecutar producción certificada en máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual garantiza que cada pieza fabricada cumple estándares industriales de precisión, repetibilidad, estabilidad, seguridad y trazabilidad.


2. Alcance

Este documento cubre:


requisitos previos de producción,


validación de máquina,


validación de proceso,


control de calidad en producción,


control de seguridad en producción,


control de FLOW en producción,


control CNC‑CAT en producción,


documentación de producción,


auditoría de producción,


criterios de aceptación,


emisión de lote certificado.


No cubre instalación, mantenimiento ni diagnóstico.


3. Requisitos Previos de Producción

3.1 Máquina

CNC‑CAT en estado Ready,


FLOW operativo,


seguridad estable,


EtherCAT sincronizado,


IO sin fallos,


spindle dentro de parámetros.


3.2 Entorno

temperatura 15–30 °C,


humedad \< 70 %,


ausencia de vibraciones externas.


3.3 Operario

formación certificada,


conocimiento de enclavamientos,


EPI obligatorio.


3.4 Documentación

plano de pieza,


tolerancias,


material,


proceso,


herramientas,


parámetros CNC.


4. Validación de Máquina para Producción

4.1 Validación mecánica

homing repetible \< 0.02 mm,


backlash \< 0.03 mm,


vibración \< 0.05 mm RMS.


4.2 Validación eléctrica

alimentación estable,


aislamiento dentro de norma,


gabinete sin fallos.


4.3 Validación electrónica

drives sin fallos,


IO estable,


FSoE operativo.


4.4 Validación EtherCAT

todos los slaves online,


sincronización DC estable,


ciclo determinístico 1000 µs.


4.5 Validación FLOW

sensores dentro de rango,


actuadores operativos,


estados auxiliares Ready.


4.6 Validación de seguridad

enclavamiento de puerta,


zona segura,


parada segura,


SafetyOk estable.


5. Validación del Proceso de Producción

5.1 Material

lote verificado,


dureza dentro de rango,


dimensiones certificadas.


5.2 Herramientas

herramienta correcta,


desgaste dentro de tolerancia,


offsets verificados.


5.3 Parámetros CNC

feed dentro de rango,


velocidad de spindle certificada,


profundidad de corte dentro de tolerancia.


5.4 Secuencia FLOW

vacío, aire, lubricación, hidráulica y refrigerante operativos,


sin alarmas FLOW.


5.5 Seguridad

enclavamiento activo,


zona segura estable,


sin SafetyFault.


6. Control de Calidad en Producción

6.1 Control dimensional

medición de pieza inicial,


medición de pieza intermedia,


medición de pieza final.


6.2 Control geométrico

paralelismo,


perpendicularidad,


planitud,


circularidad.


6.3 Control superficial

rugosidad,


acabado,


defectos visibles.


6.4 Control de repetibilidad

repetibilidad de lote,


desviación estándar,


estabilidad del proceso.


7. Control de Seguridad en Producción

7.1 Señales críticas

estop,


door,


zone,


safe\_motion\_ready.


7.2 Estados críticos

SafetyOk,


SafetyFault,


SafetyLock.


7.3 Reglas

SafetyOk obligatorio para producción,


SafetyFault detiene producción,


SafetyLock bloquea movimiento.


8. Control FLOW en Producción

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


9. Control CNC‑CAT en Producción

9.1 Interpolación

trayectoria estable,


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


10. Documentación de Producción

10.1 Registro

lote,


fecha,


operario,


máquina,


parámetros CNC,


parámetros FLOW,


material,


herramientas.


10.2 Evidencias

mediciones,


capturas de señales,


logs EtherCAT,


registros FLOW.


10.3 Informe final

calidad,


tolerancias,


repetibilidad,


estabilidad,


seguridad.


11. Auditoría de Producción

11.1 Auditoría interna

revisión de lote,


verificación de tolerancias,


validación de seguridad.


11.2 Auditoría externa

certificación anual,


verificación de documentación,


validación de parámetros.


11.3 Auditoría de proceso

análisis de producción,


análisis de estabilidad,


análisis de repetibilidad.


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


13. Emisión de Lote Certificado

Un lote queda certificado si:


cumple tolerancias mecánicas,


cumple tolerancias geométricas,


cumple tolerancias superficiales,


FLOW estable,


seguridad estable,


CNC‑CAT estable,


documentación completa,


auditoría aprobada.


14. Estado del Documento

Manual técnico oficial.

Base para producción certificada del ecosistema LINCAT.
