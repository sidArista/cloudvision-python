# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/serviceaccount.v1/serviceaccount.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from fmp import extensions_pb2 as fmp_dot_extensions__pb2
from fmp import wrappers_pb2 as fmp_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-arista/serviceaccount.v1/serviceaccount.proto\x12\x18\x61rista.serviceaccount.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14\x66mp/extensions.proto\x1a\x12\x66mp/wrappers.proto\">\n\nAccountKey\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\xdb\x01\n\rAccountConfig\x12\x31\n\x03key\x18\x01 \x01(\x0b\x32$.arista.serviceaccount.v1.AccountKey\x12\x37\n\x06status\x18\x02 \x01(\x0e\x32\'.arista.serviceaccount.v1.AccountStatus\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12#\n\x06groups\x18\x04 \x01(\x0b\x32\x13.fmp.RepeatedString:\x06\xfa\x8d\x19\x02rw\"\xb8\x02\n\x07\x41\x63\x63ount\x12\x31\n\x03key\x18\x01 \x01(\x0b\x32$.arista.serviceaccount.v1.AccountKey\x12\x37\n\x06status\x18\x02 \x01(\x0e\x32\'.arista.serviceaccount.v1.AccountStatus\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12#\n\x06groups\x18\x04 \x01(\x0b\x32\x13.fmp.RepeatedString\x12\x30\n\ncreated_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0blast_access\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x06\xfa\x8d\x19\x02ro\":\n\x08TokenKey\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\x84\x02\n\x0bTokenConfig\x12/\n\x03key\x18\x01 \x01(\x0b\x32\".arista.serviceaccount.v1.TokenKey\x12*\n\x04user\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\tvalid_for\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x05token\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\n\xfa\x8d\x19\x02rw\x98\x8e\x19\x00\"\xb1\x02\n\x05Token\x12/\n\x03key\x18\x01 \x01(\x0b\x32\".arista.serviceaccount.v1.TokenKey\x12*\n\x04user\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0bvalid_until\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\ncreated_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\tlast_used\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x06\xfa\x8d\x19\x02ro*h\n\rAccountStatus\x12\x1e\n\x1a\x41\x43\x43OUNT_STATUS_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x41\x43\x43OUNT_STATUS_ENABLED\x10\x01\x12\x1b\n\x17\x41\x43\x43OUNT_STATUS_DISABLED\x10\x02\x42VZTgithub.com/aristanetworks/cloudvision-go/api/arista/serviceaccount.v1;serviceaccountb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.serviceaccount.v1.serviceaccount_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZTgithub.com/aristanetworks/cloudvision-go/api/arista/serviceaccount.v1;serviceaccount'
  _globals['_ACCOUNTKEY']._options = None
  _globals['_ACCOUNTKEY']._serialized_options = b'\200\216\031\001'
  _globals['_ACCOUNTCONFIG']._options = None
  _globals['_ACCOUNTCONFIG']._serialized_options = b'\372\215\031\002rw'
  _globals['_ACCOUNT']._options = None
  _globals['_ACCOUNT']._serialized_options = b'\372\215\031\002ro'
  _globals['_TOKENKEY']._options = None
  _globals['_TOKENKEY']._serialized_options = b'\200\216\031\001'
  _globals['_TOKENCONFIG']._options = None
  _globals['_TOKENCONFIG']._serialized_options = b'\372\215\031\002rw\230\216\031\000'
  _globals['_TOKEN']._options = None
  _globals['_TOKEN']._serialized_options = b'\372\215\031\002ro'
  _globals['_ACCOUNTSTATUS']._serialized_start=1446
  _globals['_ACCOUNTSTATUS']._serialized_end=1550
  _globals['_ACCOUNTKEY']._serialized_start=214
  _globals['_ACCOUNTKEY']._serialized_end=276
  _globals['_ACCOUNTCONFIG']._serialized_start=279
  _globals['_ACCOUNTCONFIG']._serialized_end=498
  _globals['_ACCOUNT']._serialized_start=501
  _globals['_ACCOUNT']._serialized_end=813
  _globals['_TOKENKEY']._serialized_start=815
  _globals['_TOKENKEY']._serialized_end=873
  _globals['_TOKENCONFIG']._serialized_start=876
  _globals['_TOKENCONFIG']._serialized_end=1136
  _globals['_TOKEN']._serialized_start=1139
  _globals['_TOKEN']._serialized_end=1444
# @@protoc_insertion_point(module_scope)
