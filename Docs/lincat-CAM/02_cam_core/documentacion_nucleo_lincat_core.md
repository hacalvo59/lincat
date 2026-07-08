# Documentación Núcleo Lincat — 01\_core

# Destino: 01\_cam\_core/documentacion\_nucleo\_lincat\_core.md

## 1. Propósito

El núcleo Lincat (01\_core) es la base lógica del ecosistema. Contiene los motores internos, la gestión de estados, la comunicación entre módulos y las estructuras fundamentales que permiten que el sistema funcione de forma industrial, modular y escalable.

## 2. Responsabilidades del Núcleo

- Gestionar estados globales del sistema.

- Coordinar comunicación entre módulos CAM, UI y CNC-CAT.

- Proveer servicios internos reutilizables.

- Mantener lógica base independiente de hardware.

- Controlar recursos, configuraciones y rutas internas.

- Garantizar estabilidad y coherencia del ecosistema.

## 3. Submódulos del Núcleo

- **core\_state\_manager.py** — Gestión de estados globales.

- **core\_config.py** — Configuración central del sistema.

- **core\_router.py** — Enrutador interno entre módulos.

- **core\_services/** — Servicios internos reutilizables.

- **core\_logging.py** — Registro industrial de eventos.

- **core\_exceptions.py** — Manejo centralizado de errores.

- **core\_utils/** — Utilidades internas del ecosistema.

## 4. Flujo de Comunicación Interna

1. La UI solicita una acción (cargar geometría, generar trayectorias, simular).

2. El núcleo recibe la solicitud y la enruta al módulo correspondiente.

3. El módulo CAM procesa la acción y devuelve resultados.

4. El núcleo valida, registra y reenvía la información a la UI o a CNC-CAT.

5. La UI muestra resultados o ejecuta la acción final.

El núcleo actúa como **capa de coordinación**, asegurando que los módulos no dependan directamente entre sí.

## 5. Qué NO pertenece al Núcleo

- Lógica CAM (trayectorias, estrategias, simulación).

- UI industrial.

- Drivers o hardware CNC.

- Integración CNC-CAT.

- Geometría o motores gráficos.

- Código dependiente de Blender.

El núcleo debe permanecer **puro, estable y universal**.

## 6. Estándares del Núcleo

- Independencia total de hardware.

- Módulos pequeños, claros y trazables.

- Comunicación interna mediante router central.

- Configuración única y global.

- Registro industrial obligatorio.

- Manejo de errores centralizado.

## 7. Relación con el Ecosistema

El núcleo es la base sobre la cual se construyen:

- Motor CAM (02\_cam\_core)

- UI Industrial (03\_ui\_industrial)

- Simulación extendida (04\_simulacion)

- Integración CNC-CAT (05\_integracion\_cnc\_cat)

- Pruebas (06\_pruebas)

Sin el núcleo, el ecosistema no tendría coherencia ni comunicación.

## 8. Resultado

La documentación del núcleo Lincat establece la estructura, responsabilidades y estándares del módulo más importante del ecosistema, garantizando estabilidad, modularidad y escalabilidad industrial.

