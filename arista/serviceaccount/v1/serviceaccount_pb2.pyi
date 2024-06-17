"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import fmp.wrappers_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AccountStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _AccountStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AccountStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ACCOUNT_STATUS_UNSPECIFIED: _AccountStatus.ValueType  # 0
    """ACCOUNT_STATUS_UNSPECIFIED indicates the service account status is unspecified."""

    ACCOUNT_STATUS_ENABLED: _AccountStatus.ValueType  # 1
    """ACCOUNT_STATUS_ENABLED indicates the service account is enabled."""

    ACCOUNT_STATUS_DISABLED: _AccountStatus.ValueType  # 2
    """ACCOUNT_STATUS_DISABLED indicates the service account is disabled."""

class AccountStatus(_AccountStatus, metaclass=_AccountStatusEnumTypeWrapper):
    """AccountStatus determines whether an service account is enabled or disabled."""
    pass

ACCOUNT_STATUS_UNSPECIFIED: AccountStatus.ValueType  # 0
"""ACCOUNT_STATUS_UNSPECIFIED indicates the service account status is unspecified."""

ACCOUNT_STATUS_ENABLED: AccountStatus.ValueType  # 1
"""ACCOUNT_STATUS_ENABLED indicates the service account is enabled."""

ACCOUNT_STATUS_DISABLED: AccountStatus.ValueType  # 2
"""ACCOUNT_STATUS_DISABLED indicates the service account is disabled."""

global___AccountStatus = AccountStatus


class AccountKey(google.protobuf.message.Message):
    """AccountKey contains the name of the service account."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue:
        """name is the unique identifier of the service account."""
        pass
    def __init__(self,
        *,
        name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["name",b"name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___AccountKey = AccountKey

class AccountConfig(google.protobuf.message.Message):
    """AccountConfig holds the configuration for a service account."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    GROUPS_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___AccountKey:
        """key contains the name of the service account."""
        pass
    status: global___AccountStatus.ValueType
    """status determines if the service account is enabled or disabled. New service accounts are
    enabled by default.
    """

    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue:
        """description is a comment describing the service account."""
        pass
    @property
    def groups(self) -> fmp.wrappers_pb2.RepeatedString:
        """groups is a list of roles that the service account inherits permissions from."""
        pass
    def __init__(self,
        *,
        key: typing.Optional[global___AccountKey] = ...,
        status: global___AccountStatus.ValueType = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        groups: typing.Optional[fmp.wrappers_pb2.RepeatedString] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["description",b"description","groups",b"groups","key",b"key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","groups",b"groups","key",b"key","status",b"status"]) -> None: ...
global___AccountConfig = AccountConfig

class Account(google.protobuf.message.Message):
    """Account describes a service account."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    GROUPS_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    LAST_ACCESS_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___AccountKey:
        """key uniquely identifies the service account."""
        pass
    status: global___AccountStatus.ValueType
    """status determines whether the service account is enabled or disabled."""

    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue:
        """description is a comment describing the service account."""
        pass
    @property
    def groups(self) -> fmp.wrappers_pb2.RepeatedString:
        """groups is a list of roles that the service account inherits permissions from."""
        pass
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue:
        """created_by is the name of the entity that created the service account."""
        pass
    @property
    def last_access(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """last_access is the time when the service account was last fetched."""
        pass
    def __init__(self,
        *,
        key: typing.Optional[global___AccountKey] = ...,
        status: global___AccountStatus.ValueType = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        groups: typing.Optional[fmp.wrappers_pb2.RepeatedString] = ...,
        created_by: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        last_access: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_by",b"created_by","description",b"description","groups",b"groups","key",b"key","last_access",b"last_access"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_by",b"created_by","description",b"description","groups",b"groups","key",b"key","last_access",b"last_access","status",b"status"]) -> None: ...
global___Account = Account

class TokenKey(google.protobuf.message.Message):
    """TokenKey contains service account token ID."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.StringValue:
        """id is the unique identifier of the service account token."""
        pass
    def __init__(self,
        *,
        id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id",b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___TokenKey = TokenKey

class TokenConfig(google.protobuf.message.Message):
    """TokenConfig holds the configuration for a service account token. The token is a signed JWT which
    can be used as a credential for REST and WRPC endpoints.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    VALID_FOR_FIELD_NUMBER: builtins.int
    TOKEN_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___TokenKey:
        """key uniquely identifies the service account token."""
        pass
    @property
    def user(self) -> google.protobuf.wrappers_pb2.StringValue:
        """user is the name of the service account that the token is generated for."""
        pass
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue:
        """description is a short name or comment used to identify the service account token."""
        pass
    @property
    def valid_for(self) -> google.protobuf.duration_pb2.Duration:
        """valid_for determines the duration that the service account token will be valid for."""
        pass
    @property
    def token(self) -> google.protobuf.wrappers_pb2.StringValue:
        """token is the JWT token generated for a service account token.
        It is only populated in Set response.
        """
        pass
    def __init__(self,
        *,
        key: typing.Optional[global___TokenKey] = ...,
        user: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        valid_for: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        token: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["description",b"description","key",b"key","token",b"token","user",b"user","valid_for",b"valid_for"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","key",b"key","token",b"token","user",b"user","valid_for",b"valid_for"]) -> None: ...
global___TokenConfig = TokenConfig

class Token(google.protobuf.message.Message):
    """Token describes a service account token."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    VALID_UNTIL_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    LAST_USED_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___TokenKey:
        """key uniquely identifies the service account token."""
        pass
    @property
    def user(self) -> google.protobuf.wrappers_pb2.StringValue:
        """user is the name of the service account that the token is generated for."""
        pass
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue:
        """description is a short name or comment used to identify the service account token."""
        pass
    @property
    def valid_until(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """valid_until is the time that the service account token will be valid until."""
        pass
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue:
        """created_by is the name of the entity that created the service account token."""
        pass
    @property
    def last_used(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """last_used is the time when the service account token was last used to authenticate."""
        pass
    def __init__(self,
        *,
        key: typing.Optional[global___TokenKey] = ...,
        user: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        valid_until: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        created_by: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        last_used: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_by",b"created_by","description",b"description","key",b"key","last_used",b"last_used","user",b"user","valid_until",b"valid_until"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_by",b"created_by","description",b"description","key",b"key","last_used",b"last_used","user",b"user","valid_until",b"valid_until"]) -> None: ...
global___Token = Token