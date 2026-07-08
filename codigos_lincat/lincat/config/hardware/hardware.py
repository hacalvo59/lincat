# =============================================================================
#  Programa: hardware.py
#  Ubicación: codigos_lincat/lincat/config/hardware/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Configuración de Hardware del ecosistema
#      LINCAT. Su función es definir parámetros industriales relacionados con
#      dispositivos físicos, drivers, buses de campo, sensores, actuadores y
#      módulos IO utilizados por el sistema.
#
#  Descripción técnica:
#      - Administra configuración de hardware real y virtual.
#      - Permite registrar dispositivos detectados.
#      - Proporciona parámetros para EtherCAT, IO-Link, Modbus, CAN, etc.
#      - Se integra con los módulos de simulación, seguridad y CNC‑CAT.
#      - Es utilizado por bootstrap.py durante la inicialización del sistema.
#
#  Versión:
#      v1.0.0 — Implementación inicial de la Configuración de Hardware.
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
#      - Este archivo es crítico para la interacción con hardware industrial.
#      - No insertar lógica de módulos aquí. Solo configuración y registro.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DE CONFIGURACIÓN DE HARDWARE
# =============================================================================

class HardwareConfig:
    """
    Configuración de Hardware del ecosistema LINCAT.

    Administra parámetros industriales y dispositivos detectados.
    """

    def __init__(self):
        print(">>> Cargando Configuración de Hardware...")

        # Modo de operación del hardware
        self.modo_virtual = True          # True = sin hardware real
        self.detectar_dispositivos = False

        # Configuración de buses industriales
        self.buses = {
            "ethercat": {
                "habilitado": True,
                "auto_scan": False,
                "master": "ECAT_MASTER_0"
            },
            "modbus": {
                "habilitado": False,
                "puerto": "/dev/ttyS0",
                "baudrate": 9600
            },
            "can": {
                "habilitado": False,
                "interfaz": "can0"
            },
            "io_link": {
                "habilitado": False
            }
        }

        # Dispositivos detectados (sensores, actuadores, IO, drivers, etc.)
        self.dispositivos = {}

        print(">>> Configuración de Hardware cargada correctamente.")

    # -------------------------------------------------------------------------
    def registrar_dispositivo(self, device_id: str, data: dict):
        """
        Registra un dispositivo industrial detectado o configurado manualmente.

        Parámetros:
            device_id (str): Identificador único del dispositivo.
            data (dict): Información estructurada del dispositivo.
        """

        if not isinstance(device_id, str):
            raise TypeError("El ID del dispositivo debe ser una cadena de texto.")

        if not isinstance(data, dict):
            raise TypeError("Los datos del dispositivo deben ser un diccionario.")

        self.dispositivos[device_id] = data
        print(f"    [+] Dispositivo registrado: {device_id}")

    # -------------------------------------------------------------------------
    def obtener_dispositivo(self, device_id: str):
        """
        Obtiene un dispositivo por su ID.
        """

        return self.dispositivos.get(device_id, None)

    # -------------------------------------------------------------------------
    def listar_dispositivos(self):
        """
        Lista todos los dispositivos registrados.
        """

        return list(self.dispositivos.keys())

    # -------------------------------------------------------------------------
    def resumen(self):
        """
        Retorna un resumen estructurado de la configuración de hardware.
        """

        return {
            "modo_virtual": self.modo_virtual,
            "detectar_dispositivos": self.detectar_dispositivos,
            "buses": self.buses,
            "dispositivos": self.dispositivos
        }


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de la Configuración de Hardware")

    hw = HardwareConfig()

    # Registro de prueba
    hw.registrar_dispositivo("driver_servo_01", {
        "tipo": "driver",
        "fabricante": "Beckhoff",
        "modelo": "AX5000",
        "potencia": "5 kW"
    })

    print("Dispositivos registrados:", hw.listar_dispositivos())
    print("Resumen:", hw.resumen())
