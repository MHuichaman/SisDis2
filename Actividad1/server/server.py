from concurrent import futures
import logging

import grpc

import chat_pb2
import chat_pb2_grpc


class Chat(chat_pb2_grpc.ChatServicer):

    def __init__(self):
        #para el almacenamiento de msjes del chat
        self.chats = []
    
    def Channel(self, request, context):
        count = 0
        while True:
            chans = self.chats
            while len(chats) > count:
                chan = chans[count]
                count += 1
                yield chan
    

    def SendMessage(self, request, context):
        file = open("log.txt", "a")



        return chat_pb2.Empty()

    #and thats all about chat

#users @ server code here


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(Chat(), server)
    chat_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
