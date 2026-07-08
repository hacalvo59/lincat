# =============================================================================
#  Programa: smoke_test_tui_advanced.py
#  Ubicación: lincat/tests/
# =============================================================================
#
#  Propósito:
#      Smoke Test exclusivo para la TUI avanzada del ecosistema LINCAT.
#      Ejecuta el flujo automático industrial y luego lanza la interfaz
#      avanzada con múltiples ventanas curses.
#
#  Descripción técnica:
#      - Inicializa todos los módulos industriales.
#      - Ejecuta un flujo automático de prueba.
#      - Lanza la TUI avanzada (lincattui_advanced.py).
#      - No depende del smoke_test.py original.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del Smoke Test TUI avanzada.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
# =============================================================================


from lincat.modules.cam.cam import LincatCAM
from lincat.modules.cnc_cat.cnc_cat import LincatCNC
from lincat.modules.flow.flow import LincatFLOW
from lincat.modules.seguridad.seguridad import LincatSeguridad
from lincat.modules.produccion.produccion import LincatProduccion
from lincat.modules.planta.planta import LincatPlanta
from lincat.modules.maestro.maestro import LincatMaestro
from lincat.modules.normativas.normativas import LincatNormativas

from lincat.modules.ui.ui_tui.lincattui_advanced import LincatTUIAdvanced


def ejecutar_smoke_test_tui_advanced():
    print("\n============================================================")
    print(">>> SMOKE TEST TUI AVANZADA — ECOSISTEMA LINCAT")
    print("============================================================\n")

    # Inicializar módulos industriales
    cam = LincatCAM()
    cnc = LincatCNC()
    flow = LincatFLOW()
    seg = LincatSeguridad()
    prod = LincatProduccion()
    planta = LincatPlanta()
    maestro = LincatMaestro()
    norm = LincatNormativas()

    print("\n>>> Módulos inicializados correctamente.\n")

    # -------------------------------------------------------------------------
    # FLUJO AUTOMÁTICO INDUSTRIAL
    # -------------------------------------------------------------------------

    print("\n>>> [AUTO] Creando orden industrial...")
    prod.crear_orden("ORD-TUI-ADV", "Proceso avanzado TUI", {"material": "acero"})

    print("\n>>> [AUTO] Actualizando orden industrial...")
    prod.actualizar_orden("ORD-TUI-ADV", {"estado": "en_proceso"})

    print("\n>>> [AUTO] Generando trayectoria CAM...")
    cam.generar_trayectoria("roughing")

    print("\n>>> [AUTO] Ejecutando paso FLOW...")
    flow.ejecutar_paso("activar_bomba", {"rpm": 1200})

    print("\n>>> [AUTO] Validando normativa...")
    norm.validar_norma("ISO-9001", {"proceso": "mecanizado"})

    print("\n>>> [AUTO] Comando Maestro...")
    maestro.iniciar_proceso("PROC-TUI-ADV")

    print("\n>>> [AUTO] Flujo automático completado.\n")

    # -------------------------------------------------------------------------
    # LANZAR TUI AVANZADA
    # -------------------------------------------------------------------------

    print(">>> Iniciando TUI avanzada LINCAT...\n")
    tui = LincatTUIAdvanced()
    tui.ejecutar()


# =============================================================================
#  PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    ejecutar_smoke_test_tui_advanced()
