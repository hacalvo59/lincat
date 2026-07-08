# =============================================================================
#  Programa: panel_planta_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de Planta para la UI Qt de LINCAT.
#      Muestra estado general de la planta y permite acciones básicas.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra en lincatqt.py como pestaña "Planta".
#      - Usa LincatUI como backend.
#      - No toca módulos industriales directamente.
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
    QLineEdit
)
from PySide6.QtCore import Qt

from lincat.modules.ui.ui import LincatUI


class PanelPlantaQt(QWidget):
    """
    Panel Qt de Planta para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado_planta = "Planta: sin información"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel de Planta")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Estado planta
        self.label_estado = QLabel(self._estado_planta)
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_estado)

        # Zona de identificación de planta / línea
        fila_id = QHBoxLayout()
        self.input_planta = QLineEdit()
        self.input_planta.setPlaceholderText("ID planta / línea (ej: PLT-01)")
        fila_id.addWidget(self.input_planta)
        layout.addLayout(fila_id)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_consultar = QPushButton("Consultar planta")
        btn_consultar.clicked.connect(self._consultar_planta)

        btn_iniciar = QPushButton("Iniciar planta")
        btn_iniciar.clicked.connect(self._iniciar_planta)

        btn_detener = QPushButton("Detener planta")
        btn_detener.clicked.connect(self._detener_planta)

        fila_botones.addWidget(btn_consultar)
        fila_botones.addWidget(btn_iniciar)
        fila_botones.addWidget(btn_detener)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _consultar_planta(self):
        planta_id = self.input_planta.text().strip()

        self.ui.enviar_accion_usuario(
            "planta_consultar",
            {"planta_id": planta_id}
        )

        self._estado_planta = f"Consulta enviada para planta: {planta_id or 'N/D'}"
        self.label_estado.setText(self._estado_planta)

    # -------------------------------------------------------------------------
    def _iniciar_planta(self):
        planta_id = self.input_planta.text().strip()

        self.ui.enviar_accion_usuario(
            "planta_iniciar",
            {"planta_id": planta_id}
        )

        self._estado_planta = f"Planta en proceso de inicio: {planta_id or 'N/D'}"
        self.label_estado.setText(self._estado_planta)

    # -------------------------------------------------------------------------
    def _detener_planta(self):
        planta_id = self.input_planta.text().strip()

        self.ui.enviar_accion_usuario(
            "planta_detener",
            {"planta_id": planta_id}
        )

        self._estado_planta = f"Planta en proceso de parada: {planta_id or 'N/D'}"
        self.label_estado.setText(self._estado_planta)
