# Documentación Core Exceptions — Núcleo Lincat

# Destino: 02\_cam\_core/documentacion\_core\_exceptions.md

## 1. Propósito

El módulo `core\_exceptions.py` define todas las excepciones internas del ecosistema Lincat. Su objetivo es centralizar el manejo de errores, garantizar coherencia en los mensajes, evitar duplicación y permitir que cualquier módulo del sistema pueda lanzar fallos de forma clara, controlada y trazable.

Es el **sistema oficial de errores industriales** del ecosistema.

## 2. Responsabilidades de Core Exceptions

- Definir todas las excepciones internas del sistema.

- Proveer clases de error claras, consistentes y documentadas.

- Evitar que cada módulo cree sus propias excepciones.

- Garantizar que los errores sean capturados por el núcleo.

- Integrarse con el sistema de logging para trazabilidad.

- Mantener un catálogo industrial de fallos.

## 3. Tipos de Excepciones

El ecosistema utiliza excepciones clasificadas por categoría:

- **CoreError** — Error genérico del núcleo.

- **StateError** — Error relacionado con estados inválidos.

- **RouterError** — Error en enrutamiento interno.

- **ConfigError** — Error en configuración global.

- **ServiceError** — Error en servicios internos.

- **ValidationError** — Error de validación de datos.

- **SecurityError** — Error de seguridad industrial.

- **CAMError** — Error en módulos CAM.

- **CNCError** — Error en integración CNC-CAT.

- **UIError** — Error en la interfaz industrial.

Cada excepción debe tener un mensaje claro y un propósito único.

## 4. Estructura del Módulo

El módulo se organiza en archivos pequeños y específicos:

- **exceptions\_base.py** — Clase base de todas las excepciones.

- **exceptions\_core.py** — Excepciones del núcleo.

- **exceptions\_state.py** — Excepciones de estado.

- **exceptions\_router.py** — Excepciones del router.

- **exceptions\_services.py** — Excepciones de servicios internos.

- **exceptions\_validation.py** — Excepciones de validación.

- **exceptions\_security.py** — Excepciones de seguridad.

- **exceptions\_cam.py** — Excepciones del motor CAM.

- **exceptions\_cnc.py** — Excepciones de CNC-CAT.

- **exceptions\_ui.py** — Excepciones de la interfaz industrial.

Cada archivo contiene solo las excepciones de su categoría.

## 5. Flujo de Uso

1. Un módulo detecta un fallo.

2. Lanza la excepción correspondiente desde core\_exceptions.

3. El núcleo captura la excepción.

4. El núcleo registra el error en el sistema de logging.

5. El núcleo decide si el sistema debe cambiar de estado.

6. La UI recibe un mensaje claro y estructurado.

Este flujo garantiza **orden, claridad y seguridad industrial**.

## 6. Qué NO pertenece a Core Exceptions

- Lógica CAM.

- Lógica UI.

- Lógica CNC-CAT.

- Validaciones complejas.

- Manejo de estados.

- Enrutamiento interno.

- Operaciones matemáticas.

Core Exceptions solo define errores, nunca procesa lógica.

## 7. Estándares de Core Exceptions

- Nombres claros y consistentes.

- Mensajes descriptivos y no ambiguos.

- Sin duplicación de excepciones.

- Sin dependencias hacia módulos superiores.

- Documentación obligatoria.

- Integración directa con el sistema de logging.

- Uso transversal en todo el ecosistema.

## 8. Relación con el Ecosistema

Core Exceptions es utilizado por:

- Núcleo Lincat

- Motor CAM

- UI Industrial

- Simulación

- Integración CNC-CAT

- Pruebas

Es el **catálogo oficial de fallos** del ecosistema.

## 9. Resultado

La documentación de Core Exceptions establece la estructura, responsabilidades y estándares del módulo encargado de definir y centralizar los errores del ecosistema Lincat, garantizando coherencia, trazabilidad y seguridad industrial.

