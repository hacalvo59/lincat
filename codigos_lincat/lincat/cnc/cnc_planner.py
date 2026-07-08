# ============================================================
#  CNC PLANNER — LINCAT
#  Convierte trayectorias optimizadas en segmentos ejecutables
# ============================================================

class CNCPlanner:
    """
    Planner CNC:
    - recibe trayectoria optimizada
    - divide en segmentos ejecutables
    - prepara datos para el interpolador
    """

    def __init__(self):
        self.segments = []

    def load_optimized_trajectory(self, trajectory):
        """
        Recibe la trayectoria optimizada desde CAM/Optimizer.
        """
        self.segments = trajectory.get("segments", [])

    def generate_execution_plan(self):
        """
        Convierte los segmentos en un plan ejecutable:
        - feedrate por tramo
        - aceleración por tramo
        - jerk por tramo
        - tipo de interpolación
        """
        plan = []

        for seg in self.segments:
            plan.append({
                "type": seg.get("type", "line"),
                "start": seg.get("start"),
                "end": seg.get("end"),
                "feedrate": seg.get("feedrate"),
                "acceleration": seg.get("acceleration"),
                "jerk": seg.get("jerk")
            })

        return plan
