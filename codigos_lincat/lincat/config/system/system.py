# =============================================================================
#  Programa: system.py
#  Ubicación: codigos_lincat/lincat/config/system/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Configuración Global del Sistema LINCAT.
#      Su función es cargar, administrar y proveer acceso a los parámetros
#      esenciales del ecosistema industrial.
#
#  Descripción técnica:
#      - Administra configuración global del framework.
#      - Proporciona valores por defecto para el sistema.
#      - Permite cargar configuraciones externas (futuro SQL/JSON/YAML).
#      - Es utilizado por bootstrap.py durante la inicialización del sistema.
#
#  Versión:
#      v1.0.0 — Implementación inicial de la Configuración Global del Sistema.
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
#      - Este archivo es crítico para la inicialización del ecosistema.
#      - No insertar lógica de módulos aquí. Solo configuración global.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DE CONFIGURACIÓN GLOBAL DEL SISTEMA
# =============================================================================

class SystemConfig:
    """
    Configuración Global del Sistema LINCAT.

    Administra parámetros esenciales del ecosistema industrial.
    """

    def __init__(self):
        print(">>> Cargando Configuración Global del Sistema...")

        # Parámetros globales del sistema
        self.version = "1.0.0"
        self.autor = "Proyecto LINCAT"
        self.entorno = "desarrollo"  # producción / pruebas / desarrollo

        # Configuración de logs
        self.logs = {
            "nivel": "INFO",
            "ruta": "/var/log/lincat/"
        }

        # Configuración de seguridad
        self.security = {
            "modo_seguro": True,
            "auditoria": True
        }

        # Configuración de simulación
        self.simulation = {
            "habilitada": True,
            "velocidad": 1.0
        }

        # Configuración de hardware
        self.hardware = {
            "modo_virtual": True,
            "detectar_dispositivos": False
        }

        print(">>> Configuración Global del Sistema cargada correctamente.")

    # -------------------------------------------------------------------------
    def get(self, key: str):
        """
        Obtiene un parámetro global del sistema.
        """

        return getattr(self, key, None)

    # -------------------------------------------------------------------------
    def set(self, key: str, value):
        """
        Establece un parámetro global del sistema.
        """

        setattr(self, key, value)
        print(f"    [+] Parámetro actualizado: {key} = {value}")

    # -------------------------------------------------------------------------
    def summary(self):
        """
        Retorna un resumen estructurado de la configuración global.
        """

        return {
            "version": self.version,
            "autor": self.autor,
            "entorno": self.entorno,
            "logs": self.logs,
            "security": self.security,
            "simulation": self.simulation,
            "hardware": self.hardware
        }


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de la Configuración Global del Sistema")

    config = SystemConfig()

    print("Resumen:", config.summary())

    config.set("entorno", "produccion")
    print("Nuevo entorno:", config.get("entorno"))
