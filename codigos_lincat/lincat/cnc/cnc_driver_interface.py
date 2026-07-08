# ============================================================
#  CNC DRIVER INTERFACE — LINCAT
#  Comunicación con drivers reales
# ============================================================

class CNCDriverInterface:
    """
    Interfaz con drivers reales:
    - EtherCAT
    - Modbus
    - CANOpen
    """

    def send_position(self, position):
        """
        Envía posición al driver.
        """
        # TODO: implementar comunicación real
        pass

    def read_feedback(self):
        """
        Lee feedback del driver.
        """
        # TODO: implementar lectura real
        return {
            "position": (0, 0, 0),
            "current": 0,
            "temperature": 0
        }
