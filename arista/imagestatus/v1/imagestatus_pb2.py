# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/imagestatus.v1/imagestatus.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'arista/imagestatus.v1/imagestatus.proto\x12\x15\x61rista.imagestatus.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14\x66mp/extensions.proto\"\xa2\x01\n\rSoftwareImage\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07version\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x08metadata\x18\x03 \x01(\x0b\x32$.arista.imagestatus.v1.ImageMetadata\"\xf6\x01\n\rImageMetadata\x12-\n\x07version\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07release\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x66lavor\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07variant\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04\x61rch\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xf0\x02\n\tExtension\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07version\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0freboot_required\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x07present\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12@\n\tinstalled\x18\x05 \x01(\x0e\x32-.arista.imagestatus.v1.ExtensionInstallStatus\x12\x33\n\rstatus_detail\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0bis_embedded\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\">\n\nExtensions\x12\x30\n\x06values\x18\x01 \x03(\x0b\x32 .arista.imagestatus.v1.Extension\"\x8f\x02\n\x10\x43omplianceStatus\x12U\n\x1esoftware_image_compliance_code\x18\x01 \x01(\x0e\x32-.arista.imagestatus.v1.SoftwareComplianceCode\x12Q\n\x1aterminattr_compliance_code\x18\x02 \x01(\x0e\x32-.arista.imagestatus.v1.SoftwareComplianceCode\x12Q\n\x1a\x65xtensions_compliance_code\x18\x03 \x01(\x0e\x32-.arista.imagestatus.v1.SoftwareComplianceCode\"\xb9\x01\n\x15\x43omplianceStatusBySup\x12H\n\x06values\x18\x01 \x03(\x0b\x32\x38.arista.imagestatus.v1.ComplianceStatusBySup.ValuesEntry\x1aV\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.arista.imagestatus.v1.ComplianceStatus:\x02\x38\x01\"\xd3\x01\n\x0eRebootRequired\x12\x42\n\x1esoftware_image_reboot_required\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12>\n\x1aterminattr_reboot_required\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12=\n\x19\x65xtension_reboot_required\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xa2\x01\n\x11SoftwareImageDiff\x12+\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1d.arista.imagestatus.v1.DiffOp\x12/\n\x01\x61\x18\x02 \x01(\x0b\x32$.arista.imagestatus.v1.SoftwareImage\x12/\n\x01\x62\x18\x03 \x01(\x0b\x32$.arista.imagestatus.v1.SoftwareImage\"\xbe\x01\n\x17SoftwareImageDiffsBySup\x12J\n\x06values\x18\x01 \x03(\x0b\x32:.arista.imagestatus.v1.SoftwareImageDiffsBySup.ValuesEntry\x1aW\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.arista.imagestatus.v1.SoftwareImageDiff:\x02\x38\x01\"\x96\x01\n\rExtensionDiff\x12+\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1d.arista.imagestatus.v1.DiffOp\x12+\n\x01\x61\x18\x02 \x01(\x0b\x32 .arista.imagestatus.v1.Extension\x12+\n\x01\x62\x18\x03 \x01(\x0b\x32 .arista.imagestatus.v1.Extension\"\xb4\x01\n\x14TerminAttrDiffsBySup\x12G\n\x06values\x18\x01 \x03(\x0b\x32\x37.arista.imagestatus.v1.TerminAttrDiffsBySup.ValuesEntry\x1aS\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.arista.imagestatus.v1.ExtensionDiff:\x02\x38\x01\"F\n\x0e\x45xtensionDiffs\x12\x34\n\x06values\x18\x01 \x03(\x0b\x32$.arista.imagestatus.v1.ExtensionDiff\"\xb3\x01\n\x13\x45xtensionDiffsBySup\x12\x46\n\x06values\x18\x01 \x03(\x0b\x32\x36.arista.imagestatus.v1.ExtensionDiffsBySup.ValuesEntry\x1aT\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.arista.imagestatus.v1.ExtensionDiffs:\x02\x38\x01\"\x9d\x06\n\x0cImageSummary\x12)\n\x03sku\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12=\n\x19running_image_update_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\x1a\x64\x65signed_image_update_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x64ual_sup\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\x0b\x61\x63tive_slot\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x31\n\x0cstandby_slot\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12K\n\x13software_image_diff\x18\x07 \x01(\x0b\x32..arista.imagestatus.v1.SoftwareImageDiffsBySup\x12\x44\n\x0fterminattr_diff\x18\x08 \x01(\x0b\x32+.arista.imagestatus.v1.TerminAttrDiffsBySup\x12\x43\n\x0f\x65xtensions_diff\x18\t \x01(\x0b\x32*.arista.imagestatus.v1.ExtensionDiffsBySup\x12H\n\x11\x63ompliance_status\x18\n \x01(\x0e\x32-.arista.imagestatus.v1.SoftwareComplianceCode\x12@\n\ncompliance\x18\x0b \x01(\x0b\x32,.arista.imagestatus.v1.ComplianceStatusBySup\x12>\n\x0freboot_required\x18\x0c \x01(\x0b\x32%.arista.imagestatus.v1.RebootRequired\x12,\n\x06\x64igest\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\"C\n\nSummaryKey\x12/\n\tdevice_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\xe3\x01\n\x07Summary\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.imagestatus.v1.SummaryKey\x12\x34\n\x07summary\x18\x02 \x01(\x0b\x32#.arista.imagestatus.v1.ImageSummary\x12\x32\n\x06\x65rrors\x18\x03 \x01(\x0b\x32\".arista.imagestatus.v1.ImageErrors\x12\x36\n\x08warnings\x18\x04 \x01(\x0b\x32$.arista.imagestatus.v1.ImageWarnings:\x06\xfa\x8d\x19\x02ro\"\x9e\x01\n\nImageError\x12)\n\x03sku\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\nerror_code\x18\x02 \x01(\x0e\x32 .arista.imagestatus.v1.ErrorCode\x12/\n\terror_msg\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"@\n\x0bImageErrors\x12\x31\n\x06values\x18\x01 \x03(\x0b\x32!.arista.imagestatus.v1.ImageError\"\xa6\x01\n\x0cImageWarning\x12)\n\x03sku\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x0cwarning_code\x18\x02 \x01(\x0e\x32\".arista.imagestatus.v1.WarningCode\x12\x31\n\x0bwarning_msg\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"D\n\rImageWarnings\x12\x33\n\x06values\x18\x01 \x03(\x0b\x32#.arista.imagestatus.v1.ImageWarning*\xc4\x01\n\x16\x45xtensionInstallStatus\x12(\n$EXTENSION_INSTALL_STATUS_UNSPECIFIED\x10\x00\x12*\n&EXTENSION_INSTALL_STATUS_NOT_INSTALLED\x10\x01\x12&\n\"EXTENSION_INSTALL_STATUS_INSTALLED\x10\x02\x12,\n(EXTENSION_INSTALL_STATUS_FORCE_INSTALLED\x10\x03*\x92\x01\n\x16SoftwareComplianceCode\x12(\n$SOFTWARE_COMPLIANCE_CODE_UNSPECIFIED\x10\x00\x12$\n SOFTWARE_COMPLIANCE_CODE_IN_SYNC\x10\x01\x12(\n$SOFTWARE_COMPLIANCE_CODE_OUT_OF_SYNC\x10\x02*k\n\x06\x44iffOp\x12\x17\n\x13\x44IFF_OP_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x44IFF_OP_NOP\x10\x01\x12\x0f\n\x0b\x44IFF_OP_ADD\x10\x02\x12\x12\n\x0e\x44IFF_OP_DELETE\x10\x03\x12\x12\n\x0e\x44IFF_OP_CHANGE\x10\x04*\x9e\x05\n\tErrorCode\x12\x1a\n\x16\x45RROR_CODE_UNSPECIFIED\x10\x00\x12)\n!ERROR_CODE_SUPPORT_NOT_INTRODUCED\x10\x01\x1a\x02\x08\x01\x12\"\n\x1a\x45RROR_CODE_SUPPORT_REMOVED\x10\x02\x1a\x02\x08\x01\x12!\n\x1d\x45RROR_CODE_DEVICE_UNREACHABLE\x10\x03\x12 \n\x1c\x45RROR_CODE_VALIDATION_FAILED\x10\x04\x12-\n)ERROR_CODE_GET_PROPOSED_IMAGE_INFO_FAILED\x10\x05\x12G\n?ERROR_CODE_GET_RUNNING_IMAGE_INFO_FROM_ACTIVE_SUPERVISOR_FAILED\x10\x06\x1a\x02\x08\x01\x12\x45\n=ERROR_CODE_GET_RUNNING_IMAGE_INFO_FROM_PEER_SUPERVISOR_FAILED\x10\x07\x1a\x02\x08\x01\x12/\n+ERROR_CODE_EOS_TA_ARCHITECTURE_INCOMPATIBLE\x10\x08\x12!\n\x1d\x45RROR_CODE_TA_CV_INCOMPATIBLE\x10\t\x12\"\n\x1e\x45RROR_CODE_EOS_CV_INCOMPATIBLE\x10\n\x12)\n%ERROR_CODE_EOS_SUPPORT_NOT_INTRODUCED\x10\x0b\x12\"\n\x1e\x45RROR_CODE_EOS_SUPPORT_REMOVED\x10\x0c\x12/\n+ERROR_CODE_PHYSICAL_DEVICE_EOS_INCOMPATIBLE\x10\r\x12*\n&ERROR_CODE_TA_EMBEDDEDEXT_INCOMPATIBLE\x10\x0e*\xdd\x04\n\x0bWarningCode\x12\x1c\n\x18WARNING_CODE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bWARNING_CODE_NOT_APPLICABLE\x10\x01\x12$\n WARNING_CODE_SKUINFO_UNAVAILABLE\x10\x02\x12\'\n#WARNING_CODE_DEVICE_SKU_UNAVAILABLE\x10\x03\x12\x1c\n\x18WARNING_CODE_SWI_UNKNOWN\x10\x04\x12$\n WARNING_CODE_TA_EOS_INCOMPATIBLE\x10\x05\x12\'\n\x1fWARNING_CODE_TA_CV_INCOMPATIBLE\x10\x06\x1a\x02\x08\x01\x12(\n WARNING_CODE_EOS_CV_INCOMPATIBLE\x10\x07\x1a\x02\x08\x01\x12!\n\x1dWARNING_CODE_EOS_ARCH_UNKNOWN\x10\x08\x12,\n(WARNING_CODE_TA_EMBEDDEDEXT_INCOMPATIBLE\x10\t\x12&\n\x1eWARNING_CODE_ARCH_INCOMPATIBLE\x10\n\x1a\x02\x08\x01\x12,\n(WARNING_CODE_EOS_END_OF_LIFE_DATE_PASSED\x10\x0b\x12\'\n#WARNING_CODE_SUPPORT_NOT_INTRODUCED\x10\x0c\x12 \n\x1cWARNING_CODE_SUPPORT_REMOVED\x10\r\x12\x37\n3WARNING_CODE_RUNNING_TA_BELOW_MIN_SUPPORTED_VERSION\x10\x0e\x42^\n\x19\x63om.arista.imagestatus.v1B\x0bImagestatusP\x01Z2arista/resources/arista/imagestatus.v1;imagestatusb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.imagestatus.v1.imagestatus_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.arista.imagestatus.v1B\013ImagestatusP\001Z2arista/resources/arista/imagestatus.v1;imagestatus'
  _ERRORCODE.values_by_name["ERROR_CODE_SUPPORT_NOT_INTRODUCED"]._options = None
  _ERRORCODE.values_by_name["ERROR_CODE_SUPPORT_NOT_INTRODUCED"]._serialized_options = b'\010\001'
  _ERRORCODE.values_by_name["ERROR_CODE_SUPPORT_REMOVED"]._options = None
  _ERRORCODE.values_by_name["ERROR_CODE_SUPPORT_REMOVED"]._serialized_options = b'\010\001'
  _ERRORCODE.values_by_name["ERROR_CODE_GET_RUNNING_IMAGE_INFO_FROM_ACTIVE_SUPERVISOR_FAILED"]._options = None
  _ERRORCODE.values_by_name["ERROR_CODE_GET_RUNNING_IMAGE_INFO_FROM_ACTIVE_SUPERVISOR_FAILED"]._serialized_options = b'\010\001'
  _ERRORCODE.values_by_name["ERROR_CODE_GET_RUNNING_IMAGE_INFO_FROM_PEER_SUPERVISOR_FAILED"]._options = None
  _ERRORCODE.values_by_name["ERROR_CODE_GET_RUNNING_IMAGE_INFO_FROM_PEER_SUPERVISOR_FAILED"]._serialized_options = b'\010\001'
  _WARNINGCODE.values_by_name["WARNING_CODE_TA_CV_INCOMPATIBLE"]._options = None
  _WARNINGCODE.values_by_name["WARNING_CODE_TA_CV_INCOMPATIBLE"]._serialized_options = b'\010\001'
  _WARNINGCODE.values_by_name["WARNING_CODE_EOS_CV_INCOMPATIBLE"]._options = None
  _WARNINGCODE.values_by_name["WARNING_CODE_EOS_CV_INCOMPATIBLE"]._serialized_options = b'\010\001'
  _WARNINGCODE.values_by_name["WARNING_CODE_ARCH_INCOMPATIBLE"]._options = None
  _WARNINGCODE.values_by_name["WARNING_CODE_ARCH_INCOMPATIBLE"]._serialized_options = b'\010\001'
  _COMPLIANCESTATUSBYSUP_VALUESENTRY._options = None
  _COMPLIANCESTATUSBYSUP_VALUESENTRY._serialized_options = b'8\001'
  _SOFTWAREIMAGEDIFFSBYSUP_VALUESENTRY._options = None
  _SOFTWAREIMAGEDIFFSBYSUP_VALUESENTRY._serialized_options = b'8\001'
  _TERMINATTRDIFFSBYSUP_VALUESENTRY._options = None
  _TERMINATTRDIFFSBYSUP_VALUESENTRY._serialized_options = b'8\001'
  _EXTENSIONDIFFSBYSUP_VALUESENTRY._options = None
  _EXTENSIONDIFFSBYSUP_VALUESENTRY._serialized_options = b'8\001'
  _SUMMARYKEY._options = None
  _SUMMARYKEY._serialized_options = b'\200\216\031\001'
  _SUMMARY._options = None
  _SUMMARY._serialized_options = b'\372\215\031\002ro'
  _globals['_EXTENSIONINSTALLSTATUS']._serialized_start=4192
  _globals['_EXTENSIONINSTALLSTATUS']._serialized_end=4388
  _globals['_SOFTWARECOMPLIANCECODE']._serialized_start=4391
  _globals['_SOFTWARECOMPLIANCECODE']._serialized_end=4537
  _globals['_DIFFOP']._serialized_start=4539
  _globals['_DIFFOP']._serialized_end=4646
  _globals['_ERRORCODE']._serialized_start=4649
  _globals['_ERRORCODE']._serialized_end=5319
  _globals['_WARNINGCODE']._serialized_start=5322
  _globals['_WARNINGCODE']._serialized_end=5927
  _globals['_SOFTWAREIMAGE']._serialized_start=154
  _globals['_SOFTWAREIMAGE']._serialized_end=316
  _globals['_IMAGEMETADATA']._serialized_start=319
  _globals['_IMAGEMETADATA']._serialized_end=565
  _globals['_EXTENSION']._serialized_start=568
  _globals['_EXTENSION']._serialized_end=936
  _globals['_EXTENSIONS']._serialized_start=938
  _globals['_EXTENSIONS']._serialized_end=1000
  _globals['_COMPLIANCESTATUS']._serialized_start=1003
  _globals['_COMPLIANCESTATUS']._serialized_end=1274
  _globals['_COMPLIANCESTATUSBYSUP']._serialized_start=1277
  _globals['_COMPLIANCESTATUSBYSUP']._serialized_end=1462
  _globals['_COMPLIANCESTATUSBYSUP_VALUESENTRY']._serialized_start=1376
  _globals['_COMPLIANCESTATUSBYSUP_VALUESENTRY']._serialized_end=1462
  _globals['_REBOOTREQUIRED']._serialized_start=1465
  _globals['_REBOOTREQUIRED']._serialized_end=1676
  _globals['_SOFTWAREIMAGEDIFF']._serialized_start=1679
  _globals['_SOFTWAREIMAGEDIFF']._serialized_end=1841
  _globals['_SOFTWAREIMAGEDIFFSBYSUP']._serialized_start=1844
  _globals['_SOFTWAREIMAGEDIFFSBYSUP']._serialized_end=2034
  _globals['_SOFTWAREIMAGEDIFFSBYSUP_VALUESENTRY']._serialized_start=1947
  _globals['_SOFTWAREIMAGEDIFFSBYSUP_VALUESENTRY']._serialized_end=2034
  _globals['_EXTENSIONDIFF']._serialized_start=2037
  _globals['_EXTENSIONDIFF']._serialized_end=2187
  _globals['_TERMINATTRDIFFSBYSUP']._serialized_start=2190
  _globals['_TERMINATTRDIFFSBYSUP']._serialized_end=2370
  _globals['_TERMINATTRDIFFSBYSUP_VALUESENTRY']._serialized_start=2287
  _globals['_TERMINATTRDIFFSBYSUP_VALUESENTRY']._serialized_end=2370
  _globals['_EXTENSIONDIFFS']._serialized_start=2372
  _globals['_EXTENSIONDIFFS']._serialized_end=2442
  _globals['_EXTENSIONDIFFSBYSUP']._serialized_start=2445
  _globals['_EXTENSIONDIFFSBYSUP']._serialized_end=2624
  _globals['_EXTENSIONDIFFSBYSUP_VALUESENTRY']._serialized_start=2540
  _globals['_EXTENSIONDIFFSBYSUP_VALUESENTRY']._serialized_end=2624
  _globals['_IMAGESUMMARY']._serialized_start=2627
  _globals['_IMAGESUMMARY']._serialized_end=3424
  _globals['_SUMMARYKEY']._serialized_start=3426
  _globals['_SUMMARYKEY']._serialized_end=3493
  _globals['_SUMMARY']._serialized_start=3496
  _globals['_SUMMARY']._serialized_end=3723
  _globals['_IMAGEERROR']._serialized_start=3726
  _globals['_IMAGEERROR']._serialized_end=3884
  _globals['_IMAGEERRORS']._serialized_start=3886
  _globals['_IMAGEERRORS']._serialized_end=3950
  _globals['_IMAGEWARNING']._serialized_start=3953
  _globals['_IMAGEWARNING']._serialized_end=4119
  _globals['_IMAGEWARNINGS']._serialized_start=4121
  _globals['_IMAGEWARNINGS']._serialized_end=4189
# @@protoc_insertion_point(module_scope)
