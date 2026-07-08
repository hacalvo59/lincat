# ============================================================
#  LINCAT — MAIN APPLICATION
#  Ventana principal y carga de paneles
# ============================================================

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

# ------------------------------------------------------------
# Importar paneles UI
# ------------------------------------------------------------
from ui.panels.optimizer_panel import OptimizerPanel
from ui.panels.panelCNCReal import PanelCNCReal
from ui.panels.panelTwin import PanelTwin
from ui.panels.panelEstadoGlobal import PanelEstadoGlobal

# ------------------------------------------------------------
# Importar módulos CAM / CNC / Twin
# ------------------------------------------------------------
from cam.optimizer_cam_interface import OptimizerCAMInterface

from cnc.cnc_planner import CNCPlanner
from cnc.cnc_interpolator import CNCInterpolator
from cnc.cnc_servo import CNCServo
from cnc.cnc_driver_interface import CNCDriverInterface
from cnc.cnc_state import CNCState

from twin.twin_realtime import TwinRealtime


# ------------------------------------------------------------
# Ventana Principal
# ------------------------------------------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LINCAT — Sistema Industrial")
        self.resize(1600, 900)

        # ------------------------------------------------------------
        # Inicializar CNC Real
        # ------------------------------------------------------------
        self.cnc_planner = CNCPlanner()
        self.cnc_interpolator = CNCInterpolator()
        self.cnc_servo = CNCServo()
        self.cnc_driver = CNCDriverInterface()
        self.cnc_state = CNCState()

        # ------------------------------------------------------------
        # Inicializar Twin en tiempo real
        # ------------------------------------------------------------
        self.twin_realtime = TwinRealtime()

        # ------------------------------------------------------------
        # Inicializar módulos principales
        # ------------------------------------------------------------
        self.twin = None     # Twin CAM (no Twin realtime)
        self.cnc = None      # CNC CAM (no CNC realtime)

        # ------------------------------------------------------------
        # Crear interfaz del optimizador
        # ------------------------------------------------------------
        self.optimizer_interface = OptimizerCAMInterface(
            twin=self.twin,
            cnc=self.cnc
        )

        # ------------------------------------------------------------
        # Cargar trayectoria de prueba
        # ------------------------------------------------------------
        self.optimizer_interface.load_cam_trajectory({
            "segments": [
                {
                    "type": "line",
                    "start": (0, 0, 0),
                    "end": (100, 0, 0),
                    "feedrate": 1000,
                    "acceleration": 200,
                    "jerk": 50
                }
            ],
            "feedrate": 1000,
            "acceleration": 200,
            "jerk": 50
        })

        # ------------------------------------------------------------
        # Crear paneles UI
        # ------------------------------------------------------------
        self.optimizer_panel = OptimizerPanel(self.optimizer_interface, self)
        self.panel_cnc_real = PanelCNCReal(self)
        self.panel_twin = PanelTwin(self)
        self.panel_estado_global = PanelEstadoGlobal(self)

        # ------------------------------------------------------------
        # Agregar paneles como docks
        # ------------------------------------------------------------
        self.addDockWidget(
            Qt.RightDockWidgetArea,
            self.create_dock("Optimizer", self.optimizer_panel)
        )

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            self.create_dock("CNC Real", self.panel_cnc_real)
        )

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            self.create_dock("Twin", self.panel_twin)
        )

        self.addDockWidget(
            Qt.TopDockWidgetArea,
            self.create_dock("Estado Global", self.panel_estado_global)
        )

    # ------------------------------------------------------------
    # Crear dock genérico
    # ------------------------------------------------------------
    def create_dock(self, title, widget):
        from PySide6.QtWidgets import QDockWidget
        dock = QDockWidget(title, self)
        dock.setWidget(widget)
        dock.setFeatures(
            QDockWidget.DockWidgetMovable |
            QDockWidget.DockWidgetFloatable
        )
        return dock


# ------------------------------------------------------------
# Punto de entrada
# ------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
