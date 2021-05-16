import celery_worker
from src import app
import socketio
from src.utils.socketio_utils import sio

if __name__ == "__main__":
    app = app.create_app(app_name="Augmentus", celery=celery_worker.celery_app)
    app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
    app.run(host="0.0.0.0", threaded=True)
