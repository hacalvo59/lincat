10\_sim\_real\_conceptual.md

Relación Conceptual entre SIM y REAL en LINCAT

1. Propósito del Documento

Definir conceptualmente la relación entre los modos SIM (simulación) y REAL (hardware físico) dentro del ecosistema LINCAT.

El objetivo es garantizar que la máquina pueda ejecutarse sin hardware y luego trasladarse al entorno real sin modificar la arquitectura.


2. Alcance Conceptual

Este documento describe:


propósito del modo SIM,


propósito del modo REAL,


equivalencia conceptual entre ambos,


transición conceptual SIM → REAL,


validación conceptual de máquina completa.


No incluye configuraciones técnicas, APIs ni parámetros de hardware.


3. Concepto de Modo SIM

El modo SIM representa la máquina completa sin hardware real.

Incluye la simulación conceptual de:


CNC‑CAT,


FLOW,


PLC,


IO,


EtherCAT,


seguridad,


componentes industriales.


El modo SIM permite:


validar comportamiento,


probar secuencias,


verificar estados auxiliares,


simular fallos,


depurar lógica industrial,


ejecutar la máquina sin riesgo.


4. Concepto de Modo REAL

El modo REAL ejecuta la máquina sobre hardware físico.

Incluye:


drives de ejes,


drive de spindle,


módulos IO,


sensores,


actuadores,


módulos FSoE,


topología EtherCAT real.


El modo REAL permite:


ejecutar movimiento,


operar servicios industriales,


validar seguridad física,


ejecutar procesos reales,


interactuar con el entorno físico.


5. Equivalencia Conceptual SIM ↔ REAL

La arquitectura LINCAT exige equivalencia conceptual entre ambos modos:


misma estructura de módulos,


mismas interfaces conceptuales,


mismos estados,


mismos enclavamientos,


misma topología conceptual,


misma lógica conceptual.


La diferencia es únicamente el origen de las señales:


SIM genera señales simuladas.


REAL recibe señales físicas.


6. Transición Conceptual SIM → REAL

La transición conceptual se basa en:


Validación en SIM


estados auxiliares,


secuencias industriales,


seguridad,


topología conceptual,


movimiento CNC simulado.


Activación en REAL


conexión EtherCAT,


lectura de sensores reales,


activación de actuadores reales,


habilitación de seguridad física.


Equivalencia funcional


CNC‑CAT opera igual,


FLOW opera igual,


PLC ejecuta la misma lógica,


IO representa señales reales.


7. Validación Conceptual de Máquina Completa

La validación conceptual incluye:


coherencia entre estados SIM y REAL,


equivalencia de secuencias,


equivalencia de enclavamientos,


equivalencia de habilitaciones,


equivalencia de alarmas,


equivalencia de topología conceptual.


La máquina debe comportarse igual en ambos modos.


8. Integración Conceptual

La relación SIM ↔ REAL se integra con:


CNC‑CAT — movimiento simulado o real.


FLOW — servicios industriales simulados o reales.


PLC — lógica idéntica en ambos modos.


IO — señales simuladas o físicas.


EtherCAT — topología conceptual o hardware real.


Seguridad — estados simulados o físicos.


9. Principios Conceptuales SIM ↔ REAL

Equivalencia funcional completa.


Independencia del hardware real.


Modularidad extrema.


Descendencia conceptual.


Transición sin modificar arquitectura.


Expansión sin romper módulos existentes.


10. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica del módulo SIM/REAL.
