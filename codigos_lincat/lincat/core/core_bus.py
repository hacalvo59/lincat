# =============================================================================
#  Programa: core_bus.py
#  Ubicación: codigos_lincat/lincat/core/
# =============================================================================
#
#  Propósito:
#      Este archivo define la instancia global del bus industrial LINCAT.bus.
#      Todos los módulos del ecosistema deben importar esta instancia para
#      publicar y suscribirse a eventos.
#
#  Descripción técnica:
#      - Contiene una única instancia de LincatBus.
#      - Evita duplicación de buses.
#      - Garantiza un idioma común para todos los módulos.
#
#  Versión:
#      v1.0.0 — Núcleo del bus industrial.
#
#  Autor:
#      Proyecto LINCAT — Ingeniería Industrial en Plataforma Linux.
#      Responsable: Hugo Alberto Calvo.
#
#  Fecha:
#      04/07/2026 — Barcelona, España.
#
# =============================================================================

from lincat.bus.bus import LincatBus

# Instancia global del bus industrial
bus = LincatBus()

print(">>> Núcleo del bus industrial cargado (core_bus.py)")
