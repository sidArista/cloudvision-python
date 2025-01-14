"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import arista.endpointlocation.v1.endpointlocation_pb2
import arista.subscriptions.subscriptions_pb2
import arista.time.time_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MetaResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TIME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time holds the timestamp of the last item included in the metadata calculation."""
        pass
    type: arista.subscriptions.subscriptions_pb2.Operation.ValueType
    """Operation indicates how the value in this response should be considered.
    Under non-subscribe requests, this value should always be INITIAL. In a subscription,
    once all initial data is streamed and the client begins to receive modification updates,
    you should not see INITIAL again.
    """

    @property
    def count(self) -> google.protobuf.wrappers_pb2.UInt32Value:
        """Count is the number of items present under the conditions of the request."""
        pass
    def __init__(self,
        *,
        time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        type: arista.subscriptions.subscriptions_pb2.Operation.ValueType = ...,
        count: typing.Optional[google.protobuf.wrappers_pb2.UInt32Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["count",b"count","time",b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["count",b"count","time",b"time","type",b"type"]) -> None: ...
global___MetaResponse = MetaResponse

class EndpointLocationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocationKey:
        """Key uniquely identifies a EndpointLocation instance to retrieve.
        This value must be populated.
        """
        pass
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time indicates the time for which you are interested in the data.
        If no time is given, the server will use the time at which it makes the request.
        """
        pass
    def __init__(self,
        *,
        key: typing.Optional[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocationKey] = ...,
        time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["key",b"key","time",b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","time",b"time"]) -> None: ...
global___EndpointLocationRequest = EndpointLocationRequest

class EndpointLocationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation:
        """Value is the value requested.
        This structure will be fully-populated as it exists in the datastore. If
        optional fields were not given at creation, these fields will be empty or
        set to default values.
        """
        pass
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time carries the (UTC) timestamp of the last-modification of the
        EndpointLocation instance in this response.
        """
        pass
    def __init__(self,
        *,
        value: typing.Optional[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation] = ...,
        time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["time",b"time","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["time",b"time","value",b"value"]) -> None: ...
global___EndpointLocationResponse = EndpointLocationResponse

class EndpointLocationSomeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEYS_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocationKey]: ...
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time indicates the time for which you are interested in the data.
        If no time is given, the server will use the time at which it makes the request.
        """
        pass
    def __init__(self,
        *,
        keys: typing.Optional[typing.Iterable[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocationKey]] = ...,
        time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["time",b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["keys",b"keys","time",b"time"]) -> None: ...
global___EndpointLocationSomeRequest = EndpointLocationSomeRequest

class EndpointLocationSomeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation:
        """Value is the value requested.
        This structure will be fully-populated as it exists in the datastore. If
        optional fields were not given at creation, these fields will be empty or
        set to default values.
        """
        pass
    @property
    def error(self) -> google.protobuf.wrappers_pb2.StringValue:
        """Error is an optional field.
        It should be filled when there is an error in the GetSome process.
        """
        pass
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        value: typing.Optional[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation] = ...,
        error: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","time",b"time","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","time",b"time","value",b"value"]) -> None: ...
global___EndpointLocationSomeResponse = EndpointLocationSomeResponse

class EndpointLocationStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARTIAL_EQ_FILTER_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    @property
    def partial_eq_filter(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation]:
        """PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.
        This requires all provided fields to be equal to the response.

        While transparent to users, this field also allows services to optimize internal
        subscriptions if filter(s) are sufficiently specific.
        """
        pass
    @property
    def time(self) -> arista.time.time_pb2.TimeBounds:
        """TimeRange allows limiting response data to within a specified time window.
        If this field is populated, at least one of the two time fields are required.

        For GetAll, the fields start and end can be used as follows:

          * end: Returns the state of each EndpointLocation at end.
            * Each EndpointLocation response is fully-specified (all fields set).
          * start: Returns the state of each EndpointLocation at start, followed by updates until now.
            * Each EndpointLocation response at start is fully-specified, but updates may be partial.
          * start and end: Returns the state of each EndpointLocation at start, followed by updates
            until end.
            * Each EndpointLocation response at start is fully-specified, but updates until end may
              be partial.

        This field is not allowed in the Subscribe RPC.
        """
        pass
    def __init__(self,
        *,
        partial_eq_filter: typing.Optional[typing.Iterable[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation]] = ...,
        time: typing.Optional[arista.time.time_pb2.TimeBounds] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["time",b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_eq_filter",b"partial_eq_filter","time",b"time"]) -> None: ...
global___EndpointLocationStreamRequest = EndpointLocationStreamRequest

class EndpointLocationStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation:
        """Value is a value deemed relevant to the initiating request.
        This structure will always have its key-field populated. Which other fields are
        populated, and why, depends on the value of Operation and what triggered this notification.
        """
        pass
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time holds the timestamp of this EndpointLocation's last modification."""
        pass
    type: arista.subscriptions.subscriptions_pb2.Operation.ValueType
    """Operation indicates how the EndpointLocation value in this response should be considered.
    Under non-subscribe requests, this value should always be INITIAL. In a subscription,
    once all initial data is streamed and the client begins to receive modification updates,
    you should not see INITIAL again.
    """

    def __init__(self,
        *,
        value: typing.Optional[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation] = ...,
        time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        type: arista.subscriptions.subscriptions_pb2.Operation.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["time",b"time","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["time",b"time","type",b"type","value",b"value"]) -> None: ...
global___EndpointLocationStreamResponse = EndpointLocationStreamResponse

class EndpointLocationBatchedStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARTIAL_EQ_FILTER_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    MAX_MESSAGES_FIELD_NUMBER: builtins.int
    @property
    def partial_eq_filter(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation]:
        """PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.
        This requires all provided fields to be equal to the response.

        While transparent to users, this field also allows services to optimize internal
        subscriptions if filter(s) are sufficiently specific.
        """
        pass
    @property
    def time(self) -> arista.time.time_pb2.TimeBounds:
        """TimeRange allows limiting response data to within a specified time window.
        If this field is populated, at least one of the two time fields are required.

        For GetAll, the fields start and end can be used as follows:

          * end: Returns the state of each EndpointLocation at end.
            * Each EndpointLocation response is fully-specified (all fields set).
          * start: Returns the state of each EndpointLocation at start, followed by updates until now.
            * Each EndpointLocation response at start is fully-specified, but updates may be partial.
          * start and end: Returns the state of each EndpointLocation at start, followed by updates
            until end.
            * Each EndpointLocation response at start is fully-specified, but updates until end may
              be partial.

        This field is not allowed in the Subscribe RPC.
        """
        pass
    @property
    def max_messages(self) -> google.protobuf.wrappers_pb2.UInt32Value:
        """MaxMessages limits the maximum number of messages that can be contained in one batch.
        MaxMessages is required to be at least 1.
        The maximum number of messages in a batch is min(max_messages, INTERNAL_BATCH_LIMIT)
        INTERNAL_BATCH_LIMIT is set based on the maximum message size.
        """
        pass
    def __init__(self,
        *,
        partial_eq_filter: typing.Optional[typing.Iterable[arista.endpointlocation.v1.endpointlocation_pb2.EndpointLocation]] = ...,
        time: typing.Optional[arista.time.time_pb2.TimeBounds] = ...,
        max_messages: typing.Optional[google.protobuf.wrappers_pb2.UInt32Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["max_messages",b"max_messages","time",b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_messages",b"max_messages","partial_eq_filter",b"partial_eq_filter","time",b"time"]) -> None: ...
global___EndpointLocationBatchedStreamRequest = EndpointLocationBatchedStreamRequest

class EndpointLocationBatchedStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESPONSES_FIELD_NUMBER: builtins.int
    @property
    def responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EndpointLocationStreamResponse]:
        """Values are the values deemed relevant to the initiating request.
        The length of this structure is guaranteed to be between (inclusive) 1 and 
        min(req.max_messages, INTERNAL_BATCH_LIMIT).
        """
        pass
    def __init__(self,
        *,
        responses: typing.Optional[typing.Iterable[global___EndpointLocationStreamResponse]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["responses",b"responses"]) -> None: ...
global___EndpointLocationBatchedStreamResponse = EndpointLocationBatchedStreamResponse
