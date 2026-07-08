# =============================================================================
#  Programa: events.py
#  Ubicación: codigos_lincat/lincat/core/events/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Sistema Global de Eventos del ecosistema
#      LINCAT. Su función es administrar eventos internos del framework
#      industrial, permitiendo que los módulos reaccionen a situaciones
#      específicas del sistema de forma ordenada, segura y determinística.
#
#  Descripción técnica:
#      - Permite registrar eventos internos del sistema.
#      - Permite que los módulos se suscriban a eventos específicos.
#      - Permite emitir eventos y ejecutar sus callbacks asociados.
#      - Garantiza que la reacción del sistema sea predecible y estable.
#      - Es utilizado por bootstrap.py durante la inicialización del framework.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Sistema Global de Eventos.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
#  Licencia:
#      Proyecto de código abierto bajo licencia industrial LINCAT.
#      Uso permitido para fabricantes, ensambladores, universidades,
#      ingenieros, operadores y organizaciones sin fines de lucro.
#
#  Advertencias:
#      - Este archivo es crítico para la reacción interna del ecosistema.
#      - No insertar lógica de módulos aquí. Solo administración de eventos.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DEL SISTEMA GLOBAL DE EVENTOS
# =============================================================================

class EventManager:
    """
    Sistema Global de Eventos del ecosistema LINCAT.

    Permite que los módulos del framework reaccionen a eventos internos.
    Cada evento puede tener múltiples suscriptores (callbacks).
    """

    def __init__(self):
        # Diccionario donde se almacenan los eventos.
        # Clave: nombre del evento
        # Valor: lista de funciones callback
        self._events = {}

        print(">>> Sistema Global de Eventos creado.")

    # -------------------------------------------------------------------------
    def subscribe(self, event_name: str, callback):
        """
        Suscribe una función callback a un evento específico.

        Parámetros:
            event_name (str): Nombre del evento.
            callback: Función que será llamada cuando el evento ocurra.

        Requisitos:
            - El nombre debe ser una cadena.
            - El callback debe ser una función o método válido.
        """

        if not isinstance(event_name, str):
            raise TypeError("El nombre del evento debe ser una cadena de texto.")

        if not callable(callback):
            raise TypeError("El callback debe ser una función o método.")

        if event_name not in self._events:
            self._events[event_name] = []

        self._events[event_name].append(callback)
        print(f"    [+] Suscripción agregada al evento: {event_name}")

    # -------------------------------------------------------------------------
    def emit(self, event_name: str, *args, **kwargs):
        """
        Emite un evento interno del sistema.

        Parámetros:
            event_name (str): Nombre del evento.
            *args, **kwargs: Argumentos que se pasarán a los callbacks.

        Comportamiento:
            - Si el evento existe, se ejecutan todos los callbacks asociados.
            - Si no existe, se ignora silenciosamente.
        """

        callbacks = self._events.get(event_name, [])

        print(f"    [>] Emitiendo evento: {event_name} ({len(callbacks)} suscriptores)")

        for callback in callbacks:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"      [ERROR] Callback falló en evento '{event_name}': {e}")

    # -------------------------------------------------------------------------
    def list_events(self):
        """
        Lista todos los eventos registrados en el sistema.

        Retorna:
            Lista de nombres de eventos registrados.
        """

        return list(self._events.keys())

    # -------------------------------------------------------------------------
    def count(self):
        """
        Retorna la cantidad de eventos registrados.
        """

        return len(self._events)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Sistema Global de Eventos")

    events = EventManager()

    # Callback de prueba
    def test_event(msg):
        print(f"Evento ejecutado: {msg}")

    # Suscripción de prueba
    events.subscribe("arranque_sistema", test_event)

    # Emisión de prueba
    events.emit("arranque_sistema", "LINCAT ha iniciado correctamente.")

    print("Eventos registrados:", events.list_events())
    print("Cantidad:", events.count())
