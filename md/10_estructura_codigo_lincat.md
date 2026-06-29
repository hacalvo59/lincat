\# 10 – Estructura del código LINCAT / CNC‑CAT  

\*\*Norma oficial del ecosistema\*\*


\#\# 1. Propósito del documento


Este documento define la \*\*estructura oficial del código\*\* del ecosistema LINCAT / CNC‑CAT.  

Su objetivo es garantizar:


- orden,  

- modularidad,  

- claridad,  

- expansión segura,  

- coherencia con todas las normas previas,  

- y compatibilidad con la filosofía descendente del proyecto.


Toda implementación, aporte o modificación debe respetar esta estructura.


---


\#\# 2. Filosofía descendente aplicada al código


La estructura del código sigue el mismo patrón que la arquitectura conceptual:


1. \*\*Visión\*\*  

2. \*\*Arquitectura\*\*  

3. \*\*Módulos\*\*  

4. \*\*Interfaces\*\*  

5. \*\*Implementación\*\*


No se crean archivos “sueltos”, ni módulos improvisados.  

Cada carpeta y cada archivo tiene una \*\*responsabilidad clara\*\* y un \*\*límite definido\*\*.


---


\#\# 3. Estructura general del proyecto


\`\`\`text

lincat/

 ├── docs/

 ├── src/

 │    ├── core/

 │    │    ├── cnc\_cat/

 │    │    ├── plc/

 │    │    ├── ethercat/

 │    │    ├── motion\_pi/

 │    │    ├── eventbus/

 │    │    └── models/

 │    │

 │    ├── sim/

 │    ├── real/

 │    ├── ui/

 │    └── system/

 │

└── main.py


