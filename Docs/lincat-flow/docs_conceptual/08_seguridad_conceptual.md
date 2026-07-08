08\_seguridad\_conceptual.md

Concepto de Seguridad Industrial en LINCAT

1. Propósito del Documento

Definir la seguridad industrial de la máquina dentro del ecosistema LINCAT.

La seguridad conceptual establece las condiciones necesarias para habilitar movimiento, proteger al operador y garantizar operación segura en todos los estados del sistema.


2. Alcance Conceptual

Este documento describe:


enclavamientos,


zonas seguras,


sensores de seguridad,


relés de seguridad,


módulos FSoE,


condiciones de habilitación,


estados de seguridad.


No incluye configuraciones técnicas, wiring, parámetros ni asignaciones de hardware.


3. Enclavamientos Conceptuales

Los enclavamientos representan condiciones obligatorias para habilitar la máquina:


puertas cerradas,


protecciones activas,


relés de seguridad en estado válido,


zonas seguras libres,


sensores de presencia inactivos.


FLOW define conceptualmente los enclavamientos.

PLC ejecuta la lógica.

CNC‑CAT consume los estados resultantes.


4. Zonas Seguras

La máquina se divide conceptualmente en zonas seguras:


zona de movimiento CNC,


zona de spindle,


zona de herramientas,


zona de actuadores industriales,


zona de acceso del operador.


Cada zona tiene:


sensores asociados,


enclavamientos específicos,


condiciones de habilitación,


estados de bloqueo.


5. Sensores de Seguridad

FLOW representa conceptualmente los sensores de seguridad:


sensores de puerta,


sensores de presencia,


sensores de posición segura,


interruptores de emergencia,


barreras ópticas.


Estos sensores generan señales que PLC e IO ejecutan y que FLOW utiliza para definir estados de seguridad.


6. Relés y Módulos de Seguridad

La seguridad conceptual incluye:


relés de seguridad,


módulos de seguridad cableados,


módulos EtherCAT FSoE,


enclavamientos electrónicos.


FLOW define:


estados válidos,


estados de fallo,


condiciones de habilitación,


condiciones de bloqueo.


7. Seguridad FSoE

La seguridad sobre EtherCAT (FSoE) se representa conceptualmente como:


canales seguros,


entradas seguras,


salidas seguras,


estados seguros,


fallos seguros.


FLOW modela la estructura conceptual.

PLC ejecuta la lógica.

CNC‑CAT consume los estados seguros.


8. Condiciones de Habilitación

Las condiciones de habilitación conceptuales incluyen:


SafetyOk


DoorClosed


ZoneClear


EmergencyReleased


SafeMotionReady


Estas condiciones deben estar activas antes de:


habilitar servo,


arrancar spindle,


iniciar ciclo,


ejecutar cambios de herramienta.


9. Estados de Seguridad

FLOW define estados conceptuales de seguridad:


SafetyOk


SafetyWarning


SafetyError


SafetyLock


SafetyRelease


Estos estados se combinan con los estados CNC para habilitar o bloquear movimiento.


10. Integración Conceptual

La seguridad se integra con:


FLOW — define estados y enclavamientos.


PLC — ejecuta la lógica.


IO — representa señales físicas.


EtherCAT — comunica módulos FSoE.


CNC‑CAT — consume estados de seguridad.


La seguridad es condición primaria para habilitar movimiento.


11. Principios Conceptuales de Seguridad

Seguridad como prioridad absoluta.


Independencia funcional.


Integración mediante estados auxiliares.


Modularidad extrema.


Descendencia conceptual.


Expansión sin modificar la arquitectura base.


12. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica de seguridad industrial.
