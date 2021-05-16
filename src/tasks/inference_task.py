import cv2

from celery_worker import celery_app
from src.utils.redis_utils import redis_conn


@celery_app.task(bind=True)
def inference_task(self):
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break

        # run some inference
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        redis_conn.set("camera_feed", frame)

    camera.release()
    cv2.destroyAllWindows()
