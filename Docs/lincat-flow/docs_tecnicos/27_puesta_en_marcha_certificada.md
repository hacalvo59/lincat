27\_puesta\_en\_marcha\_certificada.md

Manual Técnico de Puesta en Marcha Certificada — Ecosistema LINCAT

1. Propósito del Documento

Definir los procedimientos, verificaciones, criterios técnicos y documentación necesaria para realizar una puesta en marcha certificada de máquinas CNC basadas en el ecosistema LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este manual establece los requisitos para que la máquina quede habilitada industrialmente, auditada, validada y certificada para operación real.


2. Alcance

Este documento cubre:


verificación mecánica certificada,


verificación eléctrica certificada,


verificación electrónica certificada,


verificación EtherCAT certificada,


verificación de seguridad industrial certificada,


verificación FLOW certificada,


verificación CNC‑CAT certificada,


documentación obligatoria,


criterios de aceptación,


emisión del certificado final.


No cubre instalación ni mantenimiento.


3. Requisitos Previos a la Certificación

3.1 Documentación obligatoria

planos mecánicos,


planos eléctricos,


topología EtherCAT,


mapa PLC/IO,


documentación de seguridad,


parámetros CNC‑CAT,


parámetros FLOW,


manual de instalación industrial.


3.2 Condiciones del entorno

temperatura 15–30 °C,


humedad \< 70 %,


alimentación estable,


ausencia de vibraciones externas.


3.3 Estado inicial del sistema

EtherCAT online,


FLOW inicializado,


seguridad estable,


CNC‑CAT en estado Idle.


4. Certificación Mecánica

4.1 Alineación de ejes

paralelismo \< 0.02 mm,


perpendicularidad \< 0.03 mm,


planitud \< 0.1 mm/m.


4.2 Backlash

backlash \< 0.03 mm por eje.


4.3 Rigidez estructural

deflexión \< 0.05 mm bajo carga nominal.


4.4 Vibración

RMS \< 0.05 mm,


sin resonancias críticas.


5. Certificación Eléctrica

5.1 Aislamiento

control \> 1 MΩ,


potencia \> 10 MΩ.


5.2 Protección

magnetotérmicos correctos,


diferencial operativo,


tierra verificada.


5.3 Gabinete

IP54 mínimo,


ventilación adecuada,


separación potencia/control.


6. Certificación Electrónica

6.1 Drives

encoder verificado,


homing correcto,


torque estable.


6.2 Spindle

velocidad real dentro de ±3 %,


vibración dentro de límites,


dirección correcta.


6.3 IO

entradas digitales verificadas,


salidas digitales verificadas,


entradas analógicas calibradas,


salidas analógicas verificadas.


7. Certificación EtherCAT

7.1 Slaves

todos online,


sin slave\_fault,


sincronización DC estable.


7.2 Drives

drive\_safe activo,


watchdog operativo,


ciclo determinístico 1000 µs.


7.3 FSoE

canales seguros verificados,


safe\_channel\_ok estable.


8. Certificación de Seguridad Industrial

8.1 Puerta

enclavamiento operativo,


sensor seguro verificado.


8.2 Zona segura

barreras funcionales,


sensores verificados.


8.3 Parada segura

tiempo de respuesta dentro de norma,


relés de seguridad operativos.


8.4 Estados

SafetyOk estable,


sin SafetyFault.


9. Certificación FLOW

9.1 Sensores

vacío, aire, lubricación, hidráulica, refrigerante calibrados.


9.2 Actuadores

válvulas y bombas verificadas,


caudal dentro de tolerancia.


9.3 Estados auxiliares

VacuumReady, AirReady, LubeReady, HydraulicReady, CoolantReady, SafetyOk, ProcessReady.


10. Certificación CNC‑CAT

10.1 Homing

repetibilidad \< 0.02 mm.


10.2 Interpolación

precisión lineal \< 0.05 mm,


precisión circular \< 0.07 mm.


10.3 Spindle

velocidad dentro de tolerancia,


sincronización correcta.


10.4 Herramientas

offsets verificados,


repetibilidad \< 0.03 mm.


11. Pruebas de Validación Final

11.1 Prueba de trayectoria

ejecución completa sin fallos.


11.2 Prueba de proceso FLOW

secuencia industrial completa.


11.3 Prueba de seguridad

activación de enclavamiento,


activación de parada segura,


recuperación correcta.


11.4 Prueba de integración

CNC ↔ FLOW ↔ PLC/IO ↔ EtherCAT ↔ Seguridad.


12. Criterios de Aceptación

La máquina queda certificada si:


no presenta fallos críticos,


cumple tolerancias mecánicas,


cumple tolerancias eléctricas,


cumple tolerancias electrónicas,


EtherCAT estable,


seguridad estable,


FLOW operativo,


CNC‑CAT operativo,


todas las pruebas superadas.


13. Documentación Final Entregada al Fabricante

13.1 Certificados

certificado de puesta en marcha,


certificado de seguridad,


certificado de calibración.


13.2 Informes

informe mecánico,


informe eléctrico,


informe electrónico,


informe EtherCAT,


informe FLOW,


informe CNC‑CAT.


13.3 Archivos técnicos

YAML REAL,


YAML FLOW,


YAML CNC,


topología EtherCAT,


mapa PLC/IO.


14. Estado del Documento

Manual técnico oficial.

Base para puesta en marcha certificada del ecosistema LINCAT.
