FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y netcat
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app

# vine==5.0.0
# redis==3.5.3
# kombu==5.1.0
# flower==1.0.0
# amqp==5.0.6
# billiard==3.6.4.0
# celery==5.1.2