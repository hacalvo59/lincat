\# 12 – Módulo SIM/REAL del ecosistema LINCAT / CNC‑CAT  

\*\*Norma oficial del ecosistema\*\*


\#\# 1. Propósito del módulo


El módulo SIM/REAL garantiza que cualquier funcionalidad del ecosistema pueda ejecutarse:


- \*\*en simulación\*\*, sin hardware, de forma segura, determinista y trazable,  

- \*\*en hardware real\*\*, con dispositivos físicos, manteniendo la misma interfaz.


Este documento define la estructura, responsabilidades y límites del módulo SIM/REAL.


---


\#\# 2. Filosofía descendente aplicada al módulo


El diseño SIM/REAL sigue los principios:


- \*\*Interfaz única:\*\* SIM y REAL deben compartir exactamente la misma API.  

- \*\*Determinismo:\*\* la simulación debe reproducir el comportamiento real.  

- \*\*Seguridad:\*\* el modo REAL nunca ejecuta acciones sin validación previa.  

- \*\*Modularidad:\*\* cada capa (CNC‑CAT, PLC, EtherCAT, Motion) tiene su versión SIM y REAL.  

- \*\*Trazabilidad:\*\* cada acción debe poder registrarse y auditarse.


---


\#\# 3. Estructura del módulo


\`\`\`text

src/sim/

 ├── cnc\_cat\_sim.py

 ├── plc\_sim.py

 ├── ethercat\_sim.py

 └── motion\_sim.py


src/real/

 ├── cnc\_cat\_rt.py

 ├── plc\_rt.py

 ├── ethercat\_rt.py

 └── motion\_rt.py
