# =============================================================================
#  Programa: lincattui_advanced.py
#  Ubicación: lincat/modules/ui/ui_tui/
# =============================================================================
#
#  Propósito:
#      Implementar una TUI avanzada tipo tablero industrial para LINCAT,
#      utilizando curses con múltiples ventanas, bordes y refresco dinámico.
#
#  Descripción técnica:
#      - Usa ui.py como backend de interfaz.
#      - Crea ventanas independientes para cada panel.
#      - Mantiene teclas rápidas F1/F2/F3/Q.
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Versión inicial TUI avanzada LINCAT.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
# =============================================================================


import curses
from lincat.modules.ui.ui import LincatUI

from lincat.modules.ui.ui_tui.panels.panel_estado_tui import PanelEstadoTUI
from lincat.modules.ui.ui_tui.panels.panel_ordenes_tui import PanelOrdenesTUI
from lincat.modules.ui.ui_tui.panels.panel_normativas_tui import PanelNormativasTUI
from lincat.modules.ui.ui_tui.panels.panel_maestro_tui import PanelMaestroTUI


class LincatTUIAdvanced:
    """
    TUI avanzada del ecosistema LINCAT con múltiples ventanas.
    """

    def __init__(self):
        self.ui = LincatUI()

        self.win_header = None
        self.win_planta = None
        self.win_ordenes = None
        self.win_normativas = None
        self.win_maestro = None

        self.panel_estado = None
        self.panel_ordenes = None
        self.panel_normativas = None
        self.panel_maestro = None

    # -------------------------------------------------------------------------
    def _crear_ventanas(self, stdscr):
        max_y, max_x = stdscr.getmaxyx()

        # Header
        self.win_header = curses.newwin(3, max_x, 0, 0)

        # Altura disponible para paneles
        altura_paneles = max_y - 3
        alto_panel = altura_paneles // 4

        self.win_planta = curses.newwin(alto_panel, max_x, 3, 0)
        self.win_ordenes = curses.newwin(alto_panel, max_x, 3 + alto_panel, 0)
        self.win_normativas = curses.newwin(alto_panel, max_x, 3 + 2 * alto_panel, 0)
        self.win_maestro = curses.newwin(altura_paneles - 3 * alto_panel, max_x,
                                         3 + 3 * alto_panel, 0)

    # -------------------------------------------------------------------------
    def _dibujar_header(self):
        self.win_header.clear()
        self.win_header.border()
        self.win_header.addstr(1, 2, "LINCAT TUI Avanzada — F1 Iniciar  F2 Detener  F3 Estado  Q Salir",
                               curses.A_BOLD)
        self.win_header.refresh()

    # -------------------------------------------------------------------------
    def _dibujar_paneles(self):
        # Planta
        self.win_planta.clear()
        self.win_planta.border()
        self.win_planta.addstr(0, 2, "Panel Planta")
        self.win_planta.refresh()

        # Órdenes
        self.win_ordenes.clear()
        self.win_ordenes.border()
        self.win_ordenes.addstr(0, 2, "Panel Órdenes")
        self.win_ordenes.refresh()

        # Normativas
        self.win_normativas.clear()
        self.win_normativas.border()
        self.win_normativas.addstr(0, 2, "Panel Normativas")
        self.win_normativas.refresh()

        # Maestro
        self.win_maestro.clear()
        self.win_maestro.border()
        self.win_maestro.addstr(0, 2, "Panel Maestro")
        self.win_maestro.refresh()

        # Crear paneles TUI sobre ventanas
        self.panel_estado = PanelEstadoTUI(self.win_planta, y_base=1, x_base=2)
        self.panel_ordenes = PanelOrdenesTUI(self.win_ordenes, y_base=1, x_base=2)
        self.panel_normativas = PanelNormativasTUI(self.win_normativas, y_base=1, x_base=2)
        self.panel_maestro = PanelMaestroTUI(self.win_maestro, y_base=1, x_base=2)

    # -------------------------------------------------------------------------
    def _loop_teclas(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(False)

        self._crear_ventanas(stdscr)
        self._dibujar_header()
        self._dibujar_paneles()

        while True:
            tecla = stdscr.getch()

            if tecla == curses.KEY_F1:
                self.ui.enviar_accion_usuario("iniciar", {})
            elif tecla == curses.KEY_F2:
                self.ui.enviar_accion_usuario("detener", {})
            elif tecla == curses.KEY_F3:
                self.ui.enviar_accion_usuario("estado", {})
            elif tecla in (ord('q'), ord('Q')):
                break

    # -------------------------------------------------------------------------
    def ejecutar(self):
        curses.wrapper(self._loop_teclas)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL
# =============================================================================

if __name__ == "__main__":
    tui = LincatTUIAdvanced()
    tui.ejecutar()
