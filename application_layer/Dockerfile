FROM python:3.9.4-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y netcat
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# WORKDIR /app