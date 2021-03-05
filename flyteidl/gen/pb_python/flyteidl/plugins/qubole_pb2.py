# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/plugins/qubole.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import tasks_pb2 as flyteidl_dot_core_dot_tasks__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/plugins/qubole.proto',
  package='flyteidl.plugins',
  syntax='proto3',
  serialized_options=_b('Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/plugins'),
  serialized_pb=_b('\n\x1d\x66lyteidl/plugins/qubole.proto\x12\x10\x66lyteidl.plugins\x1a\x19\x66lyteidl/core/tasks.proto\"C\n\tHiveQuery\x12\r\n\x05query\x18\x01 \x01(\t\x12\x13\n\x0btimeout_sec\x18\x02 \x01(\r\x12\x12\n\nretryCount\x18\x03 \x01(\r\"C\n\x13HiveQueryCollection\x12,\n\x07queries\x18\x02 \x03(\x0b\x32\x1b.flyteidl.plugins.HiveQuery\"\xa5\x01\n\rQuboleHiveJob\x12\x15\n\rcluster_label\x18\x01 \x01(\t\x12\x43\n\x10query_collection\x18\x02 \x01(\x0b\x32%.flyteidl.plugins.HiveQueryCollectionB\x02\x18\x01\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12*\n\x05query\x18\x04 \x01(\x0b\x32\x1b.flyteidl.plugins.HiveQueryB9Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/pluginsb\x06proto3')
  ,
  dependencies=[flyteidl_dot_core_dot_tasks__pb2.DESCRIPTOR,])




_HIVEQUERY = _descriptor.Descriptor(
  name='HiveQuery',
  full_name='flyteidl.plugins.HiveQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='flyteidl.plugins.HiveQuery.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_sec', full_name='flyteidl.plugins.HiveQuery.timeout_sec', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retryCount', full_name='flyteidl.plugins.HiveQuery.retryCount', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=78,
  serialized_end=145,
)


_HIVEQUERYCOLLECTION = _descriptor.Descriptor(
  name='HiveQueryCollection',
  full_name='flyteidl.plugins.HiveQueryCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queries', full_name='flyteidl.plugins.HiveQueryCollection.queries', index=0,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=147,
  serialized_end=214,
)


_QUBOLEHIVEJOB = _descriptor.Descriptor(
  name='QuboleHiveJob',
  full_name='flyteidl.plugins.QuboleHiveJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_label', full_name='flyteidl.plugins.QuboleHiveJob.cluster_label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_collection', full_name='flyteidl.plugins.QuboleHiveJob.query_collection', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='flyteidl.plugins.QuboleHiveJob.tags', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='flyteidl.plugins.QuboleHiveJob.query', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=217,
  serialized_end=382,
)

_HIVEQUERYCOLLECTION.fields_by_name['queries'].message_type = _HIVEQUERY
_QUBOLEHIVEJOB.fields_by_name['query_collection'].message_type = _HIVEQUERYCOLLECTION
_QUBOLEHIVEJOB.fields_by_name['query'].message_type = _HIVEQUERY
DESCRIPTOR.message_types_by_name['HiveQuery'] = _HIVEQUERY
DESCRIPTOR.message_types_by_name['HiveQueryCollection'] = _HIVEQUERYCOLLECTION
DESCRIPTOR.message_types_by_name['QuboleHiveJob'] = _QUBOLEHIVEJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HiveQuery = _reflection.GeneratedProtocolMessageType('HiveQuery', (_message.Message,), dict(
  DESCRIPTOR = _HIVEQUERY,
  __module__ = 'flyteidl.plugins.qubole_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.HiveQuery)
  ))
_sym_db.RegisterMessage(HiveQuery)

HiveQueryCollection = _reflection.GeneratedProtocolMessageType('HiveQueryCollection', (_message.Message,), dict(
  DESCRIPTOR = _HIVEQUERYCOLLECTION,
  __module__ = 'flyteidl.plugins.qubole_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.HiveQueryCollection)
  ))
_sym_db.RegisterMessage(HiveQueryCollection)

QuboleHiveJob = _reflection.GeneratedProtocolMessageType('QuboleHiveJob', (_message.Message,), dict(
  DESCRIPTOR = _QUBOLEHIVEJOB,
  __module__ = 'flyteidl.plugins.qubole_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.QuboleHiveJob)
  ))
_sym_db.RegisterMessage(QuboleHiveJob)


DESCRIPTOR._options = None
_QUBOLEHIVEJOB.fields_by_name['query_collection']._options = None
# @@protoc_insertion_point(module_scope)
