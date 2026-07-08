# =============================================================================
#  Programa: smoke_test.py
#  Ubicación: lincat/tests/
# =============================================================================
#
#  Propósito:
#      Smoke Test completo del ecosistema LINCAT, incluyendo:
#          • Inicialización de todos los módulos industriales.
#          • Validación del flujo automático del sistema.
#          • Integración de la UI CLI y la UI TUI industrial.
#
#  Descripción técnica:
#      - Inicializa CAM, CNC, FLOW, Seguridad, Producción, Planta, Maestro,
#        Normativas y UI.
#      - Ejecuta un flujo industrial automático.
#      - Permite al operador elegir entre CLI o TUI.
#      - Ambas interfaces usan ui.py como backend.
#
#  Versión:
#      v4.0.0 — Versión estable con integración CLI + TUI.
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
from lincat.modules.ui.ui import LincatUI

from lincat.modules.ui.ui_cli.ui_cli import LincatCLI
from lincat.modules.ui.ui_tui.lincattui import LincatTUI


def ejecutar_smoke_test():
    print("\n============================================================")
    print(">>> SMOKE TEST COMPLETO DEL ECOSISTEMA LINCAT")
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
    ui = LincatUI()

    print("\n>>> Módulos inicializados correctamente.\n")

    # -------------------------------------------------------------------------
    # MODO AUTOMÁTICO DEL SMOKE TEST
    # -------------------------------------------------------------------------

    print("\n>>> [AUTO] Creando orden industrial...")
    prod.crear_orden("ORD001", "Mecanizado pieza A", {"material": "aluminio"})

    print("\n>>> [AUTO] Actualizando orden industrial...")
    prod.actualizar_orden("ORD001", {"estado": "en_proceso"})

    print("\n>>> [AUTO] Generando trayectoria CAM...")
    cam.generar_trayectoria("contour")

    print("\n>>> [AUTO] Ejecutando paso FLOW...")
    flow.ejecutar_paso("activar_valvula", {"tiempo": 2})

    print("\n>>> [AUTO] Smoke Test automático completado.\n")

    # -------------------------------------------------------------------------
    # SELECCIÓN DE INTERFAZ HUMANA
    # -------------------------------------------------------------------------

    print("============================================================")
    print(">>> SELECCIONE INTERFAZ HUMANA")
    print("============================================================")
    print("1) CLI (Interfaz de Línea de Comandos)")
    print("2) TUI (Interfaz de Texto Industrial)")
    print("============================================================\n")

    opcion = input("Seleccione opción (1/2): ").strip()

    if opcion == "1":
        print("\n>>> Iniciando CLI LINCAT...\n")
        cli = LincatCLI()
        cli.loop()

    elif opcion == "2":
        print("\n>>> Iniciando TUI LINCAT...\n")
        tui = LincatTUI()
        tui.ejecutar()

    else:
        print("\n>>> Opción inválida. Finalizando Smoke Test.\n")


# =============================================================================
#  PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    ejecutar_smoke_test()
