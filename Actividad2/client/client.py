import pika
from datetime import datetime
import uuid
import logging
import json
import threading
import time

class Client():

  def __init__(self):
    print("Iniciando")
    time.sleep(5)

    self.is_on = False
    self.user = ""
    self.user_id = str(uuid.uuid4())

    self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', heartbeat=0))
    self.channel = self.connection.channel()

  def get_msgs(self):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', heartbeat=0))

    channel = connection.channel()
    channel.exchange_declare(exchange="broadcast",exchange_type="fanout")

    exclusive_queue = channel.queue_declare(queue='', exclusive= True)
    queue = exclusive_queue.method.queue

    channel.queue_bind(exchange='broadcast', queue=queue)

    def callback_get_msgs(ch, method, properties, body):

      message = json.loads(body.decode("utf-8"))

      user = message["user"]
      content = message["message"]
      time_now = message["time_now"]
      date = (datetime.fromtimestamp(time_now)).strftime("%d/%m/%Y - %H:%M:%S")

      print("[ " + date + " - " + user + " ]: " + content + " ")
      
    channel.basic_consume(
      queue=queue,
      on_message_callback=callback_get_msgs,
      auto_ack=True,
      consumer_tag=self.user
    )

    channel.start_consuming()

  def get_server_msgs(self):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', heartbeat=0))

    channel = connection.channel()

    exclusive_queue = channel.queue_declare(queue=self.user_id, exclusive= True)
    queue = exclusive_queue.method.queue

    channel.queue_bind(exchange='user_channel', queue= queue)

    def callback_get_server_msgs(ch, method, properties, body):

      response_from_server = json.loads(body.decode("utf-8"))

      user = response_from_server["user"]
      kind = response_from_server["kind"]
      response = response_from_server["response"]

      if kind == "log_in":            
        if response == "Yay":
            self.is_on = True
            print("Inicio correcto!!")

        else:
            print("Nombre de usuario ya registrado\n")
        self.checked.set()

      elif kind == "user_messages":
          print("\n--------------")
          print("Mensajes enviados: \n-----\n")

          for sent_message in response:
            json_message = json.loads(sent_message)
            user = json_message["user"]
            content =json_message["message"]
            date = datetime.fromtimestamp(json_message["time_now"])
            date_time = date.strftime("%m/%d/%Y, %H:%M:%S")

            print("[ + " + date_time + " - " + user + "]: " + content + " ")

      # Si es un mensaje con la lista de usuarios conectados al chat.
      elif kind == "users_list":
          print("\n-----------------------------")
          print("Lista de usuarios: \n-------\n")
          for user in response:
              print(user)
      else:
          print("Rip")
      
    channel.basic_consume(
      queue=queue,
      on_message_callback=callback_get_server_msgs,
      auto_ack=True
    )

    channel.start_consuming()
    
  def send_message(self, content, kind):

    time_now = datetime.timestamp(datetime.now())
    
    if content.strip():
      if kind == "log_in":
        message = {
          'message_id' : str(uuid.uuid4()),
          'kind': "log_in", #to identify source on server side
          'user': content,
          'user_id': str(self.user_id),
          'time_stamp': time_now
        }
      elif kind == "log_out":
        message = {
          'message_id' : str(uuid.uuid4()),
          'kind': "log_out", #to identify source on server side
          'user': content,
          'user_id': str(self.user_id),
          'time_stamp': time_now
        }
      elif kind == "message":
        message = {
          'message_id' : str(uuid.uuid4()),
          'user': self.user,
          'user_id': str(self.user_id),
          'message': content,#new attribute so it send message
          'kind': "message", #to identify source on server side
          'time_stamp': time_now
        }
      elif kind == "users_list":
        message = {
          'message_id' : str(uuid.uuid4()),
          'user': self.user,
          'user_id': str(self.user_id),
          'kind': "users_list", #to identify source on server side
          'time_stamp': time_now
        }
      elif kind == "users_messages":
        message = {
          'message_id' : str(uuid.uuid4()),
          'user': self.user,
          'user_id': self.user_id,
          'kind': "users_messages", #to identify source on server side
          'time_stamp': time_now
        }
      else:
        print("no!")
      
      body = json.dumps(message)
      
      self.channel.basic_publish(
        exchange='',
        routing_key='pending_messages',
        body=body,
        properties=pika.BasicProperties(content_type="text/plain", delivery_mode=2) #persistent message
      )

  def Connect(self):
    self.checked = threading.Event()
    while not self.is_on:
      user = input("Ingrese usuario: ")
      if user.strip():
        self.send_message(user, "log_in")
        self.checked.wait()
        self.checked.clear()

    self.user = user

  def Leave(self):
    self.send_message("log_out", "log_out")
    self.connection.close()

  def thread_server_msgs(self):
    threading.Thread(target=self.get_server_msgs(), daemon=True).start()
  
  def thread_msgs(self):
    threading.Thread(target=self.get_msgs(), daemon=True).start()
  
if __name__ == '__main__':
  logging.basicConfig()
  client = Client()

  client.thread_server_msgs()
  client.Connect()
  client.thread_msgs()

  while True:
    user_input = input()
    
    if user_input == "list_users!":
      client.send_message(user_input, "users_list")

    elif user_input == "list_messages!":
      client.send_message(user_input, "users_messages")

    elif user_input == "leave!":
      client.Leave()
      break

    # Envío de un mensaje normal.
    else:
      client.send_message(user_input, "message")
