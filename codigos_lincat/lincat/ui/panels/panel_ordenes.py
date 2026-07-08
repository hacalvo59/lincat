# =============================================================================
#  Programa: panel_ordenes.py
#  Ubicación: lincat/modules/ui/ui_cli/panels/
# =============================================================================
#
#  Propósito:
#      Panel CLI que muestra las órdenes industriales creadas y actualizadas
#      dentro del ecosistema LINCAT. Este panel permite al operador visualizar
#      en tiempo real el flujo de órdenes provenientes del módulo Producción.
#
#  Descripción técnica:
#      - Escucha los eventos:
#            • produccion.orden_creada
#            • produccion.orden_actualizada
#      - Imprime la información en formato CLI.
#      - No publica eventos.
#      - No depende de ningún módulo industrial.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del panel de órdenes.
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


class PanelOrdenes:
    """
    Panel CLI que muestra las órdenes industriales creadas y actualizadas.
    """

    def __init__(self):
        # Suscripciones a eventos del módulo Producción
        bus.suscribir("produccion.orden_creada", self._on_creada)
        bus.suscribir("produccion.orden_actualizada", self._on_actualizada)

    # -------------------------------------------------------------------------
    def _on_creada(self, datos: dict):
        """
        Callback que imprime una orden recién creada.

        Parámetros:
            datos (dict): Información de la orden creada.
        """

        print(f"\n[ORDEN] Creada → {datos['id']} | {datos['descripcion']}\n")

    # -------------------------------------------------------------------------
    def _on_actualizada(self, datos: dict):
        """
        Callback que imprime una orden actualizada.

        Parámetros:
            datos (dict): Información de la orden actualizada.
        """

        print(f"\n[ORDEN] Actualizada → {datos['id']} | Estado={datos['estado']}\n")
