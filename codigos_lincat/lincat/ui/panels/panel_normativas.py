# =============================================================================
#  Programa: panel_normativas.py
#  Ubicación: lincat/modules/ui/ui_cli/panels/
# =============================================================================
#
#  Propósito:
#      Panel CLI que muestra las validaciones normativas realizadas por el
#      módulo Normativas del ecosistema LINCAT. Permite al operador visualizar
#      en tiempo real si los distintos módulos cumplen o no las normas
#      industriales establecidas.
#
#  Descripción técnica:
#      - Escucha el evento normativas.norma_validada.
#      - Imprime el resultado de la validación normativa.
#      - No publica eventos.
#      - No depende de ningún módulo industrial.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del panel de normativas.
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


class PanelNormativas:
    """
    Panel CLI que muestra las validaciones normativas del ecosistema LINCAT.
    """

    def __init__(self):
        # Suscripción al evento de validación normativa
        bus.suscribir("normativas.norma_validada", self._on_validada)

    # -------------------------------------------------------------------------
    def _on_validada(self, datos: dict):
        """
        Callback que imprime el resultado de una validación normativa.

        Parámetros:
            datos (dict): Información de la validación normativa.
        """

        modulo = datos["modulo"]
        cumple = "OK" if datos["cumple"] else "NO CUMPLE"

        print(f"\n[NORMATIVAS] Módulo={modulo} → Estado={cumple}\n")
