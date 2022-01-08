import os
import time

from celery import Celery
from dotenv import load_dotenv

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

def add(x, y):
    return x + y

@celery.task(name="sample_job")
def sample_job(delta, x, y):
    time.sleep(delta)
    return add(x,y)