# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/endpointlocation.v1/services.gen.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arista.endpointlocation.v1 import endpointlocation_pb2 as arista_dot_endpointlocation_dot_v1_dot_endpointlocation__pb2
from arista.time import time_pb2 as arista_dot_time_dot_time__pb2
from arista.subscriptions import subscriptions_pb2 as arista_dot_subscriptions_dot_subscriptions__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-arista/endpointlocation.v1/services.gen.proto\x12\x1a\x61rista.endpointlocation.v1\x1a\x31\x61rista/endpointlocation.v1/endpointlocation.proto\x1a\x16\x61rista/time/time.proto\x1a(arista/subscriptions/subscriptions.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x94\x01\n\x0cMetaResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\x12+\n\x05\x63ount\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"\x81\x01\n\x17\x45ndpointLocationRequest\x12<\n\x03key\x18\x01 \x01(\x0b\x32/.arista.endpointlocation.v1.EndpointLocationKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x81\x01\n\x18\x45ndpointLocationResponse\x12;\n\x05value\x18\x01 \x01(\x0b\x32,.arista.endpointlocation.v1.EndpointLocation\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x86\x01\n\x1b\x45ndpointLocationSomeRequest\x12=\n\x04keys\x18\x01 \x03(\x0b\x32/.arista.endpointlocation.v1.EndpointLocationKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb2\x01\n\x1c\x45ndpointLocationSomeResponse\x12;\n\x05value\x18\x01 \x01(\x0b\x32,.arista.endpointlocation.v1.EndpointLocation\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8f\x01\n\x1d\x45ndpointLocationStreamRequest\x12G\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32,.arista.endpointlocation.v1.EndpointLocation\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\"\xb6\x01\n\x1e\x45ndpointLocationStreamResponse\x12;\n\x05value\x18\x01 \x01(\x0b\x32,.arista.endpointlocation.v1.EndpointLocation\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\"\xca\x01\n$EndpointLocationBatchedStreamRequest\x12G\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32,.arista.endpointlocation.v1.EndpointLocation\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\x12\x32\n\x0cmax_messages\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"v\n%EndpointLocationBatchedStreamResponse\x12M\n\tresponses\x18\x01 \x03(\x0b\x32:.arista.endpointlocation.v1.EndpointLocationStreamResponse2\xb6\x08\n\x17\x45ndpointLocationService\x12s\n\x06GetOne\x12\x33.arista.endpointlocation.v1.EndpointLocationRequest\x1a\x34.arista.endpointlocation.v1.EndpointLocationResponse\x12~\n\x07GetSome\x12\x37.arista.endpointlocation.v1.EndpointLocationSomeRequest\x1a\x38.arista.endpointlocation.v1.EndpointLocationSomeResponse0\x01\x12\x81\x01\n\x06GetAll\x12\x39.arista.endpointlocation.v1.EndpointLocationStreamRequest\x1a:.arista.endpointlocation.v1.EndpointLocationStreamResponse0\x01\x12\x84\x01\n\tSubscribe\x12\x39.arista.endpointlocation.v1.EndpointLocationStreamRequest\x1a:.arista.endpointlocation.v1.EndpointLocationStreamResponse0\x01\x12n\n\x07GetMeta\x12\x39.arista.endpointlocation.v1.EndpointLocationStreamRequest\x1a(.arista.endpointlocation.v1.MetaResponse\x12v\n\rSubscribeMeta\x12\x39.arista.endpointlocation.v1.EndpointLocationStreamRequest\x1a(.arista.endpointlocation.v1.MetaResponse0\x01\x12\x96\x01\n\rGetAllBatched\x12@.arista.endpointlocation.v1.EndpointLocationBatchedStreamRequest\x1a\x41.arista.endpointlocation.v1.EndpointLocationBatchedStreamResponse0\x01\x12\x99\x01\n\x10SubscribeBatched\x12@.arista.endpointlocation.v1.EndpointLocationBatchedStreamRequest\x1a\x41.arista.endpointlocation.v1.EndpointLocationBatchedStreamResponse0\x01\x42ZZXgithub.com/aristanetworks/cloudvision-go/api/arista/endpointlocation.v1;endpointlocationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.endpointlocation.v1.services.gen_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZXgithub.com/aristanetworks/cloudvision-go/api/arista/endpointlocation.v1;endpointlocation'
  _globals['_METARESPONSE']._serialized_start=260
  _globals['_METARESPONSE']._serialized_end=408
  _globals['_ENDPOINTLOCATIONREQUEST']._serialized_start=411
  _globals['_ENDPOINTLOCATIONREQUEST']._serialized_end=540
  _globals['_ENDPOINTLOCATIONRESPONSE']._serialized_start=543
  _globals['_ENDPOINTLOCATIONRESPONSE']._serialized_end=672
  _globals['_ENDPOINTLOCATIONSOMEREQUEST']._serialized_start=675
  _globals['_ENDPOINTLOCATIONSOMEREQUEST']._serialized_end=809
  _globals['_ENDPOINTLOCATIONSOMERESPONSE']._serialized_start=812
  _globals['_ENDPOINTLOCATIONSOMERESPONSE']._serialized_end=990
  _globals['_ENDPOINTLOCATIONSTREAMREQUEST']._serialized_start=993
  _globals['_ENDPOINTLOCATIONSTREAMREQUEST']._serialized_end=1136
  _globals['_ENDPOINTLOCATIONSTREAMRESPONSE']._serialized_start=1139
  _globals['_ENDPOINTLOCATIONSTREAMRESPONSE']._serialized_end=1321
  _globals['_ENDPOINTLOCATIONBATCHEDSTREAMREQUEST']._serialized_start=1324
  _globals['_ENDPOINTLOCATIONBATCHEDSTREAMREQUEST']._serialized_end=1526
  _globals['_ENDPOINTLOCATIONBATCHEDSTREAMRESPONSE']._serialized_start=1528
  _globals['_ENDPOINTLOCATIONBATCHEDSTREAMRESPONSE']._serialized_end=1646
  _globals['_ENDPOINTLOCATIONSERVICE']._serialized_start=1649
  _globals['_ENDPOINTLOCATIONSERVICE']._serialized_end=2727
# @@protoc_insertion_point(module_scope)
