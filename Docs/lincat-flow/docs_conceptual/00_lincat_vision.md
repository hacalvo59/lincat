00\_lincat\_vision.md

Visión General del Ecosistema LINCAT

1. Propósito del Ecosistema

LINCAT es un ecosistema industrial modular diseñado para integrar CNC, PLC, IO, EtherCAT, Motion, simulación y servicios industriales en una arquitectura unificada, libre y escalable.

Su objetivo es permitir la construcción de máquinas profesionales sin depender de firmware propietario.


2. Filosofía Modular

LINCAT se basa en los siguientes principios:


Cada módulo tiene un propósito único.


Ningún módulo rompe otro.


Los módulos se agregan sin generar dependencias rígidas.


La arquitectura es descendente, clara y extensible.


Todo componente es reemplazable sin afectar el sistema completo.


La documentación define el sistema antes de escribir código.


3. Los Dos Corazones del Ecosistema

LINCAT se estructura alrededor de dos módulos principales:


3.1 CNC‑CAT (Primer Corazón)

Responsable del movimiento:


interpolación,


servo,


ejes,


spindle,


herramientas,


sondas,


límites.


Define el comportamiento cinemático de la máquina.


3.2 LINCAT‑FLOW (Segundo Corazón)

Responsable de los servicios industriales:


vacío,


aire,


lubricación,


sensores,


válvulas,


relés,


contactores,


seguridad,


estados de proceso.


Define el comportamiento funcional de la máquina.


4. Integración Conceptual

La integración entre CNC‑CAT y FLOW se basa en:


CNC‑CAT depende de estados auxiliares generados por FLOW.


FLOW modela los servicios industriales y expone señales.


CNC‑CAT consume esas señales para habilitar movimiento.


PLC e IO ejecutan la lógica generada por FLOW.


EtherCAT provee la topología física de la máquina.


El ecosistema funciona como una máquina completa.


5. Arquitectura Conceptual

LINCAT se compone de módulos independientes:


CNC‑CAT


FLOW


PLC


IO


EtherCAT


Motion


SIM (Simulación)


REAL (Hardware real)


Seguridad


Base de datos de componentes


Topología industrial


Cada módulo se documenta por separado y se integra mediante interfaces definidas.


6. Objetivo de la Documentación Conceptual

La documentación conceptual define:


la visión,


la arquitectura,


los roles de cada módulo,


las relaciones entre módulos,


el comportamiento general del ecosistema.


No contiene detalles técnicos ni APIs.

Su función es establecer el marco conceptual antes de la documentación técnica.


7. Alcance

Este documento aplica a:


ingenieros de arquitectura,


diseñadores de sistemas,


desarrolladores de módulos,


colaboradores del ecosistema LINCAT.


8. Estado del Documento

Documento conceptual oficial.

Versión inicial.

Base para la documentación técnica posterior.
