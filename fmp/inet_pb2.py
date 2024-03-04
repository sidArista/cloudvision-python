# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fmp/inet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x66mp/inet.proto\x12\x03\x66mp\"\x1a\n\tIPAddress\x12\r\n\x05value\x18\x01 \x01(\t\"3\n\x11RepeatedIPAddress\x12\x1e\n\x06values\x18\x01 \x03(\x0b\x32\x0e.fmp.IPAddress\"\x1c\n\x0bIPv4Address\x12\r\n\x05value\x18\x01 \x01(\t\"7\n\x13RepeatedIPv4Address\x12 \n\x06values\x18\x01 \x03(\x0b\x32\x10.fmp.IPv4Address\"\x1c\n\x0bIPv6Address\x12\r\n\x05value\x18\x01 \x01(\t\"7\n\x13RepeatedIPv6Address\x12 \n\x06values\x18\x01 \x03(\x0b\x32\x10.fmp.IPv6Address\"\x19\n\x08IPPrefix\x12\r\n\x05value\x18\x01 \x01(\t\"\x1b\n\nIPv4Prefix\x12\r\n\x05value\x18\x01 \x01(\t\"\x1b\n\nIPv6Prefix\x12\r\n\x05value\x18\x01 \x01(\t\"\x15\n\x04Port\x12\r\n\x05value\x18\x01 \x01(\rB2Z0github.com/aristanetworks/cloudvision-go/api/fmpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fmp.inet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/aristanetworks/cloudvision-go/api/fmp'
  _globals['_IPADDRESS']._serialized_start=23
  _globals['_IPADDRESS']._serialized_end=49
  _globals['_REPEATEDIPADDRESS']._serialized_start=51
  _globals['_REPEATEDIPADDRESS']._serialized_end=102
  _globals['_IPV4ADDRESS']._serialized_start=104
  _globals['_IPV4ADDRESS']._serialized_end=132
  _globals['_REPEATEDIPV4ADDRESS']._serialized_start=134
  _globals['_REPEATEDIPV4ADDRESS']._serialized_end=189
  _globals['_IPV6ADDRESS']._serialized_start=191
  _globals['_IPV6ADDRESS']._serialized_end=219
  _globals['_REPEATEDIPV6ADDRESS']._serialized_start=221
  _globals['_REPEATEDIPV6ADDRESS']._serialized_end=276
  _globals['_IPPREFIX']._serialized_start=278
  _globals['_IPPREFIX']._serialized_end=303
  _globals['_IPV4PREFIX']._serialized_start=305
  _globals['_IPV4PREFIX']._serialized_end=332
  _globals['_IPV6PREFIX']._serialized_start=334
  _globals['_IPV6PREFIX']._serialized_end=361
  _globals['_PORT']._serialized_start=363
  _globals['_PORT']._serialized_end=384
# @@protoc_insertion_point(module_scope)
