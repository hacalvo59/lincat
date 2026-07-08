# =============================================================================
#  Programa: lincattui.py
#  Ubicación: lincat/modules/ui/ui_tui/
# =============================================================================
#
#  Propósito:
#      Implementar la Interfaz de Usuario en modo Texto (TUI) del ecosistema
#      LINCAT, utilizando la librería curses. La TUI permite al operador
#      visualizar información en paneles y enviar acciones mediante teclas
#      rápidas, manteniendo una interacción industrial fluida.
#
#  Descripción técnica:
#      - La lógica de interfaz está en ui.py (backend de UI).
#      - Este archivo implementa la interfaz visual en modo texto.
#      - Traduce teclas en eventos ui.evento_usuario.
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado del ecosistema.
#
#  Paneles integrados:
#      • PanelEstadoTUI
#      • PanelOrdenesTUI
#      • PanelNormativasTUI
#      • PanelMaestroTUI
#
#  Versión:
#      v2.0.0 — Versión estable con paneles TUI integrados.
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

# Paneles TUI
from lincat.modules.ui.ui_tui.panels.panel_estado_tui import PanelEstadoTUI
from lincat.modules.ui.ui_tui.panels.panel_ordenes_tui import PanelOrdenesTUI
from lincat.modules.ui.ui_tui.panels.panel_normativas_tui import PanelNormativasTUI
from lincat.modules.ui.ui_tui.panels.panel_maestro_tui import PanelMaestroTUI


class LincatTUI:
    """
    Interfaz TUI del ecosistema LINCAT.
    """

    def __init__(self):
        self.ui = LincatUI()

        # Paneles TUI (se inicializan en _dibujar_layout)
        self.panel_estado = None
        self.panel_ordenes = None
        self.panel_normativas = None
        self.panel_maestro = None

    # -------------------------------------------------------------------------
    def _dibujar_layout(self, stdscr):
        """
        Dibuja el layout principal de la TUI y crea los paneles.
        """

        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        stdscr.addstr(0, 2, "LINCAT TUI — Ecosistema Industrial", curses.A_BOLD)
        stdscr.addstr(2, 2, "[F1] Iniciar  [F2] Detener  [F3] Estado  [Q] Salir")

        # Títulos de paneles
        stdscr.addstr(4, 2, "Panel Planta:")
        stdscr.addstr(8, 2, "Panel Órdenes:")
        stdscr.addstr(12, 2, "Panel Normativas:")
        stdscr.addstr(16, 2, "Panel Maestro:")

        stdscr.refresh()

        # Crear paneles TUI
        self.panel_estado = PanelEstadoTUI(stdscr, y_base=4, x_base=2)
        self.panel_ordenes = PanelOrdenesTUI(stdscr, y_base=8, x_base=2)
        self.panel_normativas = PanelNormativasTUI(stdscr, y_base=12, x_base=2)
        self.panel_maestro = PanelMaestroTUI(stdscr, y_base=16, x_base=2)

    # -------------------------------------------------------------------------
    def _loop_teclas(self, stdscr):
        """
        Loop principal de captura de teclas.
        """

        curses.curs_set(0)
        stdscr.nodelay(False)

        # Dibujar layout y paneles
        self._dibujar_layout(stdscr)

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
        """
        Ejecuta la TUI utilizando curses.wrapper.
        """

        curses.wrapper(self._loop_teclas)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL
# =============================================================================

if __name__ == "__main__":
    tui = LincatTUI()
    tui.ejecutar()
