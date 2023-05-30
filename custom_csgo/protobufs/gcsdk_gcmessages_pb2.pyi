import steammessages_pb2 as _steammessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GCClientLauncherType_DEFAULT: GCClientLauncherType
GCClientLauncherType_PERFECTWORLD: GCClientLauncherType
GCClientLauncherType_STEAMCHINA: GCClientLauncherType
GCConnectionStatus_GC_GOING_DOWN: GCConnectionStatus
GCConnectionStatus_HAVE_SESSION: GCConnectionStatus
GCConnectionStatus_NO_SESSION: GCConnectionStatus
GCConnectionStatus_NO_SESSION_IN_LOGON_QUEUE: GCConnectionStatus
GCConnectionStatus_NO_STEAM: GCConnectionStatus

class CGCToGCMsgMasterAck(_message.Message):
    __slots__ = ["dir_index", "gc_type"]
    DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
    GC_TYPE_FIELD_NUMBER: _ClassVar[int]
    dir_index: int
    gc_type: int
    def __init__(self, dir_index: _Optional[int] = ..., gc_type: _Optional[int] = ...) -> None: ...

class CGCToGCMsgMasterAck_Response(_message.Message):
    __slots__ = ["eresult"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CGCToGCMsgMasterStartupComplete(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CGCToGCMsgRouted(_message.Message):
    __slots__ = ["ip", "msg_type", "net_message", "sender_id"]
    IP_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    NET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    ip: int
    msg_type: int
    net_message: bytes
    sender_id: int
    def __init__(self, msg_type: _Optional[int] = ..., sender_id: _Optional[int] = ..., net_message: _Optional[bytes] = ..., ip: _Optional[int] = ...) -> None: ...

class CGCToGCMsgRoutedReply(_message.Message):
    __slots__ = ["msg_type", "net_message"]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    NET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    msg_type: int
    net_message: bytes
    def __init__(self, msg_type: _Optional[int] = ..., net_message: _Optional[bytes] = ...) -> None: ...

class CGameServers_AggregationQuery_Request(_message.Message):
    __slots__ = ["filter", "group_fields"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELDS_FIELD_NUMBER: _ClassVar[int]
    filter: str
    group_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, filter: _Optional[str] = ..., group_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class CGameServers_AggregationQuery_Response(_message.Message):
    __slots__ = ["groups"]
    class Group(_message.Message):
        __slots__ = ["group_values", "player_capacity", "players_bots", "players_humans", "servers_empty", "servers_full", "servers_total"]
        GROUP_VALUES_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_BOTS_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_HUMANS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_CAPACITY_FIELD_NUMBER: _ClassVar[int]
        SERVERS_EMPTY_FIELD_NUMBER: _ClassVar[int]
        SERVERS_FULL_FIELD_NUMBER: _ClassVar[int]
        SERVERS_TOTAL_FIELD_NUMBER: _ClassVar[int]
        group_values: _containers.RepeatedScalarFieldContainer[str]
        player_capacity: int
        players_bots: int
        players_humans: int
        servers_empty: int
        servers_full: int
        servers_total: int
        def __init__(self, group_values: _Optional[_Iterable[str]] = ..., servers_empty: _Optional[int] = ..., servers_full: _Optional[int] = ..., servers_total: _Optional[int] = ..., players_humans: _Optional[int] = ..., players_bots: _Optional[int] = ..., player_capacity: _Optional[int] = ...) -> None: ...
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[CGameServers_AggregationQuery_Response.Group]
    def __init__(self, groups: _Optional[_Iterable[_Union[CGameServers_AggregationQuery_Response.Group, _Mapping]]] = ...) -> None: ...

class CMsgAccountDetails(_message.Message):
    __slots__ = ["account_locked", "account_name", "community_banned", "cyber_cafe", "eligible_for_community_market", "free_trial_account", "limited", "low_violence", "package", "public_inventory", "public_profile", "school_account", "subscribed", "time_cached", "trade_banned", "trusted", "vac_banned", "valid"]
    ACCOUNT_LOCKED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_BANNED_FIELD_NUMBER: _ClassVar[int]
    CYBER_CAFE_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_FOR_COMMUNITY_MARKET_FIELD_NUMBER: _ClassVar[int]
    FREE_TRIAL_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    LIMITED_FIELD_NUMBER: _ClassVar[int]
    LOW_VIOLENCE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SCHOOL_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    TIME_CACHED_FIELD_NUMBER: _ClassVar[int]
    TRADE_BANNED_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_FIELD_NUMBER: _ClassVar[int]
    VAC_BANNED_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    account_locked: bool
    account_name: str
    community_banned: bool
    cyber_cafe: bool
    eligible_for_community_market: bool
    free_trial_account: bool
    limited: bool
    low_violence: bool
    package: int
    public_inventory: bool
    public_profile: bool
    school_account: bool
    subscribed: bool
    time_cached: int
    trade_banned: bool
    trusted: bool
    vac_banned: bool
    valid: bool
    def __init__(self, valid: bool = ..., account_name: _Optional[str] = ..., public_profile: bool = ..., public_inventory: bool = ..., vac_banned: bool = ..., cyber_cafe: bool = ..., school_account: bool = ..., free_trial_account: bool = ..., subscribed: bool = ..., low_violence: bool = ..., limited: bool = ..., trusted: bool = ..., package: _Optional[int] = ..., time_cached: _Optional[int] = ..., account_locked: bool = ..., community_banned: bool = ..., trade_banned: bool = ..., eligible_for_community_market: bool = ...) -> None: ...

class CMsgClientHello(_message.Message):
    __slots__ = ["client_launcher", "client_session_need", "partner_accountbalance", "partner_accountflags", "partner_accountid", "partner_srcid", "socache_have_versions", "steam_launcher", "version"]
    CLIENT_LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SESSION_NEED_FIELD_NUMBER: _ClassVar[int]
    PARTNER_ACCOUNTBALANCE_FIELD_NUMBER: _ClassVar[int]
    PARTNER_ACCOUNTFLAGS_FIELD_NUMBER: _ClassVar[int]
    PARTNER_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_SRCID_FIELD_NUMBER: _ClassVar[int]
    SOCACHE_HAVE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    STEAM_LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_launcher: int
    client_session_need: int
    partner_accountbalance: int
    partner_accountflags: int
    partner_accountid: int
    partner_srcid: int
    socache_have_versions: _containers.RepeatedCompositeFieldContainer[CMsgSOCacheHaveVersion]
    steam_launcher: int
    version: int
    def __init__(self, version: _Optional[int] = ..., socache_have_versions: _Optional[_Iterable[_Union[CMsgSOCacheHaveVersion, _Mapping]]] = ..., client_session_need: _Optional[int] = ..., client_launcher: _Optional[int] = ..., partner_srcid: _Optional[int] = ..., partner_accountid: _Optional[int] = ..., partner_accountflags: _Optional[int] = ..., partner_accountbalance: _Optional[int] = ..., steam_launcher: _Optional[int] = ...) -> None: ...

class CMsgClientWelcome(_message.Message):
    __slots__ = ["balance", "balance_url", "currency", "game_data", "game_data2", "location", "outofdate_subscribed_caches", "rtime32_gc_welcome_timestamp", "txn_country_code", "uptodate_subscribed_caches", "version"]
    class Location(_message.Message):
        __slots__ = ["country", "latitude", "longitude"]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        LATITUDE_FIELD_NUMBER: _ClassVar[int]
        LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        country: str
        latitude: float
        longitude: float
        def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., country: _Optional[str] = ...) -> None: ...
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_URL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    GAME_DATA2_FIELD_NUMBER: _ClassVar[int]
    GAME_DATA_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    OUTOFDATE_SUBSCRIBED_CACHES_FIELD_NUMBER: _ClassVar[int]
    RTIME32_GC_WELCOME_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TXN_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    UPTODATE_SUBSCRIBED_CACHES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    balance: int
    balance_url: str
    currency: int
    game_data: bytes
    game_data2: bytes
    location: CMsgClientWelcome.Location
    outofdate_subscribed_caches: _containers.RepeatedCompositeFieldContainer[CMsgSOCacheSubscribed]
    rtime32_gc_welcome_timestamp: int
    txn_country_code: str
    uptodate_subscribed_caches: _containers.RepeatedCompositeFieldContainer[CMsgSOCacheSubscriptionCheck]
    version: int
    def __init__(self, version: _Optional[int] = ..., game_data: _Optional[bytes] = ..., outofdate_subscribed_caches: _Optional[_Iterable[_Union[CMsgSOCacheSubscribed, _Mapping]]] = ..., uptodate_subscribed_caches: _Optional[_Iterable[_Union[CMsgSOCacheSubscriptionCheck, _Mapping]]] = ..., location: _Optional[_Union[CMsgClientWelcome.Location, _Mapping]] = ..., game_data2: _Optional[bytes] = ..., rtime32_gc_welcome_timestamp: _Optional[int] = ..., currency: _Optional[int] = ..., balance: _Optional[int] = ..., balance_url: _Optional[str] = ..., txn_country_code: _Optional[str] = ...) -> None: ...

class CMsgConnectionStatus(_message.Message):
    __slots__ = ["client_session_need", "estimated_wait_seconds_remaining", "queue_position", "queue_size", "status", "wait_seconds"]
    CLIENT_SESSION_NEED_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_WAIT_SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    QUEUE_POSITION_FIELD_NUMBER: _ClassVar[int]
    QUEUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WAIT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    client_session_need: int
    estimated_wait_seconds_remaining: int
    queue_position: int
    queue_size: int
    status: GCConnectionStatus
    wait_seconds: int
    def __init__(self, status: _Optional[_Union[GCConnectionStatus, str]] = ..., client_session_need: _Optional[int] = ..., queue_position: _Optional[int] = ..., queue_size: _Optional[int] = ..., wait_seconds: _Optional[int] = ..., estimated_wait_seconds_remaining: _Optional[int] = ...) -> None: ...

class CMsgGCMultiplexMessage(_message.Message):
    __slots__ = ["msgtype", "payload", "replytogc", "steamids"]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REPLYTOGC_FIELD_NUMBER: _ClassVar[int]
    STEAMIDS_FIELD_NUMBER: _ClassVar[int]
    msgtype: int
    payload: bytes
    replytogc: bool
    steamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, msgtype: _Optional[int] = ..., payload: _Optional[bytes] = ..., steamids: _Optional[_Iterable[int]] = ..., replytogc: bool = ...) -> None: ...

class CMsgGCMultiplexMessage_Response(_message.Message):
    __slots__ = ["msgtype"]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    msgtype: int
    def __init__(self, msgtype: _Optional[int] = ...) -> None: ...

class CMsgGCRequestSessionIP(_message.Message):
    __slots__ = ["steamid"]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CMsgGCRequestSessionIPResponse(_message.Message):
    __slots__ = ["ip"]
    IP_FIELD_NUMBER: _ClassVar[int]
    ip: int
    def __init__(self, ip: _Optional[int] = ...) -> None: ...

class CMsgGCUpdateSessionIP(_message.Message):
    __slots__ = ["ip", "steamid"]
    IP_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    ip: int
    steamid: int
    def __init__(self, steamid: _Optional[int] = ..., ip: _Optional[int] = ...) -> None: ...

class CMsgSOCacheHaveVersion(_message.Message):
    __slots__ = ["soid", "version"]
    SOID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    soid: CMsgSOIDOwner
    version: int
    def __init__(self, soid: _Optional[_Union[CMsgSOIDOwner, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class CMsgSOCacheSubscribed(_message.Message):
    __slots__ = ["objects", "owner_soid", "version"]
    class SubscribedType(_message.Message):
        __slots__ = ["object_data", "type_id"]
        OBJECT_DATA_FIELD_NUMBER: _ClassVar[int]
        TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        object_data: _containers.RepeatedScalarFieldContainer[bytes]
        type_id: int
        def __init__(self, type_id: _Optional[int] = ..., object_data: _Optional[_Iterable[bytes]] = ...) -> None: ...
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    OWNER_SOID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[CMsgSOCacheSubscribed.SubscribedType]
    owner_soid: CMsgSOIDOwner
    version: int
    def __init__(self, objects: _Optional[_Iterable[_Union[CMsgSOCacheSubscribed.SubscribedType, _Mapping]]] = ..., version: _Optional[int] = ..., owner_soid: _Optional[_Union[CMsgSOIDOwner, _Mapping]] = ...) -> None: ...

class CMsgSOCacheSubscriptionCheck(_message.Message):
    __slots__ = ["owner_soid", "version"]
    OWNER_SOID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    owner_soid: CMsgSOIDOwner
    version: int
    def __init__(self, version: _Optional[int] = ..., owner_soid: _Optional[_Union[CMsgSOIDOwner, _Mapping]] = ...) -> None: ...

class CMsgSOCacheSubscriptionRefresh(_message.Message):
    __slots__ = ["owner_soid"]
    OWNER_SOID_FIELD_NUMBER: _ClassVar[int]
    owner_soid: CMsgSOIDOwner
    def __init__(self, owner_soid: _Optional[_Union[CMsgSOIDOwner, _Mapping]] = ...) -> None: ...

class CMsgSOCacheUnsubscribed(_message.Message):
    __slots__ = ["owner_soid"]
    OWNER_SOID_FIELD_NUMBER: _ClassVar[int]
    owner_soid: CMsgSOIDOwner
    def __init__(self, owner_soid: _Optional[_Union[CMsgSOIDOwner, _Mapping]] = ...) -> None: ...

class CMsgSOCacheVersion(_message.Message):
    __slots__ = ["version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class CMsgSOIDOwner(_message.Message):
    __slots__ = ["id", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class CMsgSOMultipleObjects(_message.Message):
    __slots__ = ["objects_modified", "owner_soid", "version"]
    class SingleObject(_message.Message):
        __slots__ = ["object_data", "type_id"]
        OBJECT_DATA_FIELD_NUMBER: _ClassVar[int]
        TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        object_data: bytes
        type_id: int
        def __init__(self, type_id: _Optional[int] = ..., object_data: _Optional[bytes] = ...) -> None: ...
    OBJECTS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    OWNER_SOID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    objects_modified: _containers.RepeatedCompositeFieldContainer[CMsgSOMultipleObjects.SingleObject]
    owner_soid: CMsgSOIDOwner
    version: int
    def __init__(self, objects_modified: _Optional[_Iterable[_Union[CMsgSOMultipleObjects.SingleObject, _Mapping]]] = ..., version: _Optional[int] = ..., owner_soid: _Optional[_Union[CMsgSOIDOwner, _Mapping]] = ...) -> None: ...

class CMsgSOSingleObject(_message.Message):
    __slots__ = ["object_data", "owner_soid", "type_id", "version"]
    OBJECT_DATA_FIELD_NUMBER: _ClassVar[int]
    OWNER_SOID_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    object_data: bytes
    owner_soid: CMsgSOIDOwner
    type_id: int
    version: int
    def __init__(self, type_id: _Optional[int] = ..., object_data: _Optional[bytes] = ..., version: _Optional[int] = ..., owner_soid: _Optional[_Union[CMsgSOIDOwner, _Mapping]] = ...) -> None: ...

class CMsgSerializedSOCache(_message.Message):
    __slots__ = ["caches", "file_version", "gc_socache_file_version"]
    class Cache(_message.Message):
        __slots__ = ["id", "type", "type_caches", "versions"]
        class Version(_message.Message):
            __slots__ = ["service", "version"]
            SERVICE_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            service: int
            version: int
            def __init__(self, service: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_CACHES_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        id: int
        type: int
        type_caches: _containers.RepeatedCompositeFieldContainer[CMsgSerializedSOCache.TypeCache]
        versions: _containers.RepeatedCompositeFieldContainer[CMsgSerializedSOCache.Cache.Version]
        def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., versions: _Optional[_Iterable[_Union[CMsgSerializedSOCache.Cache.Version, _Mapping]]] = ..., type_caches: _Optional[_Iterable[_Union[CMsgSerializedSOCache.TypeCache, _Mapping]]] = ...) -> None: ...
    class TypeCache(_message.Message):
        __slots__ = ["objects", "service_id", "type"]
        OBJECTS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        objects: _containers.RepeatedScalarFieldContainer[bytes]
        service_id: int
        type: int
        def __init__(self, type: _Optional[int] = ..., objects: _Optional[_Iterable[bytes]] = ..., service_id: _Optional[int] = ...) -> None: ...
    CACHES_FIELD_NUMBER: _ClassVar[int]
    FILE_VERSION_FIELD_NUMBER: _ClassVar[int]
    GC_SOCACHE_FILE_VERSION_FIELD_NUMBER: _ClassVar[int]
    caches: _containers.RepeatedCompositeFieldContainer[CMsgSerializedSOCache.Cache]
    file_version: int
    gc_socache_file_version: int
    def __init__(self, file_version: _Optional[int] = ..., caches: _Optional[_Iterable[_Union[CMsgSerializedSOCache.Cache, _Mapping]]] = ..., gc_socache_file_version: _Optional[int] = ...) -> None: ...

class CMsgServerHello(_message.Message):
    __slots__ = ["client_launcher", "legacy_client_session_need", "legacy_steamdatagram_routing", "required_internal_addr", "socache_have_versions", "steamdatagram_login", "version"]
    CLIENT_LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    LEGACY_CLIENT_SESSION_NEED_FIELD_NUMBER: _ClassVar[int]
    LEGACY_STEAMDATAGRAM_ROUTING_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_INTERNAL_ADDR_FIELD_NUMBER: _ClassVar[int]
    SOCACHE_HAVE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    STEAMDATAGRAM_LOGIN_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_launcher: int
    legacy_client_session_need: int
    legacy_steamdatagram_routing: bytes
    required_internal_addr: int
    socache_have_versions: _containers.RepeatedCompositeFieldContainer[CMsgSOCacheHaveVersion]
    steamdatagram_login: bytes
    version: int
    def __init__(self, version: _Optional[int] = ..., socache_have_versions: _Optional[_Iterable[_Union[CMsgSOCacheHaveVersion, _Mapping]]] = ..., legacy_client_session_need: _Optional[int] = ..., client_launcher: _Optional[int] = ..., legacy_steamdatagram_routing: _Optional[bytes] = ..., required_internal_addr: _Optional[int] = ..., steamdatagram_login: _Optional[bytes] = ...) -> None: ...

class CProductInfo_SetRichPresenceLocalization_Request(_message.Message):
    __slots__ = ["appid", "languages", "steamid"]
    class LanguageSection(_message.Message):
        __slots__ = ["language", "tokens"]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        TOKENS_FIELD_NUMBER: _ClassVar[int]
        language: str
        tokens: _containers.RepeatedCompositeFieldContainer[CProductInfo_SetRichPresenceLocalization_Request.Token]
        def __init__(self, language: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[CProductInfo_SetRichPresenceLocalization_Request.Token, _Mapping]]] = ...) -> None: ...
    class Token(_message.Message):
        __slots__ = ["token", "value"]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        token: str
        value: str
        def __init__(self, token: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    languages: _containers.RepeatedCompositeFieldContainer[CProductInfo_SetRichPresenceLocalization_Request.LanguageSection]
    steamid: int
    def __init__(self, appid: _Optional[int] = ..., languages: _Optional[_Iterable[_Union[CProductInfo_SetRichPresenceLocalization_Request.LanguageSection, _Mapping]]] = ..., steamid: _Optional[int] = ...) -> None: ...

class CProductInfo_SetRichPresenceLocalization_Response(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CWorkshop_AddSpecialPayment_Request(_message.Message):
    __slots__ = ["appid", "date", "gameitemid", "payment_row_usd", "payment_us_usd"]
    APPID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    GAMEITEMID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ROW_USD_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_US_USD_FIELD_NUMBER: _ClassVar[int]
    appid: int
    date: str
    gameitemid: int
    payment_row_usd: int
    payment_us_usd: int
    def __init__(self, appid: _Optional[int] = ..., gameitemid: _Optional[int] = ..., date: _Optional[str] = ..., payment_us_usd: _Optional[int] = ..., payment_row_usd: _Optional[int] = ...) -> None: ...

class CWorkshop_AddSpecialPayment_Response(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CWorkshop_GetContributors_Request(_message.Message):
    __slots__ = ["appid", "gameitemid"]
    APPID_FIELD_NUMBER: _ClassVar[int]
    GAMEITEMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    gameitemid: int
    def __init__(self, appid: _Optional[int] = ..., gameitemid: _Optional[int] = ...) -> None: ...

class CWorkshop_GetContributors_Response(_message.Message):
    __slots__ = ["contributors"]
    CONTRIBUTORS_FIELD_NUMBER: _ClassVar[int]
    contributors: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, contributors: _Optional[_Iterable[int]] = ...) -> None: ...

class CWorkshop_PopulateItemDescriptions_Request(_message.Message):
    __slots__ = ["appid", "languages"]
    class ItemDescriptionsLanguageBlock(_message.Message):
        __slots__ = ["descriptions", "language"]
        DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        descriptions: _containers.RepeatedCompositeFieldContainer[CWorkshop_PopulateItemDescriptions_Request.SingleItemDescription]
        language: str
        def __init__(self, language: _Optional[str] = ..., descriptions: _Optional[_Iterable[_Union[CWorkshop_PopulateItemDescriptions_Request.SingleItemDescription, _Mapping]]] = ...) -> None: ...
    class SingleItemDescription(_message.Message):
        __slots__ = ["gameitemid", "item_description", "one_per_account"]
        GAMEITEMID_FIELD_NUMBER: _ClassVar[int]
        ITEM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ONE_PER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        gameitemid: int
        item_description: str
        one_per_account: bool
        def __init__(self, gameitemid: _Optional[int] = ..., item_description: _Optional[str] = ..., one_per_account: bool = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    appid: int
    languages: _containers.RepeatedCompositeFieldContainer[CWorkshop_PopulateItemDescriptions_Request.ItemDescriptionsLanguageBlock]
    def __init__(self, appid: _Optional[int] = ..., languages: _Optional[_Iterable[_Union[CWorkshop_PopulateItemDescriptions_Request.ItemDescriptionsLanguageBlock, _Mapping]]] = ...) -> None: ...

class CWorkshop_SetItemPaymentRules_Request(_message.Message):
    __slots__ = ["appid", "associated_workshop_file_for_direct_payments", "associated_workshop_files", "gameitemid", "make_workshop_files_subscribable", "partner_accounts", "validate_only"]
    class PartnerItemPaymentRule(_message.Message):
        __slots__ = ["account_id", "revenue_percentage", "rule_description"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        REVENUE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        RULE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        revenue_percentage: float
        rule_description: str
        def __init__(self, account_id: _Optional[int] = ..., revenue_percentage: _Optional[float] = ..., rule_description: _Optional[str] = ...) -> None: ...
    class WorkshopDirectPaymentRule(_message.Message):
        __slots__ = ["rule_description", "workshop_file_id"]
        RULE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        WORKSHOP_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        rule_description: str
        workshop_file_id: int
        def __init__(self, workshop_file_id: _Optional[int] = ..., rule_description: _Optional[str] = ...) -> None: ...
    class WorkshopItemPaymentRule(_message.Message):
        __slots__ = ["revenue_percentage", "rule_description", "rule_type", "workshop_file_id"]
        REVENUE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        RULE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        RULE_TYPE_FIELD_NUMBER: _ClassVar[int]
        WORKSHOP_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        revenue_percentage: float
        rule_description: str
        rule_type: int
        workshop_file_id: int
        def __init__(self, workshop_file_id: _Optional[int] = ..., revenue_percentage: _Optional[float] = ..., rule_description: _Optional[str] = ..., rule_type: _Optional[int] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_WORKSHOP_FILES_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_WORKSHOP_FILE_FOR_DIRECT_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    GAMEITEMID_FIELD_NUMBER: _ClassVar[int]
    MAKE_WORKSHOP_FILES_SUBSCRIBABLE_FIELD_NUMBER: _ClassVar[int]
    PARTNER_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    appid: int
    associated_workshop_file_for_direct_payments: CWorkshop_SetItemPaymentRules_Request.WorkshopDirectPaymentRule
    associated_workshop_files: _containers.RepeatedCompositeFieldContainer[CWorkshop_SetItemPaymentRules_Request.WorkshopItemPaymentRule]
    gameitemid: int
    make_workshop_files_subscribable: bool
    partner_accounts: _containers.RepeatedCompositeFieldContainer[CWorkshop_SetItemPaymentRules_Request.PartnerItemPaymentRule]
    validate_only: bool
    def __init__(self, appid: _Optional[int] = ..., gameitemid: _Optional[int] = ..., associated_workshop_files: _Optional[_Iterable[_Union[CWorkshop_SetItemPaymentRules_Request.WorkshopItemPaymentRule, _Mapping]]] = ..., partner_accounts: _Optional[_Iterable[_Union[CWorkshop_SetItemPaymentRules_Request.PartnerItemPaymentRule, _Mapping]]] = ..., validate_only: bool = ..., make_workshop_files_subscribable: bool = ..., associated_workshop_file_for_direct_payments: _Optional[_Union[CWorkshop_SetItemPaymentRules_Request.WorkshopDirectPaymentRule, _Mapping]] = ...) -> None: ...

class CWorkshop_SetItemPaymentRules_Response(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GCClientLauncherType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class GCConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
