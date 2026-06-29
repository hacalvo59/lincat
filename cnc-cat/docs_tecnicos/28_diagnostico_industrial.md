28\_diagnostico\_industrial.md

Manual Técnico de Diagnóstico Industrial — Ecosistema LINCAT

1. Propósito del Documento

Definir los métodos, procedimientos, señales, estructuras y criterios técnicos para diagnosticar fallos mecánicos, eléctricos, electrónicos, EtherCAT, FLOW, PLC/IO, seguridad y CNC‑CAT dentro del ecosistema LINCAT.

Este manual permite identificar causas raíz, aislar fallos, validar hipótesis y emitir diagnósticos industriales reproducibles.


2. Alcance

Este documento cubre:


diagnóstico mecánico,


diagnóstico eléctrico,


diagnóstico electrónico,


diagnóstico EtherCAT,


diagnóstico de seguridad industrial,


diagnóstico FLOW,


diagnóstico PLC/IO,


diagnóstico CNC‑CAT,


diagnóstico predictivo,


criterios de severidad,


documentación del diagnóstico.


No cubre instalación ni mantenimiento.


3. Diagnóstico Mecánico

3.1 Alineación

desviación \> 0.02 mm indica desalineación,


verificar paralelismo y perpendicularidad,


revisar fijaciones y tensiones.


3.2 Backlash

backlash \> 0.03 mm indica desgaste,


verificar tuerca de precarga,


revisar husillo y soporte.


3.3 Vibración

RMS \> 0.05 mm indica resonancia o desgaste,


analizar FFT,


identificar frecuencias dominantes.


3.4 Guiado lineal

ruido o fricción indica contaminación,


verificar lubricación,


revisar desgaste de patines.


4. Diagnóstico Eléctrico

4.1 Alimentación

caída de tensión \> 5 %,


ruido eléctrico en señales,


verificar tierra y protección.


4.2 Gabinete

temperatura elevada,


ventilación insuficiente,


cables sueltos o dañados.


4.3 Aislamiento

control \< 1 MΩ,


potencia \< 10 MΩ.


5. Diagnóstico Electrónico

5.1 Drives

fallos recurrentes → encoder o cableado,


homing inestable → feedback incorrecto,


torque irregular → problema mecánico o eléctrico.


5.2 Spindle

velocidad inestable → variador o sensor,


vibración → rodamientos,


sobrecorriente → carga excesiva.


5.3 IO

entradas inestables → ruido eléctrico,


salidas sin respuesta → actuador o módulo,


analógicos fuera de rango → sensor o calibración.


6. Diagnóstico EtherCAT

6.1 Slaves

slave\_fault → cableado o módulo,


slave\_online=false → topología o alimentación,


jitter en DC → interferencias o mala sincronización.


6.2 Drives

drive\_fault → encoder, motor o parámetros,


drive\_safe=false → canal seguro o FSoE.


6.3 FSoE

safe\_channel\_fault → cableado seguro,


safe\_in inestable → sensor seguro defectuoso.


7. Diagnóstico de Seguridad Industrial

7.1 Puerta

enclavamiento no activa → sensor o actuador,


apertura inesperada → cableado o desgaste.


7.2 Zona segura

barrera no detecta → alineación o sensor,


activación falsa → ruido o suciedad.


7.3 Parada segura

tiempo de respuesta elevado → relé o drive,


fallo de canal → FSoE o cableado.


8. Diagnóstico FLOW

8.1 Sensores

vacío fuera de rango → fuga o bomba,


presión de aire baja → compresor o válvula,


flujo de lubricación bajo → bomba o línea,


hidráulica inestable → válvula o presión.


8.2 Actuadores

válvula sin respuesta → IO o actuador,


bomba sin caudal → motor o obstrucción.


8.3 Estados auxiliares

VacuumReady falso → fuga o sensor,


AirReady falso → compresor o regulador,


LubeReady falso → bomba o línea,


HydraulicReady falso → presión insuficiente.


9. Diagnóstico PLC/IO

9.1 Digitales

rebotes → ruido o sensor,


activación falsa → cableado o interferencia.


9.2 Analógicos

valores erráticos → sensor o calibración,


valores saturados → fallo de módulo.


9.3 Señales críticas

estop inestable → cableado o botón,


door falso → sensor o alineación,


probe errático → sonda o interferencia.


10. Diagnóstico CNC‑CAT

10.1 Interpolación

trayectoria incorrecta → parámetros o feedback,


error circular → backlash o calibración.


10.2 Servo

vibración → tuning o mecánica,


pérdida de posición → encoder o drive.


10.3 Spindle

velocidad incorrecta → variador o sensor,


potencia insuficiente → carga o drive.


10.4 Herramientas

offsets incorrectos → calibración,


repetibilidad baja → mecánica o husillo.


11. Diagnóstico Predictivo

11.1 Vibración avanzada

análisis FFT,


espectrograma,


energía por banda,


detección de resonancias.


11.2 Tendencias

análisis de sparklines,


análisis de picos intermitentes,


análisis de deriva lenta.


11.3 AI Advisor

diagnóstico probable,


severidad,


recomendación,


causa raíz sugerida.


12. Criterios de Severidad

12.1 Crítico

afecta seguridad,


afecta movimiento,


afecta spindle.


12.2 Alto

afecta precisión,


afecta proceso FLOW.


12.3 Medio

afecta estabilidad,


afecta repetibilidad.


12.4 Bajo

afecta confort,


afecta eficiencia.


13. Documentación del Diagnóstico

13.1 Registro

fecha,


técnico,


módulo afectado,


señales,


estados,


causa raíz.


13.2 Evidencias

capturas de señales,


FFT,


espectrogramas,


logs EtherCAT.


13.3 Informe final

diagnóstico,


severidad,


recomendación,


acciones correctivas.


14. Estado del Documento

Manual técnico oficial.

Base para diagnóstico industrial del ecosistema LINCAT.
