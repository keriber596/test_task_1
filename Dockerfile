FROM python:3.11

WORKDIR /usr/src/

RUN apt-get update \
    && apt-get -y install build-essential \
    && apt-get -y install libpq-dev gcc \
    && apt-get -y install netcat

COPY . .

RUN pip install -r requirements.txt