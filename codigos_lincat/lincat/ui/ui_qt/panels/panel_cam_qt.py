# =============================================================================
#  Programa: panel_cam_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de CAM para la UI Qt de LINCAT.
#      Gestiona trayectorias, herramientas y simulación CAM.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra automáticamente en lincatqt.py (auto‑descubrimiento).
#      - Usa LincatUI como backend para enviar acciones CAM.
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
    QComboBox
)
from PySide6.QtCore import Qt

from lincat.modules.ui.ui import LincatUI


class PanelCamQt(QWidget):
    """
    Panel Qt de CAM para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado = "CAM: sin acciones recientes"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel CAM — Motor de Trayectorias")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Estado
        self.label_estado = QLabel(self._estado)
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_estado)

        # Pieza / trabajo
        fila_pieza = QHBoxLayout()
        self.input_pieza = QLineEdit()
        self.input_pieza.setPlaceholderText("Pieza / trabajo (ej: PIEZA-01)")
        fila_pieza.addWidget(self.input_pieza)
        layout.addLayout(fila_pieza)

        # Estrategia CAM
        fila_estrategia = QHBoxLayout()
        self.combo_estrategia = QComboBox()
        self.combo_estrategia.addItems([
            "desbaste",
            "acabado",
            "contorneado",
            "pocketing",
            "taladrado"
        ])
        fila_estrategia.addWidget(self.combo_estrategia)
        layout.addLayout(fila_estrategia)

        # Herramienta
        fila_herramienta = QHBoxLayout()
        self.input_herramienta = QLineEdit()
        self.input_herramienta.setPlaceholderText("Herramienta (ej: T01 Ø6)")
        fila_herramienta.addWidget(self.input_herramienta)
        layout.addLayout(fila_herramienta)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_generar = QPushButton("Generar trayectorias")
        btn_generar.clicked.connect(self._generar_trayectorias)

        btn_simular = QPushButton("Simular")
        btn_simular.clicked.connect(self._simular)

        btn_exportar = QPushButton("Exportar a CNC")
        btn_exportar.clicked.connect(self._exportar_cnc)

        fila_botones.addWidget(btn_generar)
        fila_botones.addWidget(btn_simular)
        fila_botones.addWidget(btn_exportar)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _generar_trayectorias(self):
        pieza = self.input_pieza.text().strip()
        estrategia = self.combo_estrategia.currentText()
        herramienta = self.input_herramienta.text().strip()

        self.ui.enviar_accion_usuario(
            "cam_generar_trayectorias",
            {
                "pieza": pieza,
                "estrategia": estrategia,
                "herramienta": herramienta
            }
        )

        self._estado = (
            f"Trayectorias generadas para {pieza or 'N/D'} "
            f"({estrategia}, herramienta {herramienta or 'N/D'})"
        )
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _simular(self):
        pieza = self.input_pieza.text().strip()

        self.ui.enviar_accion_usuario(
            "cam_simular",
            {"pieza": pieza}
        )

        self._estado = f"Simulación iniciada para pieza: {pieza or 'N/D'}"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _exportar_cnc(self):
        pieza = self.input_pieza.text().strip()

        self.ui.enviar_accion_usuario(
            "cam_exportar_cnc",
            {"pieza": pieza}
        )

        self._estado = f"Programa CNC exportado para pieza: {pieza or 'N/D'}"
        self.label_estado.setText(self._estado)
