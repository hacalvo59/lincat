33\_trazabilidad\_industrial.md

Manual Técnico de Trazabilidad Industrial — Ecosistema LINCAT

1. Propósito del Documento

Definir los criterios, estructuras, protocolos y responsabilidades para garantizar la trazabilidad industrial completa en máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual asegura que cada acción, señal, estado, proceso, mantenimiento y producción quede registrado, verificable, auditable y reproducible.


2. Alcance

Este documento cubre:


trazabilidad mecánica,


trazabilidad eléctrica,


trazabilidad electrónica,


trazabilidad EtherCAT,


trazabilidad de seguridad industrial,


trazabilidad FLOW,


trazabilidad CNC‑CAT,


trazabilidad de producción,


trazabilidad de mantenimiento,


trazabilidad de auditoría,


estructuras de registro,


criterios de conservación,


emisión de informes.


No cubre instalación ni operación.


3. Principios de Trazabilidad Industrial

3.1 Integridad

Toda información debe ser completa, verificable y sin omisiones.


3.2 Inmutabilidad

Los registros no pueden ser alterados una vez emitidos.


3.3 Temporalidad

Cada registro debe incluir fecha, hora y versión del sistema.


3.4 Identidad

Cada acción debe estar asociada a un operario, técnico o auditor.


3.5 Reproducibilidad

Toda acción registrada debe poder repetirse con los mismos resultados.


4. Trazabilidad Mecánica

4.1 Registros obligatorios

alineación de ejes,


backlash,


vibración,


planitud,


desgaste de guías,


calibración mecánica.


4.2 Evidencias

mediciones,


gráficos,


FFT,


espectrogramas,


fotos de componentes.


4.3 Conservación

mínimo 5 años,


formato digital y físico.


5. Trazabilidad Eléctrica

5.1 Registros obligatorios

aislamiento,


caída de tensión,


estado de gabinete,


protección eléctrica.


5.2 Evidencias

mediciones,


fotos de gabinete,


registros de protección.


5.3 Conservación

mínimo 5 años.


6. Trazabilidad Electrónica

6.1 Registros obligatorios

estado de drives,


estado de IO,


estado de FSoE,


fallos electrónicos.


6.2 Evidencias

logs,


capturas de señales,


registros de fallos.


6.3 Conservación

mínimo 5 años.


7. Trazabilidad EtherCAT

7.1 Registros obligatorios

estado de slaves,


sincronización DC,


ciclo determinístico,


fallos EtherCAT.


7.2 Evidencias

topología EtherCAT,


logs DC,


registros de slaves.


7.3 Conservación

mínimo 5 años.


8. Trazabilidad de Seguridad Industrial

8.1 Registros obligatorios

enclavamiento de puerta,


zona segura,


parada segura,


canales FSoE,


estados SafetyOk, SafetyFault, SafetyLock.


8.2 Evidencias

registros FSoE,


pruebas de enclavamiento,


capturas de señales seguras.


8.3 Conservación

mínimo 10 años (normativa de seguridad).


9. Trazabilidad FLOW

9.1 Registros obligatorios

sensores industriales,


actuadores industriales,


estados auxiliares,


alarmas FLOW.


9.2 Evidencias

capturas de sensores,


registros de actuadores,


logs FLOW.


9.3 Conservación

mínimo 5 años.


10. Trazabilidad CNC‑CAT

10.1 Registros obligatorios

homing,


interpolación,


servo,


spindle,


herramientas,


fallos CNC.


10.2 Evidencias

capturas CNC,


registros de interpolación,


logs de servo.


10.3 Conservación

mínimo 5 años.


11. Trazabilidad de Producción

11.1 Registros obligatorios

lote,


material,


parámetros CNC,


parámetros FLOW,


herramientas,


tolerancias,


repetibilidad.


11.2 Evidencias

mediciones,


capturas de señales,


logs EtherCAT,


registros FLOW.


11.3 Conservación

mínimo 10 años (normativa de producción).


12. Trazabilidad de Mantenimiento

12.1 Registros obligatorios

mantenimiento diario,


mantenimiento semanal,


mantenimiento mensual,


mantenimiento avanzado,


calibraciones,


reemplazos.


12.2 Evidencias

informes,


fotos,


mediciones,


logs.


12.3 Conservación

mínimo 10 años.


13. Trazabilidad de Auditoría

13.1 Registros obligatorios

auditoría mecánica,


auditoría eléctrica,


auditoría electrónica,


auditoría EtherCAT,


auditoría FLOW,


auditoría CNC‑CAT,


auditoría de seguridad,


auditoría de documentación.


13.2 Evidencias

informes,


capturas,


logs,


firmas,


versiones.


13.3 Conservación

mínimo 10 años.


14. Estructuras de Registro

14.1 Formato estándar

Código

registro:

  fecha: YYYY-MM-DD HH:MM:SS

  operario: nombre

  modulo: CNC/FLOW/PLC/IO/ECAT/SAFETY

  accion: descripción técnica

  estado: OK/FAULT/WARNING

  evidencia: archivo o referencia

  version: sistema

14.2 Requisitos

formato YAML o JSON,


firma digital,


almacenamiento redundante.


15. Criterios de Aceptación

15.1 Crítico

afecta seguridad,


afecta movimiento,


afecta spindle.


15.2 Alto

afecta precisión,


afecta FLOW.


15.3 Medio

afecta estabilidad.


15.4 Bajo

afecta eficiencia.


16. Informe Final de Trazabilidad

16.1 Contenido

resumen,


registros,


evidencias,


fallos,


acciones correctivas.


16.2 Emisión

firma del técnico,


firma del supervisor,


registro en auditoría,


versión del informe.


17. Estado del Documento

Manual técnico oficial.

Base para trazabilidad industrial del ecosistema LINCAT.
