# =============================================================================
#  Programa: panel_almacen_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de Almacén para la UI Qt de LINCAT.
#      Gestiona stock, entradas y salidas de materiales.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra automáticamente en lincatqt.py (auto‑descubrimiento).
#      - Usa LincatUI como backend para enviar acciones de almacén.
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


class PanelAlmacenQt(QWidget):
    """
    Panel Qt de Almacén para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado = "Almacén: sin acciones recientes"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel de Almacén")
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

        # Cantidad
        fila_cantidad = QHBoxLayout()
        self.input_cantidad = QLineEdit()
        self.input_cantidad.setPlaceholderText("Cantidad")
        fila_cantidad.addWidget(self.input_cantidad)
        layout.addLayout(fila_cantidad)

        # Ubicación
        fila_ubicacion = QHBoxLayout()
        self.input_ubicacion = QLineEdit()
        self.input_ubicacion.setPlaceholderText("Ubicación (ej: EST-01)")
        fila_ubicacion.addWidget(self.input_ubicacion)
        layout.addLayout(fila_ubicacion)

        # Tipo de movimiento
        fila_tipo = QHBoxLayout()
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems([
            "entrada",
            "salida",
            "ajuste",
            "inventario"
        ])
        fila_tipo.addWidget(self.combo_tipo)
        layout.addLayout(fila_tipo)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_registrar = QPushButton("Registrar movimiento")
        btn_registrar.clicked.connect(self._registrar_movimiento)

        btn_consultar = QPushButton("Consultar stock")
        btn_consultar.clicked.connect(self._consultar_stock)

        fila_botones.addWidget(btn_registrar)
        fila_botones.addWidget(btn_consultar)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _registrar_movimiento(self):
        material = self.input_material.text().strip()
        cantidad = self.input_cantidad.text().strip()
        ubicacion = self.input_ubicacion.text().strip()
        tipo = self.combo_tipo.currentText()

        self.ui.enviar_accion_usuario(
            "almacen_registrar_movimiento",
            {
                "material": material,
                "cantidad": cantidad,
                "ubicacion": ubicacion,
                "tipo": tipo
            }
        )

        self._estado = (
            f"Movimiento '{tipo}' registrado: {cantidad or 'N/D'} "
            f"de {material or 'N/D'} en {ubicacion or 'N/D'}"
        )
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _consultar_stock(self):
        material = self.input_material.text().strip()
        ubicacion = self.input_ubicacion.text().strip()

        self.ui.enviar_accion_usuario(
            "almacen_consultar_stock",
            {"material": material, "ubicacion": ubicacion}
        )

        self._estado = (
            f"Consulta de stock enviada para {material or 'N/D'} "
            f"en {ubicacion or 'N/D'}"
        )
        self.label_estado.setText(self._estado)
