# =============================================================================
#  Programa: panel_maestro.py
#  Ubicación: lincat/modules/ui/ui_cli/panels/
# =============================================================================
#
#  Propósito:
#      Panel CLI que muestra los comandos emitidos por el Módulo Maestro del
#      ecosistema LINCAT. Permite al operador visualizar en tiempo real las
#      decisiones de orquestación tomadas por Maestro.
#
#  Descripción técnica:
#      - Escucha los eventos:
#            • maestro.comando_iniciar_proceso
#            • maestro.comando_detener_proceso
#      - Imprime la información en formato CLI.
#      - No publica eventos.
#      - No depende de ningún módulo industrial.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del panel Maestro.
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


class PanelMaestro:
    """
    Panel CLI que muestra los comandos emitidos por el Módulo Maestro.
    """

    def __init__(self):
        # Suscripciones a los comandos del Maestro
        bus.suscribir("maestro.comando_iniciar_proceso", self._on_comando)
        bus.suscribir("maestro.comando_detener_proceso", self._on_comando)

    # -------------------------------------------------------------------------
    def _on_comando(self, datos: dict):
        """
        Callback que imprime un comando emitido por Maestro.

        Parámetros:
            datos (dict): Información del comando maestro.
        """

        print(f"\n[MAESTRO] Comando recibido → {datos}\n")
