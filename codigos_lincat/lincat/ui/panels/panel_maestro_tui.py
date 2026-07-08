# =============================================================================
#  Programa: panel_maestro_tui.py
#  Ubicación: lincat/modules/ui/ui_tui/panels/
# =============================================================================
#
#  Propósito:
#      Panel TUI que muestra los comandos emitidos por el Módulo Maestro del
#      ecosistema LINCAT, utilizando curses.
#
#  Descripción técnica:
#      - Escucha los eventos:
#            • maestro.comando_iniciar_proceso
#            • maestro.comando_detener_proceso
#      - Dibuja la información en una región fija de la pantalla.
#      - No publica eventos.
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del panel Maestro TUI.
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


class PanelMaestroTUI:
    """
    Panel TUI que muestra los comandos emitidos por el Módulo Maestro.
    """

    def __init__(self, stdscr, y_base: int = 16, x_base: int = 2):
        self.stdscr = stdscr
        self.y_base = y_base
        self.x_base = x_base

        # Suscripciones a los comandos del Maestro
        bus.suscribir("maestro.comando_iniciar_proceso", self._on_comando)
        bus.suscribir("maestro.comando_detener_proceso", self._on_comando)

    # -------------------------------------------------------------------------
    def _on_comando(self, datos: dict):
        """
        Callback que dibuja un comando emitido por Maestro.
        """

        texto = f"Comando Maestro → {datos}"
        self.stdscr.addstr(self.y_base + 1, self.x_base, texto)
        self.stdscr.refresh()
