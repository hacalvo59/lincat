# Mapa de Comunicación Interna Lincat

# Destino: 00\_docs/mapa\_comunicacion\_interna\_lincat.md

## 1. Propósito

El Mapa de Comunicación Interna Lincat describe cómo se conectan y comunican los módulos del ecosistema. Define rutas, responsabilidades, direcciones de flujo y puntos de control que garantizan un sistema industrial, modular y trazable.

## 2. Principio Central

Toda comunicación interna pasa por el núcleo Lincat (01\_core).  
Ningún módulo se comunica directamente con otro sin pasar por el router central.

Esto garantiza:

- Independencia entre módulos.

- Trazabilidad completa.

- Control de errores centralizado.

- Estabilidad del ecosistema.

## 3. Componentes de Comunicación

- **core\_router.py** — Enrutador central.

- **core\_state\_manager.py** — Estado global del sistema.

- **core\_logging.py** — Registro industrial de eventos.

- **core\_config.py** — Configuración global.

- **core\_services/** — Servicios internos compartidos.

## 4. Flujo General de Comunicación

1. **UI Industrial** solicita una acción.

2. **Núcleo Lincat** recibe la solicitud.

3. El núcleo determina el módulo destino (CAM, simulación, CNC-CAT).

4. El módulo ejecuta la acción y devuelve resultados al núcleo.

5. El núcleo valida, registra y reenvía la información a la UI o a CNC-CAT.

6. La UI muestra resultados o ejecuta la acción final.

## 5. Rutas de Comunicación por Módulo

### 5.1 UI Industrial → Núcleo

- ui\_cargar\_geometria()

- ui\_seleccionar\_estrategia()

- ui\_generar\_trayectorias()

- ui\_simular()

- ui\_exportar()

### 5.2 Núcleo → Motor CAM

- router → analizador geométrico

- router → motor de trayectorias

- router → estrategias CAM

- router → simulación CAM

### 5.3 Motor CAM → Núcleo

- resultados de análisis

- trayectorias generadas

- validaciones

- errores y advertencias

### 5.4 Núcleo → CNC-CAT

- instrucciones industriales

- parámetros de máquina

- trazabilidad

### 5.5 CNC-CAT → Núcleo

- confirmaciones

- estados de ejecución

- errores de máquina

### 5.6 Núcleo → UI Industrial

- resultados finales

- simulación

- reportes

- estados de máquina

## 6. Diagrama Conceptual (texto)



UI Industrial

↓

Núcleo

↓

Motor CAM

↓ 

Simulación

 ↓ 

Integración CNC-CAT

 ↓ 

Máquina


El núcleo es el **centro de control**.

## 7. Reglas de Comunicación

- Ningún módulo CAM se comunica directamente con la UI.

- Ningún módulo CAM se comunica directamente con CNC-CAT.

- La UI nunca toca lógica CAM.

- CNC-CAT nunca toca lógica CAM.

- El núcleo es el único punto de conexión.

- Toda acción debe quedar registrada en core\_logging.

## 8. Resultado

El Mapa de Comunicación Interna Lincat garantiza un ecosistema modular, trazable y profesional, donde cada módulo cumple su función sin acoplamiento directo y con control total desde el núcleo.

