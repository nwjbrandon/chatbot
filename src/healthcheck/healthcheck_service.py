import uuid

from flask import current_app


def get_healthcheck_service():
    uid = str(uuid.uuid4())
    version = current_app.config["version"]

    return {"message": uid, "version": version}
