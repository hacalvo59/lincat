# ============================================================
#  OPTIMIZER CAM INTERFACE — LINCAT
#  Interfaz entre CAM y el Optimizador de Trayectorias
#  Autor: Hugo Alberto Calvo
#  Fecha: 2026-07-05
# ============================================================

from core.optimizer_core import OptimizerCore

class OptimizerCAMInterface:
    """
    Interfaz entre el módulo CAM y el OptimizerCore.
    Se encarga de:
    - recibir trayectorias CAM
    - enviarlas al optimizador
    - devolver la versión optimizada
    - exponer resultados a UI
    """

    def __init__(self, twin=None, cnc=None):
        # El núcleo del optimizador
        self.optimizer = OptimizerCore(twin=twin, cnc=cnc)

        # Últimos datos procesados
        self.last_original = None
        self.last_optimized = None
        self.last_report = None

    # ------------------------------------------------------------
    # 1. Cargar trayectoria CAM
    # ------------------------------------------------------------
    def load_cam_trajectory(self, trajectory):
        """
        Recibe una trayectoria generada por CAM.
        La guarda internamente para ser optimizada.
        """
        self.last_original = trajectory

    # ------------------------------------------------------------
    # 2. Enviar trayectoria al OptimizerCore
    # ------------------------------------------------------------
    def send_to_optimizer(self):
        """
        Envía la trayectoria cargada al OptimizerCore.
        Devuelve un diccionario con:
        - original
        - analysis
        - simulation
        - score
        - optimized
        """
        if self.last_original is None:
            raise RuntimeError("No hay trayectoria CAM cargada.")

        result = self.optimizer.generate_optimized_trajectory(self.last_original)

        self.last_report = result
        self.last_optimized = result["optimized"]

        return result

    # ------------------------------------------------------------
    # 3. Obtener trayectoria optimizada
    # ------------------------------------------------------------
    def get_optimized_trajectory(self):
        """
        Devuelve la última trayectoria optimizada generada.
        """
        return self.last_optimized

    # ------------------------------------------------------------
    # 4. Exportar reporte para UI
    # ------------------------------------------------------------
    def export_to_ui(self):
        """
        Devuelve el reporte completo para ser mostrado en UI:
        - análisis
        - simulación
        - score
        - trayectoria optimizada
        """
        return self.last_report
