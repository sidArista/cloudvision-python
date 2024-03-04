# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/dashboard.v1/services.gen.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arista.dashboard.v1 import dashboard_pb2 as arista_dot_dashboard_dot_v1_dot_dashboard__pb2
from arista.time import time_pb2 as arista_dot_time_dot_time__pb2
from arista.subscriptions import subscriptions_pb2 as arista_dot_subscriptions_dot_subscriptions__pb2
from fmp import deletes_pb2 as fmp_dot_deletes__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&arista/dashboard.v1/services.gen.proto\x12\x13\x61rista.dashboard.v1\x1a#arista/dashboard.v1/dashboard.proto\x1a\x16\x61rista/time/time.proto\x1a(arista/subscriptions/subscriptions.proto\x1a\x11\x66mp/deletes.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x94\x01\n\x0cMetaResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\x12+\n\x05\x63ount\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"l\n\x10\x44\x61shboardRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"l\n\x11\x44\x61shboardResponse\x12-\n\x05value\x18\x01 \x01(\x0b\x32\x1e.arista.dashboard.v1.Dashboard\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"q\n\x14\x44\x61shboardSomeRequest\x12/\n\x04keys\x18\x01 \x03(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9d\x01\n\x15\x44\x61shboardSomeResponse\x12-\n\x05value\x18\x01 \x01(\x0b\x32\x1e.arista.dashboard.v1.Dashboard\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa7\x01\n\x16\x44\x61shboardStreamRequest\x12\x39\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32\x1e.arista.dashboard.v1.Dashboard\x12+\n\x06\x66ilter\x18\x02 \x03(\x0b\x32\x1b.arista.dashboard.v1.Filter\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\"\xa1\x01\n\x17\x44\x61shboardStreamResponse\x12-\n\x05value\x18\x01 \x01(\x0b\x32\x1e.arista.dashboard.v1.Dashboard\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\"r\n\x16\x44\x61shboardConfigRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"x\n\x17\x44\x61shboardConfigResponse\x12\x33\n\x05value\x18\x01 \x01(\x0b\x32$.arista.dashboard.v1.DashboardConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"w\n\x1a\x44\x61shboardConfigSomeRequest\x12/\n\x04keys\x18\x01 \x03(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa9\x01\n\x1b\x44\x61shboardConfigSomeResponse\x12\x33\n\x05value\x18\x01 \x01(\x0b\x32$.arista.dashboard.v1.DashboardConfig\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x86\x01\n\x1c\x44\x61shboardConfigStreamRequest\x12?\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32$.arista.dashboard.v1.DashboardConfig\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\"\xad\x01\n\x1d\x44\x61shboardConfigStreamResponse\x12\x33\n\x05value\x18\x01 \x01(\x0b\x32$.arista.dashboard.v1.DashboardConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\"P\n\x19\x44\x61shboardConfigSetRequest\x12\x33\n\x05value\x18\x01 \x01(\x0b\x32$.arista.dashboard.v1.DashboardConfig\"{\n\x1a\x44\x61shboardConfigSetResponse\x12\x33\n\x05value\x18\x01 \x01(\x0b\x32$.arista.dashboard.v1.DashboardConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"U\n\x1d\x44\x61shboardConfigSetSomeRequest\x12\x34\n\x06values\x18\x01 \x03(\x0b\x32$.arista.dashboard.v1.DashboardConfig\"_\n\x1e\x44\x61shboardConfigSetSomeResponse\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"N\n\x1c\x44\x61shboardConfigDeleteRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\"y\n\x1d\x44\x61shboardConfigDeleteResponse\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"S\n DashboardConfigDeleteSomeRequest\x12/\n\x04keys\x18\x01 \x03(\x0b\x32!.arista.dashboard.v1.DashboardKey\"b\n!DashboardConfigDeleteSomeResponse\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"b\n\x1f\x44\x61shboardConfigDeleteAllRequest\x12?\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32$.arista.dashboard.v1.DashboardConfig\"\xc9\x01\n DashboardConfigDeleteAllResponse\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.fmp.DeleteError\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x03key\x18\x03 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12(\n\x04time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"H\n\x1cGlobalDashboardConfigRequest\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x84\x01\n\x1dGlobalDashboardConfigResponse\x12\x39\n\x05value\x18\x01 \x01(\x0b\x32*.arista.dashboard.v1.GlobalDashboardConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x92\x01\n\"GlobalDashboardConfigStreamRequest\x12\x45\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32*.arista.dashboard.v1.GlobalDashboardConfig\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\"\xb9\x01\n#GlobalDashboardConfigStreamResponse\x12\x39\n\x05value\x18\x01 \x01(\x0b\x32*.arista.dashboard.v1.GlobalDashboardConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\"\\\n\x1fGlobalDashboardConfigSetRequest\x12\x39\n\x05value\x18\x01 \x01(\x0b\x32*.arista.dashboard.v1.GlobalDashboardConfig\"\x87\x01\n GlobalDashboardConfigSetResponse\x12\x39\n\x05value\x18\x01 \x01(\x0b\x32*.arista.dashboard.v1.GlobalDashboardConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xde\x04\n\x10\x44\x61shboardService\x12W\n\x06GetOne\x12%.arista.dashboard.v1.DashboardRequest\x1a&.arista.dashboard.v1.DashboardResponse\x12\x62\n\x07GetSome\x12).arista.dashboard.v1.DashboardSomeRequest\x1a*.arista.dashboard.v1.DashboardSomeResponse0\x01\x12\x65\n\x06GetAll\x12+.arista.dashboard.v1.DashboardStreamRequest\x1a,.arista.dashboard.v1.DashboardStreamResponse0\x01\x12h\n\tSubscribe\x12+.arista.dashboard.v1.DashboardStreamRequest\x1a,.arista.dashboard.v1.DashboardStreamResponse0\x01\x12Y\n\x07GetMeta\x12+.arista.dashboard.v1.DashboardStreamRequest\x1a!.arista.dashboard.v1.MetaResponse\x12\x61\n\rSubscribeMeta\x12+.arista.dashboard.v1.DashboardStreamRequest\x1a!.arista.dashboard.v1.MetaResponse0\x01\x32\xea\t\n\x16\x44\x61shboardConfigService\x12\x63\n\x06GetOne\x12+.arista.dashboard.v1.DashboardConfigRequest\x1a,.arista.dashboard.v1.DashboardConfigResponse\x12n\n\x07GetSome\x12/.arista.dashboard.v1.DashboardConfigSomeRequest\x1a\x30.arista.dashboard.v1.DashboardConfigSomeResponse0\x01\x12q\n\x06GetAll\x12\x31.arista.dashboard.v1.DashboardConfigStreamRequest\x1a\x32.arista.dashboard.v1.DashboardConfigStreamResponse0\x01\x12t\n\tSubscribe\x12\x31.arista.dashboard.v1.DashboardConfigStreamRequest\x1a\x32.arista.dashboard.v1.DashboardConfigStreamResponse0\x01\x12_\n\x07GetMeta\x12\x31.arista.dashboard.v1.DashboardConfigStreamRequest\x1a!.arista.dashboard.v1.MetaResponse\x12g\n\rSubscribeMeta\x12\x31.arista.dashboard.v1.DashboardConfigStreamRequest\x1a!.arista.dashboard.v1.MetaResponse0\x01\x12\x66\n\x03Set\x12..arista.dashboard.v1.DashboardConfigSetRequest\x1a/.arista.dashboard.v1.DashboardConfigSetResponse\x12t\n\x07SetSome\x12\x32.arista.dashboard.v1.DashboardConfigSetSomeRequest\x1a\x33.arista.dashboard.v1.DashboardConfigSetSomeResponse0\x01\x12o\n\x06\x44\x65lete\x12\x31.arista.dashboard.v1.DashboardConfigDeleteRequest\x1a\x32.arista.dashboard.v1.DashboardConfigDeleteResponse\x12}\n\nDeleteSome\x12\x35.arista.dashboard.v1.DashboardConfigDeleteSomeRequest\x1a\x36.arista.dashboard.v1.DashboardConfigDeleteSomeResponse0\x01\x12z\n\tDeleteAll\x12\x34.arista.dashboard.v1.DashboardConfigDeleteAllRequest\x1a\x35.arista.dashboard.v1.DashboardConfigDeleteAllResponse0\x01\x32\xf4\x04\n\x1cGlobalDashboardConfigService\x12o\n\x06GetOne\x12\x31.arista.dashboard.v1.GlobalDashboardConfigRequest\x1a\x32.arista.dashboard.v1.GlobalDashboardConfigResponse\x12}\n\x06GetAll\x12\x37.arista.dashboard.v1.GlobalDashboardConfigStreamRequest\x1a\x38.arista.dashboard.v1.GlobalDashboardConfigStreamResponse0\x01\x12\x80\x01\n\tSubscribe\x12\x37.arista.dashboard.v1.GlobalDashboardConfigStreamRequest\x1a\x38.arista.dashboard.v1.GlobalDashboardConfigStreamResponse0\x01\x12m\n\rSubscribeMeta\x12\x37.arista.dashboard.v1.GlobalDashboardConfigStreamRequest\x1a!.arista.dashboard.v1.MetaResponse0\x01\x12r\n\x03Set\x12\x34.arista.dashboard.v1.GlobalDashboardConfigSetRequest\x1a\x35.arista.dashboard.v1.GlobalDashboardConfigSetResponseBLZJgithub.com/aristanetworks/cloudvision-go/api/arista/dashboard.v1;dashboardb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.dashboard.v1.services.gen_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgithub.com/aristanetworks/cloudvision-go/api/arista/dashboard.v1;dashboard'
  _globals['_METARESPONSE']._serialized_start=251
  _globals['_METARESPONSE']._serialized_end=399
  _globals['_DASHBOARDREQUEST']._serialized_start=401
  _globals['_DASHBOARDREQUEST']._serialized_end=509
  _globals['_DASHBOARDRESPONSE']._serialized_start=511
  _globals['_DASHBOARDRESPONSE']._serialized_end=619
  _globals['_DASHBOARDSOMEREQUEST']._serialized_start=621
  _globals['_DASHBOARDSOMEREQUEST']._serialized_end=734
  _globals['_DASHBOARDSOMERESPONSE']._serialized_start=737
  _globals['_DASHBOARDSOMERESPONSE']._serialized_end=894
  _globals['_DASHBOARDSTREAMREQUEST']._serialized_start=897
  _globals['_DASHBOARDSTREAMREQUEST']._serialized_end=1064
  _globals['_DASHBOARDSTREAMRESPONSE']._serialized_start=1067
  _globals['_DASHBOARDSTREAMRESPONSE']._serialized_end=1228
  _globals['_DASHBOARDCONFIGREQUEST']._serialized_start=1230
  _globals['_DASHBOARDCONFIGREQUEST']._serialized_end=1344
  _globals['_DASHBOARDCONFIGRESPONSE']._serialized_start=1346
  _globals['_DASHBOARDCONFIGRESPONSE']._serialized_end=1466
  _globals['_DASHBOARDCONFIGSOMEREQUEST']._serialized_start=1468
  _globals['_DASHBOARDCONFIGSOMEREQUEST']._serialized_end=1587
  _globals['_DASHBOARDCONFIGSOMERESPONSE']._serialized_start=1590
  _globals['_DASHBOARDCONFIGSOMERESPONSE']._serialized_end=1759
  _globals['_DASHBOARDCONFIGSTREAMREQUEST']._serialized_start=1762
  _globals['_DASHBOARDCONFIGSTREAMREQUEST']._serialized_end=1896
  _globals['_DASHBOARDCONFIGSTREAMRESPONSE']._serialized_start=1899
  _globals['_DASHBOARDCONFIGSTREAMRESPONSE']._serialized_end=2072
  _globals['_DASHBOARDCONFIGSETREQUEST']._serialized_start=2074
  _globals['_DASHBOARDCONFIGSETREQUEST']._serialized_end=2154
  _globals['_DASHBOARDCONFIGSETRESPONSE']._serialized_start=2156
  _globals['_DASHBOARDCONFIGSETRESPONSE']._serialized_end=2279
  _globals['_DASHBOARDCONFIGSETSOMEREQUEST']._serialized_start=2281
  _globals['_DASHBOARDCONFIGSETSOMEREQUEST']._serialized_end=2366
  _globals['_DASHBOARDCONFIGSETSOMERESPONSE']._serialized_start=2368
  _globals['_DASHBOARDCONFIGSETSOMERESPONSE']._serialized_end=2463
  _globals['_DASHBOARDCONFIGDELETEREQUEST']._serialized_start=2465
  _globals['_DASHBOARDCONFIGDELETEREQUEST']._serialized_end=2543
  _globals['_DASHBOARDCONFIGDELETERESPONSE']._serialized_start=2545
  _globals['_DASHBOARDCONFIGDELETERESPONSE']._serialized_end=2666
  _globals['_DASHBOARDCONFIGDELETESOMEREQUEST']._serialized_start=2668
  _globals['_DASHBOARDCONFIGDELETESOMEREQUEST']._serialized_end=2751
  _globals['_DASHBOARDCONFIGDELETESOMERESPONSE']._serialized_start=2753
  _globals['_DASHBOARDCONFIGDELETESOMERESPONSE']._serialized_end=2851
  _globals['_DASHBOARDCONFIGDELETEALLREQUEST']._serialized_start=2853
  _globals['_DASHBOARDCONFIGDELETEALLREQUEST']._serialized_end=2951
  _globals['_DASHBOARDCONFIGDELETEALLRESPONSE']._serialized_start=2954
  _globals['_DASHBOARDCONFIGDELETEALLRESPONSE']._serialized_end=3155
  _globals['_GLOBALDASHBOARDCONFIGREQUEST']._serialized_start=3157
  _globals['_GLOBALDASHBOARDCONFIGREQUEST']._serialized_end=3229
  _globals['_GLOBALDASHBOARDCONFIGRESPONSE']._serialized_start=3232
  _globals['_GLOBALDASHBOARDCONFIGRESPONSE']._serialized_end=3364
  _globals['_GLOBALDASHBOARDCONFIGSTREAMREQUEST']._serialized_start=3367
  _globals['_GLOBALDASHBOARDCONFIGSTREAMREQUEST']._serialized_end=3513
  _globals['_GLOBALDASHBOARDCONFIGSTREAMRESPONSE']._serialized_start=3516
  _globals['_GLOBALDASHBOARDCONFIGSTREAMRESPONSE']._serialized_end=3701
  _globals['_GLOBALDASHBOARDCONFIGSETREQUEST']._serialized_start=3703
  _globals['_GLOBALDASHBOARDCONFIGSETREQUEST']._serialized_end=3795
  _globals['_GLOBALDASHBOARDCONFIGSETRESPONSE']._serialized_start=3798
  _globals['_GLOBALDASHBOARDCONFIGSETRESPONSE']._serialized_end=3933
  _globals['_DASHBOARDSERVICE']._serialized_start=3936
  _globals['_DASHBOARDSERVICE']._serialized_end=4542
  _globals['_DASHBOARDCONFIGSERVICE']._serialized_start=4545
  _globals['_DASHBOARDCONFIGSERVICE']._serialized_end=5803
  _globals['_GLOBALDASHBOARDCONFIGSERVICE']._serialized_start=5806
  _globals['_GLOBALDASHBOARDCONFIGSERVICE']._serialized_end=6434
# @@protoc_insertion_point(module_scope)
