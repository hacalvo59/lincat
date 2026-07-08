\#\#    05\_integracion\_cnc\_cat/00\_integracion\_cam\_cnc\_cat.md


# ⭐ 05\_integracion\_cnc\_cat/00\_integracion\_cam\_cnc\_cat.md

## Integración CAM → CNC‑CAT — *Puente Industrial de Ejecución Real*

## 1. Propósito del módulo

Este módulo es el encargado de transformar las trayectorias generadas por el CAM Core y validadas por la simulación en **instrucciones industriales** que CNC‑CAT puede ejecutar.

Su función es:

- recibir paths del CAM Core

- aplicar parámetros de máquina

- aplicar herramientas y offsets

- generar instrucciones CNC

- enviar el mecanizado a CNC‑CAT

- garantizar trazabilidad completa

Este módulo es el **puente entre el mundo digital y la máquina real**.

## 2. Filosofía de diseño

Tres principios:

### ✔ **Compatibilidad total con CNC‑CAT**

El módulo debe hablar el mismo “idioma industrial” que CNC‑CAT.

### ✔ **Trazabilidad absoluta**

Cada path debe tener:

- herramienta

- material

- parámetros

- offsets

- tolerancias

- fecha

- operador

### ✔ **Seguridad operacional**

Nada se envía a la máquina sin pasar por:

- CAM Core

- simulación

- validación final

## 3. Arquitectura del módulo

Estructura propuesta:

Código

```
`05\_integracion\_cnc\_cat/`

`    exportacion\_paths/`

`    herramientas/`

`    offsets/`

`    parametros\_maquina/`

`    comunicacion\_cnc\_cat/`
```

Cada carpeta representa un bloque funcional del puente industrial.

## 4. Flujo de trabajo del módulo

1. **Entrada de trayectorias** Recibe paths desde el simulador.

2. **Aplicación de parámetros de máquina**

   - velocidades

   - aceleraciones

   - profundidad

   - herramienta

   - material

3. **Generación de instrucciones CNC**

   - formato estándar

   - bloques industriales

   - movimientos seguros

4. **Comunicación con CNC‑CAT**

   - envío de instrucciones

   - verificación

   - confirmación de ejecución

5. **Trazabilidad**

   - registro completo

   - auditoría

   - historial

## 5. API interna del módulo

Funciones principales:

- **generar\_instrucciones()**

- **aplicar\_parametros()**

- **aplicar\_offsets()**

- **exportar\_a\_cnc\_cat()**

- **registrar\_trazabilidad()**

Estas funciones serán consumidas por:

- UI Industrial

- simulación

- CNC‑CAT

## 6. Estado actual del módulo

- carpeta creada

- documento inicial listo

- cabecera y destino definidos

- arquitectura estable

- listo para prototipos en `06\_pruebas`

