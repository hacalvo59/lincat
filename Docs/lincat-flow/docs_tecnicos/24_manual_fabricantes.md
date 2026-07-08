24\_manual\_fabricantes.md

Manual Técnico para Fabricantes — Ecosistema LINCAT

1. Propósito del Manual

Este manual provee a fabricantes, integradores y talleres industriales toda la información técnica necesaria para construir, ensamblar, cablear, integrar y validar máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + SIM/REAL).


2. Alcance

Este documento cubre:


requisitos mecánicos, eléctricos y electrónicos,


integración EtherCAT,


integración PLC/IO,


integración de seguridad industrial,


interfaces CNC‑CAT y FLOW,


parámetros técnicos,


validación y pruebas,


puesta en marcha REAL,


mantenimiento técnico.


No cubre diseño conceptual ni arquitectura de software.


3. Requisitos Mecánicos del Fabricante

3.1 Estructura Mecánica

Rigidez mínima: 1.5× respecto a deflexión admisible.


Material recomendado: acero soldado o aluminio estructural.


Vibración máxima admisible: \< 0.05 mm RMS.


Planitud de bancada: \< 0.1 mm/m.


3.2 Guiado Lineal

Tipo: guías lineales recirculantes.


Precisión: clase H o superior.


Lubricación: compatible con FLOW (lube industrial).


3.3 Husillos / Correas

Husillos: paso 5–10 mm, precarga P3.


Correas: HTD o GT3, tensión controlada.


4. Requisitos Eléctricos

4.1 Alimentación

230 VAC monofásico o 400 VAC trifásico.


Protección: magnetotérmico + diferencial.


UPS opcional para control.


4.2 Gabinete Eléctrico

IP54 mínimo.


Ventilación forzada.


Separación de potencia/control.


4.3 Cableado

Señales: blindado, par trenzado.


Potencia: cables 2.5–4 mm².


Seguridad: cableado FSoE dedicado.


5. Requisitos Electrónicos

5.1 Drives

EtherCAT nativo.


Modo: posición/velocidad.


Feedback: encoder absoluto o incremental.


5.2 Spindle

Variador EtherCAT o módulo dedicado.


Feedback de velocidad obligatorio.


5.3 IO

Módulos digitales y analógicos EtherCAT.


Módulos FSoE para seguridad.


6. Integración EtherCAT

6.1 Topología

Master → Drives → IO → FSoE.


Sin bifurcaciones.


Longitud máxima por tramo: 70 m.


6.2 Configuración

Ciclo DC: 1000 µs.


Watchdog: 50 ms.


Sincronización CNC ↔ EtherCAT obligatoria.


7. Integración PLC/IO

7.1 Señales Críticas

estop


door


probe


limit\_min/max


axis\_fault


spindle\_fault


7.2 Actuadores

válvulas, bombas, contactores, relés.


7.3 Analogía

presión, nivel, flujo, velocidad.


8. Integración de Seguridad

8.1 Canales FSoE

sin\_door\_safe


sin\_zone\_safe


sin\_estop\_safe


sin\_drive\_safe


sin\_spindle\_safe


8.2 Estados

SafetyOk


SafetyFault


SafetyLock


8.3 Requisitos

enclavamiento de puerta,


zona segura,


parada segura,


canal seguro activo.


9. Integración CNC‑CAT

9.1 Interfaces CNC

servo, spindle, interpolación, herramientas.


señales determinísticas.


feedback EtherCAT.


9.2 Estados CNC

Idle, Ready, Homing, Running, Paused, Stopped, Error.


9.3 API CNC

carga de programa,


movimiento,


spindle,


herramientas,


estados,


fallos.


10. Integración FLOW

10.1 Servicios Industriales

vacío, aire, lubricación, hidráulica, refrigerante.


10.2 Estados Auxiliares

VacuumReady, AirReady, LubeReady, HydraulicReady, CoolantReady, SafetyOk, ProcessReady.


10.3 API FLOW

sensores, actuadores, seguridad, proceso.


11. Parámetros Técnicos

11.1 CNC

feed, rapid, homing, spindle.


11.2 FLOW

presión, nivel, flujo, umbrales.


11.3 EtherCAT

ciclo DC, watchdog, sincronización.


11.4 Seguridad

debounce, safe-check.


12. Validación Técnica

12.1 Validación Mecánica

alineación de ejes,


backlash,


vibración,


planitud.


12.2 Validación Eléctrica

continuidad,


aislamiento,


protección.


12.3 Validación Electrónica

drives,


IO,


FSoE.


12.4 Validación CNC

homing,


interpolación,


spindle,


herramientas.


12.5 Validación FLOW

sensores,


actuadores,


estados auxiliares.


13. Puesta en Marcha REAL

13.1 Secuencia

Energizar gabinete.


Verificar seguridad.


Inicializar EtherCAT.


Inicializar FLOW.


Habilitar servo.


Homing.


Validar estados FLOW.


Ejecutar prueba CNC.


Ejecutar proceso FLOW.


Validar integración completa.


14. Mantenimiento Técnico

14.1 Diario

lubricación,


presión de aire,


nivel de refrigerante.


14.2 Semanal

alineación,


limpieza de guías,


verificación de sensores.


14.3 Mensual

calibración,


inspección eléctrica,


verificación de seguridad.


15. Estado del Documento

Manual técnico oficial para fabricantes.

Base para construcción e integración industrial de máquinas CNC con LINCAT.
