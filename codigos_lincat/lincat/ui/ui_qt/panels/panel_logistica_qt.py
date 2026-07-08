# =============================================================================
#  Programa: panel_logistica_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de Logística para la UI Qt de LINCAT.
#      Gestiona movimientos internos, abastecimiento y transporte interno.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra automáticamente en lincatqt.py (auto‑descubrimiento).
#      - Usa LincatUI como backend para enviar acciones de logística.
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


class PanelLogisticaQt(QWidget):
    """
    Panel Qt de Logística para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado = "Logística: sin acciones recientes"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel de Logística")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Estado
        self.label_estado = QLabel(self._estado)
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_estado)

        # Material
        fila_material = QHBoxLayout()
        self.input_material = QLineEdit()
        self.input_material.setPlaceholderText("Material (ej: MAT-001)")
        fila_material.addWidget(self.input_material)
        layout.addLayout(fila_material)

        # Origen
        fila_origen = QHBoxLayout()
        self.input_origen = QLineEdit()
        self.input_origen.setPlaceholderText("Origen (ej: ALM-01)")
        fila_origen.addWidget(self.input_origen)
        layout.addLayout(fila_origen)

        # Destino
        fila_destino = QHBoxLayout()
        self.input_destino = QLineEdit()
        self.input_destino.setPlaceholderText("Destino (ej: L1, L2...)")
        fila_destino.addWidget(self.input_destino)
        layout.addLayout(fila_destino)

        # Tipo de movimiento
        fila_tipo = QHBoxLayout()
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems([
            "abastecimiento",
            "retiro",
            "transferencia",
            "devolución"
        ])
        fila_tipo.addWidget(self.combo_tipo)
        layout.addLayout(fila_tipo)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_mover = QPushButton("Registrar movimiento")
        btn_mover.clicked.connect(self._registrar_movimiento)

        btn_consultar = QPushButton("Consultar material")
        btn_consultar.clicked.connect(self._consultar_material)

        fila_botones.addWidget(btn_mover)
        fila_botones.addWidget(btn_consultar)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _registrar_movimiento(self):
        material = self.input_material.text().strip()
        origen = self.input_origen.text().strip()
        destino = self.input_destino.text().strip()
        tipo = self.combo_tipo.currentText()

        self.ui.enviar_accion_usuario(
            "logistica_registrar_movimiento",
            {
                "material": material,
                "origen": origen,
                "destino": destino,
                "tipo": tipo
            }
        )

        self._estado = (
            f"Movimiento '{tipo}' registrado: "
            f"{material or 'N/D'} de {origen or 'N/D'} a {destino or 'N/D'}"
        )
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _consultar_material(self):
        material = self.input_material.text().strip()

        self.ui.enviar_accion_usuario(
            "logistica_consultar_material",
            {"material": material}
        )

        self._estado = f"Consulta enviada para material: {material or 'N/D'}"
        self.label_estado.setText(self._estado)
