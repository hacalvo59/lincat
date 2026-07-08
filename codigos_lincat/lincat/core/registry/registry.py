# =============================================================================
#  Programa: registry.py
#  Ubicación: codigos_lincat/lincat/core/registry/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Registro Global de Módulos del ecosistema
#      LINCAT. Su función es administrar todos los módulos que se integran al
#      framework industrial, garantizando que cada uno sea identificado,
#      validado, inicializado y gestionado de forma segura y determinística.
#
#  Descripción técnica:
#      - Mantiene una lista estructurada de módulos registrados.
#      - Verifica que cada módulo cumpla con los requisitos del ecosistema.
#      - Proporciona métodos para registrar, obtener y listar módulos.
#      - Actúa como punto central de referencia para el núcleo del sistema.
#      - Es utilizado por bootstrap.py durante la inicialización del framework.
#
#  Versión:
#      v1.0.0 — Implementación inicial del Registro Global de Módulos.
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
#      Uso permitido para fabricantes, ensambladores, universidades,
#      ingenieros, operadores y organizaciones sin fines de lucro.
#
#  Advertencias:
#      - Este archivo es crítico para la arquitectura modular.
#      - No insertar lógica de módulos aquí. Solo administración del registro.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


# =============================================================================
#  CLASE PRINCIPAL DEL REGISTRO GLOBAL DE MÓDULOS
# =============================================================================

class ModuleRegistry:
    """
    Registro Global de Módulos del ecosistema LINCAT.

    Esta clase administra todos los módulos que se integran al framework.
    Permite registrar módulos, obtenerlos y listar los que están activos.
    """

    def __init__(self):
        # Diccionario donde se almacenan los módulos registrados.
        # Clave: nombre del módulo
        # Valor: instancia del módulo
        self._modules = {}

        print(">>> Registro Global de Módulos creado.")

    # -------------------------------------------------------------------------
    def register(self, name: str, module_instance):
        """
        Registra un módulo en el ecosistema LINCAT.

        Parámetros:
            name (str): Nombre único del módulo.
            module_instance: Instancia del módulo a registrar.

        Requisitos:
            - El nombre debe ser único.
            - El módulo debe ser una instancia válida.
        """

        if not isinstance(name, str):
            raise TypeError("El nombre del módulo debe ser una cadena de texto.")

        if name in self._modules:
            raise ValueError(f"El módulo '{name}' ya está registrado.")

        self._modules[name] = module_instance
        print(f"    [+] Módulo registrado: {name}")

    # -------------------------------------------------------------------------
    def get(self, name: str):
        """
        Obtiene un módulo registrado por su nombre.

        Parámetros:
            name (str): Nombre del módulo.

        Retorna:
            Instancia del módulo si existe, de lo contrario None.
        """

        return self._modules.get(name, None)

    # -------------------------------------------------------------------------
    def list_modules(self):
        """
        Lista todos los módulos registrados en el ecosistema.

        Retorna:
            Lista de nombres de módulos registrados.
        """

        return list(self._modules.keys())

    # -------------------------------------------------------------------------
    def count(self):
        """
        Retorna la cantidad de módulos registrados.
        """

        return len(self._modules)


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local del Registro Global de Módulos")

    registry = ModuleRegistry()

    # Registro de prueba
    registry.register("modulo_prueba", object())

    print("Módulos registrados:", registry.list_modules())
    print("Cantidad:", registry.count())
