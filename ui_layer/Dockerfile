# FROM python:3.7-slim
# RUN mkdir /streamlit
# COPY requirements.txt /streamlit
# WORKDIR /streamlit
# RUN pip install -r requirements.txt
# COPY ./app /streamlit
# EXPOSE 8501
# CMD ["streamlit", "run", "main.py"]

FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y netcat
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501