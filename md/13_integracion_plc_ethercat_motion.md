\# 13 – Integración PLC + EtherCAT + Motion PI  

\*\*Norma oficial del ecosistema LINCAT / CNC‑CAT\*\*


\#\# 1. Propósito del módulo


Este documento define cómo se integran los tres pilares industriales del ecosistema:


- \*\*PLC\*\* (lógica determinista)  

- \*\*EtherCAT\*\* (IO industrial en tiempo real)  

- \*\*Motion PI\*\* (cinemática y movimiento)


La integración se apoya en la arquitectura:


\`\`\`text

src/core/

 ├── common/

 ├── sim/

 └── real/
