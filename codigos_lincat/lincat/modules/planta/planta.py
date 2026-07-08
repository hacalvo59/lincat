# =============================================================================
#  Programa: planta.py
#  Ubicación: codigos_lincat/lincat/modules/planta/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo Planta del ecosistema LINCAT.
#      Su función es reaccionar a las órdenes industriales creadas o
#      actualizadas por Producción y actualizar el estado de las máquinas.
#
#  Descripción técnica:
#      - Suscripción a produccion.orden_creada.
#      - Suscripción a produccion.orden_actualizada.
#      - Actualización del estado de máquinas.
#      - Publicación del evento planta.maquina_estado.
#      - Totalmente desacoplado del resto del ecosistema.
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


class LincatPlanta:
    """
    Módulo Planta del ecosistema LINCAT.

    Actualiza el estado de las máquinas en función de las órdenes industriales.
    """

    def __init__(self):
        print(">>> Módulo Planta inicializado.")

        self.maquinas = {}

        # Suscripciones a Producción
        bus.suscribir("produccion.orden_creada", self._orden_creada)
        bus.suscribir("produccion.orden_actualizada", self._orden_actualizada)

    # -------------------------------------------------------------------------
    def _orden_creada(self, datos: dict):
        """
        Callback que reacciona a una orden creada.

        Parámetros:
            datos (dict): Información de la orden creada.
        """

        id_orden = datos["id"]
        print(f"    [PLANTA] Orden creada recibida: {id_orden}")

        # Simulación: asignar máquina a la orden
        maquina = self._asignar_maquina(id_orden)

        estado = {
            "maquina": maquina,
            "orden": id_orden,
            "estado": "asignada"
        }

        print(f"    [+] Máquina asignada: {maquina}")

        # Publicar estado de máquina
        bus.publicar("planta.maquina_estado", estado)

    # -------------------------------------------------------------------------
    def _orden_actualizada(self, datos: dict):
        """
        Callback que reacciona a una orden actualizada.

        Parámetros:
            datos (dict): Información de la orden actualizada.
        """

        id_orden = datos["id"]
        nuevo_estado = datos.get("estado", "desconocido")

        print(f"    [PLANTA] Orden actualizada recibida: {id_orden} → estado={nuevo_estado}")

        maquina = self.maquinas.get(id_orden, "sin_asignar")

        estado = {
            "maquina": maquina,
            "orden": id_orden,
            "estado": nuevo_estado
        }

        # Publicar estado de máquina
        bus.publicar("planta.maquina_estado", estado)

    # -------------------------------------------------------------------------
    def _asignar_maquina(self, id_orden: str) -> str:
        """
        Simula la asignación de una máquina a una orden.

        Parámetros:
            id_orden (str): Identificador de la orden.

        Retorna:
            str: Nombre de la máquina asignada.
        """

        maquina = f"MAQ-{id_orden[-3:]}"  # Ejemplo industrial
        self.maquinas[id_orden] = maquina
        return maquina


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo Planta")

    planta = LincatPlanta()

    # Simular eventos de Producción
    bus.publicar("produccion.orden_creada", {
        "id": "ORD001",
        "descripcion": "Mecanizado pieza A"
    })

    bus.publicar("produccion.orden_actualizada", {
        "id": "ORD001",
        "estado": "en_proceso"
    })
