# =============================================================================
#  Programa: normativas.py
#  Ubicación: codigos_lincat/lincat/modules/normativas/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo Normativas del ecosistema LINCAT.
#      Su función es validar el cumplimiento normativo reaccionando a eventos
#      del bus LINCAT.bus y publicar resultados de auditoría.
#
#  Descripción técnica:
#      - Suscripción a eventos de Seguridad, Planta y Producción.
#      - Validación de cumplimiento normativo.
#      - Publicación del evento normativas.norma_validada.
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


class LincatNormativas:
    """
    Módulo Normativas del ecosistema LINCAT.

    Valida cumplimiento normativo en tiempo real.
    """

    def __init__(self):
        print(">>> Módulo Normativas inicializado.")

        # Suscripciones a eventos relevantes
        bus.suscribir("seguridad.enclavamiento_fallo", self._on_fallo_seguridad)
        bus.suscribir("planta.maquina_estado", self._on_maquina_estado)
        bus.suscribir("produccion.orden_creada", self._on_orden_creada)
        bus.suscribir("produccion.orden_actualizada", self._on_orden_actualizada)

    # -------------------------------------------------------------------------
    def _on_fallo_seguridad(self, datos: dict):
        print(f"    [NORMATIVAS] Fallo de seguridad detectado → paso={datos['paso']}")
        self._publicar_validacion("seguridad", False, datos)

    # -------------------------------------------------------------------------
    def _on_maquina_estado(self, datos: dict):
        print(f"    [NORMATIVAS] Estado de máquina recibido → {datos['maquina']} estado={datos['estado']}")
        cumple = datos["estado"] not in ["fallo", "detenida"]
        self._publicar_validacion("planta", cumple, datos)

    # -------------------------------------------------------------------------
    def _on_orden_creada(self, datos: dict):
        print(f"    [NORMATIVAS] Orden creada → {datos['id']}")
        self._publicar_validacion("produccion", True, datos)

    # -------------------------------------------------------------------------
    def _on_orden_actualizada(self, datos: dict):
        print(f"    [NORMATIVAS] Orden actualizada → {datos['id']} estado={datos['estado']}")
        cumple = datos["estado"] not in ["rechazada", "bloqueada"]
        self._publicar_validacion("produccion", cumple, datos)

    # -------------------------------------------------------------------------
    def _publicar_validacion(self, modulo: str, cumple: bool, datos: dict):
        """
        Publica el resultado de validación normativa.
        """

        resultado = {
            "modulo": modulo,
            "cumple": cumple,
            "datos": datos
        }

        estado = "cumple" if cumple else "no_cumple"
        print(f"    [+] Validación normativa → {modulo}: {estado}")

        bus.publicar("normativas.norma_validada", resultado)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Módulo Normativas")

    norm = LincatNormativas()

    # Simular un fallo de seguridad
    bus.publicar("seguridad.enclavamiento_fallo", {
        "paso": "activar_valvula",
        "motivo": "Enclavamiento no cumplido"
    })
