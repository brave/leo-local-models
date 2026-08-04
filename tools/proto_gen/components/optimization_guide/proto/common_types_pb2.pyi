from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestContext(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTEXT_UNSPECIFIED: _ClassVar[RequestContext]
    CONTEXT_PAGE_NAVIGATION: _ClassVar[RequestContext]
    CONTEXT_BATCH_UPDATE_GOOGLE_SRP: _ClassVar[RequestContext]
    CONTEXT_BATCH_UPDATE_ACTIVE_TABS: _ClassVar[RequestContext]
    CONTEXT_BATCH_UPDATE_MODELS: _ClassVar[RequestContext]
    CONTEXT_BOOKMARKS: _ClassVar[RequestContext]
    CONTEXT_JOURNEYS: _ClassVar[RequestContext]
    CONTEXT_NEW_TAB_PAGE: _ClassVar[RequestContext]
    CONTEXT_PAGE_INSIGHTS_HUB: _ClassVar[RequestContext]
    CONTEXT_NON_PERSONALIZED_PAGE_INSIGHTS_HUB: _ClassVar[RequestContext]
    CONTEXT_SHOPPING: _ClassVar[RequestContext]
    CONTEXT_SHOP_CARD: _ClassVar[RequestContext]
    CONTEXT_GLIC_ZERO_STATE_SUGGESTIONS: _ClassVar[RequestContext]

class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLATFORM_UNDEFINED: _ClassVar[Platform]
    PLATFORM_ANDROID: _ClassVar[Platform]
    PLATFORM_CHROMEOS: _ClassVar[Platform]
    PLATFORM_IOS: _ClassVar[Platform]
    PLATFORM_LINUX: _ClassVar[Platform]
    PLATFORM_MAC: _ClassVar[Platform]
    PLATFORM_WINDOWS: _ClassVar[Platform]
CONTEXT_UNSPECIFIED: RequestContext
CONTEXT_PAGE_NAVIGATION: RequestContext
CONTEXT_BATCH_UPDATE_GOOGLE_SRP: RequestContext
CONTEXT_BATCH_UPDATE_ACTIVE_TABS: RequestContext
CONTEXT_BATCH_UPDATE_MODELS: RequestContext
CONTEXT_BOOKMARKS: RequestContext
CONTEXT_JOURNEYS: RequestContext
CONTEXT_NEW_TAB_PAGE: RequestContext
CONTEXT_PAGE_INSIGHTS_HUB: RequestContext
CONTEXT_NON_PERSONALIZED_PAGE_INSIGHTS_HUB: RequestContext
CONTEXT_SHOPPING: RequestContext
CONTEXT_SHOP_CARD: RequestContext
CONTEXT_GLIC_ZERO_STATE_SUGGESTIONS: RequestContext
PLATFORM_UNDEFINED: Platform
PLATFORM_ANDROID: Platform
PLATFORM_CHROMEOS: Platform
PLATFORM_IOS: Platform
PLATFORM_LINUX: Platform
PLATFORM_MAC: Platform
PLATFORM_WINDOWS: Platform

class FieldTrial(_message.Message):
    __slots__ = ("name_hash", "group_hash")
    NAME_HASH_FIELD_NUMBER: _ClassVar[int]
    GROUP_HASH_FIELD_NUMBER: _ClassVar[int]
    name_hash: int
    group_hash: int
    def __init__(self, name_hash: _Optional[int] = ..., group_hash: _Optional[int] = ...) -> None: ...

class Duration(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class Timestamp(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class Any(_message.Message):
    __slots__ = ("type_url", "value")
    TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type_url: str
    value: bytes
    def __init__(self, type_url: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class OriginInfo(_message.Message):
    __slots__ = ("platform", "version")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    platform: Platform
    version: str
    def __init__(self, platform: _Optional[_Union[Platform, str]] = ..., version: _Optional[str] = ...) -> None: ...
