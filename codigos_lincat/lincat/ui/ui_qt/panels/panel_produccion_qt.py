# =============================================================================
#  Programa: panel_produccion_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de Producción para la UI Qt de LINCAT.
#      Gestiona órdenes, lotes y estado de líneas de producción.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra automáticamente en lincatqt.py (auto‑descubrimiento).
#      - Usa LincatUI como backend para enviar acciones de producción.
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


class PanelProduccionQt(QWidget):
    """
    Panel Qt de Producción para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado = "Producción: sin acciones recientes"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel de Producción")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Estado
        self.label_estado = QLabel(self._estado)
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_estado)

        # Orden de producción
        fila_orden = QHBoxLayout()
        self.input_orden = QLineEdit()
        self.input_orden.setPlaceholderText("Orden de producción (ej: OP-0001)")
        fila_orden.addWidget(self.input_orden)
        layout.addLayout(fila_orden)

        # Línea de producción
        fila_linea = QHBoxLayout()
        self.input_linea = QLineEdit()
        self.input_linea.setPlaceholderText("Línea (ej: L1, L2...)")
        fila_linea.addWidget(self.input_linea)
        layout.addLayout(fila_linea)

        # Estado deseado
        fila_estado = QHBoxLayout()
        self.combo_estado = QComboBox()
        self.combo_estado.addItems([
            "programada",
            "en_proceso",
            "pausada",
            "finalizada",
            "cancelada"
        ])
        fila_estado.addWidget(self.combo_estado)
        layout.addLayout(fila_estado)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_aplicar = QPushButton("Aplicar estado")
        btn_aplicar.clicked.connect(self._aplicar_estado)

        btn_consultar = QPushButton("Consultar orden")
        btn_consultar.clicked.connect(self._consultar_orden)

        fila_botones.addWidget(btn_aplicar)
        fila_botones.addWidget(btn_consultar)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _aplicar_estado(self):
        orden = self.input_orden.text().strip()
        linea = self.input_linea.text().strip()
        estado = self.combo_estado.currentText()

        self.ui.enviar_accion_usuario(
            "produccion_aplicar_estado",
            {
                "orden": orden,
                "linea": linea,
                "estado": estado
            }
        )

        self._estado = (
            f"Estado '{estado}' aplicado a orden {orden or 'N/D'} "
            f"en línea {linea or 'N/D'}"
        )
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _consultar_orden(self):
        orden = self.input_orden.text().strip()

        self.ui.enviar_accion_usuario(
            "produccion_consultar_orden",
            {"orden": orden}
        )

        self._estado = f"Consulta enviada para orden: {orden or 'N/D'}"
        self.label_estado.setText(self._estado)
