from concurrent import futures
import logging

import grpc

import chat_pb2
import chat_pb2_grpc


class Chat(chat_pb2_grpc.ChatServicer):

    def SendMessage(self, request, context):
        return chat_pb2.ClientMessage(message='Sup!, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(Chat(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
