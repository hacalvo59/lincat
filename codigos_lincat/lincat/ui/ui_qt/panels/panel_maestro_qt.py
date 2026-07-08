# =============================================================================
#  Programa: panel_maestro_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt del módulo Maestro para la UI Qt de LINCAT.
#      Permite iniciar/detener procesos y mostrar comandos emitidos.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra en lincatqt.py.
#      - Usa LincatUI como backend.
#      - No toca módulos industriales directamente.
#      - Totalmente desacoplado.
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
    QTextEdit
)
from PySide6.QtCore import Qt

from lincat.modules.ui.ui import LincatUI


class PanelMaestroQt(QWidget):
    """
    Panel Maestro Qt — Control industrial del módulo Maestro.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._buffer = []

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel Maestro — Control Industrial")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Zona de comandos
        self.texto = QTextEdit()
        self.texto.setReadOnly(True)
        self.texto.setPlaceholderText("Comandos del Maestro aparecerán aquí...")
        layout.addWidget(self.texto)

        # Botones
        botones = QHBoxLayout()

        btn_iniciar = QPushButton("Iniciar proceso")
        btn_iniciar.clicked.connect(lambda: self._accion("maestro_iniciar"))

        btn_detener = QPushButton("Detener proceso")
        btn_detener.clicked.connect(lambda: self._accion("maestro_detener"))

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)

        botones.addWidget(btn_iniciar)
        botones.addWidget(btn_detener)
        botones.addWidget(btn_limpiar)

        layout.addLayout(botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _accion(self, accion: str):
        self.ui.enviar_accion_usuario(accion, {})
        self._agregar(f"Acción enviada al Maestro: {accion}")

    # -------------------------------------------------------------------------
    def _agregar(self, texto: str):
        self._buffer.append(texto)
        self.texto.setPlainText("\n".join(self._buffer))

    # -------------------------------------------------------------------------
    def recibir_comando_maestro(self, datos: dict):
        """
        Método opcional para recibir comandos desde el BUS.
        """
        self._agregar(f"Comando Maestro recibido → {datos}")

    # -------------------------------------------------------------------------
    def _limpiar(self):
        self._buffer = []
        self.texto.clear()
