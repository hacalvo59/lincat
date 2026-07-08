# =============================================================================
#  Programa: bus.py
#  Ubicación: codigos_lincat/lincat/bus/
# =============================================================================
#
#  Propósito:
#      Este archivo implementa el Módulo LINCAT.bus v2, el bus de eventos
#      industrial del ecosistema LINCAT. Es el idioma común entre todos
#      los módulos presentes y futuros.
#
#  Descripción técnica:
#      - Event bus en memoria, desacoplado.
#      - Namespaces por módulo (cam.*, cnc.*, flow.*, etc.).
#      - Categorías de eventos (estado, comando, resultado, error, etc.).
#      - Registro de tipos de eventos previstos para todo el ecosistema.
#      - Publicación y suscripción por nombre de evento.
#
#  Versión:
#      v2.0.0 — Bus industrial con mapa completo de módulos.
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
#      - Este bus es el sistema nervioso del ecosistema LINCAT.
#      - No insertar lógica de negocio aquí. Solo transporte de eventos.
#      - Cambios deben ser revisados por ingeniería antes de aplicarse.
#
# =============================================================================


from typing import Callable, Dict, List, Any


# =============================================================================
#  DEFINICIÓN DEL MAPA DE MÓDULOS Y EVENTOS
# =============================================================================

MODULOS_PREVISTOS = [
    "cam",
    "cnc",
    "flow",
    "ethercat",
    "maestro",
    "seguridad",
    "produccion",
    "planta",
    "normativas",
    "auxiliar",
    "ui",
    "config",
    "sim",
    "intl",
    "hardware",
    "driver",
    "kernel"
]

CATEGORIAS_EVENTO = [
    "estado",
    "comando",
    "resultado",
    "error",
    "auditoria",
    "proceso",
    "trayectoria",
    "orden",
    "alarma",
    "metrica",
    "configuracion",
    "internacionalizacion",
    "simulacion",
    "hardware",
    "driver",
    "kernel"
]

# Eventos estándar previstos (no limitan, solo documentan)
EVENTOS_PREDEFINIDOS = {
    "cam.trayectoria_generada": "Trayectoria CAM lista para CNC.",
    "cnc.movimiento_ejecutado": "Movimiento ejecutado por CNC.",
    "flow.paso_ejecutado": "Paso de proceso FLOW ejecutado.",
    "ethercat.estado_driver": "Estado de driver EtherCAT.",
    "seguridad.enclavamiento_fallo": "Fallo en enclavamiento de seguridad.",
    "produccion.orden_creada": "Orden de producción creada.",
    "produccion.orden_actualizada": "Orden de producción actualizada.",
    "planta.maquina_estado": "Estado de máquina en planta.",
    "normativas.norma_validada": "Norma marcada como cumplida.",
    "ui.evento_usuario": "Evento generado por la UI.",
    "config.cambio_parametro": "Cambio de parámetro de configuración.",
    "sim.frame_generado": "Frame de simulación generado.",
    "intl.idioma_cambiado": "Cambio de idioma del sistema.",
    "hardware.sensor_lectura": "Lectura de sensor físico.",
    "driver.pdo_actualizado": "Actualización de PDO de driver.",
    "kernel.evento_sistema": "Evento del sistema operativo."
}


# =============================================================================
#  CLASE PRINCIPAL DEL BUS DE EVENTOS
# =============================================================================

class LincatBus:
    """
    LINCAT.bus v2 — Bus de eventos industrial del ecosistema LINCAT.

    Características:
        - publish/subscribe desacoplado
        - namespaces por módulo
        - mapa de eventos previsto
        - sin lógica de negocio
    """

    def __init__(self):
        print(">>> LINCAT.bus v2 inicializado.")

        # Mapa: nombre_evento -> lista de callbacks
        self._suscriptores: Dict[str, List[Callable[[Any], None]]] = {}

        # Registro de eventos conocidos (documentación interna)
        self._eventos_registrados: Dict[str, str] = dict(EVENTOS_PREDEFINIDOS)

    # -------------------------------------------------------------------------
    def registrar_evento(self, nombre: str, descripcion: str = "") -> None:
        """
        Registra un evento en el mapa interno (documentación).

        Parámetros:
            nombre (str): Nombre completo del evento (ej: 'cam.trayectoria_generada').
            descripcion (str): Descripción técnica del evento.
        """

        self._eventos_registrados[nombre] = descripcion or "Evento sin descripción."
        print(f"    [+] Evento registrado en mapa: '{nombre}'")

    # -------------------------------------------------------------------------
    def suscribir(self, evento: str, callback: Callable[[Any], None]) -> None:
        """
        Suscribe un callback a un evento.

        Parámetros:
            evento (str): Nombre del evento (ej: 'cam.trayectoria_generada').
            callback (callable): Función que recibe los datos del evento.
        """

        if evento not in self._suscriptores:
            self._suscriptores[evento] = []

        self._suscriptores[evento].append(callback)

        print(f"    [+] Suscripción: evento='{evento}', callback='{callback.__name__}'")

        # Si el evento no estaba registrado, lo añadimos sin descripción
        if evento not in self._eventos_registrados:
            self.registrar_evento(evento, "Evento dinámico no predefinido.")

    # -------------------------------------------------------------------------
    def publicar(self, evento: str, datos: Any = None) -> None:
        """
        Publica un evento en el bus.

        Parámetros:
            evento (str): Nombre del evento.
            datos (Any): Datos asociados al evento.
        """

        print(f"    [BUS] Publicando evento: '{evento}' con datos: {datos}")

        if evento not in self._suscriptores:
            print(f"    [BUS] No hay suscriptores para el evento '{evento}'.")
            return

        for callback in self._suscriptores[evento]:
            try:
                callback(datos)
            except Exception as e:
                print(f"    [BUS] Error en callback '{callback.__name__}' para evento '{evento}': {e}")

    # -------------------------------------------------------------------------
    def listar_eventos(self) -> Dict[str, Dict[str, Any]]:
        """
        Retorna un resumen de eventos:
            - descripción
            - cantidad de suscriptores
        """

        resumen = {}
        for nombre, desc in self._eventos_registrados.items():
            cantidad = len(self._suscriptores.get(nombre, []))
            resumen[nombre] = {
                "descripcion": desc,
                "suscriptores": cantidad
            }
        return resumen

    # -------------------------------------------------------------------------
    def eventos_por_modulo(self, modulo: str) -> Dict[str, Dict[str, Any]]:
        """
        Retorna los eventos asociados a un módulo (namespace).

        Parámetros:
            modulo (str): Nombre del módulo (ej: 'cam', 'cnc', 'flow').
        """

        prefijo = f"{modulo}."
        return {
            nombre: data
            for nombre, data in self.listar_eventos().items()
            if nombre.startswith(prefijo)
        }


# =============================================================================
#  PUNTO DE PRUEBA LOCAL (solo para desarrollo)
# =============================================================================

if __name__ == "__main__":
    print(">>> Prueba local de LINCAT.bus v2")

    bus = LincatBus()

    # Ejemplo de suscriptores
    def on_cam_trayectoria(datos):
        print(f"        [CAM→CNC] Trayectoria recibida en CNC: {datos}")

    def on_flow_paso(datos):
        print(f"        [FLOW→SEGURIDAD] Paso ejecutado: {datos}")

    def on_produccion_orden(datos):
        print(f"        [PRODUCCIÓN→PLANTA] Orden: {datos}")

    # Suscribir callbacks
    bus.suscribir("cam.trayectoria_generada", on_cam_trayectoria)
    bus.suscribir("flow.paso_ejecutado", on_flow_paso)
    bus.suscribir("produccion.orden_creada", on_produccion_orden)

    # Publicar eventos
    bus.publicar("cam.trayectoria_generada", {"tipo": "contour", "puntos": [(0, 0), (10, 0)]})
    bus.publicar("flow.paso_ejecutado", {"paso": "activar_valvula"})
    bus.publicar("produccion.orden_creada", {"id": "ORD001", "descripcion": "Mecanizado pieza A"})

    print("\nResumen de eventos:")
    for nombre, info in bus.listar_eventos().items():
        print(f"    - {nombre}: {info}")

    print("\nEventos CAM:")
    for nombre, info in bus.eventos_por_modulo("cam").items():
        print(f"    - {nombre}: {info}")
