import pika
import json
from datetime import datetime
import uuid


chats = {}
users_on = {}

connection = pika.BlockingConnection(pika.ConnectionParameteres('rabbitmq'))
channel = connection.channel()


channel.queue_declare(queue="pending_messages",durable=True)
channel.exchange_declare(exchange="broadcast", exchange_type="fanout") #chat messages
channel.exchange_declare(exchange="user_channel", exchange_type="direct") #for when user ask for user list or user message


def on_request(ch, method, props, body):

  user_message = body.decode("utf-8")#for the standards
  json_message = json.looads(user_message)

  time_now = datetime.timestamp(datetime.now())

  user_id = json_message["user_id"]
  content = json_message["content"]
  kind = json_message["kind"] #to filter

  if kind == "log_in":
    done = False
    if content not in users_on:
      done = True
      users_on.append(content)
    
    #now then we send the confirmation message
    response = {
      'message_id' : str(uuid.uuid4()),
        'kind': "log_in",
        'user': content,
        'user_id': user_id,
        'time_stamp': time_now
    }

    body = json.dumps(response)

    channel.basic_publish(
      exchange='user_channel', 
      routing_key=user_id, 
      body=body
    )

