\#\#     03\_ui\_industrial/00\_ui\_lincat\_cam.md


# ⭐ 03\_ui\_industrial/00\_ui\_lincat\_cam.md

## UI Industrial Lincat‑CAM — *Interfaz Operativa del Motor CAM*

## 1. Propósito del módulo

La UI Industrial de Lincat‑CAM es la interfaz que permite a un operador:

- cargar geometría

- seleccionar estrategias CAM

- visualizar trayectorias

- ejecutar simulación

- exportar paths a CNC‑CAT

Esta interfaz **no depende de Blender**, no usa su UI, no muestra sus paneles y no expone su complejidad. Es una UI **propia**, diseñada para industria.

## 2. Filosofía de diseño

Tres principios:

### ✔ **Claridad industrial**

Botones grandes, paneles limpios, flujo directo. Nada de pestañas microscópicas ni configuraciones escondidas.

### ✔ **Flujo CAM → CNC**

La UI guía al operador paso a paso:

1. Geometría

2. Estrategia

3. Trayectoria

4. Simulación

5. Exportación

### ✔ **Independencia total de Blender**

La UI no muestra nada de:

- timeline

- sculpt

- UV

- shading

- compositor

- animación

- nodos

Solo CAM.

## 3. Arquitectura del módulo

Estructura propuesta:

Código

```
`03\_ui\_industrial/`

`    panel\_principal/`

`    panel\_geometria/`

`    panel\_estrategias/`

`    panel\_trayectorias/`

`    panel\_simulacion/`

`    panel\_exportacion/`
```

Cada panel es un bloque funcional independiente.

## 4. Flujo de interacción

1. **Cargar geometría**

   - archivo

   - pieza

   - material

2. **Seleccionar estrategia CAM**

   - **Pocketing**

   - **Contouring**

   - **Roughing**

   - **Finishing**

3. **Generar trayectorias**

   - parámetros

   - alturas

   - velocidades

4. **Simulación**

   - colisiones

   - límites

   - herramienta

5. **Exportación a CNC‑CAT**

   - path

   - herramienta

   - offsets

## 5. API interna de la UI

La UI se comunica con:

- **motor Blender**

- **CAM Core**

- **CNC‑CAT**

Funciones principales:

- **ui\_cargar\_geometria()**

- **ui\_seleccionar\_estrategia()**

- **ui\_generar\_trayectoria()**

- **ui\_simular()**

- **ui\_exportar()**

## 6. Estado actual del módulo

- carpeta creada

- documento inicial listo

- cabecera y destino definidos

- arquitectura estable

- listo para recibir prototipos en `06\_pruebas`

