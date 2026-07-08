# ============================================================
#  CNC INTERPOLATOR — LINCAT
#  Genera puntos interpolados para el servo loop
# ============================================================

import math

class CNCInterpolator:
    """
    Interpolador CNC:
    - lineal
    - circular
    - spline
    - perfiles S-curve
    """

    def interpolate_line(self, start, end, steps):
        """
        Interpolación lineal simple.
        """
        points = []
        for i in range(steps):
            t = i / (steps - 1)
            x = start[0] + (end[0] - start[0]) * t
            y = start[1] + (end[1] - start[1]) * t
            z = start[2] + (end[2] - start[2]) * t
            points.append((x, y, z))
        return points
