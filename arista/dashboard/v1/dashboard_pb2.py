# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/dashboard.v1/dashboard.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from fmp import extensions_pb2 as fmp_dot_extensions__pb2
from fmp import wrappers_pb2 as fmp_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#arista/dashboard.v1/dashboard.proto\x12\x13\x61rista.dashboard.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14\x66mp/extensions.proto\x1a\x12\x66mp/wrappers.proto\"\\\n\x08Position\x12\'\n\x01x\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\'\n\x01y\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"g\n\nDimensions\x12+\n\x05width\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12,\n\x06height\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"\xe1\x01\n\x0cWidgetStyles\x12.\n\nhide_title\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x10\x62\x61\x63kground_color\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x13hide_horizontal_bar\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\ntitle_size\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"\xaf\x03\n\x06Widget\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x08position\x18\x03 \x01(\x0b\x32\x1d.arista.dashboard.v1.Position\x12\x33\n\ndimensions\x18\x04 \x01(\x0b\x32\x1f.arista.dashboard.v1.Dimensions\x12*\n\x04type\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06inputs\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08location\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x06styles\x18\x08 \x01(\x0b\x32!.arista.dashboard.v1.WidgetStyles\x12,\n\x06parent\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\"6\n\x07Widgets\x12+\n\x06values\x18\x01 \x03(\x0b\x32\x1b.arista.dashboard.v1.Widget\"H\n\x0c\x44\x61shboardKey\x12\x32\n\x0c\x64\x61shboard_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\xd7\x01\n\x0f\x44\x61shboardConfig\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07widgets\x18\x04 \x01(\x0b\x32\x1c.arista.dashboard.v1.Widgets:\x06\xfa\x8d\x19\x02rw\"\xe5\x01\n\x11\x44\x61shboardMetadata\x12\x34\n\x0eschema_version\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nlegacy_key\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0elegacy_version\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x66rom_package\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"+\n\x06\x46ilter\x12!\n\x04tags\x18\x01 \x01(\x0b\x32\x13.fmp.RepeatedString\"\xe8\x03\n\tDashboard\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\ncreated_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10last_modified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10last_modified_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\tmeta_data\x18\x06 \x01(\x0b\x32&.arista.dashboard.v1.DashboardMetadata\x12*\n\x04name\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07widgets\x18\t \x01(\x0b\x32\x1c.arista.dashboard.v1.Widgets:\x12\xfa\x8d\x19\x02ro\x8a\x8e\x19\x08[]Filter\"]\n\x15GlobalDashboardConfig\x12<\n\x11\x64\x65\x66\x61ult_dashboard\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey:\x06\xa2\x8e\x19\x02rwBLZJgithub.com/aristanetworks/cloudvision-go/api/arista/dashboard.v1;dashboardb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.dashboard.v1.dashboard_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZJgithub.com/aristanetworks/cloudvision-go/api/arista/dashboard.v1;dashboard'
  _globals['_DASHBOARDKEY']._options = None
  _globals['_DASHBOARDKEY']._serialized_options = b'\200\216\031\001'
  _globals['_DASHBOARDCONFIG']._options = None
  _globals['_DASHBOARDCONFIG']._serialized_options = b'\372\215\031\002rw'
  _globals['_DASHBOARD']._options = None
  _globals['_DASHBOARD']._serialized_options = b'\372\215\031\002ro\212\216\031\010[]Filter'
  _globals['_GLOBALDASHBOARDCONFIG']._options = None
  _globals['_GLOBALDASHBOARDCONFIG']._serialized_options = b'\242\216\031\002rw'
  _globals['_POSITION']._serialized_start=167
  _globals['_POSITION']._serialized_end=259
  _globals['_DIMENSIONS']._serialized_start=261
  _globals['_DIMENSIONS']._serialized_end=364
  _globals['_WIDGETSTYLES']._serialized_start=367
  _globals['_WIDGETSTYLES']._serialized_end=592
  _globals['_WIDGET']._serialized_start=595
  _globals['_WIDGET']._serialized_end=1026
  _globals['_WIDGETS']._serialized_start=1028
  _globals['_WIDGETS']._serialized_end=1082
  _globals['_DASHBOARDKEY']._serialized_start=1084
  _globals['_DASHBOARDKEY']._serialized_end=1156
  _globals['_DASHBOARDCONFIG']._serialized_start=1159
  _globals['_DASHBOARDCONFIG']._serialized_end=1374
  _globals['_DASHBOARDMETADATA']._serialized_start=1377
  _globals['_DASHBOARDMETADATA']._serialized_end=1606
  _globals['_FILTER']._serialized_start=1608
  _globals['_FILTER']._serialized_end=1651
  _globals['_DASHBOARD']._serialized_start=1654
  _globals['_DASHBOARD']._serialized_end=2142
  _globals['_GLOBALDASHBOARDCONFIG']._serialized_start=2144
  _globals['_GLOBALDASHBOARDCONFIG']._serialized_end=2237
# @@protoc_insertion_point(module_scope)
