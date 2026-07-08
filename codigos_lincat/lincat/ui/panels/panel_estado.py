# =============================================================================
#  Programa: panel_estado.py
#  Ubicación: lincat/modules/ui/ui_cli/panels/
# =============================================================================
#
#  Propósito:
#      Panel CLI que muestra el estado de las máquinas de la planta industrial.
#      Este panel escucha eventos del bus LINCAT.bus y presenta la información
#      en formato textual para el operador humano.
#
#  Descripción técnica:
#      - Escucha el evento planta.maquina_estado.
#      - Imprime el estado de la máquina asignada a una orden.
#      - No publica eventos.
#      - No depende de ningún módulo industrial.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del panel de estado de planta.
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


class PanelEstadoPlanta:
    """
    Panel CLI que muestra el estado de las máquinas de la planta industrial.
    """

    def __init__(self):
        # Suscripción al evento de estado de máquina
        bus.suscribir("planta.maquina_estado", self._on_estado)

    # -------------------------------------------------------------------------
    def _on_estado(self, datos: dict):
        """
        Callback que imprime el estado de una máquina cuando Planta publica
        el evento planta.maquina_estado.

        Parámetros:
            datos (dict): Información del estado de la máquina.
        """

        maquina = datos["maquina"]
        orden = datos["orden"]
        estado = datos["estado"]

        print(f"\n[PLANTA] Máquina={maquina} | Orden={orden} | Estado={estado}\n")
