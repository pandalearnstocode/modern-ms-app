# FROM tiangolo/uvicorn-gunicorn:python3.7
# RUN mkdir /fastapi
# COPY requirements.txt /fastapi
# WORKDIR /fastapi
# RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
# COPY ./app /fastapi
# EXPOSE 8000
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y netcat
COPY requirements.txt .
RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
COPY . .