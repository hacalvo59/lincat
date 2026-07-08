# ============================================================
#  TWIN EN TIEMPO REAL — LINCAT
#  Simulación dinámica basada en feedback CNC
# ============================================================

import math
import random

class TwinRealtime:
    """
    Twin en tiempo real:
    - recibe posición real del CNC
    - simula vibración, resonancia y estabilidad
    - devuelve datos dinámicos para Optimizer y UI
    """

    def __init__(self):
        self.last_position = (0, 0, 0)
        self.vibration = 0.0
        self.resonance = 0.0
        self.stability = 1.0

    def update_from_cnc(self, position):
        """
        Recibe posición real del CNC y actualiza simulación.
        """
        self.last_position = position

        # Simulación simple (placeholder industrial)
        self.vibration = abs(math.sin(position[0] / 50)) * 0.2
        self.resonance = abs(math.cos(position[1] / 40)) * 0.15
        self.stability = 1.0 - (self.vibration + self.resonance)

        return {
            "vibration": self.vibration,
            "resonance": self.resonance,
            "stability": self.stability
        }
