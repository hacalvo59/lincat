# =============================================================================
#  Programa: panel_ordenes_tui.py
#  Ubicación: lincat/modules/ui/ui_tui/panels/
# =============================================================================
#
#  Propósito:
#      Panel TUI que muestra las órdenes industriales creadas y actualizadas
#      dentro del ecosistema LINCAT, utilizando curses.
#
#  Descripción técnica:
#      - Escucha los eventos:
#            • produccion.orden_creada
#            • produccion.orden_actualizada
#      - Dibuja la información en una región fija de la pantalla.
#      - No publica eventos.
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del panel de órdenes TUI.
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


class PanelOrdenesTUI:
    """
    Panel TUI que muestra las órdenes industriales creadas y actualizadas.
    """

    def __init__(self, stdscr, y_base: int = 8, x_base: int = 2):
        self.stdscr = stdscr
        self.y_base = y_base
        self.x_base = x_base

        # Suscripciones a eventos del módulo Producción
        bus.suscribir("produccion.orden_creada", self._on_creada)
        bus.suscribir("produccion.orden_actualizada", self._on_actualizada)

    # -------------------------------------------------------------------------
    def _on_creada(self, datos: dict):
        """
        Callback que dibuja una orden recién creada en la TUI.
        """

        texto = f"Creada → {datos['id']} | {datos['descripcion']}"
        self.stdscr.addstr(self.y_base + 1, self.x_base, texto)
        self.stdscr.refresh()

    # -------------------------------------------------------------------------
    def _on_actualizada(self, datos: dict):
        """
        Callback que dibuja una orden actualizada en la TUI.
        """

        texto = f"Actualizada → {datos['id']} | Estado={datos['estado']}"
        self.stdscr.addstr(self.y_base + 2, self.x_base, texto)
        self.stdscr.refresh()
