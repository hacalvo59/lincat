# =============================================================================
#  Programa: componentes.py
#  Ubicación: codigos_lincat/lincat/database/componentes/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa la Base de Datos de Componentes Industriales
#      del ecosistema LINCAT. Su función es almacenar, administrar y proveer
#      acceso estructurado a todos los componentes utilizados por fabricantes,
#      ensambladores, ingenieros y módulos del sistema.
#
#  Descripción técnica:
#      - Administra componentes industriales (sensores, actuadores, módulos IO,
#        controladores, motores, drivers, etc.).
#      - Permite registrar, obtener, listar y buscar componentes.
#      - Proporciona una estructura base para futuras integraciones con SQL.
#      - Es utilizado por módulos como CNC‑CAT, FLOW, EtherCAT y CAM.
#
#  Versión:
#      v1.0.0 — Implementación inicial de la Base de Datos de Componentes.
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
#      - Este archivo es crítico para la gestión de hardware industrial.
#      - No insertar lógica de módulos aquí. Solo administración de datos.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DE LA BASE DE DATOS DE COMPONENTES
# =============================================================================

class ComponentDatabase:
    """
    Base de Datos de Componentes Industriales del ecosistema LINCAT.

    Administra todos los componentes utilizados por el sistema, permitiendo
    registrar, obtener, listar y buscar elementos de forma estructurada.
    """

    def __init__(self):
        # Diccionario donde se almacenan los componentes.
        # Clave: ID del componente
        # Valor: diccionario con datos del componente
        self._components = {}

        print(">>> Base de Datos de Componentes creada.")

    # -------------------------------------------------------------------------
    def register(self, component_id: str, data: dict):
        """
        Registra un componente industrial.

        Parámetros:
            component_id (str): Identificador único del componente.
            data (dict): Información estructurada del componente.

        Requisitos:
            - component_id debe ser único.
            - data debe ser un diccionario válido.
        """

        if not isinstance(component_id, str):
            raise TypeError("El ID del componente debe ser una cadena de texto.")

        if not isinstance(data, dict):
            raise TypeError("Los datos del componente deben ser un diccionario.")

        if component_id in self._components:
            raise ValueError(f"El componente '{component_id}' ya está registrado.")

        self._components[component_id] = data
        print(f"    [+] Componente registrado: {component_id}")

    # -------------------------------------------------------------------------
    def get(self, component_id: str):
        """
        Obtiene un componente por su ID.
        """

        return self._components.get(component_id, None)

    # -------------------------------------------------------------------------
    def list_components(self):
        """
        Lista todos los componentes registrados.
        """

        return list(self._components.keys())

    # -------------------------------------------------------------------------
    def search(self, key: str, value):
        """
        Busca componentes por un campo específico.

        Parámetros:
            key (str): Campo a buscar.
            value: Valor a comparar.

        Retorna:
            Lista de IDs de componentes que coinciden.
        """

        results = []

        for cid, data in self._components.items():
            if key in data and data[key] == value:
                results.append(cid)

        return results

    # -------------------------------------------------------------------------
    def count(self):
        """
        Retorna la cantidad de componentes registrados.
        """

        return len(self._components)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de la Base de Datos de Componentes")

    db = ComponentDatabase()

    # Registro de prueba
    db.register("sensor_temp_01", {
        "tipo": "sensor",
        "fabricante": "Beckhoff",
        "modelo": "TS200",
        "rango": "-20 a 120°C"
    })

    print("Componentes registrados:", db.list_components())
    print("Cantidad:", db.count())

    print("Búsqueda por fabricante:", db.search("fabricante", "Beckhoff"))
