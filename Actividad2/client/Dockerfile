FROM python:3.7

RUN pip install pika

COPY client.py /client/

ENV PYTHONUNBUFFERED=1

WORKDIR /client/