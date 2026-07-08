# =============================================================================
#  Programa: mappings.py
#  Ubicación: codigos_lincat/lincat/database/mappings/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Sistema de Mapeo Industrial del ecosistema
#      LINCAT. Su función es relacionar fabricantes, modelos y componentes
#      dentro de una estructura única, ordenada y determinística.
#
#  Descripción técnica:
#      - Permite mapear componentes a modelos.
#      - Permite mapear modelos a fabricantes.
#      - Permite obtener relaciones completas (fabricante → modelo → componente).
#      - Proporciona una estructura base para futuras integraciones SQL.
#      - Es utilizado por módulos como CNC‑CAT, FLOW, EtherCAT y CAM.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Sistema de Mapeo Industrial.
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
#      - Este archivo es crítico para la relación entre datos industriales.
#      - No insertar lógica de módulos aquí. Solo administración de mappings.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DEL SISTEMA DE MAPEOS INDUSTRIALES
# =============================================================================

class MappingDatabase:
    """
    Sistema de Mapeo Industrial del ecosistema LINCAT.

    Administra las relaciones entre fabricantes, modelos y componentes,
    permitiendo obtener información estructurada y completa.
    """

    def __init__(self):
        # Diccionarios de mapeo
        # componente_id → nombre_modelo
        self._component_to_model = {}

        # nombre_modelo → fabricante
        self._model_to_fabricante = {}

        print(">>> Sistema de Mapeo Industrial creado.")

    # -------------------------------------------------------------------------
    def map_component_to_model(self, component_id: str, modelo: str):
        """
        Mapea un componente a un modelo industrial.

        Parámetros:
            component_id (str): ID del componente.
            modelo (str): Nombre del modelo.
        """

        if not isinstance(component_id, str):
            raise TypeError("El ID del componente debe ser una cadena de texto.")

        if not isinstance(modelo, str):
            raise TypeError("El nombre del modelo debe ser una cadena de texto.")

        self._component_to_model[component_id] = modelo
        print(f"    [+] Mapeo agregado: componente '{component_id}' → modelo '{modelo}'")

    # -------------------------------------------------------------------------
    def map_model_to_fabricante(self, modelo: str, fabricante: str):
        """
        Mapea un modelo a un fabricante industrial.

        Parámetros:
            modelo (str): Nombre del modelo.
            fabricante (str): Nombre del fabricante.
        """

        if not isinstance(modelo, str):
            raise TypeError("El nombre del modelo debe ser una cadena de texto.")

        if not isinstance(fabricante, str):
            raise TypeError("El nombre del fabricante debe ser una cadena de texto.")

        self._model_to_fabricante[modelo] = fabricante
        print(f"    [+] Mapeo agregado: modelo '{modelo}' → fabricante '{fabricante}'")

    # -------------------------------------------------------------------------
    def get_model_from_component(self, component_id: str):
        """
        Obtiene el modelo asociado a un componente.
        """

        return self._component_to_model.get(component_id, None)

    # -------------------------------------------------------------------------
    def get_fabricante_from_model(self, modelo: str):
        """
        Obtiene el fabricante asociado a un modelo.
        """

        return self._model_to_fabricante.get(modelo, None)

    # -------------------------------------------------------------------------
    def get_full_mapping(self, component_id: str):
        """
        Obtiene el mapeo completo:
            componente → modelo → fabricante

        Retorna:
            dict con la estructura completa o None si falta información.
        """

        modelo = self.get_model_from_component(component_id)

        if not modelo:
            return None

        fabricante = self.get_fabricante_from_model(modelo)

        return {
            "componente": component_id,
            "modelo": modelo,
            "fabricante": fabricante
        }

    # -------------------------------------------------------------------------
    def list_component_mappings(self):
        """
        Lista todos los componentes mapeados.
        """

        return list(self._component_to_model.keys())

    # -------------------------------------------------------------------------
    def list_model_mappings(self):
        """
        Lista todos los modelos mapeados.
        """

        return list(self._model_to_fabricante.keys())

    # -------------------------------------------------------------------------
    def count(self):
        """
        Retorna la cantidad total de mapeos registrados.
        """

        return len(self._component_to_model)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Sistema de Mapeo Industrial")

    db = MappingDatabase()

    # Mapeos de prueba
    db.map_component_to_model("sensor_temp_01", "TS200")
    db.map_model_to_fabricante("TS200", "Beckhoff")

    print("Mapeo completo:", db.get_full_mapping("sensor_temp_01"))
    print("Componentes mapeados:", db.list_component_mappings())
    print("Modelos mapeados:", db.list_model_mappings())
    print("Cantidad:", db.count())
