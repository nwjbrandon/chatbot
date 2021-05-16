from flask import Flask
from flask_cors import CORS

from src.utils.celery_utils import init_celery


def create_app(app_name, celery):
    app = Flask(app_name)
    init_celery(celery, app)

    from src.camera_feed.camera_feed_blueprint import camera_feed_blueprint
    from src.healthcheck.healthcheck_blueprint import healthcheck_blueprint
    from src.upload_model.upload_model_blueprint import upload_model_blueprint

    app.debug = True
    url_prefix = "/api/v1"
    app.register_blueprint(healthcheck_blueprint)
    app.register_blueprint(camera_feed_blueprint, url_prefix=url_prefix)
    app.register_blueprint(upload_model_blueprint, url_prefix=url_prefix)
    CORS(app)
    app.config["version"] = "v1"
    return app
