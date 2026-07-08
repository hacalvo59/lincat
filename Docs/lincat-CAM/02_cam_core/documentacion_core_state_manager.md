# Documentación Core State Manager — Núcleo Lincat

# Destino: 02\_cam\_core/documentacion\_core\_state\_manager.md

## 1. Propósito

El módulo `core\_state\_manager.py` es el encargado de **gestionar el estado global del ecosistema Lincat**. Controla los estados internos del sistema, las transiciones válidas, las condiciones de seguridad y la coherencia entre módulos. Es el componente que garantiza que el sistema siempre se encuentre en un estado válido y seguro antes de ejecutar cualquier acción.

## 2. Responsabilidades del Core State Manager

- Mantener el estado global del ecosistema.

- Validar transiciones entre estados.

- Garantizar condiciones de seguridad antes de ejecutar acciones.

- Notificar cambios de estado al núcleo y a los módulos relevantes.

- Registrar transiciones en el sistema de logs.

- Proveer acceso controlado al estado actual.

- Evitar estados inválidos o peligrosos.

## 3. Tipos de Estado

El sistema utiliza estados industriales claros y definidos:

- **INIT** — Sistema inicializado.

- **IDLE** — Sistema en reposo, esperando acción.

- **PROCESSING** — Acción en curso (CAM, simulación, CNC-CAT).

- **ERROR** — Estado de fallo.

- **CRITICAL** — Estado peligroso que requiere intervención.

- **SHUTDOWN** — Sistema apagándose o detenido.

Cada estado tiene reglas estrictas de transición.

## 4. Transiciones de Estado

Ejemplos conceptuales:

- INIT → IDLE

- IDLE → PROCESSING

- PROCESSING → IDLE

- PROCESSING → ERROR

- ERROR → IDLE

- CRITICAL → SHUTDOWN

Las transiciones inválidas deben ser bloqueadas y registradas.

## 5. Submódulos del Core State Manager

- **state\_definitions.py** — Definición de estados y constantes.

- **state\_transitions.py** — Reglas de transición.

- **state\_validator.py** — Validación de estados y condiciones.

- **state\_controller.py** — Control central de estado.

- **state\_events.py** — Notificación de cambios de estado.

Cada archivo cumple una única responsabilidad.

## 6. Flujo de Uso

1. Un módulo solicita una acción.

2. El núcleo consulta el estado actual.

3. El state manager valida si la acción es permitida.

4. Si es válida, el estado cambia y se registra.

5. El núcleo ejecuta la acción.

6. Al finalizar, el estado vuelve a IDLE o al estado correspondiente.

El state manager es el **guardia industrial** del ecosistema.

## 7. Qué NO pertenece al Core State Manager

- Lógica CAM.

- Lógica UI.

- Lógica CNC-CAT.

- Enrutamiento interno.

- Validaciones complejas de datos.

- Operaciones matemáticas.

- Gestión de archivos.

El state manager solo controla estados, nunca procesa lógica de negocio.

## 8. Estándares del Core State Manager

- Estados claros y documentados.

- Transiciones estrictas y validadas.

- Sin duplicación de lógica.

- Sin dependencias hacia módulos superiores.

- Logging obligatorio en cada transición.

- Documentación obligatoria.

- Seguridad industrial como prioridad.

## 9. Relación con el Ecosistema

El state manager es utilizado por:

- Núcleo Lincat

- Motor CAM

- UI Industrial

- Simulación

- Integración CNC-CAT

- Pruebas

Es el **controlador de estabilidad** del ecosistema.

## 10. Resultado

La documentación del Core State Manager establece la estructura, responsabilidades y estándares del módulo encargado de gestionar el estado global del ecosistema Lincat, garantizando seguridad, coherencia y estabilidad industrial.

