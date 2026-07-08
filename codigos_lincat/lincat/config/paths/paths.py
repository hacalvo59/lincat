# =============================================================================
#  Programa: paths.py
#  Ubicación: codigos_lincat/lincat/config/paths/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Configuración de Rutas del ecosistema LINCAT.
#      Su función es definir, administrar y proveer acceso a todas las rutas
#      internas del framework industrial, garantizando que los módulos puedan
#      localizar sus archivos y carpetas de forma segura y determinística.
#
#  Descripción técnica:
#      - Define rutas base del proyecto.
#      - Administra rutas de módulos internos.
#      - Proporciona métodos para obtener rutas completas.
#      - Permite expandir rutas dinámicamente en futuras integraciones.
#      - Es utilizado por bootstrap.py, database, modules y simulation.
#
#  Versión:
#      v1.0.0 — Implementación inicial de la Configuración de Rutas.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
#  Licencia:
#      Proyecto de código abierto bajo licencia industrial LINCAT.
#
#  Advertencias:
#      - Este archivo es crítico para la estructura del ecosistema.
#      - No insertar lógica de módulos aquí. Solo administración de rutas.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


import os


# =============================================================================
#  CLASE PRINCIPAL DE CONFIGURACIÓN DE RUTAS
# =============================================================================

class PathConfig:
    """
    Configuración de Rutas del ecosistema LINCAT.

    Administra todas las rutas internas del framework industrial.
    """

    def __init__(self, base_path: str = None):
        print(">>> Cargando Configuración de Rutas...")

        # Ruta base del proyecto
        self.base_path = base_path if base_path else os.getcwd()

        # Rutas internas del ecosistema
        self.paths = {
            "core": os.path.join(self.base_path, "lincat", "core"),
            "database": os.path.join(self.base_path, "lincat", "database"),
            "config": os.path.join(self.base_path, "lincat", "config"),
            "modules": os.path.join(self.base_path, "lincat", "modules"),
            "ui": os.path.join(self.base_path, "lincat", "ui"),
            "simulation": os.path.join(self.base_path, "lincat", "simulation"),
            "security": os.path.join(self.base_path, "lincat", "security"),
            "internationalization": os.path.join(self.base_path, "lincat", "internacionalizacion"),
            "docs": os.path.join(self.base_path, "lincat", "docs")
        }

        print(">>> Configuración de Rutas cargada correctamente.")

    # -------------------------------------------------------------------------
    def get(self, key: str):
        """
        Obtiene una ruta interna del ecosistema.
        """

        return self.paths.get(key, None)

    # -------------------------------------------------------------------------
    def set(self, key: str, value: str):
        """
        Establece una ruta interna del ecosistema.
        """

        self.paths[key] = value
        print(f"    [+] Ruta actualizada: {key} = {value}")

    # -------------------------------------------------------------------------
    def exists(self, key: str):
        """
        Verifica si la ruta existe en el sistema de archivos.
        """

        ruta = self.get(key)
        return os.path.exists(ruta)

    # -------------------------------------------------------------------------
    def summary(self):
        """
        Retorna un resumen estructurado de todas las rutas internas.
        """

        return self.paths


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de la Configuración de Rutas")

    paths = PathConfig()

    print("Resumen de rutas:")
    for k, v in paths.summary().items():
        print(f" - {k}: {v}")

    print("Ruta 'core' existe:", paths.exists("core"))
