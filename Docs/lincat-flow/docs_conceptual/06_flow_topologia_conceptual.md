06\_flow\_topologia\_conceptual.md

Topología Conceptual del Módulo LINCAT‑FLOW

1. Propósito del Documento

Definir la topología industrial conceptual del módulo FLOW dentro del ecosistema LINCAT.

La topología describe la estructura EtherCAT, los módulos involucrados y la organización conceptual de sensores, actuadores y elementos de seguridad.


2. Alcance Conceptual

Este documento incluye:


estructura EtherCAT conceptual,


organización de módulos IO,


drives y actuadores,


sensores industriales,


elementos de seguridad,


mapa conceptual de la máquina.


No incluye configuraciones técnicas, archivos XML, ni asignaciones de direcciones.


3. Estructura EtherCAT Conceptual

La topología EtherCAT se organiza de forma descendente:


Master EtherCAT  

Controlador principal del bus.


Slaves EtherCAT  

Módulos conectados en cadena que representan:


IO digitales,


IO analógicas,


módulos de seguridad,


drives de ejes,


drive de spindle,


sensores industriales,


actuadores neumáticos e hidráulicos.


Componentes Industriales  

Elementos conectados a los módulos IO:


válvulas,


relés,


contactores,


sensores de presión,


sensores de nivel,


sensores de temperatura,


bombas,


actuadores.


4. Organización Conceptual de Módulos IO

Los módulos IO se agrupan conceptualmente según su función:


IO de servicios industriales  

vacío, aire, lubricación, bombas, válvulas.


IO de seguridad  

puertas, enclavamientos, relés de seguridad, FSoE.


IO de proceso  

sensores de nivel, presión, temperatura, flujo.


IO auxiliares  

señales de estado, alarmas, habilitaciones.


FLOW representa esta organización como un mapa conceptual de la máquina.


5. Drives y Actuadores

La topología conceptual incluye:


Drives de ejes  

utilizados por CNC‑CAT.


Drive de spindle  

utilizado por CNC‑CAT.


Actuadores industriales  

utilizados por FLOW:


válvulas neumáticas,


válvulas hidráulicas,


bombas,


relés,


contactores.


FLOW modela estos actuadores como parte del camino industrial.


6. Sensores Industriales

FLOW representa conceptualmente los sensores:


presión,


nivel,


temperatura,


flujo,


vacío,


presencia,


posición industrial.


Estos sensores generan señales que PLC e IO ejecutan y que FLOW utiliza para definir estados auxiliares.


7. Seguridad Conceptual en la Topología

La topología incluye elementos de seguridad:


módulos FSoE,


relés de seguridad,


sensores de puerta,


enclavamientos,


zonas seguras.


FLOW define conceptualmente:


condiciones de habilitación,


enclavamientos,


estados de seguridad.


PLC ejecuta la lógica.

CNC‑CAT consume los estados.


8. Mapa Conceptual de la Máquina

FLOW organiza la máquina como un mapa conceptual:


master EtherCAT,


cadena de slaves,


módulos IO,


drives,


sensores,


actuadores,


seguridad.


Este mapa representa la estructura industrial completa, independiente del movimiento CNC.


9. Principios Conceptuales de Topología

Representación completa de la máquina.


Modularidad extrema.


Independencia funcional.


Integración mediante estados auxiliares.


Descendencia conceptual.


Expansión sin modificar la arquitectura base.


10. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica de la topología EtherCAT.
