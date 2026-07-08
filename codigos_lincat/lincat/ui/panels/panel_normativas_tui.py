# =============================================================================
#  Programa: panel_normativas_tui.py
#  Ubicación: lincat/modules/ui/ui_tui/panels/
# =============================================================================
#
#  Propósito:
#      Panel TUI que muestra las validaciones normativas realizadas por el
#      módulo Normativas del ecosistema LINCAT, utilizando curses.
#
#  Descripción técnica:
#      - Escucha el evento normativas.norma_validada.
#      - Dibuja el resultado de la validación normativa en una región fija.
#      - No publica eventos.
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del panel de normativas TUI.
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


class PanelNormativasTUI:
    """
    Panel TUI que muestra las validaciones normativas del ecosistema LINCAT.
    """

    def __init__(self, stdscr, y_base: int = 12, x_base: int = 2):
        self.stdscr = stdscr
        self.y_base = y_base
        self.x_base = x_base

        # Suscripción al evento de validación normativa
        bus.suscribir("normativas.norma_validada", self._on_validada)

    # -------------------------------------------------------------------------
    def _on_validada(self, datos: dict):
        """
        Callback que dibuja el resultado de una validación normativa.
        """

        modulo = datos["modulo"]
        cumple = "OK" if datos["cumple"] else "NO CUMPLE"

        texto = f"{modulo} → {cumple}"
        self.stdscr.addstr(self.y_base + 1, self.x_base, texto)
        self.stdscr.refresh()
