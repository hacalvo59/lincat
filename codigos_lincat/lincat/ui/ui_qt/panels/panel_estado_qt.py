# =============================================================================
#  Programa: panel_estado_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Implementar el panel gráfico de Estado/Planta para la UI Qt de LINCAT,
#      utilizando PySide6. Este panel muestra información básica del estado
#      del sistema y de la planta, y permite acciones rápidas.
#
#  Descripción técnica:
#      - Es un widget Qt independiente y modular.
#      - Se integra en la ventana principal (lincatqt.py) como panel de estado.
#      - Usa LincatUI como backend de interfaz (mismo núcleo que CLI/TUI).
#      - Traduce acciones de usuario en ui.enviar_accion_usuario(...).
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado del ecosistema.
#
#  Versión:
#      v1.0.0 — Primera versión estable del Panel Estado Qt LINCAT.
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
)
from PySide6.QtCore import Qt

from lincat.modules.ui.ui import LincatUI


class PanelEstadoQt(QWidget):
    """
    Panel gráfico de Estado/Planta para la UI Qt de LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Backend de interfaz
        self.ui = LincatUI()

        # Estado interno mínimo
        self._estado_texto = "Estado: desconocido"

        # Construcción de la UI
        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout_principal = QVBoxLayout()

        # Título del panel
        titulo = QLabel("Panel de Estado / Planta")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout_principal.addWidget(titulo)

        # Línea de estado
        layout_estado = QHBoxLayout()

        self.label_estado = QLabel(self._estado_texto)
        self.label_estado.setAlignment(Qt.AlignLeft)

        boton_actualizar = QPushButton("Actualizar estado")
        boton_actualizar.clicked.connect(
            lambda: self._accion_usuario("estado", {})
        )

        layout_estado.addWidget(self.label_estado)
        layout_estado.addWidget(boton_actualizar)

        layout_principal.addLayout(layout_estado)

        # Acciones rápidas de planta
        layout_acciones = QHBoxLayout()

        boton_iniciar_planta = QPushButton("Iniciar planta")
        boton_iniciar_planta.clicked.connect(
            lambda: self._accion_usuario("iniciar_planta", {})
        )

        boton_detener_planta = QPushButton("Detener planta")
        boton_detener_planta.clicked.connect(
            lambda: self._accion_usuario("detener_planta", {})
        )

        layout_acciones.addWidget(boton_iniciar_planta)
        layout_acciones.addWidget(boton_detener_planta)

        layout_principal.addLayout(layout_acciones)

        self.setLayout(layout_principal)

    # -------------------------------------------------------------------------
    def _accion_usuario(self, accion: str, datos: dict):
        """
        Traduce una acción del panel al backend LincatUI.
        """

        self.ui.enviar_accion_usuario(accion, datos)

        # Feedback mínimo en el propio panel
        if accion == "estado":
            self._estado_texto = "Estado: consulta enviada al backend."
            self.label_estado.setText(self._estado_texto)
        elif accion == "iniciar_planta":
            self._estado_texto = "Estado: planta en proceso de inicio."
            self.label_estado.setText(self._estado_texto)
        elif accion == "detener_planta":
            self._estado_texto = "Estado: planta en proceso de parada."
            self.label_estado.setText(self._estado_texto)
