# =============================================================================
#  Programa: maestro.py
#  Ubicación: codigos_lincat/lincat/modules/maestro/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo Maestro del ecosistema LINCAT.
#      Su función es orquestar el comportamiento global del sistema
#      reaccionando a eventos del bus LINCAT.bus y publicando comandos.
#
#  Descripción técnica:
#      - Suscripción a eventos de CAM, CNC, FLOW, Seguridad, Producción y Planta.
#      - Publicación de comandos maestro.* para coordinar el ecosistema.
#      - Totalmente desacoplado del resto de los módulos.
#
#  Versión:
#      v2.0.0 — Integración con LINCAT.bus v2.
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


class LincatMaestro:
    """
    Módulo Maestro del ecosistema LINCAT.

    Orquesta el comportamiento global del sistema.
    """

    def __init__(self):
        print(">>> Módulo Maestro inicializado.")

        # Suscripciones a eventos clave del ecosistema
        bus.suscribir("cam.trayectoria_generada", self._on_trayectoria_generada)
        bus.suscribir("cnc.movimiento_ejecutado", self._on_movimiento_ejecutado)
        bus.suscribir("flow.paso_ejecutado", self._on_paso_ejecutado)
        bus.suscribir("seguridad.enclavamiento_fallo", self._on_fallo_seguridad)
        bus.suscribir("produccion.orden_creada", self._on_orden_creada)
        bus.suscribir("produccion.orden_actualizada", self._on_orden_actualizada)
        bus.suscribir("planta.maquina_estado", self._on_maquina_estado)

    # -------------------------------------------------------------------------
    def _on_trayectoria_generada(self, datos: dict):
        print(f"    [MAESTRO] Trayectoria generada → tipo={datos['tipo']}")
        bus.publicar("maestro.comando_iniciar_proceso", {
            "accion": "iniciar_cnc",
            "trayectoria": datos
        })

    # -------------------------------------------------------------------------
    def _on_movimiento_ejecutado(self, datos: dict):
        print(f"    [MAESTRO] Movimiento ejecutado por CNC → puntos={datos['puntos_ejecutados']}")
        bus.publicar("maestro.comando_iniciar_proceso", {
            "accion": "siguiente_paso_flow"
        })

    # -------------------------------------------------------------------------
    def _on_paso_ejecutado(self, datos: dict):
        print(f"    [MAESTRO] Paso FLOW ejecutado → {datos['paso']}")
        bus.publicar("maestro.comando_iniciar_proceso", {
            "accion": "validar_seguridad",
            "paso": datos["paso"]
        })

    # -------------------------------------------------------------------------
    def _on_fallo_seguridad(self, datos: dict):
        print(f"    [MAESTRO] FALLO DE SEGURIDAD → paso={datos['paso']}")
        bus.publicar("maestro.comando_detener_proceso", {
            "motivo": "fallo_seguridad",
            "paso": datos["paso"]
        })

    # -------------------------------------------------------------------------
    def _on_orden_creada(self, datos: dict):
        print(f"    [MAESTRO] Orden creada → {datos['id']}")
        bus.publicar("maestro.comando_iniciar_proceso", {
            "accion": "asignar_maquina",
            "orden": datos["id"]
        })

    # -------------------------------------------------------------------------
    def _on_orden_actualizada(self, datos: dict):
        print(f"    [MAESTRO] Orden actualizada → {datos['id']} estado={datos['estado']}")
        bus.publicar("maestro.comando_iniciar_proceso", {
            "accion": "sincronizar_planta",
            "orden": datos["id"],
            "estado": datos["estado"]
        })

    # -------------------------------------------------------------------------
    def _on_maquina_estado(self, datos: dict):
        print(f"    [MAESTRO] Estado de máquina → {datos['maquina']} orden={datos['orden']} estado={datos['estado']}")
        bus.publicar("maestro.comando_iniciar_proceso", {
            "accion": "actualizar_ui",
            "maquina": datos["maquina"],
            "orden": datos["orden"],
            "estado": datos["estado"]
        })


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo Maestro")

    maestro = LincatMaestro()

    # Simular un evento de CAM
    bus.publicar("cam.trayectoria_generada", {
        "tipo": "contour",
        "puntos": [(0, 0), (10, 0)]
    })
