01\_lincat\_arquitectura\_general.md

Arquitectura General del Ecosistema LINCAT

1. Alcance del Documento

Este documento define la arquitectura conceptual completa del ecosistema LINCAT.

Describe los módulos principales, sus roles, sus relaciones y la estructura descendente del sistema.

No contiene detalles técnicos ni APIs.


2. Estructura Modular del Ecosistema

LINCAT se compone de módulos independientes, cada uno con un propósito único:


CNC‑CAT — motor de movimiento.


FLOW — servicios industriales y estados auxiliares.


PLC — lógica de control.


IO — entradas y salidas físicas.


EtherCAT — bus de campo y topología industrial.


Motion — control de servo y cinemática.


SIM — simulación completa del ecosistema.


REAL — ejecución sobre hardware real.


Seguridad — enclavamientos, zonas seguras, FSoE.


Componentes — biblioteca industrial.


Base de datos industrial — definición de elementos eléctricos, neumáticos, hidráulicos y de proceso.


Cada módulo se documenta por separado y se integra mediante interfaces definidas.


3. Relación entre Módulos

La arquitectura se organiza de forma descendente:


CNC‑CAT depende de:


Motion


PLC


IO


FLOW


EtherCAT


FLOW depende de:


01\_lincat\_arquitectura\_general.md

Arquitectura General del Ecosistema LINCAT

1. Alcance del Documento

Este documento define la arquitectura conceptual completa del ecosistema LINCAT.

Describe los módulos principales, sus roles, sus relaciones y la estructura descendente del sistema.

No contiene detalles técnicos ni APIs.


2. Estructura Modular del Ecosistema

LINCAT se compone de módulos independientes, cada uno con un propósito único:


CNC‑CAT — motor de movimiento.


FLOW — servicios industriales y estados auxiliares.


PLC — lógica de control.


IO — entradas y salidas físicas.


EtherCAT — bus de campo y topología industrial.


Motion — control de servo y cinemática.


SIM — simulación completa del ecosistema.


REAL — ejecución sobre hardware real.


Seguridad — enclavamientos, zonas seguras, FSoE.


Componentes — biblioteca industrial.


Base de datos industrial — definición de elementos eléctricos, neumáticos, hidráulicos y de proceso.


Cada módulo se documenta por separado y se integra mediante interfaces definidas.


3. Relación entre Módulos

La arquitectura se organiza de forma descendente:


CNC‑CAT depende de:


Motion


PLC


IO


FLOW


EtherCAT


FLOW depende de:


PLC


IO


EtherCAT


Base de datos de componentes


PLC depende de:


IO


EtherCAT


SIM depende de:


CNC‑CAT


FLOW


PLC


IO


EtherCAT


REAL depende de:


SIM


Hardware físico


EtherCAT


4. Los Dos Corazones del Ecosistema

4.1 CNC‑CAT

Define el comportamiento cinemático de la máquina:


interpolación,


servo,


ejes,


spindle,


herramientas.


4.2 FLOW

Define el comportamiento funcional de la máquina:


vacío,


aire,


lubricación,


sensores,


válvulas,


relés,


seguridad,


estados de proceso.


Ambos módulos se integran mediante estados auxiliares y señales de proceso.


5. Camino CNC y Camino FLOW

La arquitectura distingue dos caminos principales:


5.1 Camino CNC

movimiento,


interpolación,


servo,


spindle,


herramientas.


5.2 Camino FLOW

servicios industriales,


condiciones de habilitación,


enclavamientos,


seguridad,


estados de proceso.


El CNC depende de FLOW para habilitar movimiento seguro.


6. Topología Industrial

EtherCAT define la estructura física de la máquina:


master,


slaves,


módulos IO,


servo drives,


sensores,


actuadores,


seguridad FSoE.


FLOW representa la topología completa.

CNC‑CAT utiliza solo los elementos relevantes para movimiento.


7. Simulación y Ejecución

7.1 SIM

Simula:


CNC‑CAT,


FLOW,


PLC,


IO,


EtherCAT,


seguridad.


Permite validar la máquina completa sin hardware.


7.2 REAL

Ejecuta el ecosistema sobre hardware físico.


8. Base de Datos Industrial

Define los componentes utilizados por FLOW:


eléctricos,


neumáticos,


hidráulicos,


sensores,


actuadores,


módulos EtherCAT.


Cada componente incluye:


parámetros,


entradas,


salidas,


estados,


alarmas.


9. Principios de Arquitectura

Modularidad extrema.


Independencia entre módulos.


Integración mediante interfaces claras.


Documentación antes de código.


Expansión sin romper módulos existentes.


Descendencia conceptual y técnica.


10. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica de cada módulo.PLC


IO


EtherCAT


Base de datos de componentes


PLC depende de:


IO


EtherCAT


SIM depende de:


CNC‑CAT


FLOW


PLC


IO


EtherCAT


REAL depende de:


SIM


Hardware físico


EtherCAT


4. Los Dos Corazones del Ecosistema

4.1 CNC‑CAT

Define el comportamiento cinemático de la máquina:


interpolación,


servo,


ejes,


spindle,


herramientas.


4.2 FLOW

Define el comportamiento funcional de la máquina:


vacío,


aire,


lubricación,


sensores,


válvulas,


relés,


seguridad,


estados de proceso.


Ambos módulos se integran mediante estados auxiliares y señales de proceso.


5. Camino CNC y Camino FLOW

La arquitectura distingue dos caminos principales:


5.1 Camino CNC

movimiento,


interpolación,


servo,


spindle,


herramientas.


5.2 Camino FLOW

servicios industriales,


condiciones de habilitación,


enclavamientos,


seguridad,


estados de proceso.


El CNC depende de FLOW para habilitar movimiento seguro.


6. Topología Industrial

EtherCAT define la estructura física de la máquina:


master,


slaves,


módulos IO,


servo drives,


sensores,


actuadores,


seguridad FSoE.


FLOW representa la topología completa.

CNC‑CAT utiliza solo los elementos relevantes para movimiento.


7. Simulación y Ejecución

7.1 SIM

Simula:


CNC‑CAT,


FLOW,


PLC,


IO,


EtherCAT,


seguridad.


Permite validar la máquina completa sin hardware.


7.2 REAL

Ejecuta el ecosistema sobre hardware físico.


8. Base de Datos Industrial

Define los componentes utilizados por FLOW:


eléctricos,


neumáticos,


hidráulicos,


sensores,


actuadores,


módulos EtherCAT.


Cada componente incluye:


parámetros,


entradas,


salidas,


estados,


alarmas.


9. Principios de Arquitectura

Modularidad extrema.


Independencia entre módulos.


Integración mediante interfaces claras.


Documentación antes de código.


Expansión sin romper módulos existentes.


Descendencia conceptual y técnica.


10. Estado del Documento

Documento conceptual oficial.

Base para la documentación técnica de cada módulo.
