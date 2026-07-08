# ============================================================
#  CNC SERVO LOOP — LINCAT
#  Control PID + FeedForward + filtros
# ============================================================

class CNCServo:
    """
    Servo Loop CNC:
    - ejecuta puntos interpolados
    - aplica PID
    - aplica FeedForward
    - aplica filtros
    """

    def __init__(self):
        self.position = (0, 0, 0)

    def execute_point(self, point):
        """
        Ejecuta un punto interpolado.
        """
        # TODO: aplicar PID real
        # TODO: aplicar FF real
        # TODO: aplicar filtros reales

        self.position = point
        return self.position
