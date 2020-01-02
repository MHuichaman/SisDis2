FROM python:3.7

RUN python -m pip install grpcio && python -m pip install grpcio-tools

ADD client.py /client/

WORKDIR /client/