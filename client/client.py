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
    #go for the basics first
    def getUsers(self):
        print("---\n Lista de usuarios on: ")
        list_users = self.user_stub.GetUsersList(chat_pb2.Empty())
        
        for user in list_users.users:
            print("- ", user.user_id)
        
        print("---\n")

    #how to leave server
    def leave(self):
        current_user = chat_pb2.UserID()
        current_user.user_id = self.user_name
        self.user_stub.Leave(current_user)


if __name__ == '__main__':
    logging.basicConfig()
