# =============================================================================
#  Programa: produccion.py
#  Ubicación: codigos_lincat/lincat/modules/produccion/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo Producción del ecosistema LINCAT.
#      Su función es crear y actualizar órdenes industriales y publicarlas
#      en el bus LINCAT.bus para que otros módulos reaccionen (Planta, Maestro, UI).
#
#  Descripción técnica:
#      - Publicación de eventos produccion.orden_creada.
#      - Publicación de eventos produccion.orden_actualizada.
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


class LincatProduccion:
    """
    Módulo Producción del ecosistema LINCAT.

    Crea y actualiza órdenes industriales.
    """

    def __init__(self):
        print(">>> Módulo Producción inicializado.")
        self.ordenes = {}

    # -------------------------------------------------------------------------
    def crear_orden(self, id_orden: str, descripcion: str, parametros: dict = None) -> dict:
        """
        Crea una orden industrial.

        Parámetros:
            id_orden (str): Identificador único de la orden.
            descripcion (str): Descripción de la orden.
            parametros (dict): Parámetros opcionales.

        Retorna:
            dict: Datos de la orden creada.
        """

        orden = {
            "id": id_orden,
            "descripcion": descripcion,
            "parametros": parametros or {},
            "estado": "creada"
        }

        self.ordenes[id_orden] = orden

        print(f"    [+] Orden creada: {id_orden}")

        # Publicar evento en el bus
        bus.publicar("produccion.orden_creada", orden)

        return orden

    # -------------------------------------------------------------------------
    def actualizar_orden(self, id_orden: str, cambios: dict) -> dict:
        """
        Actualiza una orden industrial.

        Parámetros:
            id_orden (str): Identificador de la orden.
            cambios (dict): Cambios a aplicar.

        Retorna:
            dict: Orden actualizada.
        """

        if id_orden not in self.ordenes:
            raise ValueError(f"La orden '{id_orden}' no existe.")

        self.ordenes[id_orden].update(cambios)

        print(f"    [+] Orden actualizada: {id_orden}")

        # Publicar evento en el bus
        bus.publicar("produccion.orden_actualizada", self.ordenes[id_orden])

        return self.ordenes[id_orden]


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo Producción")

    prod = LincatProduccion()

    prod.crear_orden("ORD001", "Mecanizado pieza A", {"material": "aluminio"})
    prod.actualizar_orden("ORD001", {"estado": "en_proceso"})
