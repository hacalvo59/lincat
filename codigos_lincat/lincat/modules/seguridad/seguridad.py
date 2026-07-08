# =============================================================================
#  Programa: seguridad.py
#  Ubicación: codigos_lincat/lincat/modules/seguridad/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo de Seguridad Industrial del ecosistema
#      LINCAT. Su función es supervisar enclavamientos, permisos, auditorías,
#      estados críticos y condiciones de operación segura.
#
#  Descripción técnica:
#      - Administra enclavamientos industriales.
#      - Supervisa estados de módulos críticos (CNC‑CAT, EtherCAT, FLOW).
#      - Proporciona auditoría de eventos y fallos.
#      - Permite activar modos seguros y bloqueos críticos.
#      - Se integra con Maestro, HardwareConfig y SimulationConfig.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Módulo Seguridad.
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
#      - No insertar lógica de hardware aquí. Solo administración y control.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DEL MÓDULO SEGURIDAD
# =============================================================================

class LincatSeguridad:
    """
    Módulo de Seguridad Industrial del ecosistema LINCAT.

    Supervisa enclavamientos, permisos, auditorías y estados críticos.
    """

    def __init__(self):
        print(">>> Módulo Seguridad inicializado.")

        # Estado del módulo
        self.estado = "ok"  # ok / warning / error / bloqueo

        # Enclavamientos industriales
        self.enclavamientos = {}

        # Auditoría de eventos
        self.auditoria = []

        # Permisos del sistema
        self.permisos = {
            "ejecutar_cnc": True,
            "ejecutar_flow": True,
            "modificar_config": False,
            "modificar_hardware": False,
            "modificar_simulacion": False
        }

        # Modo seguro
        self.modo_seguro = True

        # Bloqueo crítico
        self.bloqueo_critico = False

    # -------------------------------------------------------------------------
    def registrar_enclavamiento(self, nombre: str, condicion):
        """
        Registra un enclavamiento industrial.

        Parámetros:
            nombre (str): Nombre del enclavamiento.
            condicion: Función que retorna True/False.
        """

        self.enclavamientos[nombre] = condicion
        print(f"    [+] Enclavamiento registrado: {nombre}")

    # -------------------------------------------------------------------------
    def verificar_enclavamientos(self):
        """
        Verifica todos los enclavamientos industriales.

        Retorna:
            True si todos los enclavamientos están OK.
            False si alguno falla.
        """

        print("    [>] Verificando enclavamientos industriales...")

        for nombre, condicion in self.enclavamientos.items():
            if not condicion():
                self.estado = "error"
                self.bloqueo_critico = True
                self.registrar_evento(f"Fallo en enclavamiento: {nombre}")
                print(f"    [!] Enclavamiento falló: {nombre}")
                return False

        print("    [+] Todos los enclavamientos OK.")
        return True

    # -------------------------------------------------------------------------
    def registrar_evento(self, descripcion: str):
        """
        Registra un evento en la auditoría.
        """

        self.auditoria.append(descripcion)
        print(f"    [AUDITORÍA] {descripcion}")

    # -------------------------------------------------------------------------
    def verificar_permiso(self, permiso: str):
        """
        Verifica si un permiso está habilitado.
        """

        return self.permisos.get(permiso, False)

    # -------------------------------------------------------------------------
    def activar_modo_seguro(self):
        """
        Activa el modo seguro del sistema.
        """

        self.modo_seguro = True
        self.registrar_evento("Modo seguro activado.")
        print("    [+] Modo seguro activado.")

    # -------------------------------------------------------------------------
    def desactivar_modo_seguro(self):
        """
        Desactiva el modo seguro del sistema.
        """

        self.modo_seguro = False
        self.registrar_evento("Modo seguro desactivado.")
        print("    [+] Modo seguro desactivado.")

    # -------------------------------------------------------------------------
    def estado_actual(self):
        """
        Retorna el estado actual del módulo Seguridad.
        """

        return {
            "estado": self.estado,
            "modo_seguro": self.modo_seguro,
            "bloqueo_critico": self.bloqueo_critico,
            "permisos": self.permisos,
            "auditoria": self.auditoria
        }


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo Seguridad")

    seg = LincatSeguridad()

    # Registrar enclavamiento
    seg.registrar_enclavamiento("presion_ok", lambda: True)
    seg.registrar_enclavamiento("temperatura_ok", lambda: False)

    # Verificar enclavamientos
    seg.verificar_enclavamientos()

    # Activar modo seguro
    seg.activar_modo_seguro()

    print("Estado final:", seg.estado_actual())
