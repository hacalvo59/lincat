05\_cnc\_flow\_integracion\_conceptual.md

Integración Conceptual entre CNC‑CAT y LINCAT‑FLOW

1. Propósito del Documento

Definir conceptualmente cómo se integran los módulos CNC‑CAT y FLOW dentro del ecosistema LINCAT.

La integración establece la relación entre el camino CNC (movimiento) y el camino FLOW (servicios industriales), garantizando operación segura y completa de la máquina.


2. Alcance Conceptual

Este documento describe:


los roles de cada módulo,


los estados auxiliares,


las señales conceptuales,


las dependencias funcionales,


la relación entre movimiento y servicios industriales.


No incluye detalles técnicos, APIs ni estructuras de datos.


3. Relación entre los Dos Corazones del Ecosistema

LINCAT se basa en dos módulos principales:


3.1 CNC‑CAT

Responsable del movimiento:


interpolación,


servo,


ejes,


spindle,


herramientas,


sondas,


límites.


3.2 FLOW

Responsable de los servicios industriales:


vacío,


aire,


lubricación,


sensores,


válvulas,


relés,


contactores,


enclavamientos,


seguridad,


estados de proceso.


La integración se basa en que CNC‑CAT consume estados generados por FLOW.


4. Estados Auxiliares

FLOW provee estados auxiliares que CNC‑CAT utiliza como condiciones previas para habilitar movimiento:


VacuumReady


AirReady


LubeReady


SafetyOk


ProcessReady


Estos estados deben estar activos antes de:


habilitar ejes,


arrancar spindle,


iniciar ciclo,


ejecutar cambios de herramienta,


avanzar bloques críticos.


5. Señales Conceptuales FLOW → CNC‑CAT

FLOW expone señales conceptuales que CNC‑CAT consulta:


nivel de vacío,


presión de aire,


flujo de lubricación,


estado de seguridad,


avance de proceso.


Estas señales se utilizan como condiciones de habilitación y enclavamientos.


6. Integración con PLC e IO

FLOW define la lógica conceptual que PLC ejecuta.

IO representa las señales físicas de sensores y actuadores.


CNC‑CAT no genera lógica PLC.

CNC‑CAT consume:


habilitaciones,


enclavamientos,


límites,


sondas,


señales de spindle,


señales de herramientas.


7. Integración con EtherCAT

FLOW representa la topología EtherCAT completa:


master,


slaves,


módulos IO,


drives,


sensores,


actuadores,


seguridad FSoE.


CNC‑CAT utiliza únicamente:


drives de ejes,


drive de spindle,


IO relevante para movimiento.


8. Concepto de Máquina Completa

La integración FLOW ↔ CNC‑CAT define la máquina completa:


CNC‑CAT ejecuta movimiento.


FLOW habilita movimiento.


PLC ejecuta lógica.


IO representa señales.


EtherCAT conecta hardware.


Seguridad define enclavamientos.


SIM simula la máquina completa.


REAL ejecuta la máquina sobre hardware.


9. Principios de Integración

Independencia funcional.


Modularidad extrema.


Integración mediante estados auxiliares.


Descendencia conceptual.


Expansión sin romper módulos existentes.


Claridad en roles y dependencias.


10. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica de integración FLOW ↔ CNC‑CAT.
