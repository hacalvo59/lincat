# =============================================================================
#  Programa: signals.py
#  Ubicación: codigos_lincat/lincat/core/signals/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Sistema Global de Señales del ecosistema
#      LINCAT. Su función es permitir la comunicación interna entre los módulos
#      del framework industrial mediante señales estructuradas, seguras y
#      determinísticas.
#
#  Descripción técnica:
#      - Permite emitir señales internas del sistema.
#      - Permite que los módulos se suscriban a señales específicas.
#      - Administra callbacks asociados a cada señal.
#      - Garantiza que la comunicación interna sea ordenada y predecible.
#      - Es utilizado por bootstrap.py durante la inicialización del framework.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Sistema Global de Señales.
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
#      - Este archivo es crítico para la comunicación interna del ecosistema.
#      - No insertar lógica de módulos aquí. Solo administración de señales.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DEL SISTEMA GLOBAL DE SEÑALES
# =============================================================================

class SignalManager:
    """
    Sistema Global de Señales del ecosistema LINCAT.

    Permite que los módulos del framework se comuniquen mediante señales
    internas. Cada señal puede tener múltiples suscriptores (callbacks).
    """

    def __init__(self):
        # Diccionario donde se almacenan las señales.
        # Clave: nombre de la señal
        # Valor: lista de funciones callback
        self._signals = {}

        print(">>> Sistema Global de Señales creado.")

    # -------------------------------------------------------------------------
    def subscribe(self, signal_name: str, callback):
        """
        Suscribe una función callback a una señal específica.

        Parámetros:
            signal_name (str): Nombre de la señal.
            callback: Función que será llamada cuando la señal se emita.

        Requisitos:
            - El nombre debe ser una cadena.
            - El callback debe ser una función o método válido.
        """

        if not isinstance(signal_name, str):
            raise TypeError("El nombre de la señal debe ser una cadena de texto.")

        if not callable(callback):
            raise TypeError("El callback debe ser una función o método.")

        if signal_name not in self._signals:
            self._signals[signal_name] = []

        self._signals[signal_name].append(callback)
        print(f"    [+] Suscripción agregada a la señal: {signal_name}")

    # -------------------------------------------------------------------------
    def emit(self, signal_name: str, *args, **kwargs):
        """
        Emite una señal interna del sistema.

        Parámetros:
            signal_name (str): Nombre de la señal.
            *args, **kwargs: Argumentos que se pasarán a los callbacks.

        Comportamiento:
            - Si la señal existe, se ejecutan todos los callbacks asociados.
            - Si no existe, se ignora silenciosamente.
        """

        callbacks = self._signals.get(signal_name, [])

        print(f"    [>] Emitiendo señal: {signal_name} ({len(callbacks)} suscriptores)")

        for callback in callbacks:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"      [ERROR] Callback falló en señal '{signal_name}': {e}")

    # -------------------------------------------------------------------------
    def list_signals(self):
        """
        Lista todas las señales registradas en el sistema.

        Retorna:
            Lista de nombres de señales.
        """

        return list(self._signals.keys())

    # -------------------------------------------------------------------------
    def count(self):
        """
        Retorna la cantidad de señales registradas.
        """

        return len(self._signals)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Sistema Global de Señales")

    signals = SignalManager()

    # Callback de prueba
    def test_callback(msg):
        print(f"Callback ejecutado: {msg}")

    # Suscripción de prueba
    signals.subscribe("inicio_sistema", test_callback)

    # Emisión de prueba
    signals.emit("inicio_sistema", "LINCAT está arrancando...")

    print("Señales registradas:", signals.list_signals())
    print("Cantidad:", signals.count())
