# Pruebas CAM

# Destino: 06\_pruebas/pruebas\_cam.md

## 1. Definición

El módulo de Pruebas CAM es el laboratorio experimental donde se validan, comparan y estresan los componentes del motor Lincat-CAM sin afectar los módulos oficiales. Permite experimentar con geometrías, trayectorias, estrategias y simulación en un entorno aislado.

## 2. Responsabilidades

- Probar el analizador geométrico con diferentes piezas.

- Validar trayectorias generadas por el motor de trayectorias.

- Testear estrategias CAM (pocketing, contouring, roughing, finishing).

- Ejecutar simulaciones controladas.

- Detectar fallos, inconsistencias y mejoras potenciales.

- Registrar resultados y conclusiones.

- Mantener un entorno aislado del motor oficial.

## 3. Submódulos

- pruebas\_geometria.py

- pruebas\_trayectorias.py

- pruebas\_pocketing.py

- pruebas\_contouring.py

- pruebas\_roughing.py

- pruebas\_finishing.py

- pruebas\_simulacion.py

- pruebas\_integracion.py

## 4. Flujo de trabajo

1. Selección: elegir el módulo CAM a probar.

2. Geometría: cargar pieza experimental.

3. Estrategias: ejecutar pocketing, contouring, roughing o finishing.

4. Trayectorias: validar movimientos generados.

5. Simulación: verificar colisiones y remoción de material.

6. Integración: probar exportación a CNC-CAT.

7. Registro: documentar resultados, fallos y mejoras.

## 5. Resultado

El módulo de Pruebas CAM garantiza que cada componente del motor Lincat-CAM evolucione de forma segura, controlada y modular, permitiendo experimentar sin afectar el sistema oficial.

