import pika
import json
from datetime import datetime
import uuid
import time


chats = {}
users_on = []

time.sleep(13) #pika throws error if not used

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()


channel.queue_declare(queue="pending_messages",durable=True)
channel.exchange_declare(exchange="broadcast", exchange_type="fanout") #chat messages
channel.exchange_declare(exchange="user_channel", exchange_type="direct") #for when user ask for user list or user message


def on_request(ch, method, props, body):

  user_message = body.decode("utf-8")#for the standards
  json_message = json.loads(user_message)

  time_now = datetime.timestamp(datetime.now())

  user_id = json_message["user_id"]
  user = json_message["user"]
  kind = json_message["kind"] #to filter

  if kind == "log_in":
    done = "Nope"
    if user not in users_on:
      done = "Yay"
      users_on.append(user)
    
    #now then we send the confirmation message
    response = {
      'message_id' : str(uuid.uuid4()),
      'kind': "log_in",
      'response': done,
      'user_id': user_id,
      'time_now': time_now
    }
    body = json.dumps(response)
    channel.basic_publish(
      exchange='user_channel', 
      routing_key=user_id, 
      body=body
    )
  elif kind == "log_out":
    user = json_message["user"]
    users_on.remove(user)
  elif kind == "message":
    if user not in chats:
      chats[user] = [user_message]
    else:
      chats[user].append(user_message)

    body = json.dumps(json_message)
    channel.basic_publish(
      exchange='broadcast', #since all users will see this message 
      routing_key='', 
      body=body
    )
    time_sender = json_message["time_now"]
    json_message["time_now"] = time_now
    file = open("log.txt","a")
    server_date = (datetime.fromtimestamp(time_now)).strftime("%d/%m/%Y - %H:%M:%S")
    user_time = (datetime.fromtimestamp(time_sender)).strftime("%d/%m/%Y - %H:%M:%S")
    file.write("[" + json_message["message_id"] + "] - " )
    file.write("user: " + user + ", user_id: " + user_id + ", ")
    file.write("server_date: " + server_date + ", user_date: " + user_time + ", ")
    file.write("message: " + json_message["message"] + "\n")
    file.close()

    file.write()
  elif kind == "users_list":
    response_message = {
        'message_id': str(uuid.uuid4()),
        'type': "users_list",
        'response': users_on
    }
    body_response = json.dumps(response_message)
    channel.basic_publish(
      exchange='user_channel', 
      routing_key=user_id, 
      body=body
    )
  elif kind == "users_messages":
    if user in chats:
        user_messages = chats[user]
    else:
      user_messages = []
      response_message = {
        'message_id': str(uuid.uuid4()),
        'kind': "user_messages",
        'response': user_messages
      }

    body_response = json.dumps(response_message)

    channel.basic_publish(
      exchange='user_channel', 
      routing_key=user_id, 
      body=body
    )
  channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='pending_messages', on_message_callback=on_request)

channel.start_consuming()
