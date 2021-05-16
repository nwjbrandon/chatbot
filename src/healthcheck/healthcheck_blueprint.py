from flask import Blueprint, jsonify

from src.healthcheck.healthcheck_service import get_healthcheck_service

healthcheck_blueprint = Blueprint("healthcheck_blueprint", __name__)


@healthcheck_blueprint.route("/", methods=["GET"])
def get_healthcheck_api():
    return jsonify(get_healthcheck_service())
