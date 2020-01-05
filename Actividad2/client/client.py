import pika
from datetime import datetime
import uuid
import logging
import json


class Client():

  def __init__(self):
    print("Iniciando")


    self.is_on = False
    self.user = ""
    self.user_id = str(uuid.uuid4())

    self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmw', heartbeat=0))
    self.channel = self.connection.channel()

  def Connect(self):

    while not self.is_on:
      user = input("Ingrese usuario: ")
      if user.strip():
        self.log(user, "log_in")

    self.user = user

  def Leave(self):
    self.log(user, "log_out")
    self.connection.close()


  def get_msgs(self):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', heartbeat=0))

    channel = connection.channel()
    channel.exchange_declare(exchange="broadcast",exchange_type="fanout")

    
  def send_mesage(self, kind, content):

    time_now = datetime.timestamp(datetime.now())
    
    if content.strip():

      if kind == "log_in":

        message = {
          'message_id' : str(uuid.uuid4()),
          'kind': "log_in", #to identify source on server side
          'user': content,
          'user_id': self.user_id,
          'time_stamp': time_now
        }
      elif kind == "log_out":

        message = {
          'message_id' : str(uuid.uuid4()),
          'kind': "log_out", #to identify source on server side
          'user': content,
          'user_id': self.user_id,
          'time_stamp': time_now
        }
      
      message_body = json.dumps(message)
      
      self.channel.basic_publish(
        exchange='',
        routing_keys='pending_messages',
        body=message_body,
        properties=pika.BasicProperties(content_type="text/plain", delivery_mode=2) #persistent message
      )

  
if __name__ == '__main__':
  logging.basicConfig()
  client = Client()

  client.Connect()

  while True:
    user_input = input()
    
    if user_input == "list_users!":
        client.send_message(user_input, "users_list")

    elif user_input == "list_messages!":
        client.send_message(user_input, "user_messages")

    elif user_input == "leave!":
        client.Leave()
        break

    # Envío de un mensaje normal.
    else:
        client.send(user_input, "message")
