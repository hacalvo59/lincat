39\_arquitectura\_multinivel\_planta.md

Arquitectura Multinivel de Planta — Ecosistema LINCAT

1. Propósito del Documento

Definir la arquitectura multinivel de una planta industrial que opera máquinas CNC basadas en LINCAT (CNC‑CAT + FLOW + PLC/IO + EtherCAT + Seguridad + REAL).

Este documento establece las capas jerárquicas, sus responsabilidades, sus interconexiones y los criterios de diseño para garantizar una planta modular, escalable, segura y certificable.


2. Alcance

Este documento cubre:


arquitectura física,


arquitectura de infraestructura,


arquitectura de ingeniería,


arquitectura de operación,


arquitectura de seguridad,


arquitectura de calidad,


arquitectura de mantenimiento,


arquitectura de producción,


arquitectura de documentación,


arquitectura de trazabilidad,


arquitectura de auditoría,


arquitectura de gobernanza industrial.


No cubre operación diaria ni mantenimiento.


3. Modelo Multinivel de Planta

La arquitectura se organiza en 14 niveles, cada uno independiente y con responsabilidades claras.


Código

Nivel 01 — Infraestructura física

Nivel 02 — Ingeniería mecánica

Nivel 03 — Ingeniería eléctrica

Nivel 04 — Ingeniería electrónica

Nivel 05 — Arquitectura EtherCAT

Nivel 06 — Seguridad industrial

Nivel 07 — FLOW industrial

Nivel 08 — CNC‑CAT

Nivel 09 — Procesos industriales

Nivel 10 — Calidad industrial

Nivel 11 — Mantenimiento industrial

Nivel 12 — Producción certificada

Nivel 13 — Documentación técnica

Nivel 14 — Trazabilidad y auditoría

Cada nivel depende del anterior y alimenta al siguiente.


4. Nivel 01 — Infraestructura Física

4.1 Entorno

temperatura 15–30 °C,


humedad \< 70 %,


ventilación industrial,


iluminación certificada.


4.2 Distribución

zona de producción,


zona de seguridad,


zona de mantenimiento,


zona de almacenamiento.


4.3 Suelo

nivelación \< 0.1 mm/m,


aislamiento de vibraciones.


5. Nivel 02 — Ingeniería Mecánica

5.1 Estructura

rigidez mínima 1.5×,


materiales certificados.


5.2 Guiado

clase H o superior,


alineación \< 0.02 mm.


5.3 Husillos

backlash \< 0.03 mm,


precarga P3.


6. Nivel 03 — Ingeniería Eléctrica

6.1 Alimentación

líneas dedicadas,


caída de tensión \< 5 %.


6.2 Gabinetes

IP54 mínimo,


ventilación forzada.


6.3 Aislamiento

control \> 1 MΩ,


potencia \> 10 MΩ.


7. Nivel 04 — Ingeniería Electrónica

7.1 Drives

EtherCAT nativo,


feedback estable.


7.2 IO

módulos digitales y analógicos,


FSoE operativo.


7.3 Spindle

variador certificado.


8. Nivel 05 — Arquitectura EtherCAT

8.1 Topología

Master → Drives → IO → FSoE.


8.2 Sincronización

ciclo DC 1000 µs.


8.3 Slaves

todos online,


sin slave\_fault.


9. Nivel 06 — Seguridad Industrial

9.1 Elementos

enclavamiento de puerta,


zona segura,


parada segura.


9.2 Estados

SafetyOk,


SafetyFault,


SafetyLock.


10. Nivel 07 — FLOW Industrial

10.1 Sensores

vacío, aire, lubricación, hidráulica, refrigerante.


10.2 Actuadores

válvulas, bombas.


10.3 Estados auxiliares

VacuumReady, AirReady, LubeReady, HydraulicReady, CoolantReady.


11. Nivel 08 — CNC‑CAT

11.1 Capas

interpolación,


servo,


spindle,


herramientas.


11.2 Señales

servo\_enabled,


spindle\_enabled,


interp\_active.


12. Nivel 09 — Procesos Industriales

12.1 Secuencias FLOW

sensores → estados → actuadores.


12.2 Secuencias CNC

homing → interpolación → spindle → herramientas.


12.3 Integración

CNC ↔ FLOW ↔ PLC/IO ↔ EtherCAT ↔ Seguridad.


13. Nivel 10 — Calidad Industrial

13.1 Dimensional

tolerancias certificadas.


13.2 Geométrica

paralelismo,


perpendicularidad.


13.3 Superficial

rugosidad certificada.


14. Nivel 11 — Mantenimiento Industrial

14.1 Mecánico

alineación,


backlash.


14.2 Eléctrico

aislamiento,


protección.


14.3 Electrónico

drives,


IO.


15. Nivel 12 — Producción Certificada

15.1 Validación

máquina,


proceso,


calidad.


15.2 Control

dimensional,


geométrico,


superficial.


16. Nivel 13 — Documentación Técnica

16.1 Obligatoria

planos,


parámetros,


topología EtherCAT,


manuales técnicos.


16.2 Repositorio

versionado,


trazabilidad.


17. Nivel 14 — Trazabilidad y Auditoría

17.1 Registros

mantenimiento,


producción,


auditorías.


17.2 Conservación

mínimo 15 años.


18. Integración Multinivel Completa

18.1 Modelo

Código

Infraestructura

  → Mecánica

    → Eléctrica

      → Electrónica

        → EtherCAT

          → Seguridad

            → FLOW

              → CNC‑CAT

                → Procesos

                  → Calidad

                    → Mantenimiento

                      → Producción

                        → Documentación

                          → Trazabilidad

                            → Auditoría

18.2 Criterios

modularidad,


escalabilidad,


determinismo,


interoperabilidad.


19. Estado del Documento

Documento técnico oficial.

Base para arquitectura multinivel de planta en el ecosistema LINCAT.
