# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/event.v1/event.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61rista/event.v1/event.proto\x12\x0f\x61rista.event.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14\x66mp/extensions.proto\"\xb6\x01\n\x0e\x45ventComponent\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.arista.event.v1.ComponentType\x12\x43\n\ncomponents\x18\x02 \x03(\x0b\x32/.arista.event.v1.EventComponent.ComponentsEntry\x1a\x31\n\x0f\x43omponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\x0f\x45ventComponents\x12\x33\n\ncomponents\x18\x01 \x03(\x0b\x32\x1f.arista.event.v1.EventComponent\"\x8e\x01\n\x08\x45ventAck\x12\'\n\x03\x61\x63k\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x05\x61\x63ker\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x08\x61\x63k_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x92\x01\n\tEventRead\x12(\n\x04read\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x06reader\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\tread_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"=\n\x0f\x45ventNoteConfig\x12*\n\x04note\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"k\n\tEventNote\x12*\n\x04note\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cnote_creator\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"j\n\x08\x45ventKey\x12)\n\x03key\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x04\x80\x8e\x19\x01\"l\n\tEventData\x12\x32\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32$.arista.event.v1.EventData.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9f\x01\n\x10\x45ventNotesConfig\x12;\n\x05notes\x18\x01 \x03(\x0b\x32,.arista.event.v1.EventNotesConfig.NotesEntry\x1aN\n\nNotesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .arista.event.v1.EventNoteConfig:\x02\x38\x01\"\xcc\x01\n\x15\x45ventAnnotationConfig\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.arista.event.v1.EventKey\x12\'\n\x03\x61\x63k\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\x05notes\x18\x03 \x01(\x0b\x32!.arista.event.v1.EventNotesConfig\x12(\n\x04read\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue:\x06\xfa\x8d\x19\x02rw\"\x8d\x01\n\nEventNotes\x12\x35\n\x05notes\x18\x01 \x03(\x0b\x32&.arista.event.v1.EventNotes.NotesEntry\x1aH\n\nNotesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.arista.event.v1.EventNote:\x02\x38\x01\"\xbf\x04\n\x05\x45vent\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.arista.event.v1.EventKey\x12\x30\n\x08severity\x18\x02 \x01(\x0e\x32\x1e.arista.event.v1.EventSeverity\x12+\n\x05title\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nevent_type\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x1a.arista.event.v1.EventData\x12\x34\n\ncomponents\x18\x07 \x01(\x0b\x32 .arista.event.v1.EventComponents\x12&\n\x03\x61\x63k\x18\x08 \x01(\x0b\x32\x19.arista.event.v1.EventAck\x12*\n\x05notes\x18\t \x01(\x0b\x32\x1b.arista.event.v1.EventNotes\x12\x35\n\x11last_updated_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04read\x18\x0b \x01(\x0b\x32\x1a.arista.event.v1.EventRead\x12-\n\x07rule_id\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x06\xfa\x8d\x19\x02ro\"G\n\x14UserEventCreationKey\x12)\n\x03key\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\xae\x03\n\x17UserEventCreationConfig\x12\x32\n\x03key\x18\x01 \x01(\x0b\x32%.arista.event.v1.UserEventCreationKey\x12\x30\n\x08severity\x18\x02 \x01(\x0e\x32\x1e.arista.event.v1.EventSeverity\x12+\n\x05title\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nevent_type\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07rule_id\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\ncomponents\x18\x07 \x01(\x0b\x32 .arista.event.v1.EventComponents\x12.\n\nstart_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x06\xfa\x8d\x19\x02rw*\xb5\x01\n\rEventSeverity\x12\x1e\n\x1a\x45VENT_SEVERITY_UNSPECIFIED\x10\x00\x12\x17\n\x13\x45VENT_SEVERITY_INFO\x10\x01\x12\x1a\n\x16\x45VENT_SEVERITY_WARNING\x10\x02\x12\x18\n\x14\x45VENT_SEVERITY_ERROR\x10\x03\x12\x1b\n\x17\x45VENT_SEVERITY_CRITICAL\x10\x04\x12\x18\n\x14\x45VENT_SEVERITY_DEBUG\x10\x05*\x85\x03\n\rComponentType\x12\x1e\n\x1a\x43OMPONENT_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43OMPONENT_TYPE_DEVICE\x10\x01\x12\x1c\n\x18\x43OMPONENT_TYPE_INTERFACE\x10\x02\x12\x1a\n\x16\x43OMPONENT_TYPE_TURBINE\x10\x03\x12\x16\n\x12\x43OMPONENT_TYPE_VDS\x10\x04\x12 \n\x1c\x43OMPONENT_TYPE_VDS_INTERFACE\x10\x05\x12\x15\n\x11\x43OMPONENT_TYPE_VM\x10\x06\x12\x1f\n\x1b\x43OMPONENT_TYPE_VM_INTERFACE\x10\x07\x12\"\n\x1e\x43OMPONENT_TYPE_WORKLOAD_SERVER\x10\x08\x12,\n(COMPONENT_TYPE_WORKLOAD_SERVER_INTERFACE\x10\t\x12\x1e\n\x1a\x43OMPONENT_TYPE_APPLICATION\x10\n\x12\x1b\n\x17\x43OMPONENT_TYPE_CVP_NODE\x10\x0b\x42(Z&arista/resources/arista/event.v1;eventb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.event.v1.event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&arista/resources/arista/event.v1;event'
  _EVENTCOMPONENT_COMPONENTSENTRY._options = None
  _EVENTCOMPONENT_COMPONENTSENTRY._serialized_options = b'8\001'
  _EVENTKEY._options = None
  _EVENTKEY._serialized_options = b'\200\216\031\001'
  _EVENTDATA_DATAENTRY._options = None
  _EVENTDATA_DATAENTRY._serialized_options = b'8\001'
  _EVENTNOTESCONFIG_NOTESENTRY._options = None
  _EVENTNOTESCONFIG_NOTESENTRY._serialized_options = b'8\001'
  _EVENTANNOTATIONCONFIG._options = None
  _EVENTANNOTATIONCONFIG._serialized_options = b'\372\215\031\002rw'
  _EVENTNOTES_NOTESENTRY._options = None
  _EVENTNOTES_NOTESENTRY._serialized_options = b'8\001'
  _EVENT._options = None
  _EVENT._serialized_options = b'\372\215\031\002ro'
  _USEREVENTCREATIONKEY._options = None
  _USEREVENTCREATIONKEY._serialized_options = b'\200\216\031\001'
  _USEREVENTCREATIONCONFIG._options = None
  _USEREVENTCREATIONCONFIG._serialized_options = b'\372\215\031\002rw'
  _globals['_EVENTSEVERITY']._serialized_start=2674
  _globals['_EVENTSEVERITY']._serialized_end=2855
  _globals['_COMPONENTTYPE']._serialized_start=2858
  _globals['_COMPONENTTYPE']._serialized_end=3247
  _globals['_EVENTCOMPONENT']._serialized_start=136
  _globals['_EVENTCOMPONENT']._serialized_end=318
  _globals['_EVENTCOMPONENT_COMPONENTSENTRY']._serialized_start=269
  _globals['_EVENTCOMPONENT_COMPONENTSENTRY']._serialized_end=318
  _globals['_EVENTCOMPONENTS']._serialized_start=320
  _globals['_EVENTCOMPONENTS']._serialized_end=390
  _globals['_EVENTACK']._serialized_start=393
  _globals['_EVENTACK']._serialized_end=535
  _globals['_EVENTREAD']._serialized_start=538
  _globals['_EVENTREAD']._serialized_end=684
  _globals['_EVENTNOTECONFIG']._serialized_start=686
  _globals['_EVENTNOTECONFIG']._serialized_end=747
  _globals['_EVENTNOTE']._serialized_start=749
  _globals['_EVENTNOTE']._serialized_end=856
  _globals['_EVENTKEY']._serialized_start=858
  _globals['_EVENTKEY']._serialized_end=964
  _globals['_EVENTDATA']._serialized_start=966
  _globals['_EVENTDATA']._serialized_end=1074
  _globals['_EVENTDATA_DATAENTRY']._serialized_start=1031
  _globals['_EVENTDATA_DATAENTRY']._serialized_end=1074
  _globals['_EVENTNOTESCONFIG']._serialized_start=1077
  _globals['_EVENTNOTESCONFIG']._serialized_end=1236
  _globals['_EVENTNOTESCONFIG_NOTESENTRY']._serialized_start=1158
  _globals['_EVENTNOTESCONFIG_NOTESENTRY']._serialized_end=1236
  _globals['_EVENTANNOTATIONCONFIG']._serialized_start=1239
  _globals['_EVENTANNOTATIONCONFIG']._serialized_end=1443
  _globals['_EVENTNOTES']._serialized_start=1446
  _globals['_EVENTNOTES']._serialized_end=1587
  _globals['_EVENTNOTES_NOTESENTRY']._serialized_start=1515
  _globals['_EVENTNOTES_NOTESENTRY']._serialized_end=1587
  _globals['_EVENT']._serialized_start=1590
  _globals['_EVENT']._serialized_end=2165
  _globals['_USEREVENTCREATIONKEY']._serialized_start=2167
  _globals['_USEREVENTCREATIONKEY']._serialized_end=2238
  _globals['_USEREVENTCREATIONCONFIG']._serialized_start=2241
  _globals['_USEREVENTCREATIONCONFIG']._serialized_end=2671
# @@protoc_insertion_point(module_scope)
