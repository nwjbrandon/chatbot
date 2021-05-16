from flask import Blueprint, jsonify, request

from src.upload_model.upload_model_service import (
    upload_model_service,
    upload_program_script_service,
)

upload_model_blueprint = Blueprint("upload_model_blueprint", __name__)


@upload_model_blueprint.route("/upload-model", methods=["POST"])
def upload_model_api():
    return jsonify(upload_model_service())


@upload_model_blueprint.route("/upload-program-script", methods=["POST"])
def upload_program_script_api():
    return jsonify(upload_program_script_service(**request.json))
