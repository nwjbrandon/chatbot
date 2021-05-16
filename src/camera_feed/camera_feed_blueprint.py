from flask import Blueprint

from src.camera_feed.camera_feed_service import view_camera_feed_service

camera_feed_blueprint = Blueprint("camera_feed_blueprint", __name__)


@camera_feed_blueprint.route("/camera-feed", methods=["GET"])
def view_camera_feed_api():
    return view_camera_feed_service()
