\#\#    docs/lincat/produccion/16\_convenciones\_codigo.md



# 📘 **16\_convenciones\_codigo.md**

**Convenciones oficiales de código del ecosistema CNC‑CAT / LINCAT**

# ⭐ 1. Propósito

Definir las **reglas oficiales de estilo y estructura de código** para todos los módulos del ecosistema CNC‑CAT:

- UI LINCAT

- Motion API

- Motores (sim/real)

- CORE

- Drivers

- EtherCAT Layer

- PLC integrado

- Documentación técnica

Estas convenciones garantizan:

- claridad

- mantenibilidad

- consistencia

- profesionalismo

- calidad industrial

# ⭐ 2. Lenguaje principal

El proyecto CNC‑CAT utiliza:

### ✔️ **Python 3.12+**

Con:

- tipado obligatorio

- módulos organizados

- clases claras

- funciones pequeñas

- documentación integrada

# ⭐ 3. Reglas generales de estilo

### ✔️ 3.1 Tipado obligatorio

Ejemplo:

python

```
\`def move\\\_axis(axis: str, speed: float) -\\\> None:\`  
  
\`    ...\`
```

### ✔️ 3.2 Líneas máximo 100 caracteres

Evita scroll horizontal.

### ✔️ 3.3 Nombres descriptivos

Nada de:

❌ `a`, `tmp`, `data2`, `x1`

Siempre:

✔️ `axis\\\_name`, `trajectory\\\_point`, `ethercat\\\_state`

### ✔️ 3.4 Comentarios útiles

No comentar lo obvio.

# ⭐ 4. Convenciones de nombres

### ✔️ 4.1 Archivos

`snake\\\_case.py`

Ejemplos:

- `real\\\_cycle.py`

- `sim\\\_planner.py`

- `motion\\\_api.py`

### ✔️ 4.2 Clases

`PascalCase`

Ejemplos:

- `RealMotionController`

- `SimulationPlanner`

- `EtherCATMaster`

### ✔️ 4.3 Métodos y funciones

`snake\\\_case`

Ejemplos:

- `read\\\_inputs()`

- `update\\\_state()`

- `compute\\\_trajectory()`

### ✔️ 4.4 Constantes

`UPPER\\\_CASE`

Ejemplo:

python

```
\`CYCLE\\\_TIME\\\_MS = 1\`
```

# ⭐ 5. Convenciones de estructura

### ✔️ 5.1 Orden dentro de un archivo

Código

```
\`imports\`  
  
\`constantes\`  
  
\`clases\`  
  
\`funciones\`  
  
\`main (si aplica)\`
```

### ✔️ 5.2 Orden dentro de una clase

Código

```
\`atributos\`  
  
\`\\\_\\\_init\\\_\\\_\`  
  
\`métodos públicos\`  
  
\`métodos privados\`
```

### ✔️ 5.3 Un archivo = un propósito

Nada de mezclar:

❌ planner + interpolador ❌ drivers + lógica CNC ❌ UI + hardware

# ⭐ 6. Manejo de errores

### ✔️ 6.1 Excepciones específicas

Nunca usar:

❌ `Exception` genérica

Siempre:

✔️ `GcodeError` ✔️ `EtherCATTimeoutError` ✔️ `InvalidStateError`

### ✔️ 6.2 Mensajes claros

Ejemplo:

python

```
\`raise InvalidStateError("Cannot jog while machine is RUNNING")\`
```

# ⭐ 7. Documentación en código

### ✔️ Docstrings obligatorios

Ejemplo:

python

```
\`def home(self, axis: str) -\\\> None:\`  
  
\`    """\`  
  
\`    Ejecuta el ciclo de homing del eje indicado.\`  
  
\`    """\`
```

### ✔️ Comentarios solo cuando aportan valor

Nada de:

python

```
\`i = i + 1  \\\# incrementa i\`
```

# ⭐ 8. Convenciones para módulos críticos

### ✔️ 8.1 Planner

- funciones puras

- sin efectos secundarios

- sin acceso a IO

### ✔️ 8.2 Interpolador

- determinista

- sin dependencias externas

### ✔️ 8.3 Cycle (1 kHz)

- sin asignaciones pesadas

- sin logs excesivos

- sin estructuras dinámicas

### ✔️ 8.4 Drivers

- sin lógica CNC

- solo acceso a hardware

# ⭐ 9. Convenciones de rendimiento

- evitar objetos temporales en el ciclo

- evitar listas dinámicas en 1 kHz

- usar estructuras prealocadas

- minimizar conversiones de tipo

- evitar lambdas en loops críticos

# ⭐ 10. Convenciones de seguridad

- validar parámetros

- validar estados

- validar límites

- nunca confiar en hardware

- nunca ignorar alarmas

# ⭐ 11. Ejemplo completo

python

```
\`class RealCycle:\`  
  
\`    """\`  
  
\`    Ciclo de control real (1 kHz).\`  
  
\`    """\`  
  
  
\`    def \\\_\\\_init\\\_\\\_(self, io: RealIO, planner: RealPlanner):\`  
  
\`        self.io = io\`  
  
\`        self.planner = planner\`  
  
  
\`    def tick(self) -\\\> None:\`  
  
\`        inputs = self.io.read\\\_inputs()\`  
  
\`        point = self.planner.next\\\_step()\`  
  
\`        self.io.write\\\_outputs(point)\`
```

# ⭐ 12. Objetivo final

Estas convenciones garantizan que CNC‑CAT sea:

- limpio

- profesional

- mantenible

- escalable

- industrial

Son las reglas oficiales del código del ecosistema.

