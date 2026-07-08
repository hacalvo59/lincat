# =============================================================================
#  Programa: ui_tui.py
#  Ubicación: lincat/modules/ui/ui_tui/
# =============================================================================
#
#  Propósito:
#      Implementar la Interfaz de Usuario en modo Texto (TUI) del ecosistema
#      LINCAT, utilizando curses. La TUI permite al operador visualizar
#      información en paneles y enviar acciones mediante teclas.
#
#  Descripción técnica:
#      - La lógica de interfaz está en ui.py (backend de UI).
#      - ui_tui.py dibuja paneles y captura teclas.
#      - Traduce teclas en eventos ui.evento_usuario.
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplada del ecosistema.
#
#  Versión:
#      v1.0.0 — Versión inicial TUI LINCAT.
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


class LincatTUI:
    """
    Interfaz TUI del ecosistema LINCAT.
    """

    def __init__(self):
        self.ui = LincatUI()

    # -------------------------------------------------------------------------
    def _dibujar_layout(self, stdscr):
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        stdscr.addstr(0, 2, "LINCAT TUI — Ecosistema Industrial", curses.A_BOLD)
        stdscr.addstr(2, 2, "[F1] Iniciar  [F2] Detener  [F3] Estado  [Q] Salir")

        stdscr.addstr(4, 2, "Panel Planta:")
        stdscr.addstr(8, 2, "Panel Órdenes:")
        stdscr.addstr(12, 2, "Panel Normativas:")
        stdscr.addstr(16, 2, "Panel Maestro:")

        stdscr.refresh()

    # -------------------------------------------------------------------------
    def _loop_teclas(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(False)
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
        curses.wrapper(self._loop_teclas)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL
# =============================================================================

if __name__ == "__main__":
    tui = LincatTUI()
    tui.ejecutar()
