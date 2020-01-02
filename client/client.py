from __future__ import print_function
import logging
import grpc

import chat_pb2
import chat_pb2_grpc

class Client:

    def __init__(self): #as to initialize client
        with grpc.insecure_channel('localhost:50051') as channel:
            self.chat_stub = chat_pb2_grpc.ChatStub(channel)
            self.user_stub = chat_pb2_grpc.UserStub(channel)

            auth = chat_pb2.UserID()

            done = False

            #time to choose user_name
            while not done:
                user_name = input("Ingrese usuario: ")
                auth.user_id = user_name
                join_response = self.user_stub.JoinServer(auth)

                if join_response.response:
                    print("Inicio correcto!")
                    self.user_name = user_name
                    done = True

                else:
                    #this way we make sure that id is unique
                    print("Por favor escoger otro nombre de usuario")
    #

if __name__ == '__main__':
    logging.basicConfig()
