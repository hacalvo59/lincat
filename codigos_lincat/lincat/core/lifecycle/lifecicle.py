# =============================================================================
#  Programa: lifecycle.py
#  Ubicación: codigos_lincat/lincat/core/lifecycle/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Ciclo de Vida Global del ecosistema LINCAT.
#      Su función es administrar los estados fundamentales del framework
#      industrial, garantizando que cada módulo pueda reaccionar de forma
#      ordenada y segura a los cambios de estado del sistema.
#
#  Descripción técnica:
#      - Define los estados principales del ecosistema.
#      - Permite transiciones controladas entre estados.
#      - Notifica a los módulos sobre cambios de estado.
#      - Se integra con signals.py y events.py para emitir señales y eventos.
#      - Es utilizado por bootstrap.py durante la inicialización del framework.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Ciclo de Vida del ecosistema.
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
#      - Este archivo es crítico para la estabilidad del ecosistema.
#      - No insertar lógica de módulos aquí. Solo administración del ciclo.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  IMPORTS INTERNOS DEL FRAMEWORK
# =============================================================================

try:
    from lincat.core.signals.signals import SignalManager
    from lincat.core.events.events import EventManager
except ImportError:
    SignalManager = None
    EventManager = None


# =============================================================================
#  DEFINICIÓN DE ESTADOS DEL CICLO DE VIDA
# =============================================================================

class LincatState:
    """Estados principales del ecosistema LINCAT."""

    INITIALIZING = "initializing"
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"
    ERROR = "error"


# =============================================================================
#  CLASE PRINCIPAL DEL CICLO DE VIDA GLOBAL
# =============================================================================

class LincatLifecycle:
    """
    Ciclo de Vida Global del ecosistema LINCAT.

    Administra los estados fundamentales del framework y permite transiciones
    controladas entre ellos. Emite señales y eventos cuando el estado cambia.
    """

    def __init__(self, signals=None, events=None):
        self.state = LincatState.INITIALIZING

        # Sistemas internos
        self.signals = signals if signals else (SignalManager() if SignalManager else None)
        self.events = events if events else (EventManager() if EventManager else None)

        print(f">>> Ciclo de Vida creado. Estado inicial: {self.state}")

    # -------------------------------------------------------------------------
    def set_state(self, new_state: str):
        """
        Cambia el estado del ecosistema LINCAT.

        Parámetros:
            new_state (str): Nuevo estado del sistema.

        Comportamiento:
            - Valida el estado.
            - Emite señal interna.
            - Emite evento global.
            - Actualiza el estado del ciclo de vida.
        """

        if new_state not in vars(LincatState).values():
            raise ValueError(f"Estado inválido: {new_state}")

        print(f"    [>] Cambio de estado: {self.state} -> {new_state}")

        self.state = new_state

        # Emitir señal interna
        if self.signals:
            self.signals.emit("estado_cambiado", new_state)

        # Emitir evento global
        if self.events:
            self.events.emit("estado_cambiado", new_state)

    # -------------------------------------------------------------------------
    def get_state(self):
        """Retorna el estado actual del ecosistema."""
        return self.state

    # -------------------------------------------------------------------------
    def is_ready(self):
        """Retorna True si el ecosistema está listo."""
        return self.state == LincatState.READY

    # -------------------------------------------------------------------------
    def is_running(self):
        """Retorna True si el ecosistema está en ejecución."""
        return self.state == LincatState.RUNNING

    # -------------------------------------------------------------------------
    def is_paused(self):
        """Retorna True si el ecosistema está pausado."""
        return self.state == LincatState.PAUSED

    # -------------------------------------------------------------------------
    def is_stopped(self):
        """Retorna True si el ecosistema está detenido."""
        return self.state == LincatState.STOPPED


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Ciclo de Vida Global")

    lifecycle = LincatLifecycle()

    lifecycle.set_state(LincatState.READY)
    lifecycle.set_state(LincatState.RUNNING)
    lifecycle.set_state(LincatState.PAUSED)
    lifecycle.set_state(LincatState.STOPPED)

    print("Estado final:", lifecycle.get_state())
