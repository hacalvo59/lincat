# ============================================================
#  PANEL CNC REAL — LINCAT UI
#  Estado y ejecución del CNC real
# ============================================================

from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout
)
from PySide6.QtCore import Qt, QTimer


class PanelCNCReal(QWidget):
    """
    Panel CNC Real:
    - muestra estado CNC
    - ejecuta puntos interpolados
    - lee feedback del driver
    - actualiza UI en tiempo real
    """

    def __init__(self, main_window):
        super().__init__()

        self.main = main_window

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # ------------------------------------------------------------
        # Título
        # ------------------------------------------------------------
        title = QLabel("CNC Real — Estado y Ejecución")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        # ------------------------------------------------------------
        # Estado CNC
        # ------------------------------------------------------------
        self.state_label = QLabel("Estado CNC no disponible.")
        self.state_label.setStyleSheet("font-size: 16px; color: #ccc;")
        layout.addWidget(self.state_label)

        # ------------------------------------------------------------
        # Botón de ejecución
        # ------------------------------------------------------------
        btn_exec = QPushButton("Ejecutar Trayectoria")
        btn_exec.setStyleSheet("""
            QPushButton {
                background-color: #0078d7;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
        """)
        btn_exec.clicked.connect(self.execute_trajectory)
        layout.addWidget(btn_exec, alignment=Qt.AlignCenter)

        # ------------------------------------------------------------
        # Timer de actualización
        # ------------------------------------------------------------
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_state)
        self.timer.start(200)  # 5 veces por segundo

        self.setLayout(layout)

    # ------------------------------------------------------------
    # Ejecutar trayectoria CNC
    # ------------------------------------------------------------
    def execute_trajectory(self):
        """
        Ejecuta la trayectoria optimizada:
        Planner → Interpolator → Servo → Driver → State
        """

        # 1. Obtener plan del planner
        plan = self.main.cnc_planner.generate_execution_plan()

        points = []

        # 2. Interpolar cada segmento
        for seg in plan:
            if seg["type"] == "line":
                pts = self.main.cnc_interpolator.interpolate_line(
                    seg["start"],
                    seg["end"],
                    steps=50
                )
                points.extend(pts)

        # 3. Ejecutar puntos en el servo
        for p in points:
            pos = self.main.cnc_servo.execute_point(p)
            self.main.cnc_driver.send_position(pos)
            feedback = self.main.cnc_driver.read_feedback()
            self.main.cnc_state.position = feedback["position"]

    # ------------------------------------------------------------
    # Actualizar estado CNC en UI
    # ------------------------------------------------------------
    def update_state(self):
        pos = self.main.cnc_state.position
        self.state_label.setText(
            f"<b>Posición:</b> {pos}<br>"
            f"<b>Velocidad:</b> {self.main.cnc_state.velocity}<br>"
            f"<b>Aceleración:</b> {self.main.cnc_state.acceleration}<br>"
            f"<b>Alarmas:</b> {self.main.cnc_state.alarms}"
        )
