26\_mantenimiento\_avanzado.md

Manual Técnico de Mantenimiento Avanzado — Ecosistema LINCAT

1. Propósito del Documento

Definir los procedimientos técnicos avanzados de mantenimiento para máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Incluye calibraciones, diagnósticos, reemplazos, validaciones, análisis de vibración, mantenimiento predictivo y criterios de intervención.


2. Alcance

Este documento cubre:


mantenimiento mecánico avanzado,


mantenimiento eléctrico,


mantenimiento electrónico,


mantenimiento EtherCAT,


mantenimiento de seguridad industrial,


mantenimiento FLOW,


mantenimiento CNC‑CAT,


mantenimiento predictivo,


criterios de reemplazo,


validación post‑mantenimiento.


No cubre instalación ni integración.


3. Mantenimiento Mecánico Avanzado

3.1 Alineación de guías lineales

Verificación con reloj comparador (\< 0.02 mm).


Corrección mediante ajuste de tornillería.


Validación con recorrido completo.


3.2 Backlash de husillos

Medición con indicador (\< 0.03 mm).


Ajuste de tuerca de precarga.


Reemplazo si supera tolerancia.


3.3 Vibración estructural

Análisis RMS y FFT.


Identificación de resonancias.


Ajuste de rigidez o amortiguación.


3.4 Lubricación avanzada

Verificación de flujo real.


Limpieza de líneas.


Reemplazo de bomba si el caudal cae \> 30%.


4. Mantenimiento Eléctrico Avanzado

4.1 Verificación de aislamiento

Megóhmetro: \> 1 MΩ en control.


10 MΩ en potencia.


4.2 Revisión de gabinete

Limpieza de polvo.


Verificación de ventilación.


Reapriete de borneras.


4.3 Protección eléctrica

Verificación de magnetotérmicos.


Verificación de diferencial.


Test de caída de tensión.


5. Mantenimiento Electrónico Avanzado

5.1 Drives

Verificación de encoder.


Revisión de parámetros.


Test de homing.


Validación de torque.


5.2 Spindle

Verificación de variador.


Test de velocidad real.


Revisión de rodamientos.


Análisis de vibración del spindle.


5.3 IO

Test de entradas digitales.


Test de salidas digitales.


Test de entradas analógicas.


Test de salidas analógicas.


6. Mantenimiento EtherCAT Avanzado

6.1 Slaves

Verificación de estado online.


Revisión de slave\_fault.


Validación de sincronización DC.


6.2 Drives

Verificación de drive\_safe.


Test de watchdog.


Validación de ciclo determinístico.


6.3 FSoE

Test de canales seguros.


Verificación de safe\_channel\_ok.


Validación de enclavamientos.


7. Mantenimiento de Seguridad Industrial

7.1 Puerta

Test de enclavamiento.


Verificación de sensor seguro.


Validación de apertura controlada.


7.2 Zona segura

Test de barreras.


Verificación de sensores.


Validación de bloqueo.


7.3 Parada segura

Test de sin\_estop\_safe.


Verificación de relés de seguridad.


Validación de tiempo de respuesta.


8. Mantenimiento FLOW Avanzado

8.1 Sensores industriales

Calibración de presión.


Calibración de nivel.


Calibración de flujo.


Validación de estabilidad.


8.2 Actuadores industriales

Test de válvulas.


Test de bombas.


Verificación de caudal real.


8.3 Estados auxiliares

Validación de VacuumReady.


Validación de AirReady.


Validación de LubeReady.


Validación de HydraulicReady.


Validación de CoolantReady.


9. Mantenimiento CNC‑CAT Avanzado

9.1 Interpolación

Validación de trayectoria.


Test de precisión.


Verificación de feed.


9.2 Servo

Test de habilitación.


Verificación de torque.


Validación de estabilidad.


9.3 Spindle

Test de velocidad.


Verificación de dirección.


Validación de potencia.


9.4 Herramientas

Verificación de offsets.


Test de cambio de herramienta.


Validación de repetibilidad.


10. Mantenimiento Predictivo

10.1 Vibración

RMS, pico, FFT, espectrograma.


Identificación de desgaste.


Detección de resonancias.


10.2 Tendencias

análisis de sparklines,


análisis de energía por banda,


análisis de picos intermitentes.


10.3 AI Advisor

diagnóstico probable,


severidad,


recomendación,


causa raíz sugerida.


11. Criterios de Reemplazo

11.1 Mecánicos

backlash \> 0.05 mm,


vibración \> 0.1 mm RMS,


guías con desgaste visible.


11.2 Eléctricos

aislamiento \< 1 MΩ,


conectores dañados,


cables con rotura.


11.3 Electrónicos

drives con fallos recurrentes,


IO inestable,


FSoE con fallos.


12. Validación Post‑Mantenimiento

12.1 CNC

homing,


interpolación,


spindle,


herramientas.


12.2 FLOW

sensores,


actuadores,


estados auxiliares.


12.3 Seguridad

enclavamientos,


zonas,


parada segura.


12.4 EtherCAT

slaves,


drives,


FSoE.


13. Estado del Documento

Manual técnico oficial.

Base para mantenimiento avanzado del ecosistema LINCAT.
