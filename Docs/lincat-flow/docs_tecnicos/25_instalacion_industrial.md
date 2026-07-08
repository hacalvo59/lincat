25\_instalacion\_industrial.md

Documentación de Instalación Industrial — Ecosistema LINCAT

1. Propósito del Documento

Definir los requisitos, procedimientos técnicos, conexiones, verificaciones y parámetros necesarios para instalar el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL) en una máquina CNC industrial.


2. Alcance

Este documento cubre:


instalación mecánica,


instalación eléctrica,


instalación electrónica,


instalación EtherCAT,


instalación PLC/IO,


instalación de seguridad industrial,


instalación de sensores y actuadores FLOW,


instalación del control CNC‑CAT,


instalación del gabinete industrial,


instalación del modo REAL.


No cubre diseño conceptual ni simulación.


3. Instalación Mecánica

3.1 Bancada y estructura

Nivelación industrial (\< 0.1 mm/m).


Rigidez mínima 1.5× respecto a deflexión admisible.


Aislamiento de vibraciones.


Puntos de anclaje definidos.


3.2 Guiado lineal

Montaje de guías lineales clase H o superior.


Alineación paralela \< 0.02 mm.


Lubricación compatible con FLOW.


3.3 Husillos / Correas

Husillos: precarga P3, alineación axial \< 0.03 mm.


Correas: tensión controlada, poleas alineadas.


4. Instalación Eléctrica

4.1 Alimentación

230 VAC monofásico o 400 VAC trifásico.


Protección: magnetotérmico + diferencial.


UPS opcional para control.


4.2 Gabinete industrial

IP54 mínimo.


Placas DIN para drives, IO, FSoE.


Separación potencia/control.


Ventilación forzada.


4.3 Cableado

Señales: blindado, par trenzado.


Potencia: 2.5–4 mm².


Seguridad: cableado dedicado FSoE.


5. Instalación Electrónica

5.1 Drives

Montaje en riel DIN.


Conexión EtherCAT IN/OUT.


Conexión encoder.


Conexión motor trifásico.


5.2 Spindle

Variador EtherCAT o módulo dedicado.


Feedback de velocidad obligatorio.


Conexión de potencia trifásica.


5.3 IO

Módulos digitales y analógicos EtherCAT.


Módulos FSoE para seguridad.


6. Instalación EtherCAT

6.1 Topología

Master → Drives → IO → FSoE.


Sin bifurcaciones.


Cable CAT6 industrial.


Longitud máxima por tramo: 70 m.


6.2 Configuración

Ciclo DC: 1000 µs.


Watchdog: 50 ms.


Sincronización CNC ↔ EtherCAT obligatoria.


6.3 Verificación

Todos los slaves deben estar online.


Sin fallos en drives.


Canales seguros activos.


7. Instalación PLC/IO

7.1 Entradas críticas

estop


door


probe


limit\_min/max


axis\_fault


spindle\_fault


7.2 Salidas críticas

servo\_enable


spindle\_enable


tool\_change


probe\_enable


7.3 Señales analógicas

presión, nivel, flujo, velocidad.


8. Instalación de Seguridad Industrial

8.1 Canales FSoE

sin\_door\_safe


sin\_zone\_safe


sin\_estop\_safe


sin\_drive\_safe


sin\_spindle\_safe


8.2 Elementos físicos

enclavamiento de puerta,


zona segura,


parada segura,


relés de seguridad.


8.3 Verificación

SafetyOk antes de habilitar servo.


SafetyLock bloquea movimiento.


SafetyFault requiere reset.


9. Instalación de Sensores y Actuadores FLOW

9.1 Sensores industriales

vacío, aire, lubricación, hidráulica, refrigerante.


montaje en puntos accesibles.


calibración inicial.


9.2 Actuadores industriales

válvulas, bombas, contactores.


conexión IO EtherCAT.


verificación de respuesta.


9.3 Estados auxiliares

VacuumReady


AirReady


LubeReady


HydraulicReady


CoolantReady


SafetyOk


ProcessReady


10. Instalación del Control CNC‑CAT

10.1 Conexiones

EtherCAT master.


IO crítico.


sensores de límites.


sonda.


spindle.


drives.


10.2 Verificación

homing,


interpolación,


spindle,


herramientas.


11. Instalación del Modo REAL

11.1 Parámetros

sync\_cycle\_us: 1000


servo\_timeout\_ms: 200


sensor\_poll\_ms: 20


safe\_check\_ms: 10


11.2 Activación

EtherCAT online.


FLOW operativo.


Seguridad estable.


CNC en estado Ready.


12. Validación de Instalación

12.1 Mecánica

alineación,


backlash,


vibración.


12.2 Eléctrica

continuidad,


aislamiento,


protección.


12.3 Electrónica

drives,


IO,


FSoE.


12.4 CNC

homing,


interpolación,


spindle.


12.5 FLOW

sensores,


actuadores,


estados auxiliares.


13. Estado del Documento

Documento técnico oficial.

Base para instalación industrial del ecosistema LINCAT.
