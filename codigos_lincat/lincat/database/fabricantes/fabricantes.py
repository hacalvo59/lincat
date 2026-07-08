# =============================================================================
#  Programa: fabricantes.py
#  Ubicación: codigos_lincat/lincat/database/fabricantes/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Base de Datos de Fabricantes Industriales
#      del ecosistema LINCAT. Su función es almacenar, administrar y proveer
#      acceso estructurado a todos los fabricantes de componentes utilizados
#      por el sistema y sus módulos (CNC‑CAT, FLOW, EtherCAT, CAM, etc.).
#
#  Descripción técnica:
#      - Administra fabricantes industriales (Siemens, Beckhoff, Omron, Festo,
#        Schneider, Allen‑Bradley, etc.).
#      - Permite registrar, obtener, listar y buscar fabricantes.
#      - Proporciona una estructura base para futuras integraciones SQL.
#      - Se integra con los módulos de componentes, modelos y mappings.
#
#  Versión:
#      v1.0.0 — Implementación inicial de la Base de Datos de Fabricantes.
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
#      - Este archivo es crítico para la gestión de fabricantes industriales.
#      - No insertar lógica de módulos aquí. Solo administración de datos.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DE LA BASE DE DATOS DE FABRICANTES
# =============================================================================

class FabricanteDatabase:
    """
    Base de Datos de Fabricantes Industriales del ecosistema LINCAT.

    Administra todos los fabricantes utilizados por el sistema, permitiendo
    registrar, obtener, listar y buscar elementos de forma estructurada.
    """

    def __init__(self):
        # Diccionario donde se almacenan los fabricantes.
        # Clave: nombre del fabricante
        # Valor: diccionario con datos del fabricante
        self._fabricantes = {}

        print(">>> Base de Datos de Fabricantes creada.")

    # -------------------------------------------------------------------------
    def register(self, nombre: str, data: dict):
        """
        Registra un fabricante industrial.

        Parámetros:
            nombre (str): Nombre del fabricante (único).
            data (dict): Información estructurada del fabricante.

        Requisitos:
            - nombre debe ser único.
            - data debe ser un diccionario válido.
        """

        if not isinstance(nombre, str):
            raise TypeError("El nombre del fabricante debe ser una cadena de texto.")

        if not isinstance(data, dict):
            raise TypeError("Los datos del fabricante deben ser un diccionario.")

        if nombre in self._fabricantes:
            raise ValueError(f"El fabricante '{nombre}' ya está registrado.")

        self._fabricantes[nombre] = data
        print(f"    [+] Fabricante registrado: {nombre}")

    # -------------------------------------------------------------------------
    def get(self, nombre: str):
        """
        Obtiene un fabricante por su nombre.
        """

        return self._fabricantes.get(nombre, None)

    # -------------------------------------------------------------------------
    def list_fabricantes(self):
        """
        Lista todos los fabricantes registrados.
        """

        return list(self._fabricantes.keys())

    # -------------------------------------------------------------------------
    def search(self, key: str, value):
        """
        Busca fabricantes por un campo específico.

        Parámetros:
            key (str): Campo a buscar.
            value: Valor a comparar.

        Retorna:
            Lista de nombres de fabricantes que coinciden.
        """

        results = []

        for nombre, data in self._fabricantes.items():
            if key in data and data[key] == value:
                results.append(nombre)

        return results

    # -------------------------------------------------------------------------
    def count(self):
        """
        Retorna la cantidad de fabricantes registrados.
        """

        return len(self._fabricantes)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de la Base de Datos de Fabricantes")

    db = FabricanteDatabase()

    # Registro de prueba
    db.register("Beckhoff", {
        "pais": "Alemania",
        "especialidad": "Automatización industrial",
        "fundacion": 1980
    })

    db.register("Siemens", {
        "pais": "Alemania",
        "especialidad": "Automatización y energía",
        "fundacion": 1847
    })

    print("Fabricantes registrados:", db.list_fabricantes())
    print("Cantidad:", db.count())

    print("Búsqueda por país:", db.search("pais", "Alemania"))
