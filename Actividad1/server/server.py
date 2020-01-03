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
class User(chat_pb2_grpc.UserServicer):

    def __init__(self):
        self.users = []

    def JoinServer(self, request, context):
        joined = chat_pb2.JoinResponse()

        if request.user_id in self.users:
            joined.response = False
            #because already joined
            return joined

        joined.response = True
        self.users.append(request.user_id)

        return joined

    def Leave(self, request, context):
        user = request.user_id
        self.users.remove(user) #remove id from existing list

        #return none
        return chat_pb2.Empty()

    def GetUsersList(self, request, context):
        list_users = chat_pb2.UserList() #inicializa lista de usuarios

        #como definimos un repeated, ahora debemos llenarlo
        #usando una lista auxiliar
        users_on = []
        for user in self.users:
            user_joined = chat_pb2.UserID()
            user_joined.user_id = user
            users_on.append(user_joined)

        list_users.users.extend(users_on)
        return list_users

#will be needed a message code here

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
