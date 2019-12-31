from __future__ import print_function
import logging
import socket
import grpc

import chat_pb2
import chat_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        name_client = socket.gethostname()
        response = stub.SendMessage(chat_pb2.ClientRequest(name='you'))
    print("Message client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
