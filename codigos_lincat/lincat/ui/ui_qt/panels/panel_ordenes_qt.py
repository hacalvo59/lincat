# =============================================================================
#  Programa: panel_ordenes_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Implementar el panel gráfico de Órdenes para la UI Qt de LINCAT,
#      utilizando PySide6. Este panel permite crear, actualizar y consultar
#      órdenes industriales del ecosistema.
#
#  Descripción técnica:
#      - Es un widget Qt independiente y modular.
#      - Se integra en la ventana principal (lincatqt.py) como panel de órdenes.
#      - Usa LincatUI como backend de interfaz (mismo núcleo que CLI/TUI).
#      - Traduce acciones de usuario en ui.enviar_accion_usuario(...).
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del Panel Órdenes Qt LINCAT.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
# =============================================================================


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
)
from PySide6.QtCore import Qt

from lincat.modules.ui.ui import LincatUI


class PanelOrdenesQt(QWidget):
    """
    Panel gráfico de Órdenes para la UI Qt de LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Backend de interfaz
        self.ui = LincatUI()

        # Estado interno mínimo
        self._orden_actual = "Ninguna orden seleccionada"

        # Construcción de la UI
        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout_principal = QVBoxLayout()

        # Título del panel
        titulo = QLabel("Panel de Órdenes Industriales")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout_principal.addWidget(titulo)

        # Línea de estado de orden
        self.label_orden = QLabel(f"Orden actual: {self._orden_actual}")
        self.label_orden.setAlignment(Qt.AlignLeft)
        layout_principal.addWidget(self.label_orden)

        # Campo para ID de orden
        layout_id = QHBoxLayout()
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("ID de orden (ej: ORD-001)")
        layout_id.addWidget(self.input_id)

        layout_principal.addLayout(layout_id)

        # Campo para descripción
        layout_desc = QHBoxLayout()
        self.input_desc = QLineEdit()
        self.input_desc.setPlaceholderText("Descripción de la orden")
        layout_desc.addWidget(self.input_desc)

        layout_principal.addLayout(layout_desc)

        # Botones de acción
        layout_botones = QHBoxLayout()

        boton_crear = QPushButton("Crear orden")
        boton_crear.clicked.connect(self._crear_orden)

        boton_actualizar = QPushButton("Actualizar orden")
        boton_actualizar.clicked.connect(self._actualizar_orden)

        boton_consultar = QPushButton("Consultar orden")
        boton_consultar.clicked.connect(self._consultar_orden)

        layout_botones.addWidget(boton_crear)
        layout_botones.addWidget(boton_actualizar)
        layout_botones.addWidget(boton_consultar)

        layout_principal.addLayout(layout_botones)

        self.setLayout(layout_principal)

    # -------------------------------------------------------------------------
    def _crear_orden(self):
        orden_id = self.input_id.text().strip()
        descripcion = self.input_desc.text().strip()

        if orden_id:
            self.ui.enviar_accion_usuario(
                "crear_orden",
                {"id": orden_id, "descripcion": descripcion}
            )
            self._orden_actual = orden_id
            self.label_orden.setText(f"Orden actual: {self._orden_actual}")

    # -------------------------------------------------------------------------
    def _actualizar_orden(self):
        orden_id = self.input_id.text().strip()
        descripcion = self.input_desc.text().strip()

        if orden_id:
            self.ui.enviar_accion_usuario(
                "actualizar_orden",
                {"id": orden_id, "descripcion": descripcion}
            )
            self._orden_actual = orden_id
            self.label_orden.setText(f"Orden actual: {self._orden_actual}")

    # -------------------------------------------------------------------------
    def _consultar_orden(self):
        orden_id = self.input_id.text().strip()

        if orden_id:
            self.ui.enviar_accion_usuario(
                "consultar_orden",
                {"id": orden_id}
            )
            self._orden_actual = orden_id
            self.label_orden.setText(f"Orden actual: {self._orden_actual}")
