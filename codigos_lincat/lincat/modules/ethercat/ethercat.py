# =============================================================================
#  Programa: ethercat.py
#  Ubicación: codigos_lincat/lincat/modules/ethercat/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo EtherCAT del ecosistema LINCAT.
#      Su función es administrar la comunicación industrial con esclavos
#      EtherCAT, drivers, módulos IO, sensores y actuadores.
#
#  Descripción técnica:
#      - Administra el maestro EtherCAT.
#      - Permite escanear esclavos conectados.
#      - Proporciona métodos para leer y escribir PDOs.
#      - Simula comunicación cuando el hardware no está disponible.
#      - Se integra con CNC‑CAT, FLOW, HardwareConfig y Simulación.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Módulo EtherCAT.
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
#      - Este archivo es crítico para la comunicación industrial.
#      - No insertar lógica de hardware real aquí. Solo interfaz y simulación.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DEL MÓDULO ETHERCAT
# =============================================================================

class LincatEtherCAT:
    """
    Módulo EtherCAT del ecosistema LINCAT.

    Administra comunicación con esclavos EtherCAT y PDOs.
    """

    def __init__(self):
        print(">>> Módulo EtherCAT inicializado.")

        # Estado del maestro EtherCAT
        self.maestro_activo = False

        # Lista de esclavos detectados
        self.esclavos = {}

        # Simulación de PDOs
        self.pdos = {}

    # -------------------------------------------------------------------------
    def iniciar_maestro(self):
        """
        Inicia el maestro EtherCAT.
        """

        self.maestro_activo = True
        print("    [+] Maestro EtherCAT iniciado.")

    # -------------------------------------------------------------------------
    def detener_maestro(self):
        """
        Detiene el maestro EtherCAT.
        """

        self.maestro_activo = False
        print("    [+] Maestro EtherCAT detenido.")

    # -------------------------------------------------------------------------
    def escanear_esclavos(self):
        """
        Simula el escaneo de esclavos EtherCAT conectados.
        """

        if not self.maestro_activo:
            raise RuntimeError("El maestro EtherCAT no está activo.")

        print("    [>] Escaneando esclavos EtherCAT...")

        # Simulación de esclavos detectados
        self.esclavos = {
            1: {"nombre": "AX5000", "tipo": "driver", "fabricante": "Beckhoff"},
            2: {"nombre": "EL1008", "tipo": "input", "fabricante": "Beckhoff"},
            3: {"nombre": "EL2008", "tipo": "output", "fabricante": "Beckhoff"}
        }

        print("    [+] Esclavos detectados:", list(self.esclavos.keys()))

    # -------------------------------------------------------------------------
    def leer_pdo(self, esclavo_id: int, pdo: str):
        """
        Lee un PDO de un esclavo EtherCAT.

        Parámetros:
            esclavo_id (int): ID del esclavo.
            pdo (str): Nombre del PDO.

        Retorna:
            Valor simulado del PDO.
        """

        if esclavo_id not in self.esclavos:
            raise ValueError(f"El esclavo {esclavo_id} no existe.")

        valor = self.pdos.get((esclavo_id, pdo), 0)

        print(f"    [>] Leer PDO '{pdo}' del esclavo {esclavo_id}: {valor}")

        return valor

    # -------------------------------------------------------------------------
    def escribir_pdo(self, esclavo_id: int, pdo: str, valor):
        """
        Escribe un valor en un PDO de un esclavo EtherCAT.

        Parámetros:
            esclavo_id (int): ID del esclavo.
            pdo (str): Nombre del PDO.
            valor: Valor a escribir.
        """

        if esclavo_id not in self.esclavos:
            raise ValueError(f"El esclavo {esclavo_id} no existe.")

        self.pdos[(esclavo_id, pdo)] = valor

        print(f"    [>] Escribir PDO '{pdo}' del esclavo {esclavo_id}: {valor}")

    # -------------------------------------------------------------------------
    def listar_esclavos(self):
        """
        Lista todos los esclavos EtherCAT detectados.
        """

        return self.esclavos

    # -------------------------------------------------------------------------
    def estado_maestro(self):
        """
        Retorna el estado del maestro EtherCAT.
        """

        return self.maestro_activo


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo EtherCAT")

    ecat = LincatEtherCAT()

    ecat.iniciar_maestro()
    ecat.escanear_esclavos()

    ecat.escribir_pdo(1, "velocidad", 1500)
    ecat.leer_pdo(1, "velocidad")

    print("Esclavos:", ecat.listar_esclavos())
    print("Estado maestro:", ecat.estado_maestro())
