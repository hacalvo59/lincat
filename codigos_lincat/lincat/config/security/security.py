# =============================================================================
#  Programa: security.py
#  Ubicación: codigos_lincat/lincat/config/security/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Configuración de Seguridad del ecosistema
#      LINCAT. Su función es definir parámetros industriales relacionados con
#      protección del sistema, auditoría, permisos, integridad y modos seguros.
#
#  Descripción técnica:
#      - Administra configuración de seguridad global.
#      - Permite habilitar/deshabilitar auditoría del sistema.
#      - Define niveles de seguridad y modos de operación.
#      - Proporciona parámetros para protección de hardware y simulación.
#      - Se integra con los módulos de hardware, simulation y CNC‑CAT.
#
#  Versión:
#      v1.0.0 — Implementación inicial de la Configuración de Seguridad.
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
#      - Este archivo es crítico para la protección del ecosistema.
#      - No insertar lógica de módulos aquí. Solo configuración y parámetros.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DE CONFIGURACIÓN DE SEGURIDAD
# =============================================================================

class SecurityConfig:
    """
    Configuración de Seguridad del ecosistema LINCAT.

    Administra parámetros globales de seguridad industrial.
    """

    def __init__(self):
        print(">>> Cargando Configuración de Seguridad...")

        # Estado general de seguridad
        self.modo_seguro = True
        self.auditoria = True
        self.proteger_hardware = True
        self.proteger_simulacion = True

        # Niveles de seguridad
        self.niveles = {
            "bajo": {
                "restricciones": False,
                "auditoria": False,
                "proteccion_hardware": False
            },
            "medio": {
                "restricciones": True,
                "auditoria": True,
                "proteccion_hardware": True
            },
            "alto": {
                "restricciones": True,
                "auditoria": True,
                "proteccion_hardware": True,
                "bloqueo_critico": True
            }
        }

        # Nivel actual
        self.nivel_actual = "medio"

        # Configuración de permisos
        self.permisos = {
            "modificar_config": False,
            "modificar_hardware": False,
            "modificar_simulacion": False,
            "ejecutar_cnc": True,
            "ejecutar_flow": True
        }

        print(">>> Configuración de Seguridad cargada correctamente.")

    # -------------------------------------------------------------------------
    def set_nivel(self, nivel: str):
        """
        Establece el nivel de seguridad del sistema.
        """

        if nivel not in self.niveles:
            raise ValueError(f"Nivel de seguridad inválido: {nivel}")

        self.nivel_actual = nivel
        print(f"    [+] Nivel de seguridad actualizado: {nivel}")

    # -------------------------------------------------------------------------
    def get_nivel(self):
        """
        Obtiene el nivel de seguridad actual.
        """

        return self.nivel_actual

    # -------------------------------------------------------------------------
    def set_permiso(self, permiso: str, valor: bool):
        """
        Establece un permiso específico del sistema.
        """

        if permiso not in self.permisos:
            raise ValueError(f"Permiso inválido: {permiso}")

        self.permisos[permiso] = valor
        print(f"    [+] Permiso actualizado: {permiso} = {valor}")

    # -------------------------------------------------------------------------
    def get_permiso(self, permiso: str):
        """
        Obtiene el valor de un permiso específico.
        """

        return self.permisos.get(permiso, None)

    # -------------------------------------------------------------------------
    def resumen(self):
        """
        Retorna un resumen estructurado de la configuración de seguridad.
        """

        return {
            "modo_seguro": self.modo_seguro,
            "auditoria": self.auditoria,
            "proteger_hardware": self.proteger_hardware,
            "proteger_simulacion": self.proteger_simulacion,
            "nivel_actual": self.nivel_actual,
            "niveles": self.niveles,
            "permisos": self.permisos
        }


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de la Configuración de Seguridad")

    sec = SecurityConfig()

    print("Resumen:", sec.resumen())

    sec.set_nivel("alto")
    print("Nuevo nivel:", sec.get_nivel())

    sec.set_permiso("modificar_config", True)
    print("Permiso modificar_config:", sec.get_permiso("modificar_config"))
