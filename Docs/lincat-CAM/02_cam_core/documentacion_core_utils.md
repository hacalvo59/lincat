# Documentación Core Utils — Núcleo Lincat

# Destino: 02\_cam\_core/documentacion\_core\_utils.md

## 1. Propósito

El módulo `core\_utils/` reúne utilidades internas del ecosistema Lincat que no pertenecen a ningún servicio específico, pero que son necesarias para operaciones comunes, repetitivas o auxiliares dentro del núcleo y los módulos CAM. Su función es **reducir duplicación**, **centralizar funciones genéricas** y **mantener el código limpio y trazable**.

## 2. Características de Core Utils

- Funciones pequeñas, puras y reutilizables.

- Sin dependencias hacia módulos CAM o CNC-CAT.

- Sin lógica de negocio.

- Sin acceso a hardware.

- Documentación obligatoria por archivo.

- Uso transversal en todo el ecosistema.

- Registro opcional en `core\_logging.py` cuando la operación lo amerita.

## 3. Submódulos de Core Utils

- **utils\_strings.py** — Manipulación de cadenas, normalización, limpieza.

- **utils\_numbers.py** — Operaciones numéricas simples, redondeos, límites.

- **utils\_files.py** — Lectura y escritura básica de archivos internos.

- **utils\_dict.py** — Utilidades para diccionarios, merges, filtros.

- **utils\_types.py** — Validación y conversión de tipos simples.

- **utils\_format.py** — Formateo de datos para UI o logs.

- **utils\_checks.py** — Comprobaciones rápidas de estado o valores.

Cada archivo debe contener una única responsabilidad clara.

## 4. Flujo de Uso

1. Un módulo (núcleo, CAM, UI, simulación) necesita una operación auxiliar.

2. El núcleo enruta la solicitud hacia el util correspondiente.

3. El util ejecuta la operación de forma pura y aislada.

4. El resultado vuelve al núcleo.

5. El núcleo lo entrega al módulo solicitante.

Los utils **no** deben comunicarse entre sí salvo casos estrictamente necesarios.

## 5. Qué NO pertenece a Core Utils

- Lógica CAM (trayectorias, estrategias).

- Lógica UI.

- Lógica CNC-CAT.

- Validaciones complejas (van en core\_services).

- Operaciones matemáticas industriales (van en service\_math).

- Gestión de rutas (va en service\_paths).

- Manejo de estados (va en core\_state\_manager).

Core Utils debe permanecer **mínimo, puro y universal**.

## 6. Estándares de Core Utils

- Un archivo por utilidad.

- Nombres claros y consistentes.

- Funciones pequeñas y puras.

- Sin duplicación de lógica.

- Sin dependencias hacia módulos superiores.

- Documentación obligatoria.

- Uso transversal permitido, pero controlado por el núcleo.

## 7. Relación con el Ecosistema

Core Utils es utilizado por:

- Núcleo Lincat

- Motor CAM

- UI Industrial

- Simulación

- Integración CNC-CAT

- Pruebas

Es el **nivel más bajo de utilidades**, la base auxiliar del ecosistema.

## 8. Resultado

La documentación de Core Utils establece la estructura, responsabilidades y estándares del módulo que provee funciones auxiliares esenciales para el ecosistema Lincat, garantizando limpieza, modularidad y coherencia industrial.

