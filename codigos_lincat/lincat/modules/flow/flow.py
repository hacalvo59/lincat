# =============================================================================
#  Programa: seguridad.py
#  Ubicación: codigos_lincat/lincat/modules/seguridad/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo Seguridad del ecosistema LINCAT.
#      Su función es validar enclavamientos y condiciones de seguridad
#      reaccionando a los pasos ejecutados por FLOW mediante el bus LINCAT.bus.
#
#  Descripción técnica:
#      - Suscripción al evento flow.paso_ejecutado.
#      - Validación de enclavamientos industriales.
#      - Publicación del evento seguridad.enclavamiento_fallo.
#      - Totalmente desacoplado del resto del ecosistema.
#
#  Versión:
#      v2.0.0 — Integración con LINCAT.bus v2.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
# =============================================================================


from lincat.core.core_bus import bus


class LincatSeguridad:
    """
    Módulo Seguridad del ecosistema LINCAT.

    Valida enclavamientos y condiciones de seguridad.
    """

    def __init__(self):
        print(">>> Módulo Seguridad inicializado.")

        # Suscribirse a los pasos ejecutados por FLOW
        bus.suscribir("flow.paso_ejecutado", self._validar_paso)

    # -------------------------------------------------------------------------
    def _validar_paso(self, datos: dict):
        """
        Callback que valida un paso ejecutado por FLOW.

        Parámetros:
            datos (dict): Información del paso ejecutado.
        """

        paso = datos["paso"]
        print(f"    [SEGURIDAD] Validando paso: {paso}")

        # Simulación de validación industrial
        if self._fallo_enclavamiento(paso):
            print("    [!] FALLO DE SEGURIDAD DETECTADO")
            bus.publicar("seguridad.enclavamiento_fallo", {
                "paso": paso,
                "motivo": "Enclavamiento no cumplido"
            })
        else:
            print("    [+] Paso validado sin fallos de seguridad.")

    # -------------------------------------------------------------------------
    def _fallo_enclavamiento(self, paso: str) -> bool:
        """
        Simula un fallo de enclavamiento para ciertos pasos.

        Parámetros:
            paso (str): Nombre del paso.

        Retorna:
            bool: True si hay fallo, False si no.
        """

        # Ejemplo industrial: ciertos pasos requieren enclavamiento
        pasos_riesgo = ["activar_valvula", "iniciar_mecanizado"]

        return paso in pasos_riesgo


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo Seguridad")

    seg = LincatSeguridad()

    # Simular un paso ejecutado por FLOW
    bus.publicar("flow.paso_ejecutado", {
        "paso": "activar_valvula",
        "parametros": {"tiempo": 2}
    })
