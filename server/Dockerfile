FROM python:3.7

RUN python -m pip install grpcio && python -m pip install grpcio-tools

#as in the example of grpc
EXPOSE 50051 

ADD server.py /server/

WORKDIR /server/