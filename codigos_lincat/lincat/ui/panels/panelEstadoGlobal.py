# ============================================================
#  PANEL ESTADO GLOBAL — LINCAT UI
#  Visión general del sistema industrial
# ============================================================

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer


class PanelEstadoGlobal(QWidget):
    """
    Panel Estado Global:
    - muestra estado CNC
    - muestra estado Twin
    - muestra estado Optimizer
    - muestra alarmas globales
    """

    def __init__(self, main_window):
        super().__init__()

        self.main = main_window

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Título
        title = QLabel("Estado Global — LINCAT")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        # Área de estado
        self.label = QLabel("Sin datos de estado global.")
        self.label.setStyleSheet("font-size: 16px; color: #ccc;")
        layout.addWidget(self.label)

        # Timer de actualización
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_state)
        self.timer.start(300)  # ~3 Hz

        self.setLayout(layout)

    def update_state(self):
        # CNC
        cnc_pos = getattr(self.main.cnc_state, "position", (0, 0, 0))
        cnc_vel = getattr(self.main.cnc_state, "velocity", 0)
        cnc_acc = getattr(self.main.cnc_state, "acceleration", 0)
        cnc_alarms = getattr(self.main.cnc_state, "alarms", [])

        # Twin
        twin_vib = getattr(self.main.twin_realtime, "vibration", 0.0)
        twin_res = getattr(self.main.twin_realtime, "resonance", 0.0)
        twin_stab = getattr(self.main.twin_realtime, "stability", 1.0)

        # Optimizer (placeholder: asumimos que existe last_report)
        opt_report = getattr(self.main.optimizer_interface, "last_report", None)
        opt_score = opt_report["score"] if isinstance(opt_report, dict) and "score" in opt_report else "N/D"

        self.label.setText(
            f"<b>CNC posición:</b> {cnc_pos}<br>"
            f"<b>CNC vel:</b> {cnc_vel}<br>"
            f"<b>CNC acc:</b> {cnc_acc}<br>"
            f"<b>CNC alarmas:</b> {cnc_alarms}<br><br>"
            f"<b>Twin vibración:</b> {twin_vib:.3f}<br>"
            f"<b>Twin resonancia:</b> {twin_res:.3f}<br>"
            f"<b>Twin estabilidad:</b> {twin_stab:.3f}<br><br>"
            f"<b>Optimizer score:</b> {opt_score}"
        )
