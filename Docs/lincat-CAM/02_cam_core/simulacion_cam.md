# Simulación CAM

# Destino: 02\_cam\_core/simulacion\_cam.md

## 1. Definición

La simulación CAM es la máquina encargada de validar trayectorias, detectar colisiones, visualizar el mecanizado y verificar la remoción de material antes de enviar los movimientos a CNC-CAT. Es el módulo que garantiza que el mecanizado sea seguro, eficiente y libre de errores.

## 2. Responsabilidades

- Recibir trayectorias desde el motor de trayectorias.

- Simular el movimiento de la herramienta en tiempo real.

- Detectar colisiones con la pieza, paredes y geometrías internas.

- Simular remoción de material (stock removal).

- Visualizar el mecanizado en 3D.

- Validar profundidades, rampas y offsets.

- Generar reportes de errores y advertencias.

- Preparar datos finales para exportación a CNC-CAT.

## 3. Submódulos

- sim\_interpreter.py

- sim\_movimiento.py

- sim\_colisiones.py

- sim\_remocion\_material.py

- sim\_visualizador.py

- sim\_validacion.py

- sim\_reportes.py

- sim\_exportador.py

## 4. Flujo de trabajo

1. Entrada: trayectorias desde el motor de trayectorias.

2. Movimiento: simulación del recorrido de la herramienta.

3. Colisiones: detección de choques con pieza o geometrías internas.

4. Remoción: simulación del material eliminado en cada pasada.

5. Visualización: renderizado 3D del mecanizado.

6. Validación: verificación de rampas, offsets y profundidades.

7. Reportes: generación de errores, advertencias y métricas.

8. Salida: simulación validada lista para exportación a CNC-CAT.

## 5. Resultado

La simulación CAM garantiza que las trayectorias sean seguras, eficientes y correctas antes de ejecutar el mecanizado real, asegurando compatibilidad total con CNC-CAT y el flujo industrial de Lincat-CAM.

