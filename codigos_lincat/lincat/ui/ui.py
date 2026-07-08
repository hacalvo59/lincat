# =============================================================================
#  Programa: ui.py
#  Ubicación: codigos_lincat/lincat/modules/ui/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo UI del ecosistema LINCAT.
#      Su función es actuar como interfaz de usuario, observando eventos
#      del bus LINCAT.bus y publicando acciones del operador.
#
#  Descripción técnica:
#      - Suscripción a eventos de Planta, Producción, Normativas y Maestro.
#      - Publicación del evento ui.evento_usuario.
#      - Totalmente desacoplado del resto del ecosistema.
#
#  Versión:
#      v2.0.0 — Integración con LINCAT.bus v2.
#
# =============================================================================


from lincat.core.core_bus import bus


class LincatUI:
    """
    Módulo UI del ecosistema LINCAT.

    Observa el estado del sistema y publica acciones del operador.
    """

    def __init__(self):
        print(">>> Módulo UI inicializado.")

        # Suscripciones a eventos relevantes
        bus.suscribir("planta.maquina_estado", self._on_maquina_estado)
        bus.suscribir("produccion.orden_creada", self._on_orden_creada)
        bus.suscribir("produccion.orden_actualizada", self._on_orden_actualizada)
        bus.suscribir("normativas.norma_validada", self._on_norma_validada)
        bus.suscribir("maestro.comando_iniciar_proceso", self._on_comando_maestro)
        bus.suscribir("maestro.comando_detener_proceso", self._on_comando_maestro)

    # -------------------------------------------------------------------------
    def _on_maquina_estado(self, datos: dict):
        print(f"    [UI] Estado máquina → {datos['maquina']} | orden={datos['orden']} | estado={datos['estado']}")

    # -------------------------------------------------------------------------
    def _on_orden_creada(self, datos: dict):
        print(f"    [UI] Orden creada → {datos['id']} | {datos['descripcion']}")

    # -------------------------------------------------------------------------
    def _on_orden_actualizada(self, datos: dict):
        print(f"    [UI] Orden actualizada → {datos['id']} | estado={datos['estado']}")

    # -------------------------------------------------------------------------
    def _on_norma_validada(self, datos: dict):
        estado = "OK" if datos["cumple"] else "NO CUMPLE"
        print(f"    [UI] Validación normativa → módulo={datos['modulo']} | estado={estado}")

    # -------------------------------------------------------------------------
    def _on_comando_maestro(self, datos: dict):
        print(f"    [UI] Comando Maestro → {datos}")

    # -------------------------------------------------------------------------
    def enviar_accion_usuario(self, accion: str, parametros: dict = None):
        """
        Publica un evento generado por el operador humano.

        Parámetros:
            accion (str): Acción del operador.
            parametros (dict): Datos adicionales.
        """

        evento = {
            "accion": accion,
            "parametros": parametros or {}
        }

        print(f"    [UI] Acción usuario → {accion}")

        bus.publicar("ui.evento_usuario", evento)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo UI")

    ui = LincatUI()

    # Simular acción del operador
    ui.enviar_accion_usuario("iniciar_proceso", {"orden": "ORD001"})
