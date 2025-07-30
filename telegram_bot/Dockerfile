FROM python:3.11

WORKDIR /usr/src/fastapi_app

RUN apt-get update \
    && apt-get -y install build-essential \
    && apt-get -y install libpq-dev gcc \
    && apt-get -y install netcat

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
