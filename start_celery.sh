kill $(ps aux | grep 'celery' | awk '{print $2}')
celery --app src.tasks.inference_task.celery_app worker --loglevel=DEBUG