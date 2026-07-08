# ============================================================
#  PANEL TWIN — LINCAT UI
#  Simulación dinámica en tiempo real
# ============================================================

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer

class PanelTwin(QWidget):
    """
    Panel Twin:
    - muestra vibración
    - muestra resonancia
    - muestra estabilidad
    - se actualiza en tiempo real
    """

    def __init__(self, main_window):
        super().__init__()

        self.main = main_window

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Twin — Simulación en Tiempo Real")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        self.label = QLabel("Sin datos del Twin.")
        self.label.setStyleSheet("font-size: 16px; color: #ccc;")
        layout.addWidget(self.label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_twin)
        self.timer.start(200)

        self.setLayout(layout)

    def update_twin(self):
        data = {
            "vibration": self.main.twin_realtime.vibration,
            "resonance": self.main.twin_realtime.resonance,
            "stability": self.main.twin_realtime.stability
        }

        self.label.setText(
            f"<b>Vibración:</b> {data['vibration']:.3f}<br>"
            f"<b>Resonancia:</b> {data['resonance']:.3f}<br>"
            f"<b>Estabilidad:</b> {data['stability']:.3f}"
        )
