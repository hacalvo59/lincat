# CAM Pocketing

# Destino: 02\_cam\_core/cam\_pocketing.md

## 1. Definición

CAM Pocketing es la estrategia encargada de mecanizar cavidades internas (pockets) mediante trayectorias de desbaste controladas. Utiliza la geometría detectada por el analizador geométrico y genera movimientos seguros, eficientes y optimizados para remover material dentro de una región cerrada.

## 2. Responsabilidades

- Interpretar cavidades detectadas por el analizador geométrico.

- Generar trayectorias internas de desbaste.

- Calcular offsets de herramienta para cavidades.

- Definir rampas de entrada seguras.

- Crear pasadas concéntricas o paralelas según la geometría.

- Controlar profundidad por capas.

- Evitar colisiones con paredes internas.

- Preparar datos para el motor de trayectorias y simulación.

## 3. Submódulos

- pocket\_interpreter.py

- pocket\_offsets.py

- pocket\_rampas.py

- pocket\_pasadas.py

- pocket\_profundidades.py

- pocket\_limites.py

- pocket\_validacion.py

- pocket\_exportador.py

## 4. Flujo de trabajo

1. Entrada: cavidades desde el analizador geométrico.

2. Offsets: compensación de herramienta dentro del pocket.

3. Rampas: definición de entrada segura (helical, linear, zig-zag).

4. Pasadas: generación de trayectorias internas (concéntricas o paralelas).

5. Profundidades: control de capas y niveles de corte.

6. Límites: verificación de paredes internas y zonas prohibidas.

7. Validación: colisiones preliminares dentro del pocket.

8. Salida: trayectorias de pocketing listas para el motor de trayectorias.

## 5. Resultado

CAM Pocketing produce trayectorias internas optimizadas para remover material dentro de cavidades, garantizando seguridad, eficiencia y compatibilidad con la simulación CAM y la integración CNC-CAT.

