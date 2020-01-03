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


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nchat.proto\x12\x04grpc\x1a\x1fgoogle/protobuf/timestamp.proto\"\x07\n\x05\x45mpty\" \n\x0cJoinResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"Q\n\x03Msg\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x19\n\x06UserID\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\'\n\x08UserList\x12\x1b\n\x05users\x18\x01 \x03(\x0b\x32\x0c.grpc.UserID\"*\n\x0bUserMsgList\x12\x1b\n\x08messages\x18\x01 \x03(\x0b\x32\t.grpc.Msg2V\n\x04\x43hat\x12\'\n\x0bSendMessage\x12\t.grpc.Msg\x1a\x0b.grpc.Empty\"\x00\x12%\n\x07\x43hannel\x12\x0b.grpc.Empty\x1a\t.grpc.Msg\"\x00\x30\x01\x32\x87\x01\n\x04User\x12+\n\x0cGetUsersList\x12\x0b.grpc.Empty\x1a\x0e.grpc.UserList\x12\"\n\x05Leave\x12\x0c.grpc.UserID\x1a\x0b.grpc.Empty\x12.\n\nJoinServer\x12\x0c.grpc.UserID\x1a\x12.grpc.JoinResponse2g\n\x07Message\x12.\n\x0bgetMessages\x12\x0c.grpc.UserID\x1a\x11.grpc.UserMsgList\x12,\n\x0fSaveUserMessage\x12\x0c.grpc.UserID\x1a\x0b.grpc.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=53,
  serialized_end=60,
)


_JOINRESPONSE = _descriptor.Descriptor(
  name='JoinResponse',
  full_name='grpc.JoinResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='grpc.JoinResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=62,
  serialized_end=94,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='grpc.Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.Msg.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc.Msg.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='grpc.Msg.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=96,
  serialized_end=177,
)


_USERID = _descriptor.Descriptor(
  name='UserID',
  full_name='grpc.UserID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='grpc.UserID.user_id', index=0,
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
  serialized_start=179,
  serialized_end=204,
)


_USERLIST = _descriptor.Descriptor(
  name='UserList',
  full_name='grpc.UserList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='grpc.UserList.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=206,
  serialized_end=245,
)


_USERMSGLIST = _descriptor.Descriptor(
  name='UserMsgList',
  full_name='grpc.UserMsgList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='grpc.UserMsgList.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=247,
  serialized_end=289,
)

_MSG.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USERLIST.fields_by_name['users'].message_type = _USERID
_USERMSGLIST.fields_by_name['messages'].message_type = _MSG
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['JoinResponse'] = _JOINRESPONSE
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['UserID'] = _USERID
DESCRIPTOR.message_types_by_name['UserList'] = _USERLIST
DESCRIPTOR.message_types_by_name['UserMsgList'] = _USERMSGLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Empty)
  })
_sym_db.RegisterMessage(Empty)

JoinResponse = _reflection.GeneratedProtocolMessageType('JoinResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOINRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.JoinResponse)
  })
_sym_db.RegisterMessage(JoinResponse)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Msg)
  })
_sym_db.RegisterMessage(Msg)

UserID = _reflection.GeneratedProtocolMessageType('UserID', (_message.Message,), {
  'DESCRIPTOR' : _USERID,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.UserID)
  })
_sym_db.RegisterMessage(UserID)

UserList = _reflection.GeneratedProtocolMessageType('UserList', (_message.Message,), {
  'DESCRIPTOR' : _USERLIST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.UserList)
  })
_sym_db.RegisterMessage(UserList)

UserMsgList = _reflection.GeneratedProtocolMessageType('UserMsgList', (_message.Message,), {
  'DESCRIPTOR' : _USERMSGLIST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.UserMsgList)
  })
_sym_db.RegisterMessage(UserMsgList)



_CHAT = _descriptor.ServiceDescriptor(
  name='Chat',
  full_name='grpc.Chat',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=291,
  serialized_end=377,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='grpc.Chat.SendMessage',
    index=0,
    containing_service=None,
    input_type=_MSG,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Channel',
    full_name='grpc.Chat.Channel',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_MSG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHAT)

DESCRIPTOR.services_by_name['Chat'] = _CHAT


_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='grpc.User',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=380,
  serialized_end=515,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUsersList',
    full_name='grpc.User.GetUsersList',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_USERLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Leave',
    full_name='grpc.User.Leave',
    index=1,
    containing_service=None,
    input_type=_USERID,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='JoinServer',
    full_name='grpc.User.JoinServer',
    index=2,
    containing_service=None,
    input_type=_USERID,
    output_type=_JOINRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER


_MESSAGE = _descriptor.ServiceDescriptor(
  name='Message',
  full_name='grpc.Message',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=517,
  serialized_end=620,
  methods=[
  _descriptor.MethodDescriptor(
    name='getMessages',
    full_name='grpc.Message.getMessages',
    index=0,
    containing_service=None,
    input_type=_USERID,
    output_type=_USERMSGLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SaveUserMessage',
    full_name='grpc.Message.SaveUserMessage',
    index=1,
    containing_service=None,
    input_type=_USERID,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSAGE)

DESCRIPTOR.services_by_name['Message'] = _MESSAGE

# @@protoc_insertion_point(module_scope)