# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/studio.v1/studio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fmp import extensions_pb2 as fmp_dot_extensions__pb2
from fmp import wrappers_pb2 as fmp_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61rista/studio.v1/studio.proto\x12\x10\x61rista.studio.v1\x1a\x14\x66mp/extensions.proto\x1a\x12\x66mp/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"v\n\tStudioKey\x12/\n\tstudio_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cworkspace_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\xb6\x02\n\x0cStudioConfig\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.arista.studio.v1.StudioKey\x12*\n\x06remove\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0c\x64isplay_name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x08template\x18\x05 \x01(\x0b\x32\x1a.arista.studio.v1.Template\x12\x33\n\x0cinput_schema\x18\x06 \x01(\x0b\x32\x1d.arista.studio.v1.InputSchema:\x06\xfa\x8d\x19\x02rw\"\xb1\x02\n\rStudioSummary\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.arista.studio.v1.StudioKey\x12\x32\n\x0c\x64isplay_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\timmutable\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08\x65ntities\x18\x05 \x01(\x0b\x32\x1a.arista.studio.v1.Entities\x12*\n\x06in_use\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue:\x06\xfa\x8d\x19\x02ro\"\xd6\x01\n\x06\x45ntity\x12\x31\n\x0b\x65ntity_type\x18\x01 \x01(\x0e\x32\x1c.arista.studio.v1.EntityType\x12\x34\n\x10last_modified_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10last_modified_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x07removed\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x8b\x01\n\x08\x45ntities\x12\x36\n\x06values\x18\x01 \x03(\x0b\x32&.arista.studio.v1.Entities.ValuesEntry\x1aG\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.arista.studio.v1.Entity:\x02\x38\x01\"\x8e\x04\n\x06Studio\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.arista.studio.v1.StudioKey\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\ncreated_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10last_modified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10last_modified_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x64isplay_name\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x08template\x18\x08 \x01(\x0b\x32\x1a.arista.studio.v1.Template\x12\x33\n\x0cinput_schema\x18\t \x01(\x0b\x32\x1d.arista.studio.v1.InputSchema\x12\x32\n\x0c\x66rom_package\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x06\xfa\x8d\x19\x02roJ\x04\x08\n\x10\x0b\"\x9f\x01\n\x12\x41ssignedTagsConfig\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.arista.studio.v1.StudioKey\x12*\n\x06remove\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x05query\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x06\xfa\x8d\x19\x02rw\"\xbd\x02\n\x0c\x41ssignedTags\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.arista.studio.v1.StudioKey\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\ncreated_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10last_modified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10last_modified_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05query\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x06\xfa\x8d\x19\x02ro\"\x99\x01\n\tInputsKey\x12/\n\tstudio_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cworkspace_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12!\n\x04path\x18\x03 \x01(\x0b\x32\x13.fmp.RepeatedString:\x04\x80\x8e\x19\x01\"\x9a\x01\n\x0cInputsConfig\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.arista.studio.v1.InputsKey\x12*\n\x06remove\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x06inputs\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x06\xfa\x8d\x19\x02rw\"\xb8\x02\n\x06Inputs\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.arista.studio.v1.InputsKey\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\ncreated_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10last_modified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10last_modified_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06inputs\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x06\xfa\x8d\x19\x02ro\"d\n\x08Template\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.arista.studio.v1.TemplateType\x12*\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"K\n\x16\x42ooleanInputFieldProps\x12\x31\n\rdefault_value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x8d\x02\n\x16IntegerInputFieldProps\x12\x32\n\rdefault_value\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x0estatic_options\x18\x02 \x01(\x0b\x32\x12.fmp.RepeatedInt64\x12+\n\x05range\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x0f\x64ynamic_options\x18\x04 \x01(\x0b\x32\x13.fmp.RepeatedString\x12\x38\n\x14\x65xtra_values_allowed\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xde\x01\n\x14\x46loatInputFieldProps\x12\x32\n\rdefault_value\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12*\n\x0estatic_options\x18\x03 \x01(\x0b\x32\x12.fmp.RepeatedFloat\x12,\n\x0f\x64ynamic_options\x18\x04 \x01(\x0b\x32\x13.fmp.RepeatedString\x12\x38\n\x14\x65xtra_values_allowed\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x9b\x03\n\x15StringInputFieldProps\x12\x33\n\rdefault_value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x0estatic_options\x18\x03 \x01(\x0b\x32\x13.fmp.RepeatedString\x12,\n\x0f\x64ynamic_options\x18\x04 \x01(\x0b\x32\x13.fmp.RepeatedString\x12,\n\x06length\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07pattern\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x66ormat\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\tis_secret\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14\x65xtra_values_allowed\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"<\n\x14GroupInputFieldProps\x12$\n\x07members\x18\x01 \x01(\x0b\x32\x13.fmp.RepeatedString\"{\n\x19\x43ollectionInputFieldProps\x12\x33\n\rbase_field_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x03key\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xbd\x02\n\x17ResolverInputFieldProps\x12\x33\n\rbase_field_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12@\n\x0c\x64isplay_mode\x18\x02 \x01(\x0e\x32*.arista.studio.v1.ResolverFieldDisplayMode\x12<\n\ninput_mode\x18\x03 \x01(\x0e\x32(.arista.studio.v1.ResolverFieldInputMode\x12\x35\n\x0finput_tag_label\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10tag_filter_query\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x8d\x02\n\x19TagMatcherInputFieldProps\x12?\n\x10tag_matcher_mode\x18\x01 \x01(\x0e\x32%.arista.studio.v1.TagMatcherFieldMode\x12\x37\n\x11tag_matcher_label\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10tag_filter_query\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12>\n\x1aresolver_filtering_allowed\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xe8\x06\n\nInputField\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x04type\x18\x02 \x01(\x0e\x32 .arista.studio.v1.InputFieldType\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05label\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x08required\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\rboolean_props\x18\x07 \x01(\x0b\x32(.arista.studio.v1.BooleanInputFieldProps\x12?\n\rinteger_props\x18\x08 \x01(\x0b\x32(.arista.studio.v1.IntegerInputFieldProps\x12;\n\x0b\x66loat_props\x18\t \x01(\x0b\x32&.arista.studio.v1.FloatInputFieldProps\x12=\n\x0cstring_props\x18\n \x01(\x0b\x32\'.arista.studio.v1.StringInputFieldProps\x12;\n\x0bgroup_props\x18\x0b \x01(\x0b\x32&.arista.studio.v1.GroupInputFieldProps\x12\x45\n\x10\x63ollection_props\x18\x0c \x01(\x0b\x32+.arista.studio.v1.CollectionInputFieldProps\x12\x41\n\x0eresolver_props\x18\r \x01(\x0b\x32).arista.studio.v1.ResolverInputFieldProps\x12\x39\n\x13\x61uto_fill_action_id\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x46\n\x11tag_matcher_props\x18\x0f \x01(\x0b\x32+.arista.studio.v1.TagMatcherInputFieldProps\"\x95\x01\n\x0bInputFields\x12\x39\n\x06values\x18\x01 \x03(\x0b\x32).arista.studio.v1.InputFields.ValuesEntry\x1aK\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.arista.studio.v1.InputField:\x02\x38\x01\"5\n\x06Layout\x12+\n\x05value\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"f\n\x0bInputSchema\x12-\n\x06\x66ields\x18\x01 \x01(\x0b\x32\x1d.arista.studio.v1.InputFields\x12(\n\x06layout\x18\x02 \x01(\x0b\x32\x18.arista.studio.v1.Layout\"q\n\x0bSecretInput\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.arista.studio.v1.InputsKey\x12\x30\n\nplain_text\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x06\xfa\x8d\x19\x02ro\"\xb4\x01\n\x11\x41utofillActionKey\x12/\n\tstudio_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cworkspace_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0einput_field_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\xa9\x02\n\x14\x41utofillActionConfig\x12\x30\n\x03key\x18\x01 \x01(\x0b\x32#.arista.studio.v1.AutofillActionKey\x12*\n\x06remove\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\taction_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12G\n\x12\x61rgument_providers\x18\x05 \x01(\x0b\x32+.arista.studio.v1.AutofillArgumentProviders:\x06\xfa\x8d\x19\x02rw\"\xc7\x03\n\x0e\x41utofillAction\x12\x30\n\x03key\x18\x01 \x01(\x0b\x32#.arista.studio.v1.AutofillActionKey\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\ncreated_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10last_modified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10last_modified_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\taction_id\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12G\n\x12\x61rgument_providers\x18\x08 \x01(\x0b\x32+.arista.studio.v1.AutofillArgumentProviders:\x06\xfa\x8d\x19\x02ro\"\xbf\x01\n\x19\x41utofillArgumentProviders\x12G\n\x06values\x18\x01 \x03(\x0b\x32\x37.arista.studio.v1.AutofillArgumentProviders.ValuesEntry\x1aY\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.arista.studio.v1.AutofillArgumentProvider:\x02\x38\x01\"}\n\x18\x41utofillArgumentProvider\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.arista.studio.v1.AutofillProviderType\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue*\xb5\x01\n\nEntityType\x12\x1b\n\x17\x45NTITY_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x45NTITY_TYPE_STUDIO\x10\x01\x12\x16\n\x12\x45NTITY_TYPE_INPUTS\x10\x02\x12\x1d\n\x19\x45NTITY_TYPE_ASSIGNED_TAGS\x10\x03\x12\x1a\n\x16\x45NTITY_TYPE_BUILD_HOOK\x10\x04\x12\x1f\n\x1b\x45NTITY_TYPE_AUTOFILL_ACTION\x10\x05*t\n\x0cTemplateType\x12\x1d\n\x19TEMPLATE_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12TEMPLATE_TYPE_MAKO\x10\x01\x12\x17\n\x13TEMPLATE_TYPE_JINJA\x10\x02\x12\x14\n\x10TEMPLATE_TYPE_GO\x10\x03*\xa5\x02\n\x0eInputFieldType\x12 \n\x1cINPUT_FIELD_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18INPUT_FIELD_TYPE_BOOLEAN\x10\x01\x12\x1c\n\x18INPUT_FIELD_TYPE_INTEGER\x10\x02\x12\x1a\n\x16INPUT_FIELD_TYPE_FLOAT\x10\x03\x12\x1b\n\x17INPUT_FIELD_TYPE_STRING\x10\x04\x12\x1a\n\x16INPUT_FIELD_TYPE_GROUP\x10\x05\x12\x1f\n\x1bINPUT_FIELD_TYPE_COLLECTION\x10\x06\x12\x1d\n\x19INPUT_FIELD_TYPE_RESOLVER\x10\x07\x12 \n\x1cINPUT_FIELD_TYPE_TAG_MATCHER\x10\x08*\x8b\x02\n\x16ResolverFieldInputMode\x12)\n%RESOLVER_FIELD_INPUT_MODE_UNSPECIFIED\x10\x00\x12/\n+RESOLVER_FIELD_INPUT_MODE_SINGLE_DEVICE_TAG\x10\x01\x12\x32\n.RESOLVER_FIELD_INPUT_MODE_SINGLE_INTERFACE_TAG\x10\x02\x12.\n*RESOLVER_FIELD_INPUT_MODE_MULTI_DEVICE_TAG\x10\x03\x12\x31\n-RESOLVER_FIELD_INPUT_MODE_MULTI_INTERFACE_TAG\x10\x04*\x94\x01\n\x18ResolverFieldDisplayMode\x12+\n\'RESOLVER_FIELD_DISPLAY_MODE_UNSPECIFIED\x10\x00\x12#\n\x1fRESOLVER_FIELD_DISPLAY_MODE_ALL\x10\x01\x12&\n\"RESOLVER_FIELD_DISPLAY_MODE_SPARSE\x10\x02*\xf9\x01\n\x13TagMatcherFieldMode\x12&\n\"TAG_MATCHER_FIELD_MODE_UNSPECIFIED\x10\x00\x12,\n(TAG_MATCHER_FIELD_MODE_SINGLE_DEVICE_TAG\x10\x01\x12/\n+TAG_MATCHER_FIELD_MODE_SINGLE_INTERFACE_TAG\x10\x02\x12+\n\'TAG_MATCHER_FIELD_MODE_MULTI_DEVICE_TAG\x10\x03\x12.\n*TAG_MATCHER_FIELD_MODE_MULTI_INTERFACE_TAG\x10\x04*\xb3\x01\n\x14\x41utofillProviderType\x12&\n\"AUTOFILL_PROVIDER_TYPE_UNSPECIFIED\x10\x00\x12)\n%AUTOFILL_PROVIDER_TYPE_USER_SPECIFIED\x10\x01\x12%\n!AUTOFILL_PROVIDER_TYPE_PREDEFINED\x10\x02\x12!\n\x1d\x41UTOFILL_PROVIDER_TYPE_LINKED\x10\x03\x42]ZDgithub.com/aristanetworks/cloudvision-go/api/arista/studio.v1;studio\xba\x9a\x19\x13repeated-key-fieldsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.studio.v1.studio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/aristanetworks/cloudvision-go/api/arista/studio.v1;studio\272\232\031\023repeated-key-fields'
  _STUDIOKEY._options = None
  _STUDIOKEY._serialized_options = b'\200\216\031\001'
  _STUDIOCONFIG._options = None
  _STUDIOCONFIG._serialized_options = b'\372\215\031\002rw'
  _STUDIOSUMMARY._options = None
  _STUDIOSUMMARY._serialized_options = b'\372\215\031\002ro'
  _ENTITIES_VALUESENTRY._options = None
  _ENTITIES_VALUESENTRY._serialized_options = b'8\001'
  _STUDIO._options = None
  _STUDIO._serialized_options = b'\372\215\031\002ro'
  _ASSIGNEDTAGSCONFIG._options = None
  _ASSIGNEDTAGSCONFIG._serialized_options = b'\372\215\031\002rw'
  _ASSIGNEDTAGS._options = None
  _ASSIGNEDTAGS._serialized_options = b'\372\215\031\002ro'
  _INPUTSKEY._options = None
  _INPUTSKEY._serialized_options = b'\200\216\031\001'
  _INPUTSCONFIG._options = None
  _INPUTSCONFIG._serialized_options = b'\372\215\031\002rw'
  _INPUTS._options = None
  _INPUTS._serialized_options = b'\372\215\031\002ro'
  _INPUTFIELDS_VALUESENTRY._options = None
  _INPUTFIELDS_VALUESENTRY._serialized_options = b'8\001'
  _SECRETINPUT._options = None
  _SECRETINPUT._serialized_options = b'\372\215\031\002ro'
  _AUTOFILLACTIONKEY._options = None
  _AUTOFILLACTIONKEY._serialized_options = b'\200\216\031\001'
  _AUTOFILLACTIONCONFIG._options = None
  _AUTOFILLACTIONCONFIG._serialized_options = b'\372\215\031\002rw'
  _AUTOFILLACTION._options = None
  _AUTOFILLACTION._serialized_options = b'\372\215\031\002ro'
  _AUTOFILLARGUMENTPROVIDERS_VALUESENTRY._options = None
  _AUTOFILLARGUMENTPROVIDERS_VALUESENTRY._serialized_options = b'8\001'
  _globals['_ENTITYTYPE']._serialized_start=7330
  _globals['_ENTITYTYPE']._serialized_end=7511
  _globals['_TEMPLATETYPE']._serialized_start=7513
  _globals['_TEMPLATETYPE']._serialized_end=7629
  _globals['_INPUTFIELDTYPE']._serialized_start=7632
  _globals['_INPUTFIELDTYPE']._serialized_end=7925
  _globals['_RESOLVERFIELDINPUTMODE']._serialized_start=7928
  _globals['_RESOLVERFIELDINPUTMODE']._serialized_end=8195
  _globals['_RESOLVERFIELDDISPLAYMODE']._serialized_start=8198
  _globals['_RESOLVERFIELDDISPLAYMODE']._serialized_end=8346
  _globals['_TAGMATCHERFIELDMODE']._serialized_start=8349
  _globals['_TAGMATCHERFIELDMODE']._serialized_end=8598
  _globals['_AUTOFILLPROVIDERTYPE']._serialized_start=8601
  _globals['_AUTOFILLPROVIDERTYPE']._serialized_end=8780
  _globals['_STUDIOKEY']._serialized_start=158
  _globals['_STUDIOKEY']._serialized_end=276
  _globals['_STUDIOCONFIG']._serialized_start=279
  _globals['_STUDIOCONFIG']._serialized_end=589
  _globals['_STUDIOSUMMARY']._serialized_start=592
  _globals['_STUDIOSUMMARY']._serialized_end=897
  _globals['_ENTITY']._serialized_start=900
  _globals['_ENTITY']._serialized_end=1114
  _globals['_ENTITIES']._serialized_start=1117
  _globals['_ENTITIES']._serialized_end=1256
  _globals['_ENTITIES_VALUESENTRY']._serialized_start=1185
  _globals['_ENTITIES_VALUESENTRY']._serialized_end=1256
  _globals['_STUDIO']._serialized_start=1259
  _globals['_STUDIO']._serialized_end=1785
  _globals['_ASSIGNEDTAGSCONFIG']._serialized_start=1788
  _globals['_ASSIGNEDTAGSCONFIG']._serialized_end=1947
  _globals['_ASSIGNEDTAGS']._serialized_start=1950
  _globals['_ASSIGNEDTAGS']._serialized_end=2267
  _globals['_INPUTSKEY']._serialized_start=2270
  _globals['_INPUTSKEY']._serialized_end=2423
  _globals['_INPUTSCONFIG']._serialized_start=2426
  _globals['_INPUTSCONFIG']._serialized_end=2580
  _globals['_INPUTS']._serialized_start=2583
  _globals['_INPUTS']._serialized_end=2895
  _globals['_TEMPLATE']._serialized_start=2897
  _globals['_TEMPLATE']._serialized_end=2997
  _globals['_BOOLEANINPUTFIELDPROPS']._serialized_start=2999
  _globals['_BOOLEANINPUTFIELDPROPS']._serialized_end=3074
  _globals['_INTEGERINPUTFIELDPROPS']._serialized_start=3077
  _globals['_INTEGERINPUTFIELDPROPS']._serialized_end=3346
  _globals['_FLOATINPUTFIELDPROPS']._serialized_start=3349
  _globals['_FLOATINPUTFIELDPROPS']._serialized_end=3571
  _globals['_STRINGINPUTFIELDPROPS']._serialized_start=3574
  _globals['_STRINGINPUTFIELDPROPS']._serialized_end=3985
  _globals['_GROUPINPUTFIELDPROPS']._serialized_start=3987
  _globals['_GROUPINPUTFIELDPROPS']._serialized_end=4047
  _globals['_COLLECTIONINPUTFIELDPROPS']._serialized_start=4049
  _globals['_COLLECTIONINPUTFIELDPROPS']._serialized_end=4172
  _globals['_RESOLVERINPUTFIELDPROPS']._serialized_start=4175
  _globals['_RESOLVERINPUTFIELDPROPS']._serialized_end=4492
  _globals['_TAGMATCHERINPUTFIELDPROPS']._serialized_start=4495
  _globals['_TAGMATCHERINPUTFIELDPROPS']._serialized_end=4764
  _globals['_INPUTFIELD']._serialized_start=4767
  _globals['_INPUTFIELD']._serialized_end=5639
  _globals['_INPUTFIELDS']._serialized_start=5642
  _globals['_INPUTFIELDS']._serialized_end=5791
  _globals['_INPUTFIELDS_VALUESENTRY']._serialized_start=5716
  _globals['_INPUTFIELDS_VALUESENTRY']._serialized_end=5791
  _globals['_LAYOUT']._serialized_start=5793
  _globals['_LAYOUT']._serialized_end=5846
  _globals['_INPUTSCHEMA']._serialized_start=5848
  _globals['_INPUTSCHEMA']._serialized_end=5950
  _globals['_SECRETINPUT']._serialized_start=5952
  _globals['_SECRETINPUT']._serialized_end=6065
  _globals['_AUTOFILLACTIONKEY']._serialized_start=6068
  _globals['_AUTOFILLACTIONKEY']._serialized_end=6248
  _globals['_AUTOFILLACTIONCONFIG']._serialized_start=6251
  _globals['_AUTOFILLACTIONCONFIG']._serialized_end=6548
  _globals['_AUTOFILLACTION']._serialized_start=6551
  _globals['_AUTOFILLACTION']._serialized_end=7006
  _globals['_AUTOFILLARGUMENTPROVIDERS']._serialized_start=7009
  _globals['_AUTOFILLARGUMENTPROVIDERS']._serialized_end=7200
  _globals['_AUTOFILLARGUMENTPROVIDERS_VALUESENTRY']._serialized_start=7111
  _globals['_AUTOFILLARGUMENTPROVIDERS_VALUESENTRY']._serialized_end=7200
  _globals['_AUTOFILLARGUMENTPROVIDER']._serialized_start=7202
  _globals['_AUTOFILLARGUMENTPROVIDER']._serialized_end=7327
# @@protoc_insertion_point(module_scope)
