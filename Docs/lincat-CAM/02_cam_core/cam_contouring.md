# CAM Contouring

# Destino: 02\_cam\_core/cam\_contouring.md

## 1. Definición

CAM Contouring es la estrategia encargada de mecanizar perfiles exteriores e interiores mediante trayectorias perimetrales controladas. Utiliza los contornos detectados por el analizador geométrico y genera movimientos precisos para corte, perfilado y acabado de bordes.

## 2. Responsabilidades

- Interpretar contornos exteriores e interiores.

- Generar trayectorias perimetrales de corte.

- Calcular offsets de herramienta para perfiles.

- Definir rampas de entrada y salida.

- Crear pasadas de desbaste y acabado perimetral.

- Controlar profundidad por capas.

- Evitar colisiones con paredes y geometrías adyacentes.

- Preparar datos para el motor de trayectorias y simulación.

## 3. Submódulos

- contour\_interpreter.py

- contour\_offsets.py

- contour\_rampas.py

- contour\_pasadas.py

- contour\_profundidades.py

- contour\_limites.py

- contour\_validacion.py

- contour\_exportador.py

## 4. Flujo de trabajo

1. Entrada: contornos desde el analizador geométrico.

2. Offsets: compensación de herramienta para perfiles.

3. Rampas: definición de entrada segura (helical, linear, tangencial).

4. Pasadas: generación de trayectorias perimetrales (desbaste y acabado).

5. Profundidades: control de capas y niveles de corte.

6. Límites: verificación de paredes y zonas prohibidas.

7. Validación: colisiones preliminares en el perfilado.

8. Salida: trayectorias de contouring listas para el motor de trayectorias.

## 5. Resultado

CAM Contouring produce trayectorias perimetrales optimizadas para corte y perfilado, garantizando precisión, seguridad y compatibilidad con la simulación CAM y la integración CNC-CAT.

