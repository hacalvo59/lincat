# =============================================================================
#  Programa: panel_seguridad_qt.py
#  Ubicación: lincat/modules/ui/ui_qt/panels/
# =============================================================================
#
#  Propósito:
#      Panel Qt de Seguridad para la UI Qt de LINCAT.
#      Permite gestionar usuarios, roles y bloqueo/desbloqueo de acceso.
#
#  Descripción técnica:
#      - Widget Qt independiente.
#      - Se integra automáticamente en lincatqt.py (auto‑descubrimiento).
#      - Usa LincatUI como backend para enviar acciones de seguridad.
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


class PanelSeguridadQt(QWidget):
    """
    Panel Qt de Seguridad para LINCAT.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LincatUI()
        self._estado = "Seguridad: sin acciones recientes"

        self._crear_layout()

    # -------------------------------------------------------------------------
    def _crear_layout(self):
        layout = QVBoxLayout()

        titulo = QLabel("Panel de Seguridad")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Estado
        self.label_estado = QLabel(self._estado)
        self.label_estado.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_estado)

        # Usuario
        fila_usuario = QHBoxLayout()
        self.input_usuario = QLineEdit()
        self.input_usuario.setPlaceholderText("Usuario (ej: operador01)")
        fila_usuario.addWidget(self.input_usuario)
        layout.addLayout(fila_usuario)

        # Rol
        fila_rol = QHBoxLayout()
        self.combo_rol = QComboBox()
        self.combo_rol.addItems([
            "operador",
            "supervisor",
            "administrador",
            "mantenimiento"
        ])
        fila_rol.addWidget(self.combo_rol)
        layout.addLayout(fila_rol)

        # Botones de acción
        fila_botones = QHBoxLayout()

        btn_asignar = QPushButton("Asignar rol")
        btn_asignar.clicked.connect(self._asignar_rol)

        btn_bloquear = QPushButton("Bloquear usuario")
        btn_bloquear.clicked.connect(self._bloquear_usuario)

        btn_desbloquear = QPushButton("Desbloquear usuario")
        btn_desbloquear.clicked.connect(self._desbloquear_usuario)

        fila_botones.addWidget(btn_asignar)
        fila_botones.addWidget(btn_bloquear)
        fila_botones.addWidget(btn_desbloquear)

        layout.addLayout(fila_botones)

        self.setLayout(layout)

    # -------------------------------------------------------------------------
    def _asignar_rol(self):
        usuario = self.input_usuario.text().strip()
        rol = self.combo_rol.currentText()

        self.ui.enviar_accion_usuario(
            "seguridad_asignar_rol",
            {"usuario": usuario, "rol": rol}
        )

        self._estado = f"Rol '{rol}' asignado a usuario: {usuario or 'N/D'}"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _bloquear_usuario(self):
        usuario = self.input_usuario.text().strip()

        self.ui.enviar_accion_usuario(
            "seguridad_bloquear_usuario",
            {"usuario": usuario}
        )

        self._estado = f"Usuario bloqueado: {usuario or 'N/D'}"
        self.label_estado.setText(self._estado)

    # -------------------------------------------------------------------------
    def _desbloquear_usuario(self):
        usuario = self.input_usuario.text().strip()

        self.ui.enviar_accion_usuario(
            "seguridad_desbloquear_usuario",
            {"usuario": usuario}
        )

        self._estado = f"Usuario desbloqueado: {usuario or 'N/D'}"
        self.label_estado.setText(self._estado)
