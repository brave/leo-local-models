from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PassageEmbeddingsModelMetadata(_message.Message):
    __slots__ = ("input_window_size", "output_size", "score_threshold")
    INPUT_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SIZE_FIELD_NUMBER: _ClassVar[int]
    SCORE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    input_window_size: int
    output_size: int
    score_threshold: float
    def __init__(self, input_window_size: _Optional[int] = ..., output_size: _Optional[int] = ..., score_threshold: _Optional[float] = ...) -> None: ...
