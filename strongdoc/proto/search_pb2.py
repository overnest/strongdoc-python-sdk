# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from strongdoc.proto.protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='search.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.strongsalt.strongdoc.sdk.protoB\006Search\210\001\001',
  serialized_pb=b'\n\x0csearch.proto\x12\x05proto\x1a,protoc-gen-swagger/options/annotations.proto\"N\n\tSearchReq\x12\r\n\x05query\x18\x01 \x01(\t:2\x92\x41/\n\x0b*\tSearchReq2 \x12\x1e{\"query\": \"ukraine documents\"}\"\x82\x01\n\nSearchResp\x12#\n\x04hits\x18\x01 \x03(\x0b\x32\x15.proto.DocumentResult:O\x92\x41L\n\x0c*\nSearchResp2<\x12:{\"hits\": [{\"docID\": \"biden_investigation\", \"score\": 100}]}\".\n\x0e\x44ocumentResult\x12\r\n\x05\x64ocID\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x01\x42/\n\"com.strongsalt.strongdoc.sdk.protoB\x06Search\x88\x01\x01\x62\x06proto3'
  ,
  dependencies=[protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])




_SEARCHREQ = _descriptor.Descriptor(
  name='SearchReq',
  full_name='proto.SearchReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='proto.SearchReq.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\222A/\n\013*\tSearchReq2 \022\036{\"query\": \"ukraine documents\"}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=147,
)


_SEARCHRESP = _descriptor.Descriptor(
  name='SearchResp',
  full_name='proto.SearchResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hits', full_name='proto.SearchResp.hits', index=0,
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
  serialized_options=b'\222AL\n\014*\nSearchResp2<\022:{\"hits\": [{\"docID\": \"biden_investigation\", \"score\": 100}]}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=280,
)


_DOCUMENTRESULT = _descriptor.Descriptor(
  name='DocumentResult',
  full_name='proto.DocumentResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docID', full_name='proto.DocumentResult.docID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='proto.DocumentResult.score', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=282,
  serialized_end=328,
)

_SEARCHRESP.fields_by_name['hits'].message_type = _DOCUMENTRESULT
DESCRIPTOR.message_types_by_name['SearchReq'] = _SEARCHREQ
DESCRIPTOR.message_types_by_name['SearchResp'] = _SEARCHRESP
DESCRIPTOR.message_types_by_name['DocumentResult'] = _DOCUMENTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchReq = _reflection.GeneratedProtocolMessageType('SearchReq', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQ,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:proto.SearchReq)
  })
_sym_db.RegisterMessage(SearchReq)

SearchResp = _reflection.GeneratedProtocolMessageType('SearchResp', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESP,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:proto.SearchResp)
  })
_sym_db.RegisterMessage(SearchResp)

DocumentResult = _reflection.GeneratedProtocolMessageType('DocumentResult', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTRESULT,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:proto.DocumentResult)
  })
_sym_db.RegisterMessage(DocumentResult)


DESCRIPTOR._options = None
_SEARCHREQ._options = None
_SEARCHRESP._options = None
# @@protoc_insertion_point(module_scope)
