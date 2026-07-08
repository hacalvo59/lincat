# Documentación Core Router — Núcleo Lincat

# Destino: 02\_cam\_core/documentacion\_core\_router.md

## 1. Propósito

El módulo `core\_router.py` es el **centro de comunicación interna** del ecosistema Lincat. Su responsabilidad es recibir solicitudes de cualquier módulo (UI, CAM, simulación, CNC-CAT), determinar el destino correcto y coordinar el flujo de información de forma ordenada, trazable y sin acoplamiento directo.

Es el **corazón del sistema**, el punto donde todo pasa y todo se controla.

## 2. Responsabilidades del Core Router

- Recibir solicitudes internas del ecosistema.

- Determinar el módulo destino según la acción requerida.

- Enrutar mensajes hacia CAM, UI, simulación o CNC-CAT.

- Validar la estructura de la solicitud.

- Registrar cada acción en el sistema de logs.

- Garantizar que ningún módulo se comunique directamente con otro.

- Mantener trazabilidad completa del flujo interno.

## 3. Estructura del Router

El router se organiza en funciones claras:

- **router\_dispatch()** — Punto de entrada principal.

- **router\_to\_cam()** — Enrutamiento hacia módulos CAM.

- **router\_to\_ui()** — Enrutamiento hacia la interfaz industrial.

- **router\_to\_sim()** — Enrutamiento hacia simulación.

- **router\_to\_cnc()** — Enrutamiento hacia CNC-CAT.

- **router\_validate()** — Validación de solicitudes.

- **router\_log()** — Registro de acciones internas.

Cada función debe cumplir una única responsabilidad.

## 4. Flujo de Comunicación

1. Un módulo envía una solicitud al núcleo.

2. El núcleo la entrega al router.

3. El router valida la solicitud.

4. El router determina el destino correcto.

5. El router envía la solicitud al módulo correspondiente.

6. El módulo procesa la acción y devuelve resultados.

7. El router registra la operación.

8. El núcleo entrega el resultado al módulo solicitante.

Este flujo garantiza orden, trazabilidad y modularidad.

## 5. Qué NO pertenece al Core Router

- Lógica CAM.

- Lógica UI.

- Lógica CNC-CAT.

- Validaciones complejas (van en core\_services).

- Gestión de estados (va en core\_state\_manager).

- Configuración global (va en core\_config).

- Utilidades auxiliares (van en core\_utils).

El router solo enruta, nunca procesa lógica de negocio.

## 6. Estándares del Core Router

- Funciones pequeñas y claras.

- Sin duplicación de rutas.

- Sin lógica CAM, UI o CNC-CAT.

- Validación mínima, solo estructural.

- Logging obligatorio en cada acción.

- Comunicación estrictamente unidireccional.

- Documentación obligatoria.

## 7. Relación con el Ecosistema

El router es utilizado por:

- Núcleo Lincat

- Motor CAM

- UI Industrial

- Simulación

- Integración CNC-CAT

- Pruebas

Es el **punto de control central** del ecosistema.

## 8. Resultado

La documentación del Core Router establece la estructura, responsabilidades y estándares del módulo que coordina toda la comunicación interna del ecosistema Lincat, garantizando orden, modularidad y trazabilidad industrial.

