# Estándares de Desarrollo Lincat

# Destino: 00\_docs/estandares\_desarrollo\_lincat.md

## 1. Propósito

Los Estándares de Desarrollo Lincat definen las reglas, prácticas y criterios que deben seguir todos los módulos del ecosistema. Garantizan coherencia, trazabilidad, modularidad y calidad industrial en cada componente del sistema.

## 2. Principios Fundamentales

- **Modularidad estricta**: cada archivo cumple una única responsabilidad.

- **Documentación obligatoria**: todo módulo debe tener su archivo .md correspondiente.

- **Cabecera fija**: primera línea con título, segunda línea con destino.

- **Sin duplicación**: ningún concepto se documenta dos veces.

- **Rutas coherentes**: cada archivo pertenece a una carpeta única y lógica.

- **Independencia de hardware**: el código no depende de máquinas específicas.

- **Trazabilidad completa**: cada acción queda registrada en core\_logging.

- **Comunicación centralizada**: todos los módulos se comunican vía núcleo Lincat.

## 3. Estructura de Archivos

Cada archivo debe contener:

1. Cabecera

2. Destino

3. Definición

4. Responsabilidades

5. Submódulos

6. Flujo de trabajo

7. Resultado

Esta estructura es obligatoria para:

- Núcleo Lincat

- Motor CAM

- UI Industrial

- Simulación

- Integración CNC-CAT

- Pruebas

- Notas técnicas

## 4. Estándares de Código

- Nombres claros y consistentes.

- Prefijos por módulo (cam\_, core\_, ui\_, cnc\_).

- Carpetas por función (core\_services/, core\_utils/, etc.).

- Excepciones centralizadas en core\_exceptions.py.

- Logging obligatorio en cada acción relevante.

- Router central para comunicación interna.

- Configuración global en core\_config.py.

## 5. Estándares de Documentación

- Un archivo por módulo.

- Sin contenido repetido entre documentos.

- Terminología industrial coherente.

- Diagramas conceptuales en texto cuando sea necesario.

- Índices actualizados en 00\_docs/.

- Notas técnicas en 07\_notas/.

## 6. Estándares de Comunicación Interna

- Ningún módulo se comunica directamente con otro.

- Toda comunicación pasa por core\_router.py.

- La UI nunca toca lógica CAM.

- CAM nunca toca CNC-CAT directamente.

- CNC-CAT nunca toca CAM directamente.

- El núcleo es el único punto de conexión.

## 7. Estándares de Carpeta

- 00\_docs → documentación global

- 01\_cam\_core → núcleo Lincat

- 02\_cam\_core → motor CAM

- 03\_ui\_industrial → interfaz industrial

- 04\_simulacion → simulación extendida

- 05\_integracion\_cnc\_cat → integración avanzada

- 06\_pruebas → laboratorio

- 07\_notas → notas técnicas

## 8. Estándares de Evolución

- Toda mejora debe registrarse en notas de laboratorio.

- Ningún módulo se modifica sin actualizar su documentación.

- Cambios estructurales deben reflejarse en el índice general.

- Nuevos módulos deben seguir la estructura estándar.

## 9. Resultado

Los Estándares de Desarrollo Lincat garantizan que el ecosistema crezca de forma ordenada, industrial, modular y profesional, manteniendo coherencia total entre documentación, código y arquitectura.

