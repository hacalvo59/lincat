# =============================================================================
#  Programa: panel_cnc_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de CNC para la UI Qt de LINCAT.
#      Controla ejecución de programas CNC, estado de máquina y comandos básicos.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra automáticamente en lincatqt.py (auto‑descubrimiento).
#      - Usa LincatUI como backend para enviar acciones CNC.
#
#  Versión:
#      v1.0.0 — Primera versión estable.
#
# =============================================================================

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit
)
from PySide6.QtCore import Qt

from lincat.modules.ui.ui import LincatUI


class PanelCncQt(QWidget):
    """
    Panel Qt de CNC para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado = "CNC: sin acciones recientes"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel CNC — Control de Máquina")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Estado
        self.label_estado = QLabel(self._estado)
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_estado)

        # Programa CNC
        fila_programa = QHBoxLayout()
        self.input_programa = QLineEdit()
        self.input_programa.setPlaceholderText("Programa CNC (ej: programa.nc)")
        fila_programa.addWidget(self.input_programa)
        layout.addLayout(fila_programa)

        # Comandos manuales
        self.texto_comando = QTextEdit()
        self.texto_comando.setPlaceholderText("Comando manual (ej: G0 X10 Y20)")
        layout.addWidget(self.texto_comando)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_cargar = QPushButton("Cargar programa")
        btn_cargar.clicked.connect(self._cargar_programa)

        btn_ejecutar = QPushButton("Ejecutar")
        btn_ejecutar.clicked.connect(self._ejecutar_programa)

        btn_pausar = QPushButton("Pausar")
        btn_pausar.clicked.connect(self._pausar)

        btn_detener = QPushButton("Detener")
        btn_detener.clicked.connect(self._detener)

        btn_comando = QPushButton("Enviar comando")
        btn_comando.clicked.connect(self._enviar_comando)

        fila_botones.addWidget(btn_cargar)
        fila_botones.addWidget(btn_ejecutar)
        fila_botones.addWidget(btn_pausar)
        fila_botones.addWidget(btn_detener)
        fila_botones.addWidget(btn_comando)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _cargar_programa(self):
        programa = self.input_programa.text().strip()

        self.ui.enviar_accion_usuario(
            "cnc_cargar_programa",
            {"programa": programa}
        )

        self._estado = f"Programa cargado: {programa or 'N/D'}"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _ejecutar_programa(self):
        programa = self.input_programa.text().strip()

        self.ui.enviar_accion_usuario(
            "cnc_ejecutar_programa",
            {"programa": programa}
        )

        self._estado = f"Ejecutando programa: {programa or 'N/D'}"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _pausar(self):
        self.ui.enviar_accion_usuario("cnc_pausar", {})
        self._estado = "CNC pausado"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _detener(self):
        self.ui.enviar_accion_usuario("cnc_detener", {})
        self._estado = "CNC detenido"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _enviar_comando(self):
        comando = self.texto_comando.toPlainText().strip()

        self.ui.enviar_accion_usuario(
            "cnc_enviar_comando",
            {"comando": comando}
        )

        self._estado = f"Comando enviado: {comando or 'N/D'}"
        self.label_estado.setText(self._estado)
