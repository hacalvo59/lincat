# ============================================================
#  OPTIMIZER PANEL — LINCAT UI
#  Panel de visualización del Optimizador de Trayectorias
#  Autor: Hugo Alberto Calvo
#  Fecha: 2026-07-05
# ============================================================

from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
)
from PySide6.QtCore import Qt, Signal

class OptimizerPanel(QWidget):
    """
    Panel UI del Optimizador de Trayectorias LINCAT.
    Muestra:
    - trayectoria original
    - trayectoria optimizada
    - análisis
    - simulación Twin
    - score dinámico
    - reporte completo
    """

    optimize_requested = Signal()

    def __init__(self, optimizer_interface):
        super().__init__()

        self.optimizer = optimizer_interface
        self.last_report = None

        main = QVBoxLayout()
        main.setContentsMargins(20, 20, 20, 20)
        main.setSpacing(15)

        # ------------------------------------------------------------
        # Título
        # ------------------------------------------------------------
        title = QLabel("Optimizer — Análisis y Mejora de Trayectorias")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        main.addWidget(title)

        # ------------------------------------------------------------
        # Área de reporte
        # ------------------------------------------------------------
        self.report_frame = QFrame()
        self.report_frame.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border: 1px solid #444;
                border-radius: 8px;
                min-height: 300px;
            }
        """)
        self.report_layout = QVBoxLayout()
        self.report_frame.setLayout(self.report_layout)

        self.report_label = QLabel("No hay reporte disponible.")
        self.report_label.setStyleSheet("color: #aaa; font-size: 14px;")
        self.report_label.setAlignment(Qt.AlignCenter)

        self.report_layout.addWidget(self.report_label)
        main.addWidget(self.report_frame)

        # ------------------------------------------------------------
        # Botón de optimización
        # ------------------------------------------------------------
        btn_opt = QPushButton("Optimizar Trayectoria")
        btn_opt.setStyleSheet("""
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
        btn_opt.clicked.connect(self.run_optimizer)
        main.addWidget(btn_opt, alignment=Qt.AlignCenter)

        self.setLayout(main)

    # ------------------------------------------------------------
    # Ejecutar optimizador
    # ------------------------------------------------------------
    def run_optimizer(self):
        """
        Ejecuta el optimizador a través de la interfaz CAM.
        Actualiza el panel con el reporte generado.
        """
        result = self.optimizer.send_to_optimizer()
        self.last_report = result

        text = (
            f"<b>Análisis:</b> {result['analysis']}<br><br>"
            f"<b>Simulación:</b> {result['simulation']}<br><br>"
            f"<b>Score:</b> {result['score']}<br><br>"
            f"<b>Optimizada:</b> {result['optimized']}<br><br>"
        )

        self.report_label.setText(text)
