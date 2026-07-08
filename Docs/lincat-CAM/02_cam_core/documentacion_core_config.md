# Documentación Core Config — Núcleo Lincat

# Destino: 02\_cam\_core/documentacion\_core\_config.md

## 1. Propósito

El módulo `core\_config.py` define y gestiona la **configuración global del ecosistema Lincat**. Su función es centralizar parámetros, constantes, modos de operación y ajustes internos para que todos los módulos trabajen con una base común, estable y coherente.

Es el **punto único de verdad** para la configuración del sistema.

## 2. Responsabilidades de Core Config

- Proveer acceso centralizado a la configuración global.

- Cargar parámetros iniciales del sistema.

- Validar configuraciones antes de iniciar el ecosistema.

- Exponer constantes industriales para todos los módulos.

- Mantener coherencia entre CAM, UI, simulación y CNC-CAT.

- Registrar cambios de configuración cuando corresponda.

- Evitar que cada módulo defina su propia configuración.

## 3. Tipos de Configuración

Core Config gestiona configuraciones agrupadas por categoría:

- **config\_general** — Parámetros globales del ecosistema.

- **config\_cam** — Ajustes del motor CAM.

- **config\_ui** — Preferencias de la interfaz industrial.

- **config\_sim** — Parámetros de simulación.

- **config\_cnc** — Ajustes de integración CNC-CAT.

- **config\_security** — Límites y reglas de seguridad industrial.

- **config\_paths** — Rutas internas del sistema (sin rutas absolutas).

Cada categoría debe estar documentada y aislada.

## 4. Estructura del Módulo

El módulo se organiza en archivos específicos:

- **config\_loader.py** — Carga inicial de configuraciones.

- **config\_validator.py** — Validación de parámetros.

- **config\_defaults.py** — Valores por defecto del ecosistema.

- **config\_constants.py** — Constantes industriales.

- **config\_manager.py** — Control central de configuración.

- **config\_utils.py** — Utilidades auxiliares.

Cada archivo cumple una única responsabilidad.

## 5. Flujo de Uso

1. El ecosistema inicia.

2. Core Config carga configuraciones desde valores por defecto.

3. Valida parámetros críticos.

4. Expone la configuración global al núcleo.

5. El núcleo distribuye la configuración a los módulos que la necesitan.

6. Si un módulo requiere un parámetro, lo solicita al núcleo.

7. El núcleo consulta Core Config y devuelve el valor.

Este flujo garantiza **coherencia y estabilidad industrial**.

## 6. Qué NO pertenece a Core Config

- Lógica CAM.

- Lógica UI.

- Lógica CNC-CAT.

- Enrutamiento interno.

- Gestión de estados.

- Validaciones complejas de datos.

- Operaciones matemáticas.

Core Config solo gestiona configuración, nunca procesa lógica.

## 7. Estándares de Core Config

- Configuración centralizada y única.

- Sin duplicación de parámetros.

- Sin valores mágicos dentro del código.

- Documentación obligatoria por categoría.

- Validación estricta de parámetros críticos.

- Integración directa con el núcleo.

- Formato claro y consistente.

## 8. Relación con el Ecosistema

Core Config es utilizado por:

- Núcleo Lincat

- Motor CAM

- UI Industrial

- Simulación

- Integración CNC-CAT

- Pruebas

Es el **punto único de verdad** para la configuración del ecosistema.

## 9. Resultado

La documentación de Core Config establece la estructura, responsabilidades y estándares del módulo encargado de gestionar la configuración global del ecosistema Lincat, garantizando coherencia, estabilidad y profesionalismo industrial.

