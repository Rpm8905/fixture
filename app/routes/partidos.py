from flask import Blueprint, jsonify, request
from app.services.partido_service import (
    obtener_todos_los_partidos,
    obtener_partido_por_id,
    crear_partido,
    eliminar_partido,
    validar_partido,
    contar_partidos
)
from app.utils.paginacion import construir_links_paginacion

partidos_bp = Blueprint("partidos", __name__)


@partidos_bp.route("/partidos", methods=["GET"])
def get_partidos():
    filtro_equipo = request.args.get("equipo")
    filtro_fecha  = request.args.get("fecha")
    filtro_fase   = request.args.get("fase")
    cantidad      = int(request.args.get("_limit", 10))
    desde         = int(request.args.get("_offset", 0))

    partidos, error = obtener_todos_los_partidos(
        equipo = filtro_equipo,
        fecha  = filtro_fecha,
        fase   = filtro_fase,
        limit  = cantidad,
        offset = desde
    )

    if error:
        return jsonify({"errors": [error]}), 400

    if not partidos:
        return "", 204

    total_partidos = contar_partidos(
        equipo = filtro_equipo,
        fecha  = filtro_fecha,
        fase   = filtro_fase
    )

    links = construir_links_paginacion(
        url_base        = request.base_url,
        offset_actual   = desde,
        limit           = cantidad,
        total_registros = total_partidos
    )

    return jsonify({
        "partidos": partidos,
        "_links":   links
    }), 200


@partidos_bp.route("/partidos/<int:id_partido>", methods=["GET"])
def get_partido(id_partido):
    partido = obtener_partido_por_id(id_partido)

    if not partido:
        return jsonify({"errors": ["Partido no encontrado"]}), 404

    return jsonify(partido), 200


@partidos_bp.route("/partidos", methods=["POST"])
def post_partido():
    datos_nuevo_partido = request.json

    errores = validar_partido(datos_nuevo_partido)
    if errores:
        return jsonify({"errors": errores}), 400

    id_partido_creado = crear_partido(datos_nuevo_partido)
    return jsonify({"id": id_partido_creado}), 201


@partidos_bp.route("/partidos/<int:id_partido>", methods=["DELETE"])
def delete_partido(id_partido):
    partido_eliminado = eliminar_partido(id_partido)

    if not partido_eliminado:
        return jsonify({"errors": ["Partido no encontrado"]}), 404

    return "", 204