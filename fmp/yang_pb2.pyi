"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MACAddress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: typing.Text
    def __init__(self,
        *,
        value: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___MACAddress = MACAddress

class RepeatedMACAddress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MACAddress]: ...
    def __init__(self,
        *,
        values: typing.Optional[typing.Iterable[global___MACAddress]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values",b"values"]) -> None: ...
global___RepeatedMACAddress = RepeatedMACAddress