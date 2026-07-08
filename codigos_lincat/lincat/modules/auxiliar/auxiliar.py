# =============================================================================
#  Programa: auxiliar.py
#  Ubicación: codigos_lincat/lincat/modules/auxiliar/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo Auxiliar del ecosistema LINCAT.
#      Su función es proporcionar herramientas y utilidades industriales
#      compartidas por los módulos principales del sistema.
#
#  Descripción técnica:
#      - Funciones de cálculo industrial.
#      - Conversión de unidades.
#      - Validaciones de datos.
#      - Utilidades de formato.
#      - Herramientas de soporte para CAM, CNC‑CAT, FLOW, EtherCAT y Maestro.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Módulo Auxiliar.
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
#      - Este archivo contiene utilidades comunes del ecosistema.
#      - No insertar lógica de módulos aquí. Solo funciones auxiliares.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


import math


# =============================================================================
#  CLASE PRINCIPAL DEL MÓDULO AUXILIAR
# =============================================================================

class LincatAuxiliar:
    """
    Módulo Auxiliar del ecosistema LINCAT.

    Proporciona utilidades industriales comunes.
    """

    def __init__(self):
        print(">>> Módulo Auxiliar inicializado.")

    # -------------------------------------------------------------------------
    #  CONVERSIÓN DE UNIDADES
    # -------------------------------------------------------------------------

    def mm_a_m(self, mm: float) -> float:
        """Convierte milímetros a metros."""
        return mm / 1000.0

    def m_a_mm(self, m: float) -> float:
        """Convierte metros a milímetros."""
        return m * 1000.0

    def rpm_a_rad_s(self, rpm: float) -> float:
        """Convierte RPM a radianes por segundo."""
        return rpm * (2 * math.pi / 60)

    # -------------------------------------------------------------------------
    #  VALIDACIONES INDUSTRIALES
    # -------------------------------------------------------------------------

    def validar_coordenada(self, punto: tuple) -> bool:
        """
        Valida que una coordenada industrial sea correcta.

        Parámetros:
            punto (tuple): (x, y, z)

        Retorna:
            True si es válida, False si no.
        """
        if not isinstance(punto, tuple):
            return False
        if len(punto) != 3:
            return False
        return all(isinstance(v, (int, float)) for v in punto)

    def validar_parametro(self, valor, minimo=None, maximo=None) -> bool:
        """
        Valida un parámetro industrial dentro de un rango.

        Parámetros:
            valor: Valor a validar.
            minimo: Límite inferior.
            maximo: Límite superior.
        """
        if minimo is not None and valor < minimo:
            return False
        if maximo is not None and valor > maximo:
            return False
        return True

    # -------------------------------------------------------------------------
    #  FORMATO Y UTILIDADES
    # -------------------------------------------------------------------------

    def formatear_vector(self, vector: tuple) -> str:
        """Devuelve un vector formateado como texto industrial."""
        return f"({vector[0]:.3f}, {vector[1]:.3f}, {vector[2]:.3f})"

    def redondear(self, valor: float, decimales: int = 3) -> float:
        """Redondea un valor industrial."""
        return round(valor, decimales)

    # -------------------------------------------------------------------------
    #  CÁLCULOS INDUSTRIALES
    # -------------------------------------------------------------------------

    def distancia(self, p1: tuple, p2: tuple) -> float:
        """
        Calcula la distancia entre dos puntos industriales.

        Parámetros:
            p1, p2 (tuple): Coordenadas (x, y, z)
        """
        if not self.validar_coordenada(p1) or not self.validar_coordenada(p2):
            raise ValueError("Coordenadas inválidas.")

        return math.sqrt(
            (p2[0] - p1[0]) ** 2 +
            (p2[1] - p1[1]) ** 2 +
            (p2[2] - p1[2]) ** 2
        )

    def interpolar_lineal(self, p1: tuple, p2: tuple, t: float) -> tuple:
        """
        Interpolación lineal entre dos puntos.

        Parámetros:
            p1, p2 (tuple): Puntos industriales.
            t (float): 0.0 → p1, 1.0 → p2
        """
        if not (0.0 <= t <= 1.0):
            raise ValueError("t debe estar entre 0.0 y 1.0")

        return (
            p1[0] + (p2[0] - p1[0]) * t,
            p1[1] + (p2[1] - p1[1]) * t,
            p1[2] + (p2[2] - p1[2]) * t
        )


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo Auxiliar")

    aux = LincatAuxiliar()

    print("mm a m:", aux.mm_a_m(1500))
    print("rpm a rad/s:", aux.rpm_a_rad_s(1200))

    p1 = (0, 0, 0)
    p2 = (10, 10, 0)

    print("Distancia:", aux.distancia(p1, p2))
    print("Interpolación t=0.5:", aux.interpolar_lineal(p1, p2, 0.5))
