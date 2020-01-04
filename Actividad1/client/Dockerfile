FROM python:3.7

RUN python -m pip install grpcio && python -m pip install grpcio-tools

#this will be needed for more clients
COPY client.py /client/
COPY chat_pb2.py /client/
COPY chat_pb2_grpc.py /client/

WORKDIR /client/