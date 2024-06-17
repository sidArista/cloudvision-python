# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/bugexposure.v1/bugexposure.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from fmp import extensions_pb2 as fmp_dot_extensions__pb2
from fmp import wrappers_pb2 as fmp_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'arista/bugexposure.v1/bugexposure.proto\x12\x15\x61rista.bugexposure.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14\x66mp/extensions.proto\x1a\x12\x66mp/wrappers.proto\"\x88\x01\n\x0e\x42ugExposureKey\x12/\n\tdevice_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12?\n\x0f\x61\x63knowledgement\x18\x02 \x01(\x0e\x32&.arista.bugexposure.v1.Acknowledgement:\x04\x80\x8e\x19\x01\"\xff\x02\n\x0b\x42ugExposure\x12\x32\n\x03key\x18\x01 \x01(\x0b\x32%.arista.bugexposure.v1.BugExposureKey\x12#\n\x07\x62ug_ids\x18\x02 \x01(\x0b\x32\x12.fmp.RepeatedInt32\x12#\n\x07\x63ve_ids\x18\x03 \x01(\x0b\x32\x12.fmp.RepeatedInt32\x12.\n\tbug_count\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12.\n\tcve_count\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x44\n\x14highest_bug_exposure\x18\x06 \x01(\x0e\x32&.arista.bugexposure.v1.HighestExposure\x12\x44\n\x14highest_cve_exposure\x18\x07 \x01(\x0e\x32&.arista.bugexposure.v1.HighestExposure:\x06\xfa\x8d\x19\x02ro*x\n\x0f\x41\x63knowledgement\x12\x1f\n\x1b\x41\x43KNOWLEDGEMENT_UNSPECIFIED\x10\x00\x12\"\n\x1e\x41\x43KNOWLEDGEMENT_UNACKNOWLEDGED\x10\x01\x12 \n\x1c\x41\x43KNOWLEDGEMENT_ACKNOWLEDGED\x10\x02*\x83\x01\n\x0fHighestExposure\x12 \n\x1cHIGHEST_EXPOSURE_UNSPECIFIED\x10\x00\x12\x19\n\x15HIGHEST_EXPOSURE_NONE\x10\x01\x12\x18\n\x14HIGHEST_EXPOSURE_LOW\x10\x02\x12\x19\n\x15HIGHEST_EXPOSURE_HIGH\x10\x03\x42z\n\x19\x63om.arista.bugexposure.v1B\x0b\x42ugExposureP\x01ZNgithub.com/aristanetworks/cloudvision-go/api/arista/bugexposure.v1;bugexposureb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.bugexposure.v1.bugexposure_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.arista.bugexposure.v1B\013BugExposureP\001ZNgithub.com/aristanetworks/cloudvision-go/api/arista/bugexposure.v1;bugexposure'
  _globals['_BUGEXPOSUREKEY']._options = None
  _globals['_BUGEXPOSUREKEY']._serialized_options = b'\200\216\031\001'
  _globals['_BUGEXPOSURE']._options = None
  _globals['_BUGEXPOSURE']._serialized_options = b'\372\215\031\002ro'
  _globals['_ACKNOWLEDGEMENT']._serialized_start=665
  _globals['_ACKNOWLEDGEMENT']._serialized_end=785
  _globals['_HIGHESTEXPOSURE']._serialized_start=788
  _globals['_HIGHESTEXPOSURE']._serialized_end=919
  _globals['_BUGEXPOSUREKEY']._serialized_start=141
  _globals['_BUGEXPOSUREKEY']._serialized_end=277
  _globals['_BUGEXPOSURE']._serialized_start=280
  _globals['_BUGEXPOSURE']._serialized_end=663
# @@protoc_insertion_point(module_scope)
