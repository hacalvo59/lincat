# =============================================================================
#  Programa: smoke_test_qt.py
#  Ubicación: lincat/tests/
# =============================================================================
#
#  Propósito:
#      Smoke Test exclusivo para la UI Qt del ecosistema LINCAT.
#      Inicializa los módulos industriales, ejecuta un flujo automático
#      de prueba y lanza la interfaz gráfica Qt completa.
#
#  Descripción técnica:
#      - Inicializa todos los módulos industriales LINCAT.
#      - Ejecuta un flujo automático representativo:
#          • creación y actualización de orden
#          • generación de trayectoria CAM
#          • ejecución de paso FLOW
#          • validación normativa
#          • comando Maestro
#      - Lanza la UI Qt (lincatqt.py) como interfaz gráfica principal.
#      - No toca módulos industriales directamente desde la UI.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del Smoke Test UI Qt.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
# =============================================================================


from PySide6.QtWidgets import QApplication

from lincat.modules.cam.cam import LincatCAM
from lincat.modules.cnc_cat.cnc_cat import LincatCNC
from lincat.modules.flow.flow import LincatFLOW
from lincat.modules.seguridad.seguridad import LincatSeguridad
from lincat.modules.produccion.produccion import LincatProduccion
from lincat.modules.planta.planta import LincatPlanta
from lincat.modules.maestro.maestro import LincatMaestro
from lincat.modules.normativas.normativas import LincatNormativas

from lincat.modules.ui.ui_qt.lincatqt import LincatQtMainWindow


def ejecutar_smoke_test_qt():
    print("\n============================================================")
    print(">>> SMOKE TEST UI Qt — ECOSISTEMA LINCAT")
    print("============================================================\n")

    # -------------------------------------------------------------------------
    # INICIALIZACIÓN DE MÓDULOS INDUSTRIALES
    # -------------------------------------------------------------------------

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
    prod.crear_orden("ORD-QT-001", "Proceso UI Qt", {"material": "aluminio"})

    print("\n>>> [AUTO] Actualizando orden industrial...")
    prod.actualizar_orden("ORD-QT-001", {"estado": "en_proceso"})

    print("\n>>> [AUTO] Generando trayectoria CAM...")
    cam.generar_trayectoria("finishing")

    print("\n>>> [AUTO] Ejecutando paso FLOW...")
    flow.ejecutar_paso("activar_bomba", {"rpm": 1500})

    print("\n>>> [AUTO] Validando normativa...")
    norm.validar_norma("ISO-9001", {"proceso": "mecanizado_ui_qt"})

    print("\n>>> [AUTO] Comando Maestro...")
    maestro.iniciar_proceso("PROC-QT-001")

    print("\n>>> [AUTO] Flujo automático completado.\n")

    # -------------------------------------------------------------------------
    # LANZAR UI Qt
    # -------------------------------------------------------------------------

    print(">>> Iniciando UI Qt LINCAT...\n")

    app = QApplication([])
    ventana = LincatQtMainWindow()
    ventana.show()
    app.exec()


# =============================================================================
#  PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    ejecutar_smoke_test_qt()
