# Motor de Trayectorias CAM

# Destino: 02\_cam\_core/motor\_trayectorias.md

## 1. Definición

El motor de trayectorias CAM es la máquina encargada de transformar el mapa de mecanizado en movimientos industriales listos para simulación y exportación a CNC-CAT.

## 2. Responsabilidades

- Generar trayectorias para cada región mecanizable.

- Calcular offsets de herramienta.

- Definir rampas de entrada y salida.

- Crear pasadas de desbaste y acabado.

- Ordenar operaciones según accesibilidad y seguridad.

- Controlar alturas, profundidades y límites.

- Validar colisiones preliminares.

- Preparar datos para la simulación.

## 3. Submódulos

- generador\_offsets.py

- generador\_rampas.py

- generador\_pasadas.py

- orden\_operaciones.py

- calculo\_alturas.py

- calculo\_limites.py

- validador\_precolisiones.py

- exportador\_trayectorias.py

## 4. Flujo de trabajo

1. Entrada: mapa CAM desde el analizador geométrico.

2. Offsets: cálculo de compensación de herramienta.

3. Rampas: definición de entradas seguras.

4. Pasadas: generación de roughing y finishing.

5. Orden: secuencia óptima de operaciones.

6. Alturas: control de niveles y profundidades.

7. Límites: verificación de zonas prohibidas.

8. Validación: colisiones preliminares.

9. Salida: trayectorias listas para simulación.

## 5. Resultado

El motor de trayectorias produce movimientos industriales optimizados que alimentan directamente la simulación CAM y la exportación a CNC-CAT.

