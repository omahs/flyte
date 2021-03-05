# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/matchable_resource.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2
from flyteidl.core import execution_pb2 as flyteidl_dot_core_dot_execution__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/matchable_resource.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_options=_b('Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin'),
  serialized_pb=_b('\n\'flyteidl/admin/matchable_resource.proto\x12\x0e\x66lyteidl.admin\x1a\x1b\x66lyteidl/admin/common.proto\x1a\x1d\x66lyteidl/core/execution.proto\"M\n\x10TaskResourceSpec\x12\x0b\n\x03\x63pu\x18\x01 \x01(\t\x12\x0b\n\x03gpu\x18\x02 \x01(\t\x12\x0e\n\x06memory\x18\x03 \x01(\t\x12\x0f\n\x07storage\x18\x04 \x01(\t\"~\n\x16TaskResourceAttributes\x12\x32\n\x08\x64\x65\x66\x61ults\x18\x01 \x01(\x0b\x32 .flyteidl.admin.TaskResourceSpec\x12\x30\n\x06limits\x18\x02 \x01(\x0b\x32 .flyteidl.admin.TaskResourceSpec\"\x9d\x01\n\x19\x43lusterResourceAttributes\x12M\n\nattributes\x18\x01 \x03(\x0b\x32\x39.flyteidl.admin.ClusterResourceAttributes.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"(\n\x18\x45xecutionQueueAttributes\x12\x0c\n\x04tags\x18\x01 \x03(\t\"&\n\x15\x45xecutionClusterLabel\x12\r\n\x05value\x18\x01 \x01(\t\"\xc1\x01\n\x0ePluginOverride\x12\x11\n\ttask_type\x18\x01 \x01(\t\x12\x11\n\tplugin_id\x18\x02 \x03(\t\x12U\n\x17missing_plugin_behavior\x18\x04 \x01(\x0e\x32\x34.flyteidl.admin.PluginOverride.MissingPluginBehavior\"2\n\x15MissingPluginBehavior\x12\x08\n\x04\x46\x41IL\x10\x00\x12\x0f\n\x0bUSE_DEFAULT\x10\x01\"D\n\x0fPluginOverrides\x12\x31\n\toverrides\x18\x01 \x03(\x0b\x32\x1e.flyteidl.admin.PluginOverride\"\xd2\x03\n\x12MatchingAttributes\x12J\n\x18task_resource_attributes\x18\x01 \x01(\x0b\x32&.flyteidl.admin.TaskResourceAttributesH\x00\x12P\n\x1b\x63luster_resource_attributes\x18\x02 \x01(\x0b\x32).flyteidl.admin.ClusterResourceAttributesH\x00\x12N\n\x1a\x65xecution_queue_attributes\x18\x03 \x01(\x0b\x32(.flyteidl.admin.ExecutionQueueAttributesH\x00\x12H\n\x17\x65xecution_cluster_label\x18\x04 \x01(\x0b\x32%.flyteidl.admin.ExecutionClusterLabelH\x00\x12=\n\x12quality_of_service\x18\x05 \x01(\x0b\x32\x1f.flyteidl.core.QualityOfServiceH\x00\x12;\n\x10plugin_overrides\x18\x06 \x01(\x0b\x32\x1f.flyteidl.admin.PluginOverridesH\x00\x42\x08\n\x06target\"\xa2\x01\n MatchableAttributesConfiguration\x12\x36\n\nattributes\x18\x01 \x01(\x0b\x32\".flyteidl.admin.MatchingAttributes\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x10\n\x08workflow\x18\x04 \x01(\t\x12\x13\n\x0blaunch_plan\x18\x05 \x01(\t\"Z\n\x1eListMatchableAttributesRequest\x12\x38\n\rresource_type\x18\x01 \x01(\x0e\x32!.flyteidl.admin.MatchableResource\"k\n\x1fListMatchableAttributesResponse\x12H\n\x0e\x63onfigurations\x18\x01 \x03(\x0b\x32\x30.flyteidl.admin.MatchableAttributesConfiguration*\xa9\x01\n\x11MatchableResource\x12\x11\n\rTASK_RESOURCE\x10\x00\x12\x14\n\x10\x43LUSTER_RESOURCE\x10\x01\x12\x13\n\x0f\x45XECUTION_QUEUE\x10\x02\x12\x1b\n\x17\x45XECUTION_CLUSTER_LABEL\x10\x03\x12$\n QUALITY_OF_SERVICE_SPECIFICATION\x10\x04\x12\x13\n\x0fPLUGIN_OVERRIDE\x10\x05\x42\x37Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_admin_dot_common__pb2.DESCRIPTOR,flyteidl_dot_core_dot_execution__pb2.DESCRIPTOR,])

_MATCHABLERESOURCE = _descriptor.EnumDescriptor(
  name='MatchableResource',
  full_name='flyteidl.admin.MatchableResource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TASK_RESOURCE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUSTER_RESOURCE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_QUEUE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_CLUSTER_LABEL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUALITY_OF_SERVICE_SPECIFICATION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLUGIN_OVERRIDE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1670,
  serialized_end=1839,
)
_sym_db.RegisterEnumDescriptor(_MATCHABLERESOURCE)

MatchableResource = enum_type_wrapper.EnumTypeWrapper(_MATCHABLERESOURCE)
TASK_RESOURCE = 0
CLUSTER_RESOURCE = 1
EXECUTION_QUEUE = 2
EXECUTION_CLUSTER_LABEL = 3
QUALITY_OF_SERVICE_SPECIFICATION = 4
PLUGIN_OVERRIDE = 5


_PLUGINOVERRIDE_MISSINGPLUGINBEHAVIOR = _descriptor.EnumDescriptor(
  name='MissingPluginBehavior',
  full_name='flyteidl.admin.PluginOverride.MissingPluginBehavior',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_DEFAULT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=712,
  serialized_end=762,
)
_sym_db.RegisterEnumDescriptor(_PLUGINOVERRIDE_MISSINGPLUGINBEHAVIOR)


_TASKRESOURCESPEC = _descriptor.Descriptor(
  name='TaskResourceSpec',
  full_name='flyteidl.admin.TaskResourceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='flyteidl.admin.TaskResourceSpec.cpu', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu', full_name='flyteidl.admin.TaskResourceSpec.gpu', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='flyteidl.admin.TaskResourceSpec.memory', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage', full_name='flyteidl.admin.TaskResourceSpec.storage', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=119,
  serialized_end=196,
)


_TASKRESOURCEATTRIBUTES = _descriptor.Descriptor(
  name='TaskResourceAttributes',
  full_name='flyteidl.admin.TaskResourceAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='defaults', full_name='flyteidl.admin.TaskResourceAttributes.defaults', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limits', full_name='flyteidl.admin.TaskResourceAttributes.limits', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=198,
  serialized_end=324,
)


_CLUSTERRESOURCEATTRIBUTES_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='flyteidl.admin.ClusterResourceAttributes.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyteidl.admin.ClusterResourceAttributes.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.admin.ClusterResourceAttributes.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=484,
)

_CLUSTERRESOURCEATTRIBUTES = _descriptor.Descriptor(
  name='ClusterResourceAttributes',
  full_name='flyteidl.admin.ClusterResourceAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='flyteidl.admin.ClusterResourceAttributes.attributes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTERRESOURCEATTRIBUTES_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=484,
)


_EXECUTIONQUEUEATTRIBUTES = _descriptor.Descriptor(
  name='ExecutionQueueAttributes',
  full_name='flyteidl.admin.ExecutionQueueAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='flyteidl.admin.ExecutionQueueAttributes.tags', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=486,
  serialized_end=526,
)


_EXECUTIONCLUSTERLABEL = _descriptor.Descriptor(
  name='ExecutionClusterLabel',
  full_name='flyteidl.admin.ExecutionClusterLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.admin.ExecutionClusterLabel.value', index=0,
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
  serialized_start=528,
  serialized_end=566,
)


_PLUGINOVERRIDE = _descriptor.Descriptor(
  name='PluginOverride',
  full_name='flyteidl.admin.PluginOverride',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_type', full_name='flyteidl.admin.PluginOverride.task_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plugin_id', full_name='flyteidl.admin.PluginOverride.plugin_id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_plugin_behavior', full_name='flyteidl.admin.PluginOverride.missing_plugin_behavior', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PLUGINOVERRIDE_MISSINGPLUGINBEHAVIOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=762,
)


_PLUGINOVERRIDES = _descriptor.Descriptor(
  name='PluginOverrides',
  full_name='flyteidl.admin.PluginOverrides',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overrides', full_name='flyteidl.admin.PluginOverrides.overrides', index=0,
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
  serialized_start=764,
  serialized_end=832,
)


_MATCHINGATTRIBUTES = _descriptor.Descriptor(
  name='MatchingAttributes',
  full_name='flyteidl.admin.MatchingAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_resource_attributes', full_name='flyteidl.admin.MatchingAttributes.task_resource_attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_resource_attributes', full_name='flyteidl.admin.MatchingAttributes.cluster_resource_attributes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execution_queue_attributes', full_name='flyteidl.admin.MatchingAttributes.execution_queue_attributes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execution_cluster_label', full_name='flyteidl.admin.MatchingAttributes.execution_cluster_label', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quality_of_service', full_name='flyteidl.admin.MatchingAttributes.quality_of_service', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plugin_overrides', full_name='flyteidl.admin.MatchingAttributes.plugin_overrides', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='target', full_name='flyteidl.admin.MatchingAttributes.target',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=835,
  serialized_end=1301,
)


_MATCHABLEATTRIBUTESCONFIGURATION = _descriptor.Descriptor(
  name='MatchableAttributesConfiguration',
  full_name='flyteidl.admin.MatchableAttributesConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='flyteidl.admin.MatchableAttributesConfiguration.attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='flyteidl.admin.MatchableAttributesConfiguration.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project', full_name='flyteidl.admin.MatchableAttributesConfiguration.project', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='flyteidl.admin.MatchableAttributesConfiguration.workflow', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='launch_plan', full_name='flyteidl.admin.MatchableAttributesConfiguration.launch_plan', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=1304,
  serialized_end=1466,
)


_LISTMATCHABLEATTRIBUTESREQUEST = _descriptor.Descriptor(
  name='ListMatchableAttributesRequest',
  full_name='flyteidl.admin.ListMatchableAttributesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='flyteidl.admin.ListMatchableAttributesRequest.resource_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=1468,
  serialized_end=1558,
)


_LISTMATCHABLEATTRIBUTESRESPONSE = _descriptor.Descriptor(
  name='ListMatchableAttributesResponse',
  full_name='flyteidl.admin.ListMatchableAttributesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configurations', full_name='flyteidl.admin.ListMatchableAttributesResponse.configurations', index=0,
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
  serialized_start=1560,
  serialized_end=1667,
)

_TASKRESOURCEATTRIBUTES.fields_by_name['defaults'].message_type = _TASKRESOURCESPEC
_TASKRESOURCEATTRIBUTES.fields_by_name['limits'].message_type = _TASKRESOURCESPEC
_CLUSTERRESOURCEATTRIBUTES_ATTRIBUTESENTRY.containing_type = _CLUSTERRESOURCEATTRIBUTES
_CLUSTERRESOURCEATTRIBUTES.fields_by_name['attributes'].message_type = _CLUSTERRESOURCEATTRIBUTES_ATTRIBUTESENTRY
_PLUGINOVERRIDE.fields_by_name['missing_plugin_behavior'].enum_type = _PLUGINOVERRIDE_MISSINGPLUGINBEHAVIOR
_PLUGINOVERRIDE_MISSINGPLUGINBEHAVIOR.containing_type = _PLUGINOVERRIDE
_PLUGINOVERRIDES.fields_by_name['overrides'].message_type = _PLUGINOVERRIDE
_MATCHINGATTRIBUTES.fields_by_name['task_resource_attributes'].message_type = _TASKRESOURCEATTRIBUTES
_MATCHINGATTRIBUTES.fields_by_name['cluster_resource_attributes'].message_type = _CLUSTERRESOURCEATTRIBUTES
_MATCHINGATTRIBUTES.fields_by_name['execution_queue_attributes'].message_type = _EXECUTIONQUEUEATTRIBUTES
_MATCHINGATTRIBUTES.fields_by_name['execution_cluster_label'].message_type = _EXECUTIONCLUSTERLABEL
_MATCHINGATTRIBUTES.fields_by_name['quality_of_service'].message_type = flyteidl_dot_core_dot_execution__pb2._QUALITYOFSERVICE
_MATCHINGATTRIBUTES.fields_by_name['plugin_overrides'].message_type = _PLUGINOVERRIDES
_MATCHINGATTRIBUTES.oneofs_by_name['target'].fields.append(
  _MATCHINGATTRIBUTES.fields_by_name['task_resource_attributes'])
_MATCHINGATTRIBUTES.fields_by_name['task_resource_attributes'].containing_oneof = _MATCHINGATTRIBUTES.oneofs_by_name['target']
_MATCHINGATTRIBUTES.oneofs_by_name['target'].fields.append(
  _MATCHINGATTRIBUTES.fields_by_name['cluster_resource_attributes'])
_MATCHINGATTRIBUTES.fields_by_name['cluster_resource_attributes'].containing_oneof = _MATCHINGATTRIBUTES.oneofs_by_name['target']
_MATCHINGATTRIBUTES.oneofs_by_name['target'].fields.append(
  _MATCHINGATTRIBUTES.fields_by_name['execution_queue_attributes'])
_MATCHINGATTRIBUTES.fields_by_name['execution_queue_attributes'].containing_oneof = _MATCHINGATTRIBUTES.oneofs_by_name['target']
_MATCHINGATTRIBUTES.oneofs_by_name['target'].fields.append(
  _MATCHINGATTRIBUTES.fields_by_name['execution_cluster_label'])
_MATCHINGATTRIBUTES.fields_by_name['execution_cluster_label'].containing_oneof = _MATCHINGATTRIBUTES.oneofs_by_name['target']
_MATCHINGATTRIBUTES.oneofs_by_name['target'].fields.append(
  _MATCHINGATTRIBUTES.fields_by_name['quality_of_service'])
_MATCHINGATTRIBUTES.fields_by_name['quality_of_service'].containing_oneof = _MATCHINGATTRIBUTES.oneofs_by_name['target']
_MATCHINGATTRIBUTES.oneofs_by_name['target'].fields.append(
  _MATCHINGATTRIBUTES.fields_by_name['plugin_overrides'])
_MATCHINGATTRIBUTES.fields_by_name['plugin_overrides'].containing_oneof = _MATCHINGATTRIBUTES.oneofs_by_name['target']
_MATCHABLEATTRIBUTESCONFIGURATION.fields_by_name['attributes'].message_type = _MATCHINGATTRIBUTES
_LISTMATCHABLEATTRIBUTESREQUEST.fields_by_name['resource_type'].enum_type = _MATCHABLERESOURCE
_LISTMATCHABLEATTRIBUTESRESPONSE.fields_by_name['configurations'].message_type = _MATCHABLEATTRIBUTESCONFIGURATION
DESCRIPTOR.message_types_by_name['TaskResourceSpec'] = _TASKRESOURCESPEC
DESCRIPTOR.message_types_by_name['TaskResourceAttributes'] = _TASKRESOURCEATTRIBUTES
DESCRIPTOR.message_types_by_name['ClusterResourceAttributes'] = _CLUSTERRESOURCEATTRIBUTES
DESCRIPTOR.message_types_by_name['ExecutionQueueAttributes'] = _EXECUTIONQUEUEATTRIBUTES
DESCRIPTOR.message_types_by_name['ExecutionClusterLabel'] = _EXECUTIONCLUSTERLABEL
DESCRIPTOR.message_types_by_name['PluginOverride'] = _PLUGINOVERRIDE
DESCRIPTOR.message_types_by_name['PluginOverrides'] = _PLUGINOVERRIDES
DESCRIPTOR.message_types_by_name['MatchingAttributes'] = _MATCHINGATTRIBUTES
DESCRIPTOR.message_types_by_name['MatchableAttributesConfiguration'] = _MATCHABLEATTRIBUTESCONFIGURATION
DESCRIPTOR.message_types_by_name['ListMatchableAttributesRequest'] = _LISTMATCHABLEATTRIBUTESREQUEST
DESCRIPTOR.message_types_by_name['ListMatchableAttributesResponse'] = _LISTMATCHABLEATTRIBUTESRESPONSE
DESCRIPTOR.enum_types_by_name['MatchableResource'] = _MATCHABLERESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskResourceSpec = _reflection.GeneratedProtocolMessageType('TaskResourceSpec', (_message.Message,), dict(
  DESCRIPTOR = _TASKRESOURCESPEC,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskResourceSpec)
  ))
_sym_db.RegisterMessage(TaskResourceSpec)

TaskResourceAttributes = _reflection.GeneratedProtocolMessageType('TaskResourceAttributes', (_message.Message,), dict(
  DESCRIPTOR = _TASKRESOURCEATTRIBUTES,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskResourceAttributes)
  ))
_sym_db.RegisterMessage(TaskResourceAttributes)

ClusterResourceAttributes = _reflection.GeneratedProtocolMessageType('ClusterResourceAttributes', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _CLUSTERRESOURCEATTRIBUTES_ATTRIBUTESENTRY,
    __module__ = 'flyteidl.admin.matchable_resource_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.admin.ClusterResourceAttributes.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _CLUSTERRESOURCEATTRIBUTES,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ClusterResourceAttributes)
  ))
_sym_db.RegisterMessage(ClusterResourceAttributes)
_sym_db.RegisterMessage(ClusterResourceAttributes.AttributesEntry)

ExecutionQueueAttributes = _reflection.GeneratedProtocolMessageType('ExecutionQueueAttributes', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONQUEUEATTRIBUTES,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ExecutionQueueAttributes)
  ))
_sym_db.RegisterMessage(ExecutionQueueAttributes)

ExecutionClusterLabel = _reflection.GeneratedProtocolMessageType('ExecutionClusterLabel', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONCLUSTERLABEL,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ExecutionClusterLabel)
  ))
_sym_db.RegisterMessage(ExecutionClusterLabel)

PluginOverride = _reflection.GeneratedProtocolMessageType('PluginOverride', (_message.Message,), dict(
  DESCRIPTOR = _PLUGINOVERRIDE,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.PluginOverride)
  ))
_sym_db.RegisterMessage(PluginOverride)

PluginOverrides = _reflection.GeneratedProtocolMessageType('PluginOverrides', (_message.Message,), dict(
  DESCRIPTOR = _PLUGINOVERRIDES,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.PluginOverrides)
  ))
_sym_db.RegisterMessage(PluginOverrides)

MatchingAttributes = _reflection.GeneratedProtocolMessageType('MatchingAttributes', (_message.Message,), dict(
  DESCRIPTOR = _MATCHINGATTRIBUTES,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.MatchingAttributes)
  ))
_sym_db.RegisterMessage(MatchingAttributes)

MatchableAttributesConfiguration = _reflection.GeneratedProtocolMessageType('MatchableAttributesConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _MATCHABLEATTRIBUTESCONFIGURATION,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.MatchableAttributesConfiguration)
  ))
_sym_db.RegisterMessage(MatchableAttributesConfiguration)

ListMatchableAttributesRequest = _reflection.GeneratedProtocolMessageType('ListMatchableAttributesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTMATCHABLEATTRIBUTESREQUEST,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ListMatchableAttributesRequest)
  ))
_sym_db.RegisterMessage(ListMatchableAttributesRequest)

ListMatchableAttributesResponse = _reflection.GeneratedProtocolMessageType('ListMatchableAttributesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTMATCHABLEATTRIBUTESRESPONSE,
  __module__ = 'flyteidl.admin.matchable_resource_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ListMatchableAttributesResponse)
  ))
_sym_db.RegisterMessage(ListMatchableAttributesResponse)


DESCRIPTOR._options = None
_CLUSTERRESOURCEATTRIBUTES_ATTRIBUTESENTRY._options = None
# @@protoc_insertion_point(module_scope)
