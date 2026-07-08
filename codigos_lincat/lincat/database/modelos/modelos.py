# =============================================================================
#  Programa: modelos.py
#  Ubicación: codigos_lincat/lincat/database/modelos/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Base de Datos de Modelos Industriales del
#      ecosistema LINCAT. Su función es almacenar, administrar y proveer acceso
#      estructurado a todos los modelos de componentes utilizados por el
#      sistema y sus módulos (CNC‑CAT, FLOW, EtherCAT, CAM, etc.).
#
#  Descripción técnica:
#      - Administra modelos industriales asociados a fabricantes y componentes.
#      - Permite registrar, obtener, listar y buscar modelos.
#      - Proporciona una estructura base para futuras integraciones SQL.
#      - Se integra con los módulos de componentes, fabricantes y mappings.
#
#  Versión:
#      v1.0.0 — Implementación inicial de la Base de Datos de Modelos.
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
#      - Este archivo es crítico para la gestión de modelos industriales.
#      - No insertar lógica de módulos aquí. Solo administración de datos.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DE LA BASE DE DATOS DE MODELOS
# =============================================================================

class ModeloDatabase:
    """
    Base de Datos de Modelos Industriales del ecosistema LINCAT.

    Administra todos los modelos utilizados por el sistema, permitiendo
    registrar, obtener, listar y buscar elementos de forma estructurada.
    """

    def __init__(self):
        # Diccionario donde se almacenan los modelos.
        # Clave: nombre del modelo
        # Valor: diccionario con datos del modelo
        self._modelos = {}

        print(">>> Base de Datos de Modelos creada.")

    # -------------------------------------------------------------------------
    def register(self, nombre_modelo: str, data: dict):
        """
        Registra un modelo industrial.

        Parámetros:
            nombre_modelo (str): Nombre del modelo (único).
            data (dict): Información estructurada del modelo.

        Requisitos:
            - nombre_modelo debe ser único.
            - data debe ser un diccionario válido.
        """

        if not isinstance(nombre_modelo, str):
            raise TypeError("El nombre del modelo debe ser una cadena de texto.")

        if not isinstance(data, dict):
            raise TypeError("Los datos del modelo deben ser un diccionario.")

        if nombre_modelo in self._modelos:
            raise ValueError(f"El modelo '{nombre_modelo}' ya está registrado.")

        self._modelos[nombre_modelo] = data
        print(f"    [+] Modelo registrado: {nombre_modelo}")

    # -------------------------------------------------------------------------
    def get(self, nombre_modelo: str):
        """
        Obtiene un modelo por su nombre.
        """

        return self._modelos.get(nombre_modelo, None)

    # -------------------------------------------------------------------------
    def list_modelos(self):
        """
        Lista todos los modelos registrados.
        """

        return list(self._modelos.keys())

    # -------------------------------------------------------------------------
    def search(self, key: str, value):
        """
        Busca modelos por un campo específico.

        Parámetros:
            key (str): Campo a buscar.
            value: Valor a comparar.

        Retorna:
            Lista de nombres de modelos que coinciden.
        """

        results = []

        for nombre, data in self._modelos.items():
            if key in data and data[key] == value:
                results.append(nombre)

        return results

    # -------------------------------------------------------------------------
    def count(self):
        """
        Retorna la cantidad de modelos registrados.
        """

        return len(self._modelos)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de la Base de Datos de Modelos")

    db = ModeloDatabase()

    # Registro de prueba
    db.register("TS200", {
        "fabricante": "Beckhoff",
        "tipo": "sensor",
        "categoria": "temperatura",
        "rango": "-20 a 120°C"
    })

    db.register("AX5000", {
        "fabricante": "Beckhoff",
        "tipo": "driver",
        "categoria": "servo",
        "potencia": "5 kW"
    })

    print("Modelos registrados:", db.list_modelos())
    print("Cantidad:", db.count())

    print("Búsqueda por tipo:", db.search("tipo", "sensor"))
