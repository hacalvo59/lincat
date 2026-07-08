# =============================================================================
#  Programa: panel_calidad_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de Calidad para la UI Qt de LINCAT.
#      Gestiona inspecciones, normas, rechazos y liberaciones de lote.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra automáticamente en lincatqt.py (auto‑descubrimiento).
#      - Usa LincatUI como backend para enviar acciones de calidad.
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


class PanelCalidadQt(QWidget):
    """
    Panel Qt de Calidad para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado = "Calidad: sin acciones recientes"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel de Calidad")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Estado
        self.label_estado = QLabel(self._estado)
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_estado)

        # Lote
        fila_lote = QHBoxLayout()
        self.input_lote = QLineEdit()
        self.input_lote.setPlaceholderText("Lote (ej: LT-2026-001)")
        fila_lote.addWidget(self.input_lote)
        layout.addLayout(fila_lote)

        # Resultado de inspección
        fila_resultado = QHBoxLayout()
        self.combo_resultado = QComboBox()
        self.combo_resultado.addItems([
            "aprobado",
            "rechazado",
            "reinspección",
            "pendiente"
        ])
        fila_resultado.addWidget(self.combo_resultado)
        layout.addLayout(fila_resultado)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_inspeccionar = QPushButton("Registrar inspección")
        btn_inspeccionar.clicked.connect(self._registrar_inspeccion)

        btn_normativa = QPushButton("Consultar normativa")
        btn_normativa.clicked.connect(self._consultar_normativa)

        btn_liberar = QPushButton("Liberar lote")
        btn_liberar.clicked.connect(self._liberar_lote)

        fila_botones.addWidget(btn_inspeccionar)
        fila_botones.addWidget(btn_normativa)
        fila_botones.addWidget(btn_liberar)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _registrar_inspeccion(self):
        lote = self.input_lote.text().strip()
        resultado = self.combo_resultado.currentText()

        self.ui.enviar_accion_usuario(
            "calidad_registrar_inspeccion",
            {"lote": lote, "resultado": resultado}
        )

        self._estado = (
            f"Inspección registrada para lote {lote or 'N/D'} "
            f"→ Resultado: {resultado}"
        )
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _consultar_normativa(self):
        lote = self.input_lote.text().strip()

        self.ui.enviar_accion_usuario(
            "calidad_consultar_normativa",
            {"lote": lote}
        )

        self._estado = f"Consulta de normativa enviada para lote: {lote or 'N/D'}"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _liberar_lote(self):
        lote = self.input_lote.text().strip()

        self.ui.enviar_accion_usuario(
            "calidad_liberar_lote",
            {"lote": lote}
        )

        self._estado = f"Lote liberado: {lote or 'N/D'}"
        self.label_estado.setText(self._estado)
