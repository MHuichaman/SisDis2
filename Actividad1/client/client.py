from __future__ import print_function
import logging
import grpc

import chat_pb2
import chat_pb2_grpc

from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import threading

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
        self.message_stub = chat_pb2_grpc.MessageStub(channel)

        #sin el thread nunca recibirán los mensajes :c
        threading.Thread(target=self.GetMessagesChat, daemon=True).start()

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

    def GetMessagesChat(self):
        user = chat_pb2.UserID()
        user.user_id = self.user_name
        messages = self.message_stub.GetMessages(user)

        print("----\n Lista de mensajes: \n----")
        for msg in self.chat_stub.Channel(chat_pb2.Empty()):
            user_name = msg.id.split(",")[1]
            timestamp = msg.timestamp
            date_time = (datetime.fromtimestamp(timestamp.seconds)).strftime("%d/%m/%Y - %H:%M:%S")
            print("[ " + date_time + " , " + user_name + " ]: " + msg.message + "\n")

    def GetMessagesList(self):
        user = chat_pb2.UserID()
        user.user_id = self.user_name
        messages = self.message_stub.GetMessages(user)

        print("----\n Lista de mensajes: \n----")
        for msg in messages.msgs:
            user_name = msg.split(",")[1]
            timestamp = msg.timestamp
            date_time = datetime.fromtimestamp(timestamp.seconds).strftime("%d/%m/%Y - %H:%M:%S")
            print("[ " + date_time + " , " + user_name + " ]: " + msg.message + "\n")

    def SendMessage(self, content):
        if content.strip():
            time_now = Timestamp()
            time_now.GetCurrentTime()
            
            message = chat_pb2.Msg()
            message.id = str(time_now.seconds) + "," + self.user_name #untested
            message.message = content
            message.timestamp.seconds = time_now.seconds

            self.chat_stub.SendMessage(message)
            self.message_stub.SaveUserMessage(message)



if __name__ == '__main__':
    logging.basicConfig()
    user = Client()
    print("Seleccione opciones: \n")
    while True:
        user_input = input()
        if user_input == "list_users!":
            user.GetUsersList()
        elif user_input == "list_messages!":
            user.GetMessagesChat()
        elif user_input == "leave!":
            user.Leave()
            print("server says... bye bye :c")
            break
        else:
            user.SendMessage(user_input)
            