FROM tiangolo/uvicorn-gunicorn:python3.7
RUN mkdir /fastapi
COPY requirements.txt /fastapi
WORKDIR /fastapi
COPY ./app /fastapi
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]