# CAM Roughing

# Destino: 02\_cam\_core/cam\_roughing.md

## 1. Definición

CAM Roughing es la estrategia encargada de realizar el desbaste principal de la pieza, removiendo grandes volúmenes de material de forma eficiente y segura. Utiliza las regiones mecanizables detectadas por el analizador geométrico y genera trayectorias de corte agresivas pero controladas.

## 2. Responsabilidades

- Interpretar regiones de desbaste desde el analizador geométrico.

- Generar trayectorias de remoción masiva de material.

- Calcular offsets de herramienta para desbaste.

- Definir rampas de entrada seguras para cortes profundos.

- Crear pasadas paralelas, zig-zag o adaptativas según la geometría.

- Controlar profundidad por capas y niveles de corte.

- Evitar colisiones con paredes y geometrías internas.

- Preparar datos para el motor de trayectorias y simulación.

## 3. Submódulos

- rough\_interpreter.py

- rough\_offsets.py

- rough\_rampas.py

- rough\_pasadas.py

- rough\_profundidades.py

- rough\_limites.py

- rough\_validacion.py

- rough\_exportador.py

## 4. Flujo de trabajo

1. Entrada: regiones de desbaste desde el analizador geométrico.

2. Offsets: compensación de herramienta para desbaste.

3. Rampas: definición de entrada segura (helical, linear, plunge controlado).

4. Pasadas: generación de trayectorias de remoción masiva (paralelas, zig-zag, adaptativas).

5. Profundidades: control de capas y niveles de corte agresivo.

6. Límites: verificación de paredes y zonas prohibidas.

7. Validación: colisiones preliminares en el desbaste.

8. Salida: trayectorias de roughing listas para el motor de trayectorias.

## 5. Resultado

CAM Roughing produce trayectorias de desbaste optimizadas para remover material de forma rápida y segura, garantizando eficiencia, robustez y compatibilidad con la simulación CAM y la integración CNC-CAT.

