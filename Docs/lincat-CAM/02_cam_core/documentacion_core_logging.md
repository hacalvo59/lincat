# Documentación Core Logging — Núcleo Lincat

# Destino: 02\_cam\_core/documentacion\_core\_logging.md

## 1. Propósito

El módulo `core\_logging.py` proporciona el sistema de registro industrial del ecosistema Lincat. Su función es capturar, almacenar y estructurar todos los eventos relevantes del sistema: solicitudes, errores, advertencias, resultados, cambios de estado y acciones internas.

Es el **registro oficial** del comportamiento del ecosistema.

## 2. Responsabilidades del Core Logging

- Registrar cada acción enviada al núcleo.

- Registrar cada operación ejecutada por CAM, UI, simulación o CNC-CAT.

- Registrar errores y excepciones internas.

- Registrar cambios de estado del sistema.

- Proveer trazabilidad completa para depuración y auditoría.

- Mantener un formato industrial, claro y consistente.

- Permitir análisis posterior de eventos.

## 3. Tipos de Registros

- **INFO** — Operaciones normales del sistema.

- **WARNING** — Situaciones anómalas no críticas.

- **ERROR** — Fallos que requieren intervención.

- **CRITICAL** — Estados peligrosos o fallos graves.

- **DEBUG** — Información extendida para desarrollo.

Cada tipo de registro debe tener su formato y estructura definidos.

## 4. Estructura del Registro

Cada entrada debe contener:

- Marca temporal

- Módulo origen

- Tipo de evento

- Mensaje descriptivo

- Datos adicionales (si aplica)

Ejemplo conceptual:

Código

```
`\[2026-07-03 18:45\] CORE\_ROUTER — INFO — Solicitud recibida: generar\_trayectorias`
```

## 5. Submódulos del Core Logging

- **logging\_writer.py** — Escritura de registros.

- **logging\_formatter.py** — Formateo de mensajes.

- **logging\_levels.py** — Definición de niveles de registro.

- **logging\_storage.py** — Almacenamiento interno.

- **logging\_utils.py** — Utilidades auxiliares.

Cada archivo cumple una única responsabilidad.

## 6. Flujo de Uso

1. Un módulo ejecuta una acción.

2. El núcleo envía la información al sistema de logging.

3. El mensaje se valida y se formatea.

4. El registro se almacena.

5. El núcleo continúa con el flujo normal.

El logging **no interrumpe** el funcionamiento del sistema.

## 7. Qué NO pertenece a Core Logging

- Lógica CAM.

- Lógica UI.

- Lógica CNC-CAT.

- Validaciones complejas.

- Gestión de estados.

- Enrutamiento interno.

Core Logging solo registra, nunca procesa lógica de negocio.

## 8. Estándares del Core Logging

- Formato consistente en todo el ecosistema.

- Sin duplicación de mensajes.

- Sin mensajes ambiguos.

- Sin dependencias hacia módulos superiores.

- Documentación obligatoria.

- Uso transversal en todo el sistema.

## 9. Relación con el Ecosistema

Core Logging es utilizado por:

- Núcleo Lincat

- Motor CAM

- UI Industrial

- Simulación

- Integración CNC-CAT

- Pruebas

Es el **sistema nervioso de trazabilidad** del ecosistema.

## 10. Resultado

La documentación de Core Logging establece la estructura, responsabilidades y estándares del módulo encargado de registrar el comportamiento del ecosistema Lincat, garantizando trazabilidad, claridad y profesionalismo industrial.

