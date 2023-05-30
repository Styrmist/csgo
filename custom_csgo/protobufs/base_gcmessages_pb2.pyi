import steammessages_pb2 as _steammessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GC_BANNED_WORD_DISABLE_WORD: GC_BannedWordType
GC_BANNED_WORD_ENABLE_WORD: GC_BannedWordType
k_EMsgGCClientConnectToServer: EGCBaseMsg
k_EMsgGCConVarUpdated: EGCBaseMsg
k_EMsgGCError: EGCBaseMsg
k_EMsgGCGameServerInfo: EGCBaseMsg
k_EMsgGCInQueue: EGCBaseMsg
k_EMsgGCInvitationCreated: EGCBaseMsg
k_EMsgGCInviteToParty: EGCBaseMsg
k_EMsgGCKickFromParty: EGCBaseMsg
k_EMsgGCLANServerAvailable: EGCBaseMsg
k_EMsgGCLeaveParty: EGCBaseMsg
k_EMsgGCPartyInviteResponse: EGCBaseMsg
k_EMsgGCReplay_UploadedToYouTube: EGCBaseMsg
k_EMsgGCReplicateConVars: EGCBaseMsg
k_EMsgGCServerAvailable: EGCBaseMsg
k_EMsgGCSystemMessage: EGCBaseMsg
k_EProtoObjectLobbyInvite: EGCBaseProtoObjectTypes
k_EProtoObjectPartyInvite: EGCBaseProtoObjectTypes

class CGCStorePurchaseInit_LineItem(_message.Message):
    __slots__ = ["cost_in_local_currency", "item_def_id", "purchase_type", "quantity"]
    COST_IN_LOCAL_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ITEM_DEF_ID_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    cost_in_local_currency: int
    item_def_id: int
    purchase_type: int
    quantity: int
    def __init__(self, item_def_id: _Optional[int] = ..., quantity: _Optional[int] = ..., cost_in_local_currency: _Optional[int] = ..., purchase_type: _Optional[int] = ...) -> None: ...

class CMsgAdjustItemEquippedState(_message.Message):
    __slots__ = ["item_id", "new_class", "new_slot", "swap"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_CLASS_FIELD_NUMBER: _ClassVar[int]
    NEW_SLOT_FIELD_NUMBER: _ClassVar[int]
    SWAP_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    new_class: int
    new_slot: int
    swap: bool
    def __init__(self, item_id: _Optional[int] = ..., new_class: _Optional[int] = ..., new_slot: _Optional[int] = ..., swap: bool = ...) -> None: ...

class CMsgAdjustItemEquippedStateMulti(_message.Message):
    __slots__ = ["ct_equips", "noteam_equips", "t_equips"]
    CT_EQUIPS_FIELD_NUMBER: _ClassVar[int]
    NOTEAM_EQUIPS_FIELD_NUMBER: _ClassVar[int]
    T_EQUIPS_FIELD_NUMBER: _ClassVar[int]
    ct_equips: _containers.RepeatedScalarFieldContainer[int]
    noteam_equips: _containers.RepeatedScalarFieldContainer[int]
    t_equips: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, t_equips: _Optional[_Iterable[int]] = ..., ct_equips: _Optional[_Iterable[int]] = ..., noteam_equips: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgApplyEggEssence(_message.Message):
    __slots__ = ["egg_item_id", "essence_item_id"]
    EGG_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ESSENCE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    egg_item_id: int
    essence_item_id: int
    def __init__(self, essence_item_id: _Optional[int] = ..., egg_item_id: _Optional[int] = ...) -> None: ...

class CMsgApplyPennantUpgrade(_message.Message):
    __slots__ = ["pennant_item_id", "upgrade_item_id"]
    PENNANT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    pennant_item_id: int
    upgrade_item_id: int
    def __init__(self, upgrade_item_id: _Optional[int] = ..., pennant_item_id: _Optional[int] = ...) -> None: ...

class CMsgApplyStatTrakSwap(_message.Message):
    __slots__ = ["item_1_item_id", "item_2_item_id", "tool_item_id"]
    ITEM_1_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_2_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_1_item_id: int
    item_2_item_id: int
    tool_item_id: int
    def __init__(self, tool_item_id: _Optional[int] = ..., item_1_item_id: _Optional[int] = ..., item_2_item_id: _Optional[int] = ...) -> None: ...

class CMsgApplySticker(_message.Message):
    __slots__ = ["baseitem_defidx", "item_item_id", "sticker_item_id", "sticker_slot", "sticker_wear"]
    BASEITEM_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    ITEM_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    STICKER_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    STICKER_SLOT_FIELD_NUMBER: _ClassVar[int]
    STICKER_WEAR_FIELD_NUMBER: _ClassVar[int]
    baseitem_defidx: int
    item_item_id: int
    sticker_item_id: int
    sticker_slot: int
    sticker_wear: float
    def __init__(self, sticker_item_id: _Optional[int] = ..., item_item_id: _Optional[int] = ..., sticker_slot: _Optional[int] = ..., baseitem_defidx: _Optional[int] = ..., sticker_wear: _Optional[float] = ...) -> None: ...

class CMsgApplyStrangePart(_message.Message):
    __slots__ = ["item_item_id", "strange_part_item_id"]
    ITEM_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    STRANGE_PART_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_item_id: int
    strange_part_item_id: int
    def __init__(self, strange_part_item_id: _Optional[int] = ..., item_item_id: _Optional[int] = ...) -> None: ...

class CMsgConVarValue(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class CMsgConsumableExhausted(_message.Message):
    __slots__ = ["item_def_id"]
    ITEM_DEF_ID_FIELD_NUMBER: _ClassVar[int]
    item_def_id: int
    def __init__(self, item_def_id: _Optional[int] = ...) -> None: ...

class CMsgDevNewItemRequest(_message.Message):
    __slots__ = ["criteria", "receiver"]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    criteria: CSOItemCriteria
    receiver: int
    def __init__(self, receiver: _Optional[int] = ..., criteria: _Optional[_Union[CSOItemCriteria, _Mapping]] = ...) -> None: ...

class CMsgGCBannedWord(_message.Message):
    __slots__ = ["word", "word_id", "word_type"]
    WORD_FIELD_NUMBER: _ClassVar[int]
    WORD_ID_FIELD_NUMBER: _ClassVar[int]
    WORD_TYPE_FIELD_NUMBER: _ClassVar[int]
    word: str
    word_id: int
    word_type: GC_BannedWordType
    def __init__(self, word_id: _Optional[int] = ..., word_type: _Optional[_Union[GC_BannedWordType, str]] = ..., word: _Optional[str] = ...) -> None: ...

class CMsgGCBannedWordListRequest(_message.Message):
    __slots__ = ["ban_list_group_id", "word_id"]
    BAN_LIST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    WORD_ID_FIELD_NUMBER: _ClassVar[int]
    ban_list_group_id: int
    word_id: int
    def __init__(self, ban_list_group_id: _Optional[int] = ..., word_id: _Optional[int] = ...) -> None: ...

class CMsgGCBannedWordListResponse(_message.Message):
    __slots__ = ["ban_list_group_id", "word_list"]
    BAN_LIST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    WORD_LIST_FIELD_NUMBER: _ClassVar[int]
    ban_list_group_id: int
    word_list: _containers.RepeatedCompositeFieldContainer[CMsgGCBannedWord]
    def __init__(self, ban_list_group_id: _Optional[int] = ..., word_list: _Optional[_Iterable[_Union[CMsgGCBannedWord, _Mapping]]] = ...) -> None: ...

class CMsgGCClientDisplayNotification(_message.Message):
    __slots__ = ["body_substring_keys", "body_substring_values", "notification_body_localization_key", "notification_title_localization_key"]
    BODY_SUBSTRING_KEYS_FIELD_NUMBER: _ClassVar[int]
    BODY_SUBSTRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_BODY_LOCALIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TITLE_LOCALIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    body_substring_keys: _containers.RepeatedScalarFieldContainer[str]
    body_substring_values: _containers.RepeatedScalarFieldContainer[str]
    notification_body_localization_key: str
    notification_title_localization_key: str
    def __init__(self, notification_title_localization_key: _Optional[str] = ..., notification_body_localization_key: _Optional[str] = ..., body_substring_keys: _Optional[_Iterable[str]] = ..., body_substring_values: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgGCClientVersionUpdated(_message.Message):
    __slots__ = ["client_version"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    def __init__(self, client_version: _Optional[int] = ...) -> None: ...

class CMsgGCCollectItem(_message.Message):
    __slots__ = ["collection_item_id", "subject_item_id"]
    COLLECTION_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    collection_item_id: int
    subject_item_id: int
    def __init__(self, collection_item_id: _Optional[int] = ..., subject_item_id: _Optional[int] = ...) -> None: ...

class CMsgGCError(_message.Message):
    __slots__ = ["error_text"]
    ERROR_TEXT_FIELD_NUMBER: _ClassVar[int]
    error_text: str
    def __init__(self, error_text: _Optional[str] = ...) -> None: ...

class CMsgGCIncrementKillCountResponse(_message.Message):
    __slots__ = ["item_def", "killer_account_id", "level_type", "num_kills"]
    ITEM_DEF_FIELD_NUMBER: _ClassVar[int]
    KILLER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_KILLS_FIELD_NUMBER: _ClassVar[int]
    item_def: int
    killer_account_id: int
    level_type: int
    num_kills: int
    def __init__(self, killer_account_id: _Optional[int] = ..., num_kills: _Optional[int] = ..., item_def: _Optional[int] = ..., level_type: _Optional[int] = ...) -> None: ...

class CMsgGCItemPreviewItemBoughtNotification(_message.Message):
    __slots__ = ["item_def_index"]
    ITEM_DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
    item_def_index: int
    def __init__(self, item_def_index: _Optional[int] = ...) -> None: ...

class CMsgGCNameItemNotification(_message.Message):
    __slots__ = ["item_def_index", "item_name_custom", "player_steamid"]
    ITEM_DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEM_NAME_CUSTOM_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    item_def_index: int
    item_name_custom: str
    player_steamid: int
    def __init__(self, player_steamid: _Optional[int] = ..., item_def_index: _Optional[int] = ..., item_name_custom: _Optional[str] = ...) -> None: ...

class CMsgGCReportAbuse(_message.Message):
    __slots__ = ["abuse_type", "content_type", "description", "gid", "target_game_server_ip", "target_game_server_port", "target_steam_id"]
    ABUSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    TARGET_GAME_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    TARGET_GAME_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    TARGET_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    abuse_type: int
    content_type: int
    description: str
    gid: int
    target_game_server_ip: int
    target_game_server_port: int
    target_steam_id: int
    def __init__(self, target_steam_id: _Optional[int] = ..., description: _Optional[str] = ..., gid: _Optional[int] = ..., abuse_type: _Optional[int] = ..., content_type: _Optional[int] = ..., target_game_server_ip: _Optional[int] = ..., target_game_server_port: _Optional[int] = ...) -> None: ...

class CMsgGCReportAbuseResponse(_message.Message):
    __slots__ = ["error_message", "result", "target_steam_id"]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TARGET_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    result: int
    target_steam_id: int
    def __init__(self, target_steam_id: _Optional[int] = ..., result: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class CMsgGCRequestAnnouncements(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgGCRequestAnnouncementsResponse(_message.Message):
    __slots__ = ["announcement", "announcement_title", "nextmatch", "nextmatch_title"]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    NEXTMATCH_FIELD_NUMBER: _ClassVar[int]
    NEXTMATCH_TITLE_FIELD_NUMBER: _ClassVar[int]
    announcement: str
    announcement_title: str
    nextmatch: str
    nextmatch_title: str
    def __init__(self, announcement_title: _Optional[str] = ..., announcement: _Optional[str] = ..., nextmatch_title: _Optional[str] = ..., nextmatch: _Optional[str] = ...) -> None: ...

class CMsgGCServerVersionUpdated(_message.Message):
    __slots__ = ["server_version"]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    server_version: int
    def __init__(self, server_version: _Optional[int] = ...) -> None: ...

class CMsgGCShowItemsPickedUp(_message.Message):
    __slots__ = ["player_steamid"]
    PLAYER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    player_steamid: int
    def __init__(self, player_steamid: _Optional[int] = ...) -> None: ...

class CMsgGCStorePurchaseCancel(_message.Message):
    __slots__ = ["txn_id"]
    TXN_ID_FIELD_NUMBER: _ClassVar[int]
    txn_id: int
    def __init__(self, txn_id: _Optional[int] = ...) -> None: ...

class CMsgGCStorePurchaseCancelResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class CMsgGCStorePurchaseFinalize(_message.Message):
    __slots__ = ["txn_id"]
    TXN_ID_FIELD_NUMBER: _ClassVar[int]
    txn_id: int
    def __init__(self, txn_id: _Optional[int] = ...) -> None: ...

class CMsgGCStorePurchaseFinalizeResponse(_message.Message):
    __slots__ = ["item_ids", "result"]
    ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    item_ids: _containers.RepeatedScalarFieldContainer[int]
    result: int
    def __init__(self, result: _Optional[int] = ..., item_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCStorePurchaseInit(_message.Message):
    __slots__ = ["country", "currency", "language", "line_items"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    country: str
    currency: int
    language: int
    line_items: _containers.RepeatedCompositeFieldContainer[CGCStorePurchaseInit_LineItem]
    def __init__(self, country: _Optional[str] = ..., language: _Optional[int] = ..., currency: _Optional[int] = ..., line_items: _Optional[_Iterable[_Union[CGCStorePurchaseInit_LineItem, _Mapping]]] = ...) -> None: ...

class CMsgGCStorePurchaseInitResponse(_message.Message):
    __slots__ = ["item_ids", "result", "txn_id", "url"]
    ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TXN_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    item_ids: _containers.RepeatedScalarFieldContainer[int]
    result: int
    txn_id: int
    url: str
    def __init__(self, result: _Optional[int] = ..., txn_id: _Optional[int] = ..., url: _Optional[str] = ..., item_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCToGCBannedWordListBroadcast(_message.Message):
    __slots__ = ["broadcast"]
    BROADCAST_FIELD_NUMBER: _ClassVar[int]
    broadcast: CMsgGCBannedWordListResponse
    def __init__(self, broadcast: _Optional[_Union[CMsgGCBannedWordListResponse, _Mapping]] = ...) -> None: ...

class CMsgGCToGCBannedWordListUpdated(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class CMsgGCToGCBroadcastConsoleCommand(_message.Message):
    __slots__ = ["con_command"]
    CON_COMMAND_FIELD_NUMBER: _ClassVar[int]
    con_command: str
    def __init__(self, con_command: _Optional[str] = ...) -> None: ...

class CMsgGCToGCDirtyMultipleSDOCache(_message.Message):
    __slots__ = ["key_uint64", "sdo_type"]
    KEY_UINT64_FIELD_NUMBER: _ClassVar[int]
    SDO_TYPE_FIELD_NUMBER: _ClassVar[int]
    key_uint64: _containers.RepeatedScalarFieldContainer[int]
    sdo_type: int
    def __init__(self, sdo_type: _Optional[int] = ..., key_uint64: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCToGCDirtySDOCache(_message.Message):
    __slots__ = ["key_uint64", "sdo_type"]
    KEY_UINT64_FIELD_NUMBER: _ClassVar[int]
    SDO_TYPE_FIELD_NUMBER: _ClassVar[int]
    key_uint64: int
    sdo_type: int
    def __init__(self, sdo_type: _Optional[int] = ..., key_uint64: _Optional[int] = ...) -> None: ...

class CMsgGCToGCIsTrustedServer(_message.Message):
    __slots__ = ["steam_id"]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ...) -> None: ...

class CMsgGCToGCIsTrustedServerResponse(_message.Message):
    __slots__ = ["is_trusted"]
    IS_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    is_trusted: bool
    def __init__(self, is_trusted: bool = ...) -> None: ...

class CMsgGCToGCRequestPassportItemGrant(_message.Message):
    __slots__ = ["league_id", "reward_flag", "steam_id"]
    LEAGUE_ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FLAG_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    league_id: int
    reward_flag: int
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ..., league_id: _Optional[int] = ..., reward_flag: _Optional[int] = ...) -> None: ...

class CMsgGCToGCUpdateSQLKeyValue(_message.Message):
    __slots__ = ["key_name"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    def __init__(self, key_name: _Optional[str] = ...) -> None: ...

class CMsgGCToGCWebAPIAccountChanged(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgGameServerInfo(_message.Message):
    __slots__ = ["parent_relay_count", "relay_clients_connected", "relay_slots_max", "relayed_game_server_steam_id", "relays_connected", "server_game_time", "server_hibernation", "server_key", "server_loadavg", "server_port", "server_private_ip_addr", "server_public_ip_addr", "server_region", "server_relay_connected_steam_id", "server_tv_broadcast_time", "server_tv_port", "server_type", "tv_secret_code"]
    class ServerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    GAME: CMsgGameServerInfo.ServerType
    PARENT_RELAY_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROXY: CMsgGameServerInfo.ServerType
    RELAYED_GAME_SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    RELAYS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    RELAY_CLIENTS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    RELAY_SLOTS_MAX_FIELD_NUMBER: _ClassVar[int]
    SERVER_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_HIBERNATION_FIELD_NUMBER: _ClassVar[int]
    SERVER_KEY_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOADAVG_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    SERVER_PRIVATE_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_PUBLIC_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_REGION_FIELD_NUMBER: _ClassVar[int]
    SERVER_RELAY_CONNECTED_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TV_BROADCAST_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_TV_PORT_FIELD_NUMBER: _ClassVar[int]
    SERVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TV_SECRET_CODE_FIELD_NUMBER: _ClassVar[int]
    UNSPECIFIED: CMsgGameServerInfo.ServerType
    parent_relay_count: int
    relay_clients_connected: int
    relay_slots_max: int
    relayed_game_server_steam_id: int
    relays_connected: int
    server_game_time: float
    server_hibernation: bool
    server_key: str
    server_loadavg: float
    server_port: int
    server_private_ip_addr: int
    server_public_ip_addr: int
    server_region: int
    server_relay_connected_steam_id: int
    server_tv_broadcast_time: float
    server_tv_port: int
    server_type: CMsgGameServerInfo.ServerType
    tv_secret_code: int
    def __init__(self, server_public_ip_addr: _Optional[int] = ..., server_private_ip_addr: _Optional[int] = ..., server_port: _Optional[int] = ..., server_tv_port: _Optional[int] = ..., server_key: _Optional[str] = ..., server_hibernation: bool = ..., server_type: _Optional[_Union[CMsgGameServerInfo.ServerType, str]] = ..., server_region: _Optional[int] = ..., server_loadavg: _Optional[float] = ..., server_tv_broadcast_time: _Optional[float] = ..., server_game_time: _Optional[float] = ..., server_relay_connected_steam_id: _Optional[int] = ..., relay_slots_max: _Optional[int] = ..., relays_connected: _Optional[int] = ..., relay_clients_connected: _Optional[int] = ..., relayed_game_server_steam_id: _Optional[int] = ..., parent_relay_count: _Optional[int] = ..., tv_secret_code: _Optional[int] = ...) -> None: ...

class CMsgIncrementKillCountAttribute(_message.Message):
    __slots__ = ["amount", "event_type", "item_id", "killer_account_id", "victim_account_id"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    KILLER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    VICTIM_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    amount: int
    event_type: int
    item_id: int
    killer_account_id: int
    victim_account_id: int
    def __init__(self, killer_account_id: _Optional[int] = ..., victim_account_id: _Optional[int] = ..., item_id: _Optional[int] = ..., event_type: _Optional[int] = ..., amount: _Optional[int] = ...) -> None: ...

class CMsgInvitationCreated(_message.Message):
    __slots__ = ["group_id", "steam_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    steam_id: int
    def __init__(self, group_id: _Optional[int] = ..., steam_id: _Optional[int] = ...) -> None: ...

class CMsgInviteToParty(_message.Message):
    __slots__ = ["client_version", "steam_id", "team_invite"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_INVITE_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    steam_id: int
    team_invite: int
    def __init__(self, steam_id: _Optional[int] = ..., client_version: _Optional[int] = ..., team_invite: _Optional[int] = ...) -> None: ...

class CMsgItemAcknowledged__DEPRECATED(_message.Message):
    __slots__ = ["account_id", "def_index", "inventory", "item_id", "origin", "quality", "rarity"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    RARITY_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    def_index: int
    inventory: int
    item_id: int
    origin: int
    quality: int
    rarity: int
    def __init__(self, account_id: _Optional[int] = ..., inventory: _Optional[int] = ..., def_index: _Optional[int] = ..., quality: _Optional[int] = ..., rarity: _Optional[int] = ..., origin: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...

class CMsgKickFromParty(_message.Message):
    __slots__ = ["steam_id"]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ...) -> None: ...

class CMsgLANServerAvailable(_message.Message):
    __slots__ = ["lobby_id"]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    lobby_id: int
    def __init__(self, lobby_id: _Optional[int] = ...) -> None: ...

class CMsgLeaveParty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgModifyItemAttribute(_message.Message):
    __slots__ = ["attr_defidx", "attr_value", "item_id"]
    ATTR_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    ATTR_VALUE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    attr_defidx: int
    attr_value: int
    item_id: int
    def __init__(self, item_id: _Optional[int] = ..., attr_defidx: _Optional[int] = ..., attr_value: _Optional[int] = ...) -> None: ...

class CMsgPartyInviteResponse(_message.Message):
    __slots__ = ["accept", "client_version", "party_id", "team_invite"]
    ACCEPT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_INVITE_FIELD_NUMBER: _ClassVar[int]
    accept: bool
    client_version: int
    party_id: int
    team_invite: int
    def __init__(self, party_id: _Optional[int] = ..., accept: bool = ..., client_version: _Optional[int] = ..., team_invite: _Optional[int] = ...) -> None: ...

class CMsgReplayUploadedToYouTube(_message.Message):
    __slots__ = ["session_id", "youtube_account_name", "youtube_url"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_URL_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    youtube_account_name: str
    youtube_url: str
    def __init__(self, youtube_url: _Optional[str] = ..., youtube_account_name: _Optional[str] = ..., session_id: _Optional[int] = ...) -> None: ...

class CMsgReplicateConVars(_message.Message):
    __slots__ = ["convars"]
    CONVARS_FIELD_NUMBER: _ClassVar[int]
    convars: _containers.RepeatedCompositeFieldContainer[CMsgConVarValue]
    def __init__(self, convars: _Optional[_Iterable[_Union[CMsgConVarValue, _Mapping]]] = ...) -> None: ...

class CMsgRequestInventoryRefresh(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgSDONoMemcached(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgServerAvailable(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgSetItemPositions(_message.Message):
    __slots__ = ["item_positions"]
    class ItemPosition(_message.Message):
        __slots__ = ["item_id", "legacy_item_id", "position"]
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        LEGACY_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        item_id: int
        legacy_item_id: int
        position: int
        def __init__(self, legacy_item_id: _Optional[int] = ..., position: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...
    ITEM_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    item_positions: _containers.RepeatedCompositeFieldContainer[CMsgSetItemPositions.ItemPosition]
    def __init__(self, item_positions: _Optional[_Iterable[_Union[CMsgSetItemPositions.ItemPosition, _Mapping]]] = ...) -> None: ...

class CMsgSortItems(_message.Message):
    __slots__ = ["sort_type"]
    SORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    sort_type: int
    def __init__(self, sort_type: _Optional[int] = ...) -> None: ...

class CMsgStoreGetUserData(_message.Message):
    __slots__ = ["currency", "price_sheet_version"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PRICE_SHEET_VERSION_FIELD_NUMBER: _ClassVar[int]
    currency: int
    price_sheet_version: int
    def __init__(self, price_sheet_version: _Optional[int] = ..., currency: _Optional[int] = ...) -> None: ...

class CMsgStoreGetUserDataResponse(_message.Message):
    __slots__ = ["country_deprecated", "currency_deprecated", "price_sheet", "price_sheet_version", "result"]
    COUNTRY_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    PRICE_SHEET_FIELD_NUMBER: _ClassVar[int]
    PRICE_SHEET_VERSION_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    country_deprecated: str
    currency_deprecated: int
    price_sheet: bytes
    price_sheet_version: int
    result: int
    def __init__(self, result: _Optional[int] = ..., currency_deprecated: _Optional[int] = ..., country_deprecated: _Optional[str] = ..., price_sheet_version: _Optional[int] = ..., price_sheet: _Optional[bytes] = ...) -> None: ...

class CMsgSystemBroadcast(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class CMsgUpdateItemSchema(_message.Message):
    __slots__ = ["item_schema_version", "items_game", "items_game_url", "items_game_url_DEPRECATED2013"]
    ITEMS_GAME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_GAME_URL_DEPRECATED2013_FIELD_NUMBER: _ClassVar[int]
    ITEMS_GAME_URL_FIELD_NUMBER: _ClassVar[int]
    ITEM_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    item_schema_version: int
    items_game: bytes
    items_game_url: str
    items_game_url_DEPRECATED2013: str
    def __init__(self, items_game: _Optional[bytes] = ..., item_schema_version: _Optional[int] = ..., items_game_url_DEPRECATED2013: _Optional[str] = ..., items_game_url: _Optional[str] = ...) -> None: ...

class CMsgUseItem(_message.Message):
    __slots__ = ["duel__class_lock", "gift__potential_targets", "initiator_steam_id", "item_id", "target_steam_id"]
    DUEL__CLASS_LOCK_FIELD_NUMBER: _ClassVar[int]
    GIFT__POTENTIAL_TARGETS_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    duel__class_lock: int
    gift__potential_targets: _containers.RepeatedScalarFieldContainer[int]
    initiator_steam_id: int
    item_id: int
    target_steam_id: int
    def __init__(self, item_id: _Optional[int] = ..., target_steam_id: _Optional[int] = ..., gift__potential_targets: _Optional[_Iterable[int]] = ..., duel__class_lock: _Optional[int] = ..., initiator_steam_id: _Optional[int] = ...) -> None: ...

class CSOEconClaimCode(_message.Message):
    __slots__ = ["account_id", "code", "code_type", "time_acquired"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_ACQUIRED_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    code: str
    code_type: int
    time_acquired: int
    def __init__(self, account_id: _Optional[int] = ..., code_type: _Optional[int] = ..., time_acquired: _Optional[int] = ..., code: _Optional[str] = ...) -> None: ...

class CSOEconDefaultEquippedDefinitionInstanceClient(_message.Message):
    __slots__ = ["account_id", "class_id", "item_definition", "slot_id"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    class_id: int
    item_definition: int
    slot_id: int
    def __init__(self, account_id: _Optional[int] = ..., item_definition: _Optional[int] = ..., class_id: _Optional[int] = ..., slot_id: _Optional[int] = ...) -> None: ...

class CSOEconGameAccountClient(_message.Message):
    __slots__ = ["additional_backpack_slots", "bonus_xp_timestamp_refresh", "bonus_xp_usedflags", "elevated_state", "elevated_timestamp"]
    ADDITIONAL_BACKPACK_SLOTS_FIELD_NUMBER: _ClassVar[int]
    BONUS_XP_TIMESTAMP_REFRESH_FIELD_NUMBER: _ClassVar[int]
    BONUS_XP_USEDFLAGS_FIELD_NUMBER: _ClassVar[int]
    ELEVATED_STATE_FIELD_NUMBER: _ClassVar[int]
    ELEVATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    additional_backpack_slots: int
    bonus_xp_timestamp_refresh: int
    bonus_xp_usedflags: int
    elevated_state: int
    elevated_timestamp: int
    def __init__(self, additional_backpack_slots: _Optional[int] = ..., bonus_xp_timestamp_refresh: _Optional[int] = ..., bonus_xp_usedflags: _Optional[int] = ..., elevated_state: _Optional[int] = ..., elevated_timestamp: _Optional[int] = ...) -> None: ...

class CSOEconItem(_message.Message):
    __slots__ = ["account_id", "attribute", "custom_desc", "custom_name", "def_index", "equipped_state", "flags", "id", "in_use", "interior_item", "inventory", "level", "origin", "original_id", "quality", "quantity", "rarity", "style"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DESC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_NAME_FIELD_NUMBER: _ClassVar[int]
    DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
    EQUIPPED_STATE_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERIOR_ITEM_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    IN_USE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    RARITY_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    attribute: _containers.RepeatedCompositeFieldContainer[CSOEconItemAttribute]
    custom_desc: str
    custom_name: str
    def_index: int
    equipped_state: _containers.RepeatedCompositeFieldContainer[CSOEconItemEquipped]
    flags: int
    id: int
    in_use: bool
    interior_item: CSOEconItem
    inventory: int
    level: int
    origin: int
    original_id: int
    quality: int
    quantity: int
    rarity: int
    style: int
    def __init__(self, id: _Optional[int] = ..., account_id: _Optional[int] = ..., inventory: _Optional[int] = ..., def_index: _Optional[int] = ..., quantity: _Optional[int] = ..., level: _Optional[int] = ..., quality: _Optional[int] = ..., flags: _Optional[int] = ..., origin: _Optional[int] = ..., custom_name: _Optional[str] = ..., custom_desc: _Optional[str] = ..., attribute: _Optional[_Iterable[_Union[CSOEconItemAttribute, _Mapping]]] = ..., interior_item: _Optional[_Union[CSOEconItem, _Mapping]] = ..., in_use: bool = ..., style: _Optional[int] = ..., original_id: _Optional[int] = ..., equipped_state: _Optional[_Iterable[_Union[CSOEconItemEquipped, _Mapping]]] = ..., rarity: _Optional[int] = ...) -> None: ...

class CSOEconItemAttribute(_message.Message):
    __slots__ = ["def_index", "value", "value_bytes"]
    DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
    VALUE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    def_index: int
    value: int
    value_bytes: bytes
    def __init__(self, def_index: _Optional[int] = ..., value: _Optional[int] = ..., value_bytes: _Optional[bytes] = ...) -> None: ...

class CSOEconItemDropRateBonus(_message.Message):
    __slots__ = ["account_id", "bonus", "bonus_count", "def_index", "expiration_date", "item_id"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BONUS_COUNT_FIELD_NUMBER: _ClassVar[int]
    BONUS_FIELD_NUMBER: _ClassVar[int]
    DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    bonus: float
    bonus_count: int
    def_index: int
    expiration_date: int
    item_id: int
    def __init__(self, account_id: _Optional[int] = ..., expiration_date: _Optional[int] = ..., bonus: _Optional[float] = ..., bonus_count: _Optional[int] = ..., item_id: _Optional[int] = ..., def_index: _Optional[int] = ...) -> None: ...

class CSOEconItemEquipped(_message.Message):
    __slots__ = ["new_class", "new_slot"]
    NEW_CLASS_FIELD_NUMBER: _ClassVar[int]
    NEW_SLOT_FIELD_NUMBER: _ClassVar[int]
    new_class: int
    new_slot: int
    def __init__(self, new_class: _Optional[int] = ..., new_slot: _Optional[int] = ...) -> None: ...

class CSOEconItemEventTicket(_message.Message):
    __slots__ = ["account_id", "event_id", "item_id"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    event_id: int
    item_id: int
    def __init__(self, account_id: _Optional[int] = ..., event_id: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...

class CSOEconItemLeagueViewPass(_message.Message):
    __slots__ = ["account_id", "admin", "itemindex", "league_id"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    ITEMINDEX_FIELD_NUMBER: _ClassVar[int]
    LEAGUE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    admin: int
    itemindex: int
    league_id: int
    def __init__(self, account_id: _Optional[int] = ..., league_id: _Optional[int] = ..., admin: _Optional[int] = ..., itemindex: _Optional[int] = ...) -> None: ...

class CSOItemCriteria(_message.Message):
    __slots__ = ["conditions", "ignore_enabled_flag", "initial_inventory", "initial_quantity", "item_level", "item_level_set", "item_quality", "item_quality_set", "item_rarity", "item_rarity_set", "recent_only"]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    INITIAL_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    INITIAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_SET_FIELD_NUMBER: _ClassVar[int]
    ITEM_QUALITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_QUALITY_SET_FIELD_NUMBER: _ClassVar[int]
    ITEM_RARITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_RARITY_SET_FIELD_NUMBER: _ClassVar[int]
    RECENT_ONLY_FIELD_NUMBER: _ClassVar[int]
    conditions: _containers.RepeatedCompositeFieldContainer[CSOItemCriteriaCondition]
    ignore_enabled_flag: bool
    initial_inventory: int
    initial_quantity: int
    item_level: int
    item_level_set: bool
    item_quality: int
    item_quality_set: bool
    item_rarity: int
    item_rarity_set: bool
    recent_only: bool
    def __init__(self, item_level: _Optional[int] = ..., item_quality: _Optional[int] = ..., item_level_set: bool = ..., item_quality_set: bool = ..., initial_inventory: _Optional[int] = ..., initial_quantity: _Optional[int] = ..., ignore_enabled_flag: bool = ..., conditions: _Optional[_Iterable[_Union[CSOItemCriteriaCondition, _Mapping]]] = ..., item_rarity: _Optional[int] = ..., item_rarity_set: bool = ..., recent_only: bool = ...) -> None: ...

class CSOItemCriteriaCondition(_message.Message):
    __slots__ = ["field", "float_value", "op", "required", "string_value"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    field: str
    float_value: float
    op: int
    required: bool
    string_value: str
    def __init__(self, op: _Optional[int] = ..., field: _Optional[str] = ..., required: bool = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ...) -> None: ...

class CSOItemRecipe(_message.Message):
    __slots__ = ["class_usage_for_output", "def_index", "desc_inputs", "desc_outputs", "di_a", "di_b", "di_c", "do_a", "do_b", "do_c", "input_item_dupe_counts", "input_items_criteria", "n_a", "name", "output_items_criteria", "requires_all_same_class", "requires_all_same_slot", "set_for_output", "slot_usage_for_output"]
    CLASS_USAGE_FOR_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
    DESC_INPUTS_FIELD_NUMBER: _ClassVar[int]
    DESC_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    DI_A_FIELD_NUMBER: _ClassVar[int]
    DI_B_FIELD_NUMBER: _ClassVar[int]
    DI_C_FIELD_NUMBER: _ClassVar[int]
    DO_A_FIELD_NUMBER: _ClassVar[int]
    DO_B_FIELD_NUMBER: _ClassVar[int]
    DO_C_FIELD_NUMBER: _ClassVar[int]
    INPUT_ITEMS_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    INPUT_ITEM_DUPE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    N_A_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ITEMS_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_ALL_SAME_CLASS_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_ALL_SAME_SLOT_FIELD_NUMBER: _ClassVar[int]
    SET_FOR_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    SLOT_USAGE_FOR_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    class_usage_for_output: int
    def_index: int
    desc_inputs: str
    desc_outputs: str
    di_a: str
    di_b: str
    di_c: str
    do_a: str
    do_b: str
    do_c: str
    input_item_dupe_counts: _containers.RepeatedScalarFieldContainer[int]
    input_items_criteria: _containers.RepeatedCompositeFieldContainer[CSOItemCriteria]
    n_a: str
    name: str
    output_items_criteria: _containers.RepeatedCompositeFieldContainer[CSOItemCriteria]
    requires_all_same_class: bool
    requires_all_same_slot: bool
    set_for_output: int
    slot_usage_for_output: int
    def __init__(self, def_index: _Optional[int] = ..., name: _Optional[str] = ..., n_a: _Optional[str] = ..., desc_inputs: _Optional[str] = ..., desc_outputs: _Optional[str] = ..., di_a: _Optional[str] = ..., di_b: _Optional[str] = ..., di_c: _Optional[str] = ..., do_a: _Optional[str] = ..., do_b: _Optional[str] = ..., do_c: _Optional[str] = ..., requires_all_same_class: bool = ..., requires_all_same_slot: bool = ..., class_usage_for_output: _Optional[int] = ..., slot_usage_for_output: _Optional[int] = ..., set_for_output: _Optional[int] = ..., input_items_criteria: _Optional[_Iterable[_Union[CSOItemCriteria, _Mapping]]] = ..., output_items_criteria: _Optional[_Iterable[_Union[CSOItemCriteria, _Mapping]]] = ..., input_item_dupe_counts: _Optional[_Iterable[int]] = ...) -> None: ...

class CSOLobbyInvite(_message.Message):
    __slots__ = ["group_id", "sender_id", "sender_name"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    sender_id: int
    sender_name: str
    def __init__(self, group_id: _Optional[int] = ..., sender_id: _Optional[int] = ..., sender_name: _Optional[str] = ...) -> None: ...

class CSOPartyInvite(_message.Message):
    __slots__ = ["group_id", "sender_id", "sender_name"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    sender_id: int
    sender_name: str
    def __init__(self, group_id: _Optional[int] = ..., sender_id: _Optional[int] = ..., sender_name: _Optional[str] = ...) -> None: ...

class EGCBaseMsg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EGCBaseProtoObjectTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class GC_BannedWordType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
