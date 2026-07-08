# =============================================================================
#  Programa: simulation.py
#  Ubicación: codigos_lincat/lincat/config/simulation/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Configuración de Simulación del ecosistema
#      LINCAT. Su función es definir parámetros industriales relacionados con
#      la simulación de hardware, procesos, señales, eventos y módulos CNC‑CAT.
#
#  Descripción técnica:
#      - Administra configuración de simulación global.
#      - Permite habilitar/deshabilitar simulación del ecosistema.
#      - Define velocidad, precisión y comportamiento del simulador.
#      - Proporciona parámetros para simulación de hardware virtual.
#      - Se integra con los módulos de hardware, seguridad y UI.
#
#  Versión:
#      v1.0.0 — Implementación inicial de la Configuración de Simulación.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
#  Licencia:
#      Proyecto de código abierto bajo licencia industrial LINCAT.
#
#  Advertencias:
#      - Este archivo es crítico para la simulación del ecosistema.
#      - No insertar lógica de módulos aquí. Solo configuración y parámetros.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DE CONFIGURACIÓN DE SIMULACIÓN
# =============================================================================

class SimulationConfig:
    """
    Configuración de Simulación del ecosistema LINCAT.

    Administra parámetros globales de simulación industrial.
    """

    def __init__(self):
        print(">>> Cargando Configuración de Simulación...")

        # Estado general de la simulación
        self.habilitada = True
        self.modo_avanzado = False

        # Parámetros de simulación
        self.parametros = {
            "velocidad": 1.0,            # velocidad de simulación (1.0 = tiempo real)
            "precision": 0.001,          # precisión de cálculo
            "actualizacion_ms": 10,      # intervalo de actualización del simulador
            "ruido_simulado": False      # ruido artificial en sensores
        }

        # Simulación de hardware virtual
        self.hardware_virtual = {
            "drivers": True,
            "sensores": True,
            "actuadores": True,
            "io_modules": True,
            "ethercat_virtual": True
        }

        # Simulación de señales y eventos
        self.signals = {
            "simular_signals": True,
            "latencia_ms": 2
        }

        # Simulación CNC‑CAT
        self.cnc = {
            "simular_movimientos": True,
            "velocidad_movimiento": 1.0,
            "simular_herramienta": True
        }

        print(">>> Configuración de Simulación cargada correctamente.")

    # -------------------------------------------------------------------------
    def get(self, key: str):
        """
        Obtiene un parámetro global de simulación.
        """

        return getattr(self, key, None)

    # -------------------------------------------------------------------------
    def set(self, key: str, value):
        """
        Establece un parámetro global de simulación.
        """

        setattr(self, key, value)
        print(f"    [+] Parámetro de simulación actualizado: {key} = {value}")

    # -------------------------------------------------------------------------
    def resumen(self):
        """
        Retorna un resumen estructurado de la configuración de simulación.
        """

        return {
            "habilitada": self.habilitada,
            "modo_avanzado": self.modo_avanzado,
            "parametros": self.parametros,
            "hardware_virtual": self.hardware_virtual,
            "signals": self.signals,
            "cnc": self.cnc
        }


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de la Configuración de Simulación")

    sim = SimulationConfig()

    print("Resumen:", sim.resumen())

    sim.set("habilitada", False)
    print("Simulación habilitada:", sim.get("habilitada"))
