# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nchat.proto\x12\x04grpc\"\x1d\n\rClientRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\rClientMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2A\n\x04\x43hat\x12\x39\n\x0bSendMessage\x12\x13.grpc.ClientRequest\x1a\x13.grpc.ClientMessage\"\x00\x62\x06proto3')
)




_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='grpc.ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc.ClientRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=49,
)


_CLIENTMESSAGE = _descriptor.Descriptor(
  name='ClientMessage',
  full_name='grpc.ClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc.ClientMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['ClientMessage'] = _CLIENTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ClientRequest)
  })
_sym_db.RegisterMessage(ClientRequest)

ClientMessage = _reflection.GeneratedProtocolMessageType('ClientMessage', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTMESSAGE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ClientMessage)
  })
_sym_db.RegisterMessage(ClientMessage)



_CHAT = _descriptor.ServiceDescriptor(
  name='Chat',
  full_name='grpc.Chat',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=85,
  serialized_end=150,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='grpc.Chat.SendMessage',
    index=0,
    containing_service=None,
    input_type=_CLIENTREQUEST,
    output_type=_CLIENTMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHAT)

DESCRIPTOR.services_by_name['Chat'] = _CHAT

# @@protoc_insertion_point(module_scope)
