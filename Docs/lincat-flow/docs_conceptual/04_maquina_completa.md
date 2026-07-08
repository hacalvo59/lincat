04\_maquina\_completa.md

Concepto de Máquina Completa en LINCAT

1. Propósito del Documento

Definir conceptualmente la máquina completa dentro del ecosistema LINCAT, integrando los caminos CNC y FLOW, la lógica PLC, la topología EtherCAT y los elementos industriales necesarios para el funcionamiento real.


2. Definición de Máquina Completa

Una máquina completa es la combinación de:


Camino CNC — movimiento, interpolación, servo, spindle, herramientas.


Camino FLOW — servicios industriales, estados auxiliares, enclavamientos, seguridad.


PLC — ejecución de lógica industrial.


IO — señales físicas de sensores y actuadores.


EtherCAT — topología industrial y comunicación determinística.


Seguridad — zonas seguras, enclavamientos, FSoE.


SIM/REAL — simulación y ejecución sobre hardware.


La máquina completa es la unión funcional de todos estos elementos.


3. Camino CNC

El camino CNC define el movimiento de la máquina:


interpolación lineal y circular,


servo y control de ejes,


spindle,


herramientas,


sondas,


límites,


homing,


ejecución de bloques.


Este camino opera de forma determinística y depende de los estados auxiliares del camino FLOW.


4. Camino FLOW

El camino FLOW define los servicios industriales:


vacío,


aire comprimido,


lubricación,


sensores industriales,


válvulas,


relés,


contactores,


enclavamientos,


seguridad,


estados de proceso.


FLOW habilita el movimiento seguro del camino CNC.


5. PLC e IO

PLC ejecuta la lógica industrial generada conceptualmente por FLOW.

IO representa las señales físicas de sensores y actuadores.


Incluye:


entradas digitales,


salidas digitales,


entradas analógicas,


salidas analógicas,


módulos de seguridad.


PLC e IO implementan el comportamiento funcional de la máquina.


6. EtherCAT

EtherCAT define la topología industrial:


master,


slaves,


módulos IO,


drives de ejes,


drive de spindle,


sensores,


actuadores,


seguridad FSoE.


FLOW representa la topología completa.

CNC‑CAT utiliza únicamente los elementos relevantes para movimiento.


7. Seguridad Industrial

La seguridad incluye:


enclavamientos,


zonas seguras,


sensores de puerta,


relés de seguridad,


módulos FSoE,


condiciones de habilitación.


FLOW define las condiciones de seguridad.

PLC las ejecuta.

CNC‑CAT las consume.


8. Estados de Máquina Completa

La máquina completa combina estados de CNC y FLOW:


CNC.Ready


FLOW.VacuumReady


FLOW.AirReady


FLOW.LubeReady


FLOW.SafetyOk


FLOW.ProcessReady


CNC.Running


CNC.Error


FLOW.Alarm


El movimiento solo se habilita cuando todos los estados auxiliares están activos.


9. Integración Conceptual

La integración se basa en:


CNC‑CAT ejecuta movimiento.


FLOW habilita movimiento.


PLC ejecuta lógica.


IO representa señales.


EtherCAT conecta hardware.


Seguridad define enclavamientos.


SIM simula la máquina completa.


REAL ejecuta la máquina sobre hardware.


Cada módulo mantiene independencia funcional.


10. Principios de Máquina Completa

Integración modular.


Independencia entre caminos.


Habilitación mediante estados auxiliares.


Seguridad como condición primaria.


Topología industrial clara.


Documentación antes de implementación.


11. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica de la máquina completa.
