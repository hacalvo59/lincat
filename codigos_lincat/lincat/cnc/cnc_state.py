# ============================================================
#  CNC STATE — LINCAT
#  Estado global del CNC
# ============================================================

class CNCState:
    """
    Estado global del CNC:
    - posición
    - velocidad
    - aceleración
    - alarmas
    """

    def __init__(self):
        self.position = (0, 0, 0)
        self.velocity = 0
        self.acceleration = 0
        self.alarms = []
