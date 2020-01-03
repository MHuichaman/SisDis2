from __future__ import print_function
import logging
import grpc

import chat_pb2
import chat_pb2_grpc

from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class Client:

    def __init__(self): #as to initialize client
        channel = grpc.insecure_channel('server:50051')

        self.user_stub = chat_pb2_grpc.UserStub(channel)

        auth = chat_pb2.UserID()

        done = False

        #time to choose user_name
        while not done:
            user_name = input("Ingrese usuario: ")
            auth.user_id = user_name
            print(auth.user_id) #test purposes, will be removed
            join_response = self.user_stub.JoinServer(auth)

            if join_response.response:
                print("Inicio correcto!")
                self.user_name = user_name
                done = True

            else:
                #this way we make sure that id is unique
                print("Por favor escoger otro nombre de usuario")

        #lets move this since it only needs to be created once user joins server
        self.chat_stub = chat_pb2_grpc.ChatStub(channel)
    #go for the basics first
    def GetUsersList(self):
        print("---\n Lista de usuarios on: ")
        list_users = self.user_stub.GetUsersList(chat_pb2.Empty())

        for user in list_users.users:
            print("- ", user.user_id)

        print("---\n")

    #how to leave server
    def Leave(self):
        current_user = chat_pb2.UserID()
        current_user.user_id = self.user_name
        self.user_stub.Leave(current_user)

    def SendMessage(self, content):
        if content.strip():
            print("hihi, i did it")
            time_now = Timestamp()
            time_now.GetCurrentTime()
            
            message = chat_pb2.Msg()
            message.id = time_now + "," + self.user_name #untested
            message.message = content
            message.timestamp = time_now

            self.chat_stub.SendMessage(message)


if __name__ == '__main__':
    logging.basicConfig()
    user = Client()
    print("Seleccione opciones: \n")
    while True:
        user_input = input()
        if user_input == "list_users!":
            user.GetUsersList()
        elif user_input == "leave!":
            user.Leave()
            print("server says... bye bye :c")
            break
        else:
            break