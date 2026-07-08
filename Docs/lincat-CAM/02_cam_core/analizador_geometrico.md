# Analizador Geométrico CAM

# Destino: 02\_core/analizador\_geometrico.md

## 1. Definición

El analizador geométrico CAM es la máquina encargada de interpretar la geometría proveniente del motor Blender, traducirla a entidades CAM y coordinar la detección de zonas mecanizables.

## 2. Responsabilidades

- Interpretar geometría (mallas, curvas, sólidos).

- Detectar contornos exteriores e interiores.

- Detectar cavidades y pockets.

- Detectar superficies planas y curvas.

- Detectar límites y zonas prohibidas.

- Normalizar unidades, tolerancias y orientación.

- Generar el mapa de mecanizado para el motor de trayectorias.

## 3. Submódulos

- lector\_geometria.py

- detector\_contornos.py

- detector\_cavidades.py

- detector\_superficies.py

- detector\_limites.py

- mapa\_mecanizado.py

- normalizador.py

- exportador\_cam\_geom.py

## 4. Flujo de trabajo

1. Entrada: geometría desde Blender.

2. Interpretación: lectura de vértices, caras, normales.

3. Detección: contornos, cavidades, superficies, límites.

4. Normalización: unidades, tolerancias, discretización.

5. Mapa CAM: regiones mecanizables.

6. Salida: datos listos para el motor de trayectorias.

## 5. Resultado

El analizador geométrico produce un mapa CAM unificado que alimenta directamente al motor de trayectorias, garantizando un flujo industrial, ordenado y modular.

