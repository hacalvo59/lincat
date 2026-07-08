# =============================================================================
#  Programa: cnc_cat.py
#  Ubicación: codigos_lincat/lincat/modules/cnc_cat/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo CNC‑CAT del ecosistema LINCAT.
#      Su función es ejecutar trayectorias industriales recibidas desde el
#      bus LINCAT.bus y publicar los movimientos ejecutados.
#
#  Descripción técnica:
#      - Suscripción al evento cam.trayectoria_generada.
#      - Ejecución de trayectorias (simulada).
#      - Publicación del evento cnc.movimiento_ejecutado.
#      - Totalmente desacoplado de CAM y otros módulos.
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


class LincatCNC:
    """
    Módulo CNC‑CAT del ecosistema LINCAT.

    Ejecuta trayectorias recibidas desde el bus industrial.
    """

    def __init__(self):
        print(">>> Módulo CNC‑CAT inicializado.")

        # Suscribirse al evento de CAM
        bus.suscribir("cam.trayectoria_generada", self._recibir_trayectoria)

    # -------------------------------------------------------------------------
    def _recibir_trayectoria(self, datos: dict):
        """
        Callback que recibe trayectorias desde CAM.

        Parámetros:
            datos (dict): Datos de la trayectoria generada por CAM.
        """

        print(f"    [CNC] Trayectoria recibida: tipo={datos['tipo']} puntos={len(datos['puntos'])}")

        # Ejecutar trayectoria (simulación)
        resultado = self._ejecutar_trayectoria(datos)

        # Publicar evento de movimiento ejecutado
        bus.publicar("cnc.movimiento_ejecutado", resultado)

    # -------------------------------------------------------------------------
    def _ejecutar_trayectoria(self, trayectoria: dict) -> dict:
        """
        Simula la ejecución de una trayectoria.

        Parámetros:
            trayectoria (dict): Datos de trayectoria.

        Retorna:
            dict: Resultado del movimiento ejecutado.
        """

        print("    [CNC] Ejecutando trayectoria...")

        # Simulación industrial básica
        resultado = {
            "tipo": trayectoria["tipo"],
            "puntos_ejecutados": len(trayectoria["puntos"]),
            "estado": "ok"
        }

        print("    [+] Trayectoria ejecutada correctamente.")

        return resultado


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo CNC‑CAT")

    cnc = LincatCNC()

    # Simular publicación desde CAM
    bus.publicar("cam.trayectoria_generada", {
        "tipo": "contour",
        "puntos": [(0, 0), (10, 0), (10, 10), (0, 10)]
    })
