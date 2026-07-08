# =============================================================================
#  Programa: panel_normativas_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Implementar el panel gráfico de Normativas para la UI Qt de LINCAT,
#      utilizando PySide6. Este panel permite validar normas industriales y
#      visualizar el estado normativo del ecosistema.
#
#  Descripción técnica:
#      - Es un widget Qt independiente y modular.
#      - Se integra en la ventana principal (lincatqt.py) como panel de normativas.
#      - Usa LincatUI como backend de interfaz (mismo núcleo que CLI/TUI).
#      - Traduce acciones de usuario en ui.enviar_accion_usuario(...).
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del Panel Normativas Qt LINCAT.
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


class PanelNormativasQt(QWidget):
    """
    Panel gráfico de Normativas para la UI Qt de LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Backend de interfaz
        self.ui = LincatUI()

        # Estado interno mínimo
        self._estado_normativa = "Sin validaciones realizadas."

        # Construcción de la UI
        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout_principal = QVBoxLayout()

        # Título del panel
        titulo = QLabel("Panel de Normativas Industriales")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout_principal.addWidget(titulo)

        # Estado normativo
        self.label_estado = QLabel(f"Estado normativo: {self._estado_normativa}")
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout_principal.addWidget(self.label_estado)

        # Campo para ID de norma
        layout_norma = QHBoxLayout()
        self.input_norma = QLineEdit()
        self.input_norma.setPlaceholderText("Norma (ej: ISO-9001)")
        layout_norma.addWidget(self.input_norma)

        layout_principal.addLayout(layout_norma)

        # Campo para contexto de validación
        layout_contexto = QHBoxLayout()
        self.input_contexto = QLineEdit()
        self.input_contexto.setPlaceholderText("Contexto (ej: mecanizado, planta, etc.)")
        layout_contexto.addWidget(self.input_contexto)

        layout_principal.addLayout(layout_contexto)

        # Botones de acción
        layout_botones = QHBoxLayout()

        boton_validar = QPushButton("Validar norma")
        boton_validar.clicked.connect(self._validar_norma)

        boton_limpiar = QPushButton("Limpiar estado")
        boton_limpiar.clicked.connect(self._limpiar_estado)

        layout_botones.addWidget(boton_validar)
        layout_botones.addWidget(boton_limpiar)

        layout_principal.addLayout(layout_botones)

        self.setLayout(layout_principal)

    # -------------------------------------------------------------------------
    def _validar_norma(self):
        norma = self.input_norma.text().strip()
        contexto = self.input_contexto.text().strip()

        if norma:
            self.ui.enviar_accion_usuario(
                "validar_norma",
                {"norma": norma, "contexto": contexto}
            )

            self._estado_normativa = f"Validación enviada: {norma}"
            self.label_estado.setText(f"Estado normativo: {self._estado_normativa}")

    # -------------------------------------------------------------------------
    def _limpiar_estado(self):
        self._estado_normativa = "Sin validaciones realizadas."
        self.label_estado.setText(f"Estado normativo: {self._estado_normativa}")
