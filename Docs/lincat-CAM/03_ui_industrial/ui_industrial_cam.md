# UI Industrial CAM

# Destino: 03\_ui\_industrial/ui\_industrial\_cam.md

## 1. Definición

La UI Industrial CAM es la interfaz operativa del motor Lincat-CAM. Permite al operador cargar geometría, seleccionar estrategias CAM, generar trayectorias, ejecutar simulación y exportar instrucciones a CNC-CAT. Es una interfaz propia, independiente de Blender y diseñada para uso industrial.

## 2. Responsabilidades

- Cargar geometría desde el motor Blender embebido.

- Mostrar regiones mecanizables detectadas por el analizador geométrico.

- Permitir seleccionar estrategias CAM (pocketing, contouring, roughing, finishing).

- Configurar parámetros de mecanizado (velocidades, profundidades, rampas).

- Ejecutar generación de trayectorias.

- Visualizar simulación CAM.

- Exportar instrucciones a CNC-CAT.

- Registrar trazabilidad de operaciones.

## 3. Paneles de la UI

- panel\_principal/

- panel\_geometria/

- panel\_estrategias/

- panel\_trayectorias/

- panel\_simulacion/

- panel\_exportacion/

## 4. Flujo de interacción

1. Geometría: carga de pieza y visualización básica.

2. Estrategias: selección de pocketing, contouring, roughing o finishing.

3. Trayectorias: generación de movimientos industriales.

4. Simulación: validación visual y detección de colisiones.

5. Exportación: envío de instrucciones a CNC-CAT.

## 5. API interna

La UI se comunica con:

- Analizador geométrico (02\_cam\_core/analizador\_geometrico.md)

- Motor de trayectorias (02\_cam\_core/motor\_trayectorias.md)

- Estrategias CAM (pocketing, contouring, roughing, finishing)

- Simulación CAM (02\_cam\_core/simulacion\_cam.md)

- Integración CNC-CAT (02\_cam\_core/integracion\_cam\_cnc\_cat.md)

Funciones principales:

- ui\_cargar\_geometria()

- ui\_seleccionar\_estrategia()

- ui\_generar\_trayectorias()

- ui\_simular()

- ui\_exportar()

## 6. Resultado

La UI Industrial CAM proporciona un flujo operativo claro, modular y seguro para controlar el motor Lincat-CAM desde la geometría hasta la exportación final a CNC-CAT.

