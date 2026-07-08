# Integración CAM → CNC-CAT

# Destino: 02\_cam\_core/integracion\_cam\_cnc\_cat.md

## 1. Definición

La integración CAM → CNC-CAT es la máquina encargada de transformar las trayectorias generadas por el motor CAM en instrucciones industriales que CNC-CAT puede ejecutar. Este módulo garantiza compatibilidad total, trazabilidad y seguridad operacional.

## 2. Responsabilidades

- Recibir trayectorias validadas desde la simulación CAM.

- Convertir movimientos en instrucciones CNC estándar.

- Aplicar parámetros de máquina (velocidades, aceleraciones, avances).

- Aplicar offsets y correcciones finales.

- Generar bloques industriales seguros (movimientos G, M, F, S).

- Validar límites de máquina y zonas prohibidas.

- Preparar el archivo final para CNC-CAT.

- Registrar trazabilidad completa del mecanizado.

## 3. Submódulos

- cnc\_interpreter.py

- cnc\_parametros\_maquina.py

- cnc\_offsets\_finales.py

- cnc\_generador\_bloques.py

- cnc\_limites\_maquina.py

- cnc\_validacion\_final.py

- cnc\_exportador.py

- cnc\_trazabilidad.py

## 4. Flujo de trabajo

1. Entrada: trayectorias desde la simulación CAM.

2. Interpretación: conversión de movimientos a instrucciones CNC.

3. Parámetros: aplicación de velocidades, avances y aceleraciones.

4. Offsets: correcciones finales de herramienta y pieza.

5. Bloques: generación de movimientos G/M industriales.

6. Límites: verificación de volumen y restricciones de máquina.

7. Validación: chequeo final de seguridad operacional.

8. Exportación: archivo CNC listo para CNC-CAT.

9. Trazabilidad: registro completo del mecanizado.

## 5. Resultado

La integración CAM → CNC-CAT produce instrucciones industriales seguras, compatibles y optimizadas, listas para ser ejecutadas por CNC-CAT, garantizando un flujo profesional desde la geometría hasta la máquina real.

