# =============================================================================
#  Programa: ui_cli.py
#  Ubicación: lincat/modules/ui/ui_cli/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Interfaz de Línea de Comandos (CLI) del
#      ecosistema LINCAT. La CLI permite la interacción del operador humano
#      mediante comandos textuales, traduciendo dichas acciones en eventos
#      ui.evento_usuario publicados en el bus LINCAT.bus.
#
#  Descripción técnica:
#      - La CLI es un frontend humano.
#      - La lógica de interfaz está en ui.py (backend de UI).
#      - ui_cli.py interpreta texto y llama a ui.enviar_accion_usuario().
#      - No escucha el bus directamente.
#      - No integra ni depende de ningún módulo industrial.
#      - Registra paneles CLI que sí escuchan el bus.
#      - Totalmente desacoplada del ecosistema.
#
#  Paneles registrados:
#      • PanelEstadoPlanta
#      • PanelOrdenes
#      • PanelNormativas
#      • PanelMaestro
#
#  Versión:
#      v2.0.0 — Versión estable con paneles CLI integrados.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
# =============================================================================


from lincat.modules.ui.ui import LincatUI

# Paneles CLI
from lincat.modules.ui.ui_cli.panels.panel_estado import PanelEstadoPlanta
from lincat.modules.ui.ui_cli.panels.panel_ordenes import PanelOrdenes
from lincat.modules.ui.ui_cli.panels.panel_normativas import PanelNormativas
from lincat.modules.ui.ui_cli.panels.panel_maestro import PanelMaestro


class LincatCLI:
    """
    Interfaz de Línea de Comandos (CLI) del ecosistema LINCAT.

    Traduce comandos textuales del operador en eventos ui.evento_usuario.
    """

    def __init__(self):
        print(">>> UI CLI LINCAT inicializada.")

        # Backend de UI
        self.ui = LincatUI()

        # Registrar comandos
        self._registrar_comandos()

        # Registrar paneles CLI
        PanelEstadoPlanta()
        PanelOrdenes()
        PanelNormativas()
        PanelMaestro()

        print(">>> Paneles CLI cargados correctamente.\n")

    # -------------------------------------------------------------------------
    def _registrar_comandos(self):
        """
        Registra los comandos disponibles en la CLI.
        """

        self.comandos = {
            "iniciar": self._cmd_iniciar,
            "detener": self._cmd_detener,
            "estado": self._cmd_estado,
            "salir": self._cmd_salir
        }

    # -------------------------------------------------------------------------
    def _cmd_iniciar(self, args):
        """
        Comando: iniciar
        Traduce: iniciar proceso / iniciar orden / iniciar acción.
        """

        self.ui.enviar_accion_usuario("iniciar", {"args": args})

    # -------------------------------------------------------------------------
    def _cmd_detener(self, args):
        """
        Comando: detener
        Traduce: detener proceso / detener orden / detener acción.
        """

        self.ui.enviar_accion_usuario("detener", {"args": args})

    # -------------------------------------------------------------------------
    def _cmd_estado(self, args):
        """
        Comando: estado
        Traduce: solicitar estado de máquina, orden o sistema.
        """

        self.ui.enviar_accion_usuario("estado", {"args": args})

    # -------------------------------------------------------------------------
    def _cmd_salir(self, args):
        """
        Comando: salir
        Finaliza la CLI.
        """

        print(">>> Saliendo de LINCAT CLI...")
        exit(0)

    # -------------------------------------------------------------------------
    def loop(self):
        """
        Loop principal de la CLI.

        Mantiene la interacción con el operador humano.
        """

        print("\n>>> CLI lista. Escriba comandos.\n")

        while True:
            entrada = input("LINCAT> ").strip()

            if not entrada:
                continue

            partes = entrada.split()
            comando = partes[0]
            args = partes[1:]

            if comando in self.comandos:
                self.comandos[comando](args)
            else:
                print(f"[CLI] Comando desconocido: {comando}")
