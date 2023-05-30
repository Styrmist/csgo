from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GCProtoBufMsgSrc_FromGC: GCProtoBufMsgSrc
GCProtoBufMsgSrc_FromSteamID: GCProtoBufMsgSrc
GCProtoBufMsgSrc_FromSystem: GCProtoBufMsgSrc
GCProtoBufMsgSrc_ReplySystem: GCProtoBufMsgSrc
GCProtoBufMsgSrc_Unspecified: GCProtoBufMsgSrc
KEY_FIELD_FIELD_NUMBER: _ClassVar[int]
MSGPOOL_HARD_LIMIT_FIELD_NUMBER: _ClassVar[int]
MSGPOOL_SOFT_LIMIT_FIELD_NUMBER: _ClassVar[int]
key_field: _descriptor.FieldDescriptor
msgpool_hard_limit: _descriptor.FieldDescriptor
msgpool_soft_limit: _descriptor.FieldDescriptor

class CChinaAgreementSessions_StartAgreementSessionInGame_Request(_message.Message):
    __slots__ = ["appid", "client_ipaddress", "steamid"]
    APPID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    client_ipaddress: str
    steamid: int
    def __init__(self, appid: _Optional[int] = ..., steamid: _Optional[int] = ..., client_ipaddress: _Optional[str] = ...) -> None: ...

class CChinaAgreementSessions_StartAgreementSessionInGame_Response(_message.Message):
    __slots__ = ["agreement_url"]
    AGREEMENT_URL_FIELD_NUMBER: _ClassVar[int]
    agreement_url: str
    def __init__(self, agreement_url: _Optional[str] = ...) -> None: ...

class CGCMsgGetIPLocation(_message.Message):
    __slots__ = ["ips"]
    IPS_FIELD_NUMBER: _ClassVar[int]
    ips: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ips: _Optional[_Iterable[int]] = ...) -> None: ...

class CGCMsgGetIPLocationResponse(_message.Message):
    __slots__ = ["infos"]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[CIPLocationInfo]
    def __init__(self, infos: _Optional[_Iterable[_Union[CIPLocationInfo, _Mapping]]] = ...) -> None: ...

class CGCMsgGetSystemStats(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CGCMsgGetSystemStatsResponse(_message.Message):
    __slots__ = ["active_jobs", "game_server_sessions", "gc_app_id", "logon_jobs", "logon_queue", "socaches", "socaches_loading", "socaches_to_unload", "stats_kv", "steamid_locks", "user_sessions", "writeback_queue", "yielding_jobs"]
    ACTIVE_JOBS_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    GC_APP_ID_FIELD_NUMBER: _ClassVar[int]
    LOGON_JOBS_FIELD_NUMBER: _ClassVar[int]
    LOGON_QUEUE_FIELD_NUMBER: _ClassVar[int]
    SOCACHES_FIELD_NUMBER: _ClassVar[int]
    SOCACHES_LOADING_FIELD_NUMBER: _ClassVar[int]
    SOCACHES_TO_UNLOAD_FIELD_NUMBER: _ClassVar[int]
    STATS_KV_FIELD_NUMBER: _ClassVar[int]
    STEAMID_LOCKS_FIELD_NUMBER: _ClassVar[int]
    USER_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    WRITEBACK_QUEUE_FIELD_NUMBER: _ClassVar[int]
    YIELDING_JOBS_FIELD_NUMBER: _ClassVar[int]
    active_jobs: int
    game_server_sessions: int
    gc_app_id: int
    logon_jobs: int
    logon_queue: int
    socaches: int
    socaches_loading: int
    socaches_to_unload: int
    stats_kv: bytes
    steamid_locks: int
    user_sessions: int
    writeback_queue: int
    yielding_jobs: int
    def __init__(self, gc_app_id: _Optional[int] = ..., stats_kv: _Optional[bytes] = ..., active_jobs: _Optional[int] = ..., yielding_jobs: _Optional[int] = ..., user_sessions: _Optional[int] = ..., game_server_sessions: _Optional[int] = ..., socaches: _Optional[int] = ..., socaches_to_unload: _Optional[int] = ..., socaches_loading: _Optional[int] = ..., writeback_queue: _Optional[int] = ..., steamid_locks: _Optional[int] = ..., logon_queue: _Optional[int] = ..., logon_jobs: _Optional[int] = ...) -> None: ...

class CGCMsgMemCachedDelete(_message.Message):
    __slots__ = ["keys"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ...) -> None: ...

class CGCMsgMemCachedGet(_message.Message):
    __slots__ = ["keys"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ...) -> None: ...

class CGCMsgMemCachedGetResponse(_message.Message):
    __slots__ = ["values"]
    class ValueTag(_message.Message):
        __slots__ = ["found", "value"]
        FOUND_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        found: bool
        value: bytes
        def __init__(self, found: bool = ..., value: _Optional[bytes] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[CGCMsgMemCachedGetResponse.ValueTag]
    def __init__(self, values: _Optional[_Iterable[_Union[CGCMsgMemCachedGetResponse.ValueTag, _Mapping]]] = ...) -> None: ...

class CGCMsgMemCachedSet(_message.Message):
    __slots__ = ["keys"]
    class KeyPair(_message.Message):
        __slots__ = ["name", "value"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: bytes
        def __init__(self, name: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[CGCMsgMemCachedSet.KeyPair]
    def __init__(self, keys: _Optional[_Iterable[_Union[CGCMsgMemCachedSet.KeyPair, _Mapping]]] = ...) -> None: ...

class CGCMsgMemCachedStats(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CGCMsgMemCachedStatsResponse(_message.Message):
    __slots__ = ["bytes", "bytes_read", "bytes_written", "cmd_flush", "cmd_get", "cmd_set", "curr_connections", "curr_items", "delete_hits", "delete_misses", "evictions", "get_hits", "get_misses", "limit_maxbytes"]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    CMD_FLUSH_FIELD_NUMBER: _ClassVar[int]
    CMD_GET_FIELD_NUMBER: _ClassVar[int]
    CMD_SET_FIELD_NUMBER: _ClassVar[int]
    CURR_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    CURR_ITEMS_FIELD_NUMBER: _ClassVar[int]
    DELETE_HITS_FIELD_NUMBER: _ClassVar[int]
    DELETE_MISSES_FIELD_NUMBER: _ClassVar[int]
    EVICTIONS_FIELD_NUMBER: _ClassVar[int]
    GET_HITS_FIELD_NUMBER: _ClassVar[int]
    GET_MISSES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_MAXBYTES_FIELD_NUMBER: _ClassVar[int]
    bytes: int
    bytes_read: int
    bytes_written: int
    cmd_flush: int
    cmd_get: int
    cmd_set: int
    curr_connections: int
    curr_items: int
    delete_hits: int
    delete_misses: int
    evictions: int
    get_hits: int
    get_misses: int
    limit_maxbytes: int
    def __init__(self, curr_connections: _Optional[int] = ..., cmd_get: _Optional[int] = ..., cmd_set: _Optional[int] = ..., cmd_flush: _Optional[int] = ..., get_hits: _Optional[int] = ..., get_misses: _Optional[int] = ..., delete_hits: _Optional[int] = ..., delete_misses: _Optional[int] = ..., bytes_read: _Optional[int] = ..., bytes_written: _Optional[int] = ..., limit_maxbytes: _Optional[int] = ..., curr_items: _Optional[int] = ..., evictions: _Optional[int] = ..., bytes: _Optional[int] = ...) -> None: ...

class CGCMsgSQLStats(_message.Message):
    __slots__ = ["schema_catalog"]
    SCHEMA_CATALOG_FIELD_NUMBER: _ClassVar[int]
    schema_catalog: int
    def __init__(self, schema_catalog: _Optional[int] = ...) -> None: ...

class CGCMsgSQLStatsResponse(_message.Message):
    __slots__ = ["deadlock_retries", "errors", "non_prepared_statements_executed", "operations_submitted", "operations_timed_out_in_queue", "prepared_statements_executed", "threads", "threads_active", "threads_connected"]
    DEADLOCK_RETRIES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    NON_PREPARED_STATEMENTS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_SUBMITTED_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_TIMED_OUT_IN_QUEUE_FIELD_NUMBER: _ClassVar[int]
    PREPARED_STATEMENTS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    THREADS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    THREADS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    deadlock_retries: int
    errors: int
    non_prepared_statements_executed: int
    operations_submitted: int
    operations_timed_out_in_queue: int
    prepared_statements_executed: int
    threads: int
    threads_active: int
    threads_connected: int
    def __init__(self, threads: _Optional[int] = ..., threads_connected: _Optional[int] = ..., threads_active: _Optional[int] = ..., operations_submitted: _Optional[int] = ..., prepared_statements_executed: _Optional[int] = ..., non_prepared_statements_executed: _Optional[int] = ..., deadlock_retries: _Optional[int] = ..., operations_timed_out_in_queue: _Optional[int] = ..., errors: _Optional[int] = ...) -> None: ...

class CGCMsgSystemStatsSchema(_message.Message):
    __slots__ = ["gc_app_id", "schema_kv"]
    GC_APP_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KV_FIELD_NUMBER: _ClassVar[int]
    gc_app_id: int
    schema_kv: bytes
    def __init__(self, gc_app_id: _Optional[int] = ..., schema_kv: _Optional[bytes] = ...) -> None: ...

class CGCSystemMsg_GetAccountDetails(_message.Message):
    __slots__ = ["appid", "steamid"]
    APPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    steamid: int
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CGCSystemMsg_GetAccountDetails_Response(_message.Message):
    __slots__ = ["account_creation_time", "account_name", "accountid", "currency", "eresult_deprecated", "free_trial_expiration", "friend_count", "has_accepted_china_ssa", "is_account_locked_down", "is_banned_steam_china", "is_community_banned", "is_cyber_cafe", "is_free_trial_account", "is_inventory_public", "is_limited", "is_low_violence", "is_phone_identifying", "is_phone_verified", "is_profile_public", "is_school_account", "is_steamguard_enabled", "is_subscribed", "is_trade_banned", "is_two_factor_auth_enabled", "is_vac_banned", "package", "persona_name", "phone_id", "phone_verification_time", "rt_birth_date", "rt_identity_linked", "steam_level", "suspension_end_time", "trade_ban_expiration", "two_factor_enabled_time", "txn_country_code"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ERESULT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    FREE_TRIAL_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    FRIEND_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_ACCEPTED_CHINA_SSA_FIELD_NUMBER: _ClassVar[int]
    IS_ACCOUNT_LOCKED_DOWN_FIELD_NUMBER: _ClassVar[int]
    IS_BANNED_STEAM_CHINA_FIELD_NUMBER: _ClassVar[int]
    IS_COMMUNITY_BANNED_FIELD_NUMBER: _ClassVar[int]
    IS_CYBER_CAFE_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_TRIAL_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_INVENTORY_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IS_LIMITED_FIELD_NUMBER: _ClassVar[int]
    IS_LOW_VIOLENCE_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_IDENTIFYING_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_PROFILE_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IS_SCHOOL_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_STEAMGUARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    IS_TRADE_BANNED_FIELD_NUMBER: _ClassVar[int]
    IS_TWO_FACTOR_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_VAC_BANNED_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    RT_BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    RT_IDENTITY_LINKED_FIELD_NUMBER: _ClassVar[int]
    STEAM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    TRADE_BAN_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_ENABLED_TIME_FIELD_NUMBER: _ClassVar[int]
    TXN_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    account_creation_time: int
    account_name: str
    accountid: int
    currency: str
    eresult_deprecated: int
    free_trial_expiration: int
    friend_count: int
    has_accepted_china_ssa: bool
    is_account_locked_down: bool
    is_banned_steam_china: bool
    is_community_banned: bool
    is_cyber_cafe: bool
    is_free_trial_account: bool
    is_inventory_public: bool
    is_limited: bool
    is_low_violence: bool
    is_phone_identifying: bool
    is_phone_verified: bool
    is_profile_public: bool
    is_school_account: bool
    is_steamguard_enabled: bool
    is_subscribed: bool
    is_trade_banned: bool
    is_two_factor_auth_enabled: bool
    is_vac_banned: bool
    package: int
    persona_name: str
    phone_id: int
    phone_verification_time: int
    rt_birth_date: int
    rt_identity_linked: int
    steam_level: int
    suspension_end_time: int
    trade_ban_expiration: int
    two_factor_enabled_time: int
    txn_country_code: str
    def __init__(self, eresult_deprecated: _Optional[int] = ..., account_name: _Optional[str] = ..., persona_name: _Optional[str] = ..., is_profile_public: bool = ..., is_inventory_public: bool = ..., is_vac_banned: bool = ..., is_cyber_cafe: bool = ..., is_school_account: bool = ..., is_limited: bool = ..., is_subscribed: bool = ..., package: _Optional[int] = ..., is_free_trial_account: bool = ..., free_trial_expiration: _Optional[int] = ..., is_low_violence: bool = ..., is_account_locked_down: bool = ..., is_community_banned: bool = ..., is_trade_banned: bool = ..., trade_ban_expiration: _Optional[int] = ..., accountid: _Optional[int] = ..., suspension_end_time: _Optional[int] = ..., currency: _Optional[str] = ..., steam_level: _Optional[int] = ..., friend_count: _Optional[int] = ..., account_creation_time: _Optional[int] = ..., is_steamguard_enabled: bool = ..., is_phone_verified: bool = ..., is_two_factor_auth_enabled: bool = ..., two_factor_enabled_time: _Optional[int] = ..., phone_verification_time: _Optional[int] = ..., phone_id: _Optional[int] = ..., is_phone_identifying: bool = ..., rt_identity_linked: _Optional[int] = ..., rt_birth_date: _Optional[int] = ..., txn_country_code: _Optional[str] = ..., has_accepted_china_ssa: bool = ..., is_banned_steam_china: bool = ...) -> None: ...

class CGCSystemMsg_GetPurchaseTrust_Request(_message.Message):
    __slots__ = ["steamid"]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CGCSystemMsg_GetPurchaseTrust_Response(_message.Message):
    __slots__ = ["has_no_recent_password_resets", "has_prior_purchase_history", "is_wallet_cash_trusted", "time_all_trusted"]
    HAS_NO_RECENT_PASSWORD_RESETS_FIELD_NUMBER: _ClassVar[int]
    HAS_PRIOR_PURCHASE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    IS_WALLET_CASH_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    TIME_ALL_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    has_no_recent_password_resets: bool
    has_prior_purchase_history: bool
    is_wallet_cash_trusted: bool
    time_all_trusted: int
    def __init__(self, has_prior_purchase_history: bool = ..., has_no_recent_password_resets: bool = ..., is_wallet_cash_trusted: bool = ..., time_all_trusted: _Optional[int] = ...) -> None: ...

class CIPLocationInfo(_message.Message):
    __slots__ = ["city", "country", "ip", "latitude", "longitude", "state"]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    city: str
    country: str
    ip: int
    latitude: float
    longitude: float
    state: str
    def __init__(self, ip: _Optional[int] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., country: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...

class CMsgAMAddFreeLicense(_message.Message):
    __slots__ = ["ip_public", "packageid", "steamid", "store_country_code"]
    IP_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    STORE_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ip_public: int
    packageid: int
    steamid: int
    store_country_code: str
    def __init__(self, steamid: _Optional[int] = ..., ip_public: _Optional[int] = ..., packageid: _Optional[int] = ..., store_country_code: _Optional[str] = ...) -> None: ...

class CMsgAMAddFreeLicenseResponse(_message.Message):
    __slots__ = ["eresult", "purchase_result_detail", "transid"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_RESULT_DETAIL_FIELD_NUMBER: _ClassVar[int]
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    purchase_result_detail: int
    transid: int
    def __init__(self, eresult: _Optional[int] = ..., purchase_result_detail: _Optional[int] = ..., transid: _Optional[int] = ...) -> None: ...

class CMsgAMFindAccounts(_message.Message):
    __slots__ = ["search_string", "search_type"]
    SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    search_string: str
    search_type: int
    def __init__(self, search_type: _Optional[int] = ..., search_string: _Optional[str] = ...) -> None: ...

class CMsgAMFindAccountsResponse(_message.Message):
    __slots__ = ["steam_id"]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steam_id: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgAMGetLicenses(_message.Message):
    __slots__ = ["steamid"]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CMsgAMGetLicensesResponse(_message.Message):
    __slots__ = ["license", "result"]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    license: _containers.RepeatedCompositeFieldContainer[CMsgPackageLicense]
    result: int
    def __init__(self, license: _Optional[_Iterable[_Union[CMsgPackageLicense, _Mapping]]] = ..., result: _Optional[int] = ...) -> None: ...

class CMsgAMGetUserGameStats(_message.Message):
    __slots__ = ["game_id", "stats", "steam_id"]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    stats: _containers.RepeatedScalarFieldContainer[int]
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ..., game_id: _Optional[int] = ..., stats: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgAMGetUserGameStatsResponse(_message.Message):
    __slots__ = ["achievement_blocks", "eresult", "game_id", "stats", "steam_id"]
    class Achievement_Blocks(_message.Message):
        __slots__ = ["achievement_bit_id", "achievement_id", "unlock_time"]
        ACHIEVEMENT_BIT_ID_FIELD_NUMBER: _ClassVar[int]
        ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        UNLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
        achievement_bit_id: int
        achievement_id: int
        unlock_time: int
        def __init__(self, achievement_id: _Optional[int] = ..., achievement_bit_id: _Optional[int] = ..., unlock_time: _Optional[int] = ...) -> None: ...
    class Stats(_message.Message):
        __slots__ = ["stat_id", "stat_value"]
        STAT_ID_FIELD_NUMBER: _ClassVar[int]
        STAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        stat_id: int
        stat_value: int
        def __init__(self, stat_id: _Optional[int] = ..., stat_value: _Optional[int] = ...) -> None: ...
    ACHIEVEMENT_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_blocks: _containers.RepeatedCompositeFieldContainer[CMsgAMGetUserGameStatsResponse.Achievement_Blocks]
    eresult: int
    game_id: int
    stats: _containers.RepeatedCompositeFieldContainer[CMsgAMGetUserGameStatsResponse.Stats]
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ..., game_id: _Optional[int] = ..., eresult: _Optional[int] = ..., stats: _Optional[_Iterable[_Union[CMsgAMGetUserGameStatsResponse.Stats, _Mapping]]] = ..., achievement_blocks: _Optional[_Iterable[_Union[CMsgAMGetUserGameStatsResponse.Achievement_Blocks, _Mapping]]] = ...) -> None: ...

class CMsgAMGrantGuestPasses2(_message.Message):
    __slots__ = ["action", "days_to_expiration", "package_id", "passes_to_grant", "steam_id"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DAYS_TO_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PASSES_TO_GRANT_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    action: int
    days_to_expiration: int
    package_id: int
    passes_to_grant: int
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ..., package_id: _Optional[int] = ..., passes_to_grant: _Optional[int] = ..., days_to_expiration: _Optional[int] = ..., action: _Optional[int] = ...) -> None: ...

class CMsgAMGrantGuestPasses2Response(_message.Message):
    __slots__ = ["eresult", "passes_granted"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PASSES_GRANTED_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    passes_granted: int
    def __init__(self, eresult: _Optional[int] = ..., passes_granted: _Optional[int] = ...) -> None: ...

class CMsgAMSendEmail(_message.Message):
    __slots__ = ["email_format", "email_msg_type", "persona_name_tokens", "source_gc", "steamid", "tokens"]
    class PersonaNameReplacementToken(_message.Message):
        __slots__ = ["steamid", "token_name"]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        TOKEN_NAME_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        token_name: str
        def __init__(self, steamid: _Optional[int] = ..., token_name: _Optional[str] = ...) -> None: ...
    class ReplacementToken(_message.Message):
        __slots__ = ["token_name", "token_value"]
        TOKEN_NAME_FIELD_NUMBER: _ClassVar[int]
        TOKEN_VALUE_FIELD_NUMBER: _ClassVar[int]
        token_name: str
        token_value: str
        def __init__(self, token_name: _Optional[str] = ..., token_value: _Optional[str] = ...) -> None: ...
    EMAIL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GC_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    email_format: int
    email_msg_type: int
    persona_name_tokens: _containers.RepeatedCompositeFieldContainer[CMsgAMSendEmail.PersonaNameReplacementToken]
    source_gc: int
    steamid: int
    tokens: _containers.RepeatedCompositeFieldContainer[CMsgAMSendEmail.ReplacementToken]
    def __init__(self, steamid: _Optional[int] = ..., email_msg_type: _Optional[int] = ..., email_format: _Optional[int] = ..., persona_name_tokens: _Optional[_Iterable[_Union[CMsgAMSendEmail.PersonaNameReplacementToken, _Mapping]]] = ..., source_gc: _Optional[int] = ..., tokens: _Optional[_Iterable[_Union[CMsgAMSendEmail.ReplacementToken, _Mapping]]] = ...) -> None: ...

class CMsgAMSendEmailResponse(_message.Message):
    __slots__ = ["eresult"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgDPPartnerMicroTxns(_message.Message):
    __slots__ = ["appid", "gc_name", "partner", "transactions"]
    class PartnerInfo(_message.Message):
        __slots__ = ["currency_code", "currency_name", "partner_id", "partner_name"]
        CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_NAME_FIELD_NUMBER: _ClassVar[int]
        PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
        PARTNER_NAME_FIELD_NUMBER: _ClassVar[int]
        currency_code: str
        currency_name: str
        partner_id: int
        partner_name: str
        def __init__(self, partner_id: _Optional[int] = ..., partner_name: _Optional[str] = ..., currency_code: _Optional[str] = ..., currency_name: _Optional[str] = ...) -> None: ...
    class PartnerMicroTxn(_message.Message):
        __slots__ = ["account_id", "country_code", "def_index", "init_time", "item_id", "last_update_time", "line_item", "price", "price_usd", "purchase_type", "quantity", "ref_trans_id", "region_code", "steam_txn_type", "tax", "tax_usd", "txn_id"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
        INIT_TIME_FIELD_NUMBER: _ClassVar[int]
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        LINE_ITEM_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        PRICE_USD_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_TYPE_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        REF_TRANS_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        STEAM_TXN_TYPE_FIELD_NUMBER: _ClassVar[int]
        TAX_FIELD_NUMBER: _ClassVar[int]
        TAX_USD_FIELD_NUMBER: _ClassVar[int]
        TXN_ID_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        country_code: str
        def_index: int
        init_time: int
        item_id: int
        last_update_time: int
        line_item: int
        price: int
        price_usd: int
        purchase_type: int
        quantity: int
        ref_trans_id: int
        region_code: str
        steam_txn_type: int
        tax: int
        tax_usd: int
        txn_id: int
        def __init__(self, init_time: _Optional[int] = ..., last_update_time: _Optional[int] = ..., txn_id: _Optional[int] = ..., account_id: _Optional[int] = ..., line_item: _Optional[int] = ..., item_id: _Optional[int] = ..., def_index: _Optional[int] = ..., price: _Optional[int] = ..., tax: _Optional[int] = ..., price_usd: _Optional[int] = ..., tax_usd: _Optional[int] = ..., purchase_type: _Optional[int] = ..., steam_txn_type: _Optional[int] = ..., country_code: _Optional[str] = ..., region_code: _Optional[str] = ..., quantity: _Optional[int] = ..., ref_trans_id: _Optional[int] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    GC_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    gc_name: str
    partner: CMsgDPPartnerMicroTxns.PartnerInfo
    transactions: _containers.RepeatedCompositeFieldContainer[CMsgDPPartnerMicroTxns.PartnerMicroTxn]
    def __init__(self, appid: _Optional[int] = ..., gc_name: _Optional[str] = ..., partner: _Optional[_Union[CMsgDPPartnerMicroTxns.PartnerInfo, _Mapping]] = ..., transactions: _Optional[_Iterable[_Union[CMsgDPPartnerMicroTxns.PartnerMicroTxn, _Mapping]]] = ...) -> None: ...

class CMsgDPPartnerMicroTxnsResponse(_message.Message):
    __slots__ = ["eerrorcode", "eresult"]
    class EErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eerrorcode: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    eresult: int
    k_MsgAlreadyRunning: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgInvalidAppID: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgInvalidPartnerInfo: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgInvalidTransactionData: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgNoTransactions: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgPartnerInfoDiscrepancy: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgSQLFailure: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgTransactionInsertFailed: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgValid: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    def __init__(self, eresult: _Optional[int] = ..., eerrorcode: _Optional[_Union[CMsgDPPartnerMicroTxnsResponse.EErrorCode, str]] = ...) -> None: ...

class CMsgGCCheckFriendship(_message.Message):
    __slots__ = ["steamid_left", "steamid_right"]
    STEAMID_LEFT_FIELD_NUMBER: _ClassVar[int]
    STEAMID_RIGHT_FIELD_NUMBER: _ClassVar[int]
    steamid_left: int
    steamid_right: int
    def __init__(self, steamid_left: _Optional[int] = ..., steamid_right: _Optional[int] = ...) -> None: ...

class CMsgGCCheckFriendship_Response(_message.Message):
    __slots__ = ["found_friendship", "success"]
    FOUND_FRIENDSHIP_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    found_friendship: bool
    success: bool
    def __init__(self, success: bool = ..., found_friendship: bool = ...) -> None: ...

class CMsgGCGetCommandList(_message.Message):
    __slots__ = ["app_id", "command_prefix"]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_PREFIX_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    command_prefix: str
    def __init__(self, app_id: _Optional[int] = ..., command_prefix: _Optional[str] = ...) -> None: ...

class CMsgGCGetCommandListResponse(_message.Message):
    __slots__ = ["command_name"]
    COMMAND_NAME_FIELD_NUMBER: _ClassVar[int]
    command_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, command_name: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgGCGetEmailTemplate(_message.Message):
    __slots__ = ["app_id", "email_format", "email_lang", "email_msg_type"]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_LANG_FIELD_NUMBER: _ClassVar[int]
    EMAIL_MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    email_format: int
    email_lang: int
    email_msg_type: int
    def __init__(self, app_id: _Optional[int] = ..., email_msg_type: _Optional[int] = ..., email_lang: _Optional[int] = ..., email_format: _Optional[int] = ...) -> None: ...

class CMsgGCGetEmailTemplateResponse(_message.Message):
    __slots__ = ["eresult", "template", "template_exists"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_EXISTS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    template: str
    template_exists: bool
    def __init__(self, eresult: _Optional[int] = ..., template_exists: bool = ..., template: _Optional[str] = ...) -> None: ...

class CMsgGCGetPartnerAccountLink(_message.Message):
    __slots__ = ["steamid"]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CMsgGCGetPartnerAccountLink_Response(_message.Message):
    __slots__ = ["ageclass", "id_verified", "is_adult", "nexonid", "pwid"]
    AGECLASS_FIELD_NUMBER: _ClassVar[int]
    ID_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_ADULT_FIELD_NUMBER: _ClassVar[int]
    NEXONID_FIELD_NUMBER: _ClassVar[int]
    PWID_FIELD_NUMBER: _ClassVar[int]
    ageclass: int
    id_verified: bool
    is_adult: bool
    nexonid: int
    pwid: int
    def __init__(self, pwid: _Optional[int] = ..., nexonid: _Optional[int] = ..., ageclass: _Optional[int] = ..., id_verified: bool = ..., is_adult: bool = ...) -> None: ...

class CMsgGCGetPersonaNames(_message.Message):
    __slots__ = ["steamids"]
    STEAMIDS_FIELD_NUMBER: _ClassVar[int]
    steamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCGetPersonaNames_Response(_message.Message):
    __slots__ = ["failed_lookup_steamids", "succeeded_lookups"]
    class PersonaName(_message.Message):
        __slots__ = ["persona_name", "steamid"]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        persona_name: str
        steamid: int
        def __init__(self, steamid: _Optional[int] = ..., persona_name: _Optional[str] = ...) -> None: ...
    FAILED_LOOKUP_STEAMIDS_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_LOOKUPS_FIELD_NUMBER: _ClassVar[int]
    failed_lookup_steamids: _containers.RepeatedScalarFieldContainer[int]
    succeeded_lookups: _containers.RepeatedCompositeFieldContainer[CMsgGCGetPersonaNames_Response.PersonaName]
    def __init__(self, succeeded_lookups: _Optional[_Iterable[_Union[CMsgGCGetPersonaNames_Response.PersonaName, _Mapping]]] = ..., failed_lookup_steamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCHAccountVacStatusChange(_message.Message):
    __slots__ = ["app_id", "is_banned_future", "is_banned_now", "rtime_vacban_starts", "steam_id"]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BANNED_FUTURE_FIELD_NUMBER: _ClassVar[int]
    IS_BANNED_NOW_FIELD_NUMBER: _ClassVar[int]
    RTIME_VACBAN_STARTS_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    is_banned_future: bool
    is_banned_now: bool
    rtime_vacban_starts: int
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ..., app_id: _Optional[int] = ..., rtime_vacban_starts: _Optional[int] = ..., is_banned_now: bool = ..., is_banned_future: bool = ...) -> None: ...

class CMsgGCHUpdateSession(_message.Message):
    __slots__ = ["app_id", "client_addr", "cm_session_identifier", "cm_session_sysid", "depot_ids", "extra_fields", "online", "os_type", "owner_id", "server_addr", "server_port", "server_steam_id", "steam_id"]
    class ExtraField(_message.Message):
        __slots__ = ["name", "value"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ADDR_FIELD_NUMBER: _ClassVar[int]
    CM_SESSION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CM_SESSION_SYSID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_IDS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    client_addr: int
    cm_session_identifier: int
    cm_session_sysid: int
    depot_ids: _containers.RepeatedScalarFieldContainer[int]
    extra_fields: _containers.RepeatedCompositeFieldContainer[CMsgGCHUpdateSession.ExtraField]
    online: bool
    os_type: int
    owner_id: int
    server_addr: int
    server_port: int
    server_steam_id: int
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ..., app_id: _Optional[int] = ..., online: bool = ..., server_steam_id: _Optional[int] = ..., server_addr: _Optional[int] = ..., server_port: _Optional[int] = ..., os_type: _Optional[int] = ..., client_addr: _Optional[int] = ..., extra_fields: _Optional[_Iterable[_Union[CMsgGCHUpdateSession.ExtraField, _Mapping]]] = ..., owner_id: _Optional[int] = ..., cm_session_sysid: _Optional[int] = ..., cm_session_identifier: _Optional[int] = ..., depot_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCMsgMasterSetClientMsgRouting(_message.Message):
    __slots__ = ["entries"]
    class Entry(_message.Message):
        __slots__ = ["msg_type", "routing"]
        MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
        ROUTING_FIELD_NUMBER: _ClassVar[int]
        msg_type: int
        routing: CMsgGCRoutingInfo
        def __init__(self, msg_type: _Optional[int] = ..., routing: _Optional[_Union[CMsgGCRoutingInfo, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCMsgMasterSetClientMsgRouting.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCMsgMasterSetClientMsgRouting.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCMsgMasterSetClientMsgRouting_Response(_message.Message):
    __slots__ = ["eresult"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgGCMsgMasterSetDirectory(_message.Message):
    __slots__ = ["dir", "master_dir_index"]
    class SubGC(_message.Message):
        __slots__ = ["box", "command_line", "dir_index", "gc_binary", "name"]
        BOX_FIELD_NUMBER: _ClassVar[int]
        COMMAND_LINE_FIELD_NUMBER: _ClassVar[int]
        DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
        GC_BINARY_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        box: str
        command_line: str
        dir_index: int
        gc_binary: str
        name: str
        def __init__(self, dir_index: _Optional[int] = ..., name: _Optional[str] = ..., box: _Optional[str] = ..., command_line: _Optional[str] = ..., gc_binary: _Optional[str] = ...) -> None: ...
    DIR_FIELD_NUMBER: _ClassVar[int]
    MASTER_DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
    dir: _containers.RepeatedCompositeFieldContainer[CMsgGCMsgMasterSetDirectory.SubGC]
    master_dir_index: int
    def __init__(self, master_dir_index: _Optional[int] = ..., dir: _Optional[_Iterable[_Union[CMsgGCMsgMasterSetDirectory.SubGC, _Mapping]]] = ...) -> None: ...

class CMsgGCMsgMasterSetDirectory_Response(_message.Message):
    __slots__ = ["eresult", "message"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    message: str
    def __init__(self, eresult: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class CMsgGCMsgMasterSetWebAPIRouting(_message.Message):
    __slots__ = ["entries"]
    class Entry(_message.Message):
        __slots__ = ["interface_name", "method_name", "routing"]
        INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
        ROUTING_FIELD_NUMBER: _ClassVar[int]
        interface_name: str
        method_name: str
        routing: CMsgGCRoutingInfo
        def __init__(self, interface_name: _Optional[str] = ..., method_name: _Optional[str] = ..., routing: _Optional[_Union[CMsgGCRoutingInfo, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCMsgMasterSetWebAPIRouting.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCMsgMasterSetWebAPIRouting.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCMsgMasterSetWebAPIRouting_Response(_message.Message):
    __slots__ = ["eresult"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgGCMsgSetOptions(_message.Message):
    __slots__ = ["client_msg_ranges", "options"]
    class Option(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class MessageRange(_message.Message):
        __slots__ = ["high", "low"]
        HIGH_FIELD_NUMBER: _ClassVar[int]
        LOW_FIELD_NUMBER: _ClassVar[int]
        high: int
        low: int
        def __init__(self, low: _Optional[int] = ..., high: _Optional[int] = ...) -> None: ...
    CLIENT_MSG_RANGES_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ACHIEVEMENTS: CMsgGCMsgSetOptions.Option
    NOTIFY_SERVER_SESSIONS: CMsgGCMsgSetOptions.Option
    NOTIFY_USER_SESSIONS: CMsgGCMsgSetOptions.Option
    NOTIFY_VAC_ACTION: CMsgGCMsgSetOptions.Option
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    client_msg_ranges: _containers.RepeatedCompositeFieldContainer[CMsgGCMsgSetOptions.MessageRange]
    options: _containers.RepeatedScalarFieldContainer[CMsgGCMsgSetOptions.Option]
    def __init__(self, options: _Optional[_Iterable[_Union[CMsgGCMsgSetOptions.Option, str]]] = ..., client_msg_ranges: _Optional[_Iterable[_Union[CMsgGCMsgSetOptions.MessageRange, _Mapping]]] = ...) -> None: ...

class CMsgGCMsgWebAPIJobRequestForwardResponse(_message.Message):
    __slots__ = ["dir_index"]
    DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
    dir_index: int
    def __init__(self, dir_index: _Optional[int] = ...) -> None: ...

class CMsgGCRoutingInfo(_message.Message):
    __slots__ = ["dir_index", "fallback", "method", "protobuf_field", "webapi_param"]
    class RoutingMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CLIENT_STEAMID: CMsgGCRoutingInfo.RoutingMethod
    DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISCARD: CMsgGCRoutingInfo.RoutingMethod
    FALLBACK_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PROTOBUF_FIELD_FIELD_NUMBER: _ClassVar[int]
    PROTOBUF_FIELD_UINT64: CMsgGCRoutingInfo.RoutingMethod
    RANDOM: CMsgGCRoutingInfo.RoutingMethod
    WEBAPI_PARAM_FIELD_NUMBER: _ClassVar[int]
    WEBAPI_PARAM_UINT64: CMsgGCRoutingInfo.RoutingMethod
    dir_index: _containers.RepeatedScalarFieldContainer[int]
    fallback: CMsgGCRoutingInfo.RoutingMethod
    method: CMsgGCRoutingInfo.RoutingMethod
    protobuf_field: int
    webapi_param: str
    def __init__(self, dir_index: _Optional[_Iterable[int]] = ..., method: _Optional[_Union[CMsgGCRoutingInfo.RoutingMethod, str]] = ..., fallback: _Optional[_Union[CMsgGCRoutingInfo.RoutingMethod, str]] = ..., protobuf_field: _Optional[int] = ..., webapi_param: _Optional[str] = ...) -> None: ...

class CMsgHttpRequest(_message.Message):
    __slots__ = ["absolute_timeout", "body", "get_params", "headers", "hostname", "post_params", "request_method", "url"]
    class QueryParam(_message.Message):
        __slots__ = ["name", "value"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: bytes
        def __init__(self, name: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class RequestHeader(_message.Message):
        __slots__ = ["name", "value"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ABSOLUTE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    GET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    POST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METHOD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    absolute_timeout: int
    body: bytes
    get_params: _containers.RepeatedCompositeFieldContainer[CMsgHttpRequest.QueryParam]
    headers: _containers.RepeatedCompositeFieldContainer[CMsgHttpRequest.RequestHeader]
    hostname: str
    post_params: _containers.RepeatedCompositeFieldContainer[CMsgHttpRequest.QueryParam]
    request_method: int
    url: str
    def __init__(self, request_method: _Optional[int] = ..., hostname: _Optional[str] = ..., url: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[CMsgHttpRequest.RequestHeader, _Mapping]]] = ..., get_params: _Optional[_Iterable[_Union[CMsgHttpRequest.QueryParam, _Mapping]]] = ..., post_params: _Optional[_Iterable[_Union[CMsgHttpRequest.QueryParam, _Mapping]]] = ..., body: _Optional[bytes] = ..., absolute_timeout: _Optional[int] = ...) -> None: ...

class CMsgHttpResponse(_message.Message):
    __slots__ = ["body", "headers", "status_code"]
    class ResponseHeader(_message.Message):
        __slots__ = ["name", "value"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    body: bytes
    headers: _containers.RepeatedCompositeFieldContainer[CMsgHttpResponse.ResponseHeader]
    status_code: int
    def __init__(self, status_code: _Optional[int] = ..., headers: _Optional[_Iterable[_Union[CMsgHttpResponse.ResponseHeader, _Mapping]]] = ..., body: _Optional[bytes] = ...) -> None: ...

class CMsgNotificationOfSuspiciousActivity(_message.Message):
    __slots__ = ["appid", "multiple_instances", "steamid"]
    class MultipleGameInstances(_message.Message):
        __slots__ = ["app_instance_count", "other_steamids"]
        APP_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        OTHER_STEAMIDS_FIELD_NUMBER: _ClassVar[int]
        app_instance_count: int
        other_steamids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, app_instance_count: _Optional[int] = ..., other_steamids: _Optional[_Iterable[int]] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    multiple_instances: CMsgNotificationOfSuspiciousActivity.MultipleGameInstances
    steamid: int
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ..., multiple_instances: _Optional[_Union[CMsgNotificationOfSuspiciousActivity.MultipleGameInstances, _Mapping]] = ...) -> None: ...

class CMsgNotifyWatchdog(_message.Message):
    __slots__ = ["alert_destination", "alert_type", "appid", "critical", "source", "text", "time"]
    ALERT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    alert_destination: int
    alert_type: int
    appid: int
    critical: bool
    source: int
    text: str
    time: int
    def __init__(self, source: _Optional[int] = ..., alert_type: _Optional[int] = ..., alert_destination: _Optional[int] = ..., critical: bool = ..., time: _Optional[int] = ..., appid: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgPackageLicense(_message.Message):
    __slots__ = ["owner_id", "package_id", "time_created"]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    owner_id: int
    package_id: int
    time_created: int
    def __init__(self, package_id: _Optional[int] = ..., time_created: _Optional[int] = ..., owner_id: _Optional[int] = ...) -> None: ...

class CMsgProtoBufHeader(_message.Message):
    __slots__ = ["client_session_id", "client_steam_id", "eresult", "error_message", "gc_dir_index_source", "gc_msg_src", "ip", "job_id_source", "job_id_target", "source_app_id", "target_job_name"]
    CLIENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GC_DIR_INDEX_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GC_MSG_SRC_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_TARGET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_APP_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    client_session_id: int
    client_steam_id: int
    eresult: int
    error_message: str
    gc_dir_index_source: int
    gc_msg_src: GCProtoBufMsgSrc
    ip: int
    job_id_source: int
    job_id_target: int
    source_app_id: int
    target_job_name: str
    def __init__(self, client_steam_id: _Optional[int] = ..., client_session_id: _Optional[int] = ..., source_app_id: _Optional[int] = ..., job_id_source: _Optional[int] = ..., job_id_target: _Optional[int] = ..., target_job_name: _Optional[str] = ..., eresult: _Optional[int] = ..., error_message: _Optional[str] = ..., ip: _Optional[int] = ..., gc_msg_src: _Optional[_Union[GCProtoBufMsgSrc, str]] = ..., gc_dir_index_source: _Optional[int] = ...) -> None: ...

class CMsgWebAPIKey(_message.Message):
    __slots__ = ["account_id", "domain", "key_id", "publisher_group_id", "status"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    domain: str
    key_id: int
    publisher_group_id: int
    status: int
    def __init__(self, status: _Optional[int] = ..., account_id: _Optional[int] = ..., publisher_group_id: _Optional[int] = ..., key_id: _Optional[int] = ..., domain: _Optional[str] = ...) -> None: ...

class CMsgWebAPIRequest(_message.Message):
    __slots__ = ["api_key", "interface_name", "method_name", "request", "routing_app_id", "version"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ROUTING_APP_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    api_key: CMsgWebAPIKey
    interface_name: str
    method_name: str
    request: CMsgHttpRequest
    routing_app_id: int
    version: int
    def __init__(self, interface_name: _Optional[str] = ..., method_name: _Optional[str] = ..., version: _Optional[int] = ..., api_key: _Optional[_Union[CMsgWebAPIKey, _Mapping]] = ..., request: _Optional[_Union[CMsgHttpRequest, _Mapping]] = ..., routing_app_id: _Optional[int] = ...) -> None: ...

class GCProtoBufMsgSrc(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
