from celery import Celery

worker = Celery('app', broker="redis://redis_r:6379/0", backend="redis://redis_r:6379/0")

def sent_task():
    worker.send_task('long_running_task')