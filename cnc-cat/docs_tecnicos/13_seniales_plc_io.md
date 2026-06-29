13\_seniales\_plc\_io.md

Mapa Técnico de Señales PLC / IO

1. Propósito del Documento

Definir el mapa técnico de señales PLC e IO dentro del ecosistema LINCAT.

Incluye entradas, salidas, señales analógicas, señales seguras, asignaciones conceptuales y estructuras técnicas utilizadas por FLOW, CNC‑CAT y PLC.


2. Alcance Técnico

Este documento describe:


señales digitales,


señales analógicas,


señales seguras (FSoE),


señales de actuadores,


señales de sensores,


señales de habilitación,


señales de enclavamiento,


estructuras técnicas de IO.


No incluye wiring ni direcciones físicas reales.


3. Señales Digitales (DI / DO)

3.1 Entradas Digitales (DI)

di\_estop — parada de emergencia.


di\_door — sensor de puerta.


di\_probe — sonda CNC.


di\_limit\_min\[N\] — límite mínimo por eje.


di\_limit\_max\[N\] — límite máximo por eje.


di\_spindle\_fault — fallo de spindle.


di\_axis\_fault\[N\] — fallo de eje.


di\_vacuum\_sensor — sensor de vacío.


di\_air\_sensor — sensor de aire.


di\_lube\_sensor — sensor de lubricación.


di\_hydraulic\_sensor — sensor hidráulico.


di\_coolant\_sensor — sensor de refrigerante.


3.2 Salidas Digitales (DO)

do\_servo\_enable — habilitación servo.


do\_spindle\_enable — habilitación spindle.


do\_tool\_change — comando de cambio de herramienta.


do\_probe\_enable — habilitación de sonda.


do\_vacuum\_valve — válvula de vacío.


do\_air\_valve — válvula de aire.


do\_lube\_pump — bomba de lubricación.


do\_hydraulic\_pump — bomba hidráulica.


do\_coolant\_pump — bomba de refrigerante.


4. Señales Analógicas (AI / AO)

4.1 Entradas Analógicas (AI)

ai\_air\_pressure — presión de aire.


ai\_vacuum\_level — nivel de vacío.


ai\_lube\_flow — flujo de lubricación.


ai\_hydraulic\_pressure — presión hidráulica.


ai\_coolant\_level — nivel de refrigerante.


ai\_spindle\_speed\_feedback — velocidad real del spindle.


ai\_axis\_pos\_feedback\[N\] — posición real del eje.


ai\_axis\_vel\_feedback\[N\] — velocidad real del eje.


4.2 Salidas Analógicas (AO)

ao\_spindle\_speed\_cmd — comando de velocidad del spindle.


ao\_axis\_vel\_cmd\[N\] — comando de velocidad por eje.


ao\_axis\_acc\_cmd\[N\] — comando de aceleración por eje.


5. Señales Seguras (FSoE)

5.1 Entradas Seguras (Safe-In)

sin\_estop\_safe — parada de emergencia segura.


sin\_door\_safe — puerta segura.


sin\_zone\_safe — zona segura.


sin\_drive\_safe\[N\] — estado seguro del drive.


sin\_spindle\_safe — estado seguro del spindle.


5.2 Salidas Seguras (Safe-Out)

sout\_servo\_safe\_enable — habilitación segura de servo.


sout\_spindle\_safe\_enable — habilitación segura de spindle.


sout\_tool\_safe\_enable — habilitación segura de herramienta.


6. Señales de Habilitación

en\_servo — habilitación general de servo.


en\_spindle — habilitación general de spindle.


en\_motion\_ready — habilitación de movimiento.


en\_flow\_ready — habilitación industrial.


en\_safety\_ok — habilitación de seguridad.


en\_process\_ready — habilitación de proceso.


7. Señales de Enclavamiento

lock\_door — enclavamiento de puerta.


lock\_zone — enclavamiento de zona.


lock\_spindle — enclavamiento de spindle.


lock\_tool\_change — enclavamiento de cambio de herramienta.


lock\_motion — enclavamiento de movimiento.


8. Señales de Estado

state\_cnc — estado CNC.


state\_flow — estado FLOW.


state\_safety — estado de seguridad.


state\_process — estado de proceso.


state\_axis\[N\] — estado de eje.


state\_spindle — estado de spindle.


9. Estructuras Técnicas IO

9.1 Estructura DI / DO

Código

struct IO\_Digital \{

    bool di\[128\];

    bool do\[128\];

\}

9.2 Estructura AI / AO

Código

struct IO\_Analog \{

    float ai\[64\];

    float ao\[64\];

\}

9.3 Estructura SAFE

Código

struct IO\_Safe \{

    bool sin\[32\];

    bool sout\[32\];

\}

9.4 Estructura IO Completa

Código

struct IO\_Map \{

    IO\_Digital digital;

    IO\_Analog analog;

    IO\_Safe safe;

\}

10. Dependencias Técnicas

Las señales PLC/IO se integran con:


interfaces CNC


interfaces FLOW


EtherCAT — módulos industriales y seguridad.


PLC — ejecución de lógica.


Seguridad — enclavamientos y zonas seguras.


11. Principios Técnicos

Señales claras y determinísticas.


Mapa industrial estable.


Modularidad extrema.


Integración mediante IO.


Expansión sin romper interfaces existentes.


12. Estado del Documento

Documento técnico oficial.

Base para implementación PLC/IO en LINCAT.
