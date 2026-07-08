# Documentación Core Services — Núcleo Lincat

# Destino: 02\_cam\_core/documentacion\_core\_services.md

## 1. Propósito

El módulo `core\_services/` centraliza los servicios internos reutilizables del ecosistema Lincat. Su objetivo es proveer funciones comunes, estables y transversales que pueden ser utilizadas por cualquier módulo del sistema sin generar acoplamiento directo, manteniendo coherencia industrial y evitando duplicación.

## 2. Características de los Servicios

- Independientes del hardware.

- Reutilizables por cualquier módulo.

- Documentados de forma aislada.

- Sin dependencias circulares.

- Controlados por el núcleo Lincat.

- Integrados con el sistema de registro interno.

- Diseñados para ser mínimos, claros y trazables.

## 3. Submódulos de Core Services

Cada servicio se implementa en un archivo independiente, con una única responsabilidad:

- **service\_paths.py** — Gestión de rutas internas del ecosistema.

- **service\_validation.py** — Validaciones comunes para datos, estados y estructuras.

- **service\_conversion.py** — Conversión de unidades, formatos y estructuras internas.

- **service\_math.py** — Funciones matemáticas industriales (interpolación, vectores, offsets).

- **service\_time.py** — Gestión de tiempos internos, marcas temporales y sincronización.

- **service\_registry.py** — Registro interno de módulos, estados y recursos.

- **service\_security.py** — Validaciones de seguridad industrial (límites, estados críticos).

- **service\_utils.py** — Utilidades generales del núcleo.

## 4. Flujo de Uso de Core Services

1. Un módulo (CAM, UI, simulación, CNC-CAT) solicita una operación interna.

2. El núcleo Lincat determina qué servicio corresponde.

3. El servicio ejecuta la operación de forma aislada.

4. El resultado vuelve al núcleo.

5. El núcleo entrega el resultado al módulo solicitante.

6. La operación queda registrada en el sistema de logs.

Este flujo garantiza orden, trazabilidad y modularidad.

## 5. Qué NO pertenece a Core Services

- Lógica CAM (trayectorias, estrategias).

- Lógica UI.

- Lógica CNC-CAT.

- Motores gráficos o geometría.

- Código dependiente de Blender.

- Simulación avanzada.

Core Services debe permanecer **puro, estable y universal**.

## 6. Estándares de Core Services

- Un archivo por servicio.

- Nombres claros y consistentes.

- Sin duplicación de funciones.

- Documentación obligatoria.

- Logging obligatorio cuando corresponda.

- Sin dependencias entre servicios (solo hacia el núcleo).

- Sin acceso directo a módulos CAM o CNC-CAT.

## 7. Relación con el Ecosistema

Core Services es utilizado por:

- Núcleo Lincat

- Motor CAM

- UI Industrial

- Simulación

- Integración CNC-CAT

- Pruebas

Es la **caja de herramientas industrial** del ecosistema.

## 8. Resultado

La documentación de Core Services establece la estructura, responsabilidades y estándares del módulo que provee las funciones internas compartidas del ecosistema Lincat, garantizando modularidad, estabilidad y coherencia industrial.

