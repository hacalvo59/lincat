# =============================================================================
#  Programa: panel_mantenimiento_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de Mantenimiento para la UI Qt de LINCAT.
#      Gestiona avisos, fallas, intervenciones y estados de equipos.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra automáticamente en lincatqt.py (auto‑descubrimiento).
#      - Usa LincatUI como backend para enviar acciones de mantenimiento.
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


class PanelMantenimientoQt(QWidget):
    """
    Panel Qt de Mantenimiento para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado = "Mantenimiento: sin acciones recientes"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel de Mantenimiento")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Estado
        self.label_estado = QLabel(self._estado)
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_estado)

        # Equipo
        fila_equipo = QHBoxLayout()
        self.input_equipo = QLineEdit()
        self.input_equipo.setPlaceholderText("Equipo (ej: EQ-01)")
        fila_equipo.addWidget(self.input_equipo)
        layout.addLayout(fila_equipo)

        # Tipo de intervención
        fila_tipo = QHBoxLayout()
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems([
            "preventivo",
            "correctivo",
            "inspección",
            "emergencia"
        ])
        fila_tipo.addWidget(self.combo_tipo)
        layout.addLayout(fila_tipo)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_crear = QPushButton("Crear aviso")
        btn_crear.clicked.connect(self._crear_aviso)

        btn_cerrar = QPushButton("Cerrar aviso")
        btn_cerrar.clicked.connect(self._cerrar_aviso)

        btn_estado = QPushButton("Consultar estado")
        btn_estado.clicked.connect(self._consultar_estado)

        fila_botones.addWidget(btn_crear)
        fila_botones.addWidget(btn_cerrar)
        fila_botones.addWidget(btn_estado)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _crear_aviso(self):
        equipo = self.input_equipo.text().strip()
        tipo = self.combo_tipo.currentText()

        self.ui.enviar_accion_usuario(
            "mantenimiento_crear_aviso",
            {"equipo": equipo, "tipo": tipo}
        )

        self._estado = (
            f"Aviso creado para equipo {equipo or 'N/D'} "
            f"({tipo})"
        )
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _cerrar_aviso(self):
        equipo = self.input_equipo.text().strip()

        self.ui.enviar_accion_usuario(
            "mantenimiento_cerrar_aviso",
            {"equipo": equipo}
        )

        self._estado = f"Aviso cerrado para equipo: {equipo or 'N/D'}"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _consultar_estado(self):
        equipo = self.input_equipo.text().strip()

        self.ui.enviar_accion_usuario(
            "mantenimiento_consultar_estado",
            {"equipo": equipo}
        )

        self._estado = f"Consulta enviada para equipo: {equipo or 'N/D'}"
        self.label_estado.setText(self._estado)
