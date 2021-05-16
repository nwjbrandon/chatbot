import time

from flask import Response

from celery_worker import celery_app
from src.tasks.inference_task import inference_task
from src.utils.redis_utils import redis_conn


def camera_feed_generator():
    while True:
        frame = redis_conn.get("camera_feed")
        if not frame:
            continue

        yield (
            b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
        )  # concat frame one by one and show result


def view_camera_feed_service():
    prev_task_id = redis_conn.get("camera_feed_task_id").decode()
    celery_app.control.revoke(prev_task_id, terminate=True)

    time.sleep(1)

    task = inference_task.apply_async()
    task_id = str(task.id)

    redis_conn.set("camera_feed_task_id", task_id)

    return Response(
        camera_feed_generator(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )
