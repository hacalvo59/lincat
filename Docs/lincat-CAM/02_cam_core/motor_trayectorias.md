# Motor de Trayectorias CAM

# Destino: 02\_cam\_core/motor\_trayectorias.md

## 1. Definición

El motor de trayectorias CAM es la máquina encargada de transformar el mapa de mecanizado en movimientos industriales listos para simulación y exportación a CNC-CAT. Es el núcleo del sistema CAM y coordina offsets, rampas, pasadas, alturas y orden de operaciones.

## 2. Responsabilidades

- Generar trayectorias para cada región mecanizable.

- Calcular offsets de herramienta.

- Definir rampas de entrada y salida.

- Crear pasadas de desbaste y acabado.

- Ordenar operaciones según accesibilidad y seguridad.

- Controlar alturas, profundidades y límites.

- Validar colisiones preliminares.

- Preparar datos para la simulación CAM.

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

4. Pasadas: generación de roughing y finishing.\# Motor de Trayectorias CAM

5. \# Destino: 02\_cam\_core/motor\_trayectorias.md


7. \#\# 1. Definición

8. El motor de trayectorias CAM es la máquina encargada de transformar el mapa de mecanizado en movimientos industriales listos para simulación y exportación a CNC-CAT. Es el núcleo del sistema CAM y coordina offsets, rampas, pasadas, alturas y orden de operaciones.


10. \#\# 2. Responsabilidades

11. - Generar trayectorias para cada región mecanizable.

12. - Calcular offsets de herramienta.

13. - Definir rampas de entrada y salida.

14. - Crear pasadas de desbaste y acabado.

15. - Ordenar operaciones según accesibilidad y seguridad.

16. - Controlar alturas, profundidades y límites.

17. - Validar colisiones preliminares.

18. - Preparar datos para la simulación CAM.


20. \#\# 3. Submódulos

21. - generador\_offsets.py  

22. - generador\_rampas.py  

23. - generador\_pasadas.py  

24. - orden\_operaciones.py  

25. - calculo\_alturas.py  

26. - calculo\_limites.py  

27. - validador\_precolisiones.py  

28. - exportador\_trayectorias.py  


30. \#\# 4. Flujo de trabajo

31. 1. Entrada: mapa CAM desde el analizador geométrico.

32. 2. Offsets: cálculo de compensación de herramienta.

33. 3. Rampas: definición de entradas seguras.

34. 4. Pasadas: generación de roughing y finishing.

35. 5. Orden: secuencia óptima de operaciones.

36. 6. Alturas: control de niveles y profundidades.

37. 7. Límites: verificación de zonas prohibidas.

38. 8. Validación: colisiones preliminares.

39. 9. Salida: trayectorias listas para simulación y exportación.


41. \#\# 5. Resultado

42. El motor de trayectorias produce movimientos industriales optimizados que alimentan directamente la simulación CAM y la integración con CNC-CAT, garantizando un flujo robusto, modular y escalable.

43. Orden: secuencia óptima de operaciones.

44. Alturas: control de niveles y profundidades.

45. Límites: verificación de zonas prohibidas.

46. Validación: colisiones preliminares.

47. Salida: trayectorias listas para simulación y exportación.

## 5. Resultado

El motor de trayectorias produce movimientos industriales optimizados que alimentan directamente la simulación CAM y la integración con CNC-CAT, garantizando un flujo robusto, modular y escalable.

