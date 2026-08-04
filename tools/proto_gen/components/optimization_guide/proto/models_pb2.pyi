from components.optimization_guide.proto import common_types_pb2 as _common_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OptimizationTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPTIMIZATION_TARGET_UNKNOWN: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PAINFUL_PAGE_LOAD: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_LANGUAGE_DETECTION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PAGE_TOPICS: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_NEW_TAB: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_SHARE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_VOICE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_VALIDATION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PAGE_ENTITIES: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_NOTIFICATION_PERMISSION_PREDICTIONS: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_DUMMY: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_CHROME_START_ANDROID: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_QUERY_TILES: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PAGE_VISIBILITY: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PAGE_TOPICS_V2: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_CHROME_LOW_USER_ENGAGEMENT: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_FEED_USER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_CONTEXTUAL_PAGE_ACTION_PRICE_TRACKING: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_TEXT_CLASSIFIER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_GEOLOCATION_PERMISSION_PREDICTIONS: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_SHOPPING_USER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_CHROME_START_ANDROID_V2: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_SEARCH_USER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_OMNIBOX_ON_DEVICE_TAIL_SUGGEST: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_CLIENT_SIDE_PHISHING: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_OMNIBOX_URL_SCORING: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_DEVICE_SWITCHER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_ADAPTIVE_TOOLBAR: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_TABLET_PRODUCTIVITY_USER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_CLIENT_SIDE_PHISHING_IMAGE_EMBEDDER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_NEW_TAB_PAGE_HISTORY_CLUSTERS_MODULE_RANKING: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_WEB_APP_INSTALLATION_PROMO: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_TEXT_EMBEDDER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_VISUAL_SEARCH_CLASSIFICATION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_BOTTOM_TOOLBAR: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_AUTOFILL_FIELD_CLASSIFICATION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_IOS_MODULE_RANKER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_DESKTOP_NTP_MODULE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PRELOADING_HEURISTICS: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_TEXT_SAFETY: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_ANDROID_HOME_MODULE_RANKER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_COMPOSE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PASSAGE_EMBEDDER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PHRASE_SEGMENTATION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_COMPOSE_PROMOTION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_URL_VISIT_RESUMPTION_RANKER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_CAMERA_BACKGROUND_SEGMENTATION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_HISTORY_SEARCH: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_PROMPT_API: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_METRICS_CLUSTERING: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_SUMMARIZE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PASSWORD_MANAGER_FORM_CLASSIFICATION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_NOTIFICATION_CONTENT_DETECTION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_HISTORY_QUERY_INTENT: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_SCAM_DETECTION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_PERMISSIONS_AI: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_EXPERIMENTAL_EMBEDDER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_FEDCM_USER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_WRITING_ASSISTANCE_API: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_GEOLOCATION_IMAGE_PERMISSION_RELEVANCE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_NOTIFICATION_IMAGE_PERMISSION_RELEVANCE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_PROOFREADER_API: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SEGMENTATION_IOS_DEFAULT_BROWSER_PROMO: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_EDU_CLASSIFIER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PERMISSIONS_AIV4_GEOLOCATION_DESKTOP: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PERMISSIONS_AIV4_NOTIFICATIONS_DESKTOP: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_GENERALIZED_SAFETY: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PERMISSIONS_AIV4_GEOLOCATION_ANDROID: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_PERMISSIONS_AIV4_NOTIFICATIONS_ANDROID: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_ON_DEVICE_SPEECH_RECOGNITION: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_WEBRTC_NEURAL_RESIDUAL_ECHO_ESTIMATOR: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_CLASSIFIER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_CONTEXTUAL_TASKS_TAB_RELEVANCE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_SHOPPING_CLASSIFIER: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_ON_DEVICE_SPEECH_RECOGNITION_TINY_GEMMA: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_CONTEXTUAL_TASKS_MULTI_TURN_TAB_RELEVANCE: _ClassVar[OptimizationTarget]
    OPTIMIZATION_TARGET_WEBRTC_VOICE_ISOLATION_DENOISER: _ClassVar[OptimizationTarget]

class ModelEngineVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_ENGINE_VERSION_UNKNOWN: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_3_0: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_3_0_1: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_4: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_7: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_8: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_9: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_9_0_1: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_10: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_11: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_12: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_13: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_14: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_14_1: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_16: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_16_1: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_17: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_18: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_20_0: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_20_1: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_20_2: _ClassVar[ModelEngineVersion]
    MODEL_ENGINE_VERSION_TFLITE_2_22_0: _ClassVar[ModelEngineVersion]
OPTIMIZATION_TARGET_UNKNOWN: OptimizationTarget
OPTIMIZATION_TARGET_PAINFUL_PAGE_LOAD: OptimizationTarget
OPTIMIZATION_TARGET_LANGUAGE_DETECTION: OptimizationTarget
OPTIMIZATION_TARGET_PAGE_TOPICS: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_NEW_TAB: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_SHARE: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_VOICE: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_VALIDATION: OptimizationTarget
OPTIMIZATION_TARGET_PAGE_ENTITIES: OptimizationTarget
OPTIMIZATION_TARGET_NOTIFICATION_PERMISSION_PREDICTIONS: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_DUMMY: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_CHROME_START_ANDROID: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_QUERY_TILES: OptimizationTarget
OPTIMIZATION_TARGET_PAGE_VISIBILITY: OptimizationTarget
OPTIMIZATION_TARGET_PAGE_TOPICS_V2: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_CHROME_LOW_USER_ENGAGEMENT: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_FEED_USER: OptimizationTarget
OPTIMIZATION_TARGET_CONTEXTUAL_PAGE_ACTION_PRICE_TRACKING: OptimizationTarget
OPTIMIZATION_TARGET_TEXT_CLASSIFIER: OptimizationTarget
OPTIMIZATION_TARGET_GEOLOCATION_PERMISSION_PREDICTIONS: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_SHOPPING_USER: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_CHROME_START_ANDROID_V2: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_SEARCH_USER: OptimizationTarget
OPTIMIZATION_TARGET_OMNIBOX_ON_DEVICE_TAIL_SUGGEST: OptimizationTarget
OPTIMIZATION_TARGET_CLIENT_SIDE_PHISHING: OptimizationTarget
OPTIMIZATION_TARGET_OMNIBOX_URL_SCORING: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_DEVICE_SWITCHER: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_ADAPTIVE_TOOLBAR: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_TABLET_PRODUCTIVITY_USER: OptimizationTarget
OPTIMIZATION_TARGET_CLIENT_SIDE_PHISHING_IMAGE_EMBEDDER: OptimizationTarget
OPTIMIZATION_TARGET_NEW_TAB_PAGE_HISTORY_CLUSTERS_MODULE_RANKING: OptimizationTarget
OPTIMIZATION_TARGET_WEB_APP_INSTALLATION_PROMO: OptimizationTarget
OPTIMIZATION_TARGET_TEXT_EMBEDDER: OptimizationTarget
OPTIMIZATION_TARGET_VISUAL_SEARCH_CLASSIFICATION: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_BOTTOM_TOOLBAR: OptimizationTarget
OPTIMIZATION_TARGET_AUTOFILL_FIELD_CLASSIFICATION: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_IOS_MODULE_RANKER: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_DESKTOP_NTP_MODULE: OptimizationTarget
OPTIMIZATION_TARGET_PRELOADING_HEURISTICS: OptimizationTarget
OPTIMIZATION_TARGET_TEXT_SAFETY: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_ANDROID_HOME_MODULE_RANKER: OptimizationTarget
OPTIMIZATION_TARGET_COMPOSE: OptimizationTarget
OPTIMIZATION_TARGET_PASSAGE_EMBEDDER: OptimizationTarget
OPTIMIZATION_TARGET_PHRASE_SEGMENTATION: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_COMPOSE_PROMOTION: OptimizationTarget
OPTIMIZATION_TARGET_URL_VISIT_RESUMPTION_RANKER: OptimizationTarget
OPTIMIZATION_TARGET_CAMERA_BACKGROUND_SEGMENTATION: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_HISTORY_SEARCH: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_PROMPT_API: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_METRICS_CLUSTERING: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_SUMMARIZE: OptimizationTarget
OPTIMIZATION_TARGET_PASSWORD_MANAGER_FORM_CLASSIFICATION: OptimizationTarget
OPTIMIZATION_TARGET_NOTIFICATION_CONTENT_DETECTION: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_HISTORY_QUERY_INTENT: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_SCAM_DETECTION: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_PERMISSIONS_AI: OptimizationTarget
OPTIMIZATION_TARGET_EXPERIMENTAL_EMBEDDER: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_FEDCM_USER: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_WRITING_ASSISTANCE_API: OptimizationTarget
OPTIMIZATION_TARGET_GEOLOCATION_IMAGE_PERMISSION_RELEVANCE: OptimizationTarget
OPTIMIZATION_TARGET_NOTIFICATION_IMAGE_PERMISSION_RELEVANCE: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_PROOFREADER_API: OptimizationTarget
OPTIMIZATION_TARGET_SEGMENTATION_IOS_DEFAULT_BROWSER_PROMO: OptimizationTarget
OPTIMIZATION_TARGET_EDU_CLASSIFIER: OptimizationTarget
OPTIMIZATION_TARGET_PERMISSIONS_AIV4_GEOLOCATION_DESKTOP: OptimizationTarget
OPTIMIZATION_TARGET_PERMISSIONS_AIV4_NOTIFICATIONS_DESKTOP: OptimizationTarget
OPTIMIZATION_TARGET_GENERALIZED_SAFETY: OptimizationTarget
OPTIMIZATION_TARGET_PERMISSIONS_AIV4_GEOLOCATION_ANDROID: OptimizationTarget
OPTIMIZATION_TARGET_PERMISSIONS_AIV4_NOTIFICATIONS_ANDROID: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_ON_DEVICE_SPEECH_RECOGNITION: OptimizationTarget
OPTIMIZATION_TARGET_WEBRTC_NEURAL_RESIDUAL_ECHO_ESTIMATOR: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_CLASSIFIER: OptimizationTarget
OPTIMIZATION_TARGET_CONTEXTUAL_TASKS_TAB_RELEVANCE: OptimizationTarget
OPTIMIZATION_TARGET_SHOPPING_CLASSIFIER: OptimizationTarget
OPTIMIZATION_TARGET_MODEL_EXECUTION_FEATURE_ON_DEVICE_SPEECH_RECOGNITION_TINY_GEMMA: OptimizationTarget
OPTIMIZATION_TARGET_CONTEXTUAL_TASKS_MULTI_TURN_TAB_RELEVANCE: OptimizationTarget
OPTIMIZATION_TARGET_WEBRTC_VOICE_ISOLATION_DENOISER: OptimizationTarget
MODEL_ENGINE_VERSION_UNKNOWN: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_3_0: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_3_0_1: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_4: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_7: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_8: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_9: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_9_0_1: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_10: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_11: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_12: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_13: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_14: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_14_1: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_16: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_16_1: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_17: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_18: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_20_0: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_20_1: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_20_2: ModelEngineVersion
MODEL_ENGINE_VERSION_TFLITE_2_22_0: ModelEngineVersion

class Model(_message.Message):
    __slots__ = ("download_url",)
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    download_url: str
    def __init__(self, download_url: _Optional[str] = ...) -> None: ...

class GetModelsRequest(_message.Message):
    __slots__ = ("requested_models", "request_context", "locale", "origin_info")
    REQUESTED_MODELS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    requested_models: _containers.RepeatedCompositeFieldContainer[ModelInfo]
    request_context: _common_types_pb2.RequestContext
    locale: str
    origin_info: _common_types_pb2.OriginInfo
    def __init__(self, requested_models: _Optional[_Iterable[_Union[ModelInfo, _Mapping]]] = ..., request_context: _Optional[_Union[_common_types_pb2.RequestContext, str]] = ..., locale: _Optional[str] = ..., origin_info: _Optional[_Union[_common_types_pb2.OriginInfo, _Mapping]] = ...) -> None: ...

class GetModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[PredictionModel]
    def __init__(self, models: _Optional[_Iterable[_Union[PredictionModel, _Mapping]]] = ...) -> None: ...

class PredictionModel(_message.Message):
    __slots__ = ("model_info", "model")
    MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model_info: ModelInfo
    model: Model
    def __init__(self, model_info: _Optional[_Union[ModelInfo, _Mapping]] = ..., model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class AdditionalModelFile(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class ModelInfo(_message.Message):
    __slots__ = ("optimization_target", "version", "supported_model_engine_versions", "supported_host_model_features", "additional_files", "valid_duration", "keep_beyond_valid_duration", "model_metadata", "model_cache_key")
    OPTIMIZATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_MODEL_ENGINE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_HOST_MODEL_FEATURES_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FILES_FIELD_NUMBER: _ClassVar[int]
    VALID_DURATION_FIELD_NUMBER: _ClassVar[int]
    KEEP_BEYOND_VALID_DURATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    MODEL_CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    optimization_target: OptimizationTarget
    version: int
    supported_model_engine_versions: _containers.RepeatedScalarFieldContainer[ModelEngineVersion]
    supported_host_model_features: _containers.RepeatedScalarFieldContainer[str]
    additional_files: _containers.RepeatedCompositeFieldContainer[AdditionalModelFile]
    valid_duration: _common_types_pb2.Duration
    keep_beyond_valid_duration: bool
    model_metadata: _common_types_pb2.Any
    model_cache_key: ModelCacheKey
    def __init__(self, optimization_target: _Optional[_Union[OptimizationTarget, str]] = ..., version: _Optional[int] = ..., supported_model_engine_versions: _Optional[_Iterable[_Union[ModelEngineVersion, str]]] = ..., supported_host_model_features: _Optional[_Iterable[str]] = ..., additional_files: _Optional[_Iterable[_Union[AdditionalModelFile, _Mapping]]] = ..., valid_duration: _Optional[_Union[_common_types_pb2.Duration, _Mapping]] = ..., keep_beyond_valid_duration: _Optional[bool] = ..., model_metadata: _Optional[_Union[_common_types_pb2.Any, _Mapping]] = ..., model_cache_key: _Optional[_Union[ModelCacheKey, _Mapping]] = ...) -> None: ...

class ModelCacheKey(_message.Message):
    __slots__ = ("locale",)
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    def __init__(self, locale: _Optional[str] = ...) -> None: ...
