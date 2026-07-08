
import pkgutil
import inspect
import importlib

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
    QVBoxLayout
)

from lincat.modules.ui.ui import LincatUI


class LincatQt(QMainWindow):
    """
    Ventana principal Qt con auto‑descubrimiento de paneles.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("LINCAT — UI Qt Industrial")
        self.resize(900, 600)

        self.ui = LincatUI()
        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        widget_central = QWidget()
        layout = QVBoxLayout()

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        # Auto‑descubrimiento de paneles Qt
        for nombre, clase in self._descubrir_paneles_qt().items():
            tabs.addTab(clase(), nombre)

        layout.addWidget(tabs)
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    # -------------------------------------------------------------------------
    def _descubrir_paneles_qt(self):
        """
        Busca automáticamente todos los paneles Qt dentro de ui_qt/panels/.
        """

        paneles = {}
        paquete = "lincat.modules.ui.ui_qt.panels"

        for _, modulo, _ in pkgutil.iter_modules(
            importlib.import_module(paquete).__path__
        ):
            mod = importlib.import_module(f"{paquete}.{modulo}")

            for nombre, obj in inspect.getmembers(mod, inspect.isclass):
                if nombre.endswith("Qt"):  # Convención industrial
                    paneles[nombre.replace("Qt", "")] = obj

        return paneles


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication([])
    ventana = LincatQt()
    ventana.show()
    app.exec()
