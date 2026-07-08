# =============================================================================
#  Programa: cnc_cat.py
#  Ubicación: codigos_lincat/lincat/modules/cnc_cat/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo CNC‑CAT del ecosistema LINCAT.
#      Su función es actuar como controlador CNC industrial, administrando
#      movimientos, trayectorias, estados, buffers, ejecución de programas,
#      comunicación con motores, drivers y simulación.
#
#  Descripción técnica:
#      - Administra ejecución de trayectorias CNC.
#      - Controla estados del sistema CNC (idle, running, paused, stopped).
#      - Proporciona métodos para cargar programas CNC.
#      - Permite ejecutar movimientos lineales y circulares.
#      - Se integra con CAM, FLOW, EtherCAT, Maestro y Simulación.
#      - Es utilizado por producción, planta y seguridad.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Módulo CNC‑CAT.
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
#      - Este archivo es crítico para el control numérico industrial.
#      - No insertar lógica de hardware aquí. Solo interfaz y administración.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DEL MÓDULO CNC‑CAT
# =============================================================================

class LincatCNC:
    """
    Módulo CNC‑CAT del ecosistema LINCAT.

    Administra ejecución de trayectorias CNC y control de movimientos.
    """

    def __init__(self):
        print(">>> Módulo CNC‑CAT inicializado.")

        # Estado del CNC
        self.estado = "idle"  # idle / running / paused / stopped / error

        # Programa CNC cargado
        self.programa = []

        # Última trayectoria recibida
        self.trayectoria_actual = None

        # Posición actual simulada
        self.posicion = (0.0, 0.0, 0.0)

    # -------------------------------------------------------------------------
    def cargar_programa(self, programa: list):
        """
        Carga un programa CNC.

        Parámetros:
            programa (list): Lista de instrucciones CNC.
        """

        if not isinstance(programa, list):
            raise TypeError("El programa CNC debe ser una lista de instrucciones.")

        self.programa = programa
        print("    [+] Programa CNC cargado.")

    # -------------------------------------------------------------------------
    def cargar_trayectoria(self, trayectoria: dict):
        """
        Carga una trayectoria generada por el módulo CAM.

        Parámetros:
            trayectoria (dict): Datos de trayectoria estructurados.
        """

        if not isinstance(trayectoria, dict):
            raise TypeError("La trayectoria debe ser un diccionario estructurado.")

        self.trayectoria_actual = trayectoria
        print("    [+] Trayectoria CNC cargada.")

    # -------------------------------------------------------------------------
    def iniciar(self):
        """
        Inicia la ejecución CNC.
        """

        if self.estado == "running":
            raise RuntimeError("El CNC ya está en ejecución.")

        self.estado = "running"
        print("    [>] CNC‑CAT en ejecución.")

    # -------------------------------------------------------------------------
    def pausar(self):
        """
        Pausa la ejecución CNC.
        """

        if self.estado != "running":
            raise RuntimeError("El CNC no está en ejecución.")

        self.estado = "paused"
        print("    [>] CNC‑CAT pausado.")

    # -------------------------------------------------------------------------
    def detener(self):
        """
        Detiene la ejecución CNC.
        """

        self.estado = "stopped"
        print("    [>] CNC‑CAT detenido.")

    # -------------------------------------------------------------------------
    def mover_lineal(self, x: float, y: float, z: float):
        """
        Ejecuta un movimiento lineal.

        Parámetros:
            x, y, z (float): Coordenadas destino.
        """

        if self.estado != "running":
            raise RuntimeError("El CNC debe estar en ejecución para mover.")

        print(f"    [>] Movimiento lineal hacia ({x}, {y}, {z})")

        # Simulación de movimiento
        self.posicion = (x, y, z)

    # -------------------------------------------------------------------------
    def mover_circular(self, centro: tuple, radio: float):
        """
        Ejecuta un movimiento circular.

        Parámetros:
            centro (tuple): Centro del arco.
            radio (float): Radio del arco.
        """

        if self.estado != "running":
            raise RuntimeError("El CNC debe estar en ejecución para mover.")

        print(f"    [>] Movimiento circular con centro {centro} y radio {radio}")

        # Simulación de movimiento
        self.posicion = (centro[0] + radio, centro[1], centro[2])

    # -------------------------------------------------------------------------
    def estado_actual(self):
        """
        Retorna el estado actual del CNC.
        """

        return self.estado

    # -------------------------------------------------------------------------
    def posicion_actual(self):
        """
        Retorna la posición actual del CNC.
        """

        return self.posicion


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo CNC‑CAT")

    cnc = LincatCNC()

    cnc.cargar_programa(["G01 X10 Y0 Z0", "G01 X10 Y10 Z0"])
    cnc.cargar_trayectoria({"tipo": "contour", "puntos": [(0, 0), (10, 0)]})

    cnc.iniciar()
    cnc.mover_lineal(10, 0, 0)
    cnc.mover_circular((5, 5, 0), 3)

    cnc.pausar()
    cnc.detener()

    print("Estado final:", cnc.estado_actual())
    print("Posición final:", cnc.posicion_actual())
