import steammessages_pb2 as _steammessages_pb2
import engine_gcmessages_pb2 as _engine_gcmessages_pb2
import gcsdk_gcmessages_pb2 as _gcsdk_gcmessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
k_EClientReportingVersion_BetaVersion: EClientReportingVersion
k_EClientReportingVersion_OldVersion: EClientReportingVersion
k_EClientReportingVersion_SupportsTrustedMode: EClientReportingVersion
k_ECsgoSteamUserStat_MatchWinsCompetitive: ECsgoSteamUserStat
k_ECsgoSteamUserStat_SurvivedDangerZone: ECsgoSteamUserStat
k_ECsgoSteamUserStat_XpEarnedGames: ECsgoSteamUserStat
k_EInitSystemResult_Existing: EInitSystemResult
k_EInitSystemResult_FailedInit: EInitSystemResult
k_EInitSystemResult_FailedOpen: EInitSystemResult
k_EInitSystemResult_Invalid: EInitSystemResult
k_EInitSystemResult_Max: EInitSystemResult
k_EInitSystemResult_Mismatch: EInitSystemResult
k_EInitSystemResult_None: EInitSystemResult
k_EInitSystemResult_NotFound: EInitSystemResult
k_EInitSystemResult_Success: EInitSystemResult
k_EMsgGCCStrike15_ClientDeepStats: ECsgoGCMsg
k_EMsgGCCStrike15_StartAgreementSessionInGame: ECsgoGCMsg
k_EMsgGCCStrike15_v2_AccountPrivacySettings: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Account_RequestCoPlays: ECsgoGCMsg
k_EMsgGCCStrike15_v2_AcknowledgePenalty: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Base: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCStreamUnlock: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCTextMsg: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientAccountBalance: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientAuthKeyCode: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientCommendPlayer: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientCommendPlayerQuery: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientCommendPlayerQueryResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientGCRankUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientLogonFatalError: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPartyJoinRelay: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPartyWarning: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPerfReport: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPlayerDecalSign: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPollState: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRedeemMissionReward: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientReportPlayer: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientReportResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientReportServer: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientReportValidation: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestJoinFriendData: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestJoinServerData: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestNewMission: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestOffers: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestPlayersProfile: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestSouvenir: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestWatchInfoFriends2: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientSubmitSurveyVote: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientToGCRequestElevate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientToGCRequestTicket: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientVarValueNotificationInfo: ECsgoGCMsg
k_EMsgGCCStrike15_v2_DraftSummary: ECsgoGCMsg
k_EMsgGCCStrike15_v2_FantasyRequestClientData: ECsgoGCMsg
k_EMsgGCCStrike15_v2_FantasyUpdateClientData: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientGlobalStats: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientInitSystem: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientInitSystem_Response: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientRefuseSecureMode: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientRequestValidation: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientTextMsg: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientTournamentInfo: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ServerReservationUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GCToClientSteamdatagramTicket: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GetEventFavorites_Request: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GetEventFavorites_Response: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GiftsLeaderboardRequest: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GiftsLeaderboardResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GlobalChat: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GlobalChat_Subscribe: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GlobalChat_Unsubscribe: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GotvSyncPacket: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchEndRewardDropsNotification: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchEndRunRewardDrops: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchList: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestFullGameInfo: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestLiveGameForUser: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestRecentUserGames: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestTournamentGames: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestTournamentPredictions: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListTournamentOperatorMgmt: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListUploadTournamentPredictions: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingClient2GCHello: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingClient2ServerPing: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ClientHello: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ClientReserve: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGCOperationalStats: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingServerReservationResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingStart: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingStop: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Party_Invite: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Party_Register: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Party_Search: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Party_Unregister: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PlayerOverwatchCaseStatus: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PlayersProfile: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PrivateQueues: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Server2GCClientValidate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ServerNotificationForUserPenalty: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ServerVarValueNotificationInfo: ECsgoGCMsg
k_EMsgGCCStrike15_v2_SetEventFavorite: ECsgoGCMsg
k_EMsgGCCStrike15_v2_SetMyActivityInfo: ECsgoGCMsg
k_EMsgGCCStrike15_v2_WatchInfoUsers: ECsgoGCMsg
k_EMsgGC_GlobalGame_Play: ECsgoGCMsg
k_EMsgGC_GlobalGame_Subscribe: ECsgoGCMsg
k_EMsgGC_GlobalGame_Unsubscribe: ECsgoGCMsg

class AccountActivity(_message.Message):
    __slots__ = ["activity", "map", "matchid", "mode"]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    activity: int
    map: int
    matchid: int
    mode: int
    def __init__(self, activity: _Optional[int] = ..., mode: _Optional[int] = ..., map: _Optional[int] = ..., matchid: _Optional[int] = ...) -> None: ...

class CClientHeaderOverwatchEvidence(_message.Message):
    __slots__ = ["accountid", "caseid"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    caseid: int
    def __init__(self, accountid: _Optional[int] = ..., caseid: _Optional[int] = ...) -> None: ...

class CDataGCCStrike15_v2_MatchInfo(_message.Message):
    __slots__ = ["matchid", "matchtime", "roundstats_legacy", "roundstatsall", "watchablematchinfo"]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    MATCHTIME_FIELD_NUMBER: _ClassVar[int]
    ROUNDSTATSALL_FIELD_NUMBER: _ClassVar[int]
    ROUNDSTATS_LEGACY_FIELD_NUMBER: _ClassVar[int]
    WATCHABLEMATCHINFO_FIELD_NUMBER: _ClassVar[int]
    matchid: int
    matchtime: int
    roundstats_legacy: CMsgGCCStrike15_v2_MatchmakingServerRoundStats
    roundstatsall: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_MatchmakingServerRoundStats]
    watchablematchinfo: WatchableMatchInfo
    def __init__(self, matchid: _Optional[int] = ..., matchtime: _Optional[int] = ..., watchablematchinfo: _Optional[_Union[WatchableMatchInfo, _Mapping]] = ..., roundstats_legacy: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingServerRoundStats, _Mapping]] = ..., roundstatsall: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_MatchmakingServerRoundStats, _Mapping]]] = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentGroup(_message.Message):
    __slots__ = ["desc", "groupid", "name", "pickableteams", "picklockuntiltime", "picks", "picks__deprecated", "points_per_pick", "stage_ids", "teams"]
    class Picks(_message.Message):
        __slots__ = ["pickids"]
        PICKIDS_FIELD_NUMBER: _ClassVar[int]
        pickids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, pickids: _Optional[_Iterable[int]] = ...) -> None: ...
    DESC_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PICKABLETEAMS_FIELD_NUMBER: _ClassVar[int]
    PICKLOCKUNTILTIME_FIELD_NUMBER: _ClassVar[int]
    PICKS_FIELD_NUMBER: _ClassVar[int]
    PICKS__DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    POINTS_PER_PICK_FIELD_NUMBER: _ClassVar[int]
    STAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    desc: str
    groupid: int
    name: str
    pickableteams: int
    picklockuntiltime: int
    picks: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentGroup.Picks]
    picks__deprecated: int
    points_per_pick: int
    stage_ids: _containers.RepeatedScalarFieldContainer[int]
    teams: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentGroupTeam]
    def __init__(self, groupid: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., picks__deprecated: _Optional[int] = ..., teams: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentGroupTeam, _Mapping]]] = ..., stage_ids: _Optional[_Iterable[int]] = ..., picklockuntiltime: _Optional[int] = ..., pickableteams: _Optional[int] = ..., points_per_pick: _Optional[int] = ..., picks: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentGroup.Picks, _Mapping]]] = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentGroupTeam(_message.Message):
    __slots__ = ["correctpick", "score", "team_id"]
    CORRECTPICK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    correctpick: bool
    score: int
    team_id: int
    def __init__(self, team_id: _Optional[int] = ..., score: _Optional[int] = ..., correctpick: bool = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentInfo(_message.Message):
    __slots__ = ["sections", "tournament_event", "tournament_teams"]
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_TEAMS_FIELD_NUMBER: _ClassVar[int]
    sections: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentSection]
    tournament_event: TournamentEvent
    tournament_teams: _containers.RepeatedCompositeFieldContainer[TournamentTeam]
    def __init__(self, sections: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentSection, _Mapping]]] = ..., tournament_event: _Optional[_Union[TournamentEvent, _Mapping]] = ..., tournament_teams: _Optional[_Iterable[_Union[TournamentTeam, _Mapping]]] = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentMatchDraft(_message.Message):
    __slots__ = ["drafts", "event_id", "event_stage_id", "maps_count", "maps_current", "team_id_0", "team_id_1", "team_id_pickn", "team_id_start", "team_id_veto1"]
    class Entry(_message.Message):
        __slots__ = ["mapid", "team_id_ct"]
        MAPID_FIELD_NUMBER: _ClassVar[int]
        TEAM_ID_CT_FIELD_NUMBER: _ClassVar[int]
        mapid: int
        team_id_ct: int
        def __init__(self, mapid: _Optional[int] = ..., team_id_ct: _Optional[int] = ...) -> None: ...
    DRAFTS_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MAPS_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAPS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_0_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_1_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_PICKN_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_START_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_VETO1_FIELD_NUMBER: _ClassVar[int]
    drafts: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentMatchDraft.Entry]
    event_id: int
    event_stage_id: int
    maps_count: int
    maps_current: int
    team_id_0: int
    team_id_1: int
    team_id_pickn: int
    team_id_start: int
    team_id_veto1: int
    def __init__(self, event_id: _Optional[int] = ..., event_stage_id: _Optional[int] = ..., team_id_0: _Optional[int] = ..., team_id_1: _Optional[int] = ..., maps_count: _Optional[int] = ..., maps_current: _Optional[int] = ..., team_id_start: _Optional[int] = ..., team_id_veto1: _Optional[int] = ..., team_id_pickn: _Optional[int] = ..., drafts: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentMatchDraft.Entry, _Mapping]]] = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentSection(_message.Message):
    __slots__ = ["desc", "groups", "name", "sectionid"]
    DESC_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECTIONID_FIELD_NUMBER: _ClassVar[int]
    desc: str
    groups: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentGroup]
    name: str
    sectionid: int
    def __init__(self, sectionid: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., groups: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentGroup, _Mapping]]] = ...) -> None: ...

class CEconItemPreviewDataBlock(_message.Message):
    __slots__ = ["accountid", "customname", "defindex", "dropreason", "entindex", "inventory", "itemid", "killeaterscoretype", "killeatervalue", "musicindex", "origin", "paintindex", "paintseed", "paintwear", "quality", "questid", "rarity", "stickers"]
    class Sticker(_message.Message):
        __slots__ = ["rotation", "scale", "slot", "sticker_id", "tint_id", "wear"]
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        SLOT_FIELD_NUMBER: _ClassVar[int]
        STICKER_ID_FIELD_NUMBER: _ClassVar[int]
        TINT_ID_FIELD_NUMBER: _ClassVar[int]
        WEAR_FIELD_NUMBER: _ClassVar[int]
        rotation: float
        scale: float
        slot: int
        sticker_id: int
        tint_id: int
        wear: float
        def __init__(self, slot: _Optional[int] = ..., sticker_id: _Optional[int] = ..., wear: _Optional[float] = ..., scale: _Optional[float] = ..., rotation: _Optional[float] = ..., tint_id: _Optional[int] = ...) -> None: ...
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMNAME_FIELD_NUMBER: _ClassVar[int]
    DEFINDEX_FIELD_NUMBER: _ClassVar[int]
    DROPREASON_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    KILLEATERSCORETYPE_FIELD_NUMBER: _ClassVar[int]
    KILLEATERVALUE_FIELD_NUMBER: _ClassVar[int]
    MUSICINDEX_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PAINTINDEX_FIELD_NUMBER: _ClassVar[int]
    PAINTSEED_FIELD_NUMBER: _ClassVar[int]
    PAINTWEAR_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    QUESTID_FIELD_NUMBER: _ClassVar[int]
    RARITY_FIELD_NUMBER: _ClassVar[int]
    STICKERS_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    customname: str
    defindex: int
    dropreason: int
    entindex: int
    inventory: int
    itemid: int
    killeaterscoretype: int
    killeatervalue: int
    musicindex: int
    origin: int
    paintindex: int
    paintseed: int
    paintwear: int
    quality: int
    questid: int
    rarity: int
    stickers: _containers.RepeatedCompositeFieldContainer[CEconItemPreviewDataBlock.Sticker]
    def __init__(self, accountid: _Optional[int] = ..., itemid: _Optional[int] = ..., defindex: _Optional[int] = ..., paintindex: _Optional[int] = ..., rarity: _Optional[int] = ..., quality: _Optional[int] = ..., paintwear: _Optional[int] = ..., paintseed: _Optional[int] = ..., killeaterscoretype: _Optional[int] = ..., killeatervalue: _Optional[int] = ..., customname: _Optional[str] = ..., stickers: _Optional[_Iterable[_Union[CEconItemPreviewDataBlock.Sticker, _Mapping]]] = ..., inventory: _Optional[int] = ..., origin: _Optional[int] = ..., questid: _Optional[int] = ..., dropreason: _Optional[int] = ..., musicindex: _Optional[int] = ..., entindex: _Optional[int] = ...) -> None: ...

class CMsgCStrike15Welcome(_message.Message):
    __slots__ = ["gscookieid", "last_ip_address", "last_time_played", "store_item_hash", "time_first_played", "timeplayedconsecutively", "uniqueid"]
    GSCOOKIEID_FIELD_NUMBER: _ClassVar[int]
    LAST_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LAST_TIME_PLAYED_FIELD_NUMBER: _ClassVar[int]
    STORE_ITEM_HASH_FIELD_NUMBER: _ClassVar[int]
    TIMEPLAYEDCONSECUTIVELY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIRST_PLAYED_FIELD_NUMBER: _ClassVar[int]
    UNIQUEID_FIELD_NUMBER: _ClassVar[int]
    gscookieid: int
    last_ip_address: int
    last_time_played: int
    store_item_hash: int
    time_first_played: int
    timeplayedconsecutively: int
    uniqueid: int
    def __init__(self, store_item_hash: _Optional[int] = ..., timeplayedconsecutively: _Optional[int] = ..., time_first_played: _Optional[int] = ..., last_time_played: _Optional[int] = ..., last_ip_address: _Optional[int] = ..., gscookieid: _Optional[int] = ..., uniqueid: _Optional[int] = ...) -> None: ...

class CMsgCsgoSteamUserStatChange(_message.Message):
    __slots__ = ["absolute", "delta", "ecsgosteamuserstat"]
    ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    ECSGOSTEAMUSERSTAT_FIELD_NUMBER: _ClassVar[int]
    absolute: bool
    delta: int
    ecsgosteamuserstat: int
    def __init__(self, ecsgosteamuserstat: _Optional[int] = ..., delta: _Optional[int] = ..., absolute: bool = ...) -> None: ...

class CMsgGCCStrike15_ClientDeepStats(_message.Message):
    __slots__ = ["account_id", "matches", "range"]
    class DeepStatsMatch(_message.Message):
        __slots__ = ["events", "player"]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_FIELD_NUMBER: _ClassVar[int]
        events: _containers.RepeatedCompositeFieldContainer[DeepPlayerMatchEvent]
        player: DeepPlayerStatsEntry
        def __init__(self, player: _Optional[_Union[DeepPlayerStatsEntry, _Mapping]] = ..., events: _Optional[_Iterable[_Union[DeepPlayerMatchEvent, _Mapping]]] = ...) -> None: ...
    class DeepStatsRange(_message.Message):
        __slots__ = ["begin", "end", "frozen"]
        BEGIN_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        FROZEN_FIELD_NUMBER: _ClassVar[int]
        begin: int
        end: int
        frozen: bool
        def __init__(self, begin: _Optional[int] = ..., end: _Optional[int] = ..., frozen: bool = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    matches: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_ClientDeepStats.DeepStatsMatch]
    range: CMsgGCCStrike15_ClientDeepStats.DeepStatsRange
    def __init__(self, account_id: _Optional[int] = ..., range: _Optional[_Union[CMsgGCCStrike15_ClientDeepStats.DeepStatsRange, _Mapping]] = ..., matches: _Optional[_Iterable[_Union[CMsgGCCStrike15_ClientDeepStats.DeepStatsMatch, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_GotvSyncPacket(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _engine_gcmessages_pb2.CEngineGotvSyncPacket
    def __init__(self, data: _Optional[_Union[_engine_gcmessages_pb2.CEngineGotvSyncPacket, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_AccountPrivacySettings(_message.Message):
    __slots__ = ["settings"]
    class Setting(_message.Message):
        __slots__ = ["setting_type", "setting_value"]
        SETTING_TYPE_FIELD_NUMBER: _ClassVar[int]
        SETTING_VALUE_FIELD_NUMBER: _ClassVar[int]
        setting_type: int
        setting_value: int
        def __init__(self, setting_type: _Optional[int] = ..., setting_value: _Optional[int] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_AccountPrivacySettings.Setting]
    def __init__(self, settings: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_AccountPrivacySettings.Setting, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Account_RequestCoPlays(_message.Message):
    __slots__ = ["players", "servertime"]
    class Player(_message.Message):
        __slots__ = ["accountid", "online", "rtcoplay"]
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        ONLINE_FIELD_NUMBER: _ClassVar[int]
        RTCOPLAY_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        online: bool
        rtcoplay: int
        def __init__(self, accountid: _Optional[int] = ..., rtcoplay: _Optional[int] = ..., online: bool = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    SERVERTIME_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Account_RequestCoPlays.Player]
    servertime: int
    def __init__(self, players: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Account_RequestCoPlays.Player, _Mapping]]] = ..., servertime: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_AcknowledgePenalty(_message.Message):
    __slots__ = ["acknowledged"]
    ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    acknowledged: int
    def __init__(self, acknowledged: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest(_message.Message):
    __slots__ = ["param_a", "param_d", "param_m", "param_s"]
    PARAM_A_FIELD_NUMBER: _ClassVar[int]
    PARAM_D_FIELD_NUMBER: _ClassVar[int]
    PARAM_M_FIELD_NUMBER: _ClassVar[int]
    PARAM_S_FIELD_NUMBER: _ClassVar[int]
    param_a: int
    param_d: int
    param_m: int
    param_s: int
    def __init__(self, param_s: _Optional[int] = ..., param_a: _Optional[int] = ..., param_d: _Optional[int] = ..., param_m: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse(_message.Message):
    __slots__ = ["iteminfo"]
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    iteminfo: CEconItemPreviewDataBlock
    def __init__(self, iteminfo: _Optional[_Union[CEconItemPreviewDataBlock, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin(_message.Message):
    __slots__ = ["defindex", "hours", "prestigetime", "upgradeid"]
    DEFINDEX_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    PRESTIGETIME_FIELD_NUMBER: _ClassVar[int]
    UPGRADEID_FIELD_NUMBER: _ClassVar[int]
    defindex: int
    hours: int
    prestigetime: int
    upgradeid: int
    def __init__(self, defindex: _Optional[int] = ..., upgradeid: _Optional[int] = ..., hours: _Optional[int] = ..., prestigetime: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCStreamUnlock(_message.Message):
    __slots__ = ["os", "ticket"]
    OS_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    os: int
    ticket: int
    def __init__(self, ticket: _Optional[int] = ..., os: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCTextMsg(_message.Message):
    __slots__ = ["args", "id"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    args: _containers.RepeatedScalarFieldContainer[bytes]
    id: int
    def __init__(self, id: _Optional[int] = ..., args: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientAccountBalance(_message.Message):
    __slots__ = ["amount", "url"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    amount: int
    url: str
    def __init__(self, amount: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientAuthKeyCode(_message.Message):
    __slots__ = ["code", "eventid"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    code: str
    eventid: int
    def __init__(self, eventid: _Optional[int] = ..., code: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientCommendPlayer(_message.Message):
    __slots__ = ["account_id", "commendation", "match_id", "tokens"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENDATION_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    commendation: PlayerCommendationInfo
    match_id: int
    tokens: int
    def __init__(self, account_id: _Optional[int] = ..., match_id: _Optional[int] = ..., commendation: _Optional[_Union[PlayerCommendationInfo, _Mapping]] = ..., tokens: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientGCRankUpdate(_message.Message):
    __slots__ = ["rankings"]
    RANKINGS_FIELD_NUMBER: _ClassVar[int]
    rankings: _containers.RepeatedCompositeFieldContainer[PlayerRankingInfo]
    def __init__(self, rankings: _Optional[_Iterable[_Union[PlayerRankingInfo, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientLogonFatalError(_message.Message):
    __slots__ = ["country", "errorcode", "message"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    country: str
    errorcode: int
    message: str
    def __init__(self, errorcode: _Optional[int] = ..., message: _Optional[str] = ..., country: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPartyJoinRelay(_message.Message):
    __slots__ = ["accountid", "lobbyid"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    lobbyid: int
    def __init__(self, accountid: _Optional[int] = ..., lobbyid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPartyWarning(_message.Message):
    __slots__ = ["entries"]
    class Entry(_message.Message):
        __slots__ = ["accountid", "warntype"]
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        WARNTYPE_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        warntype: int
        def __init__(self, accountid: _Optional[int] = ..., warntype: _Optional[int] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_ClientPartyWarning.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_ClientPartyWarning.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPerfReport(_message.Message):
    __slots__ = ["entries"]
    class Entry(_message.Message):
        __slots__ = ["actual", "length", "perfcounter", "reference", "sourceid", "status"]
        ACTUAL_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        PERFCOUNTER_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        SOURCEID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        actual: bytes
        length: int
        perfcounter: int
        reference: bytes
        sourceid: int
        status: int
        def __init__(self, perfcounter: _Optional[int] = ..., length: _Optional[int] = ..., reference: _Optional[bytes] = ..., actual: _Optional[bytes] = ..., sourceid: _Optional[int] = ..., status: _Optional[int] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_ClientPerfReport.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_ClientPerfReport.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPlayerDecalSign(_message.Message):
    __slots__ = ["data", "itemid"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    data: PlayerDecalDigitalSignature
    itemid: int
    def __init__(self, data: _Optional[_Union[PlayerDecalDigitalSignature, _Mapping]] = ..., itemid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPollState(_message.Message):
    __slots__ = ["names", "pollid", "values"]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    POLLID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    pollid: int
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, pollid: _Optional[int] = ..., names: _Optional[_Iterable[str]] = ..., values: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientReportPlayer(_message.Message):
    __slots__ = ["account_id", "match_id", "report_from_demo", "rpt_aimbot", "rpt_speedhack", "rpt_teamharm", "rpt_textabuse", "rpt_voiceabuse", "rpt_wallhack"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_FROM_DEMO_FIELD_NUMBER: _ClassVar[int]
    RPT_AIMBOT_FIELD_NUMBER: _ClassVar[int]
    RPT_SPEEDHACK_FIELD_NUMBER: _ClassVar[int]
    RPT_TEAMHARM_FIELD_NUMBER: _ClassVar[int]
    RPT_TEXTABUSE_FIELD_NUMBER: _ClassVar[int]
    RPT_VOICEABUSE_FIELD_NUMBER: _ClassVar[int]
    RPT_WALLHACK_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    match_id: int
    report_from_demo: bool
    rpt_aimbot: int
    rpt_speedhack: int
    rpt_teamharm: int
    rpt_textabuse: int
    rpt_voiceabuse: int
    rpt_wallhack: int
    def __init__(self, account_id: _Optional[int] = ..., rpt_aimbot: _Optional[int] = ..., rpt_wallhack: _Optional[int] = ..., rpt_speedhack: _Optional[int] = ..., rpt_teamharm: _Optional[int] = ..., rpt_textabuse: _Optional[int] = ..., rpt_voiceabuse: _Optional[int] = ..., match_id: _Optional[int] = ..., report_from_demo: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientReportResponse(_message.Message):
    __slots__ = ["account_id", "confirmation_id", "response_result", "response_type", "server_ip", "tokens"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_RESULT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    confirmation_id: int
    response_result: int
    response_type: int
    server_ip: int
    tokens: int
    def __init__(self, confirmation_id: _Optional[int] = ..., account_id: _Optional[int] = ..., server_ip: _Optional[int] = ..., response_type: _Optional[int] = ..., response_result: _Optional[int] = ..., tokens: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientReportServer(_message.Message):
    __slots__ = ["match_id", "rpt_abusivemodels", "rpt_badmotd", "rpt_inventoryabuse", "rpt_listingabuse", "rpt_poorperf"]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    RPT_ABUSIVEMODELS_FIELD_NUMBER: _ClassVar[int]
    RPT_BADMOTD_FIELD_NUMBER: _ClassVar[int]
    RPT_INVENTORYABUSE_FIELD_NUMBER: _ClassVar[int]
    RPT_LISTINGABUSE_FIELD_NUMBER: _ClassVar[int]
    RPT_POORPERF_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    rpt_abusivemodels: int
    rpt_badmotd: int
    rpt_inventoryabuse: int
    rpt_listingabuse: int
    rpt_poorperf: int
    def __init__(self, rpt_poorperf: _Optional[int] = ..., rpt_abusivemodels: _Optional[int] = ..., rpt_badmotd: _Optional[int] = ..., rpt_listingabuse: _Optional[int] = ..., rpt_inventoryabuse: _Optional[int] = ..., match_id: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientReportValidation(_message.Message):
    __slots__ = ["client_time", "clientreportversion", "command_line", "count_completed", "count_pending", "diagnostic1", "diagnostic2", "diagnostic3", "diagnostic4", "diagnostic5", "diagnostics", "file_report", "internal_error", "last_launch_data", "osversion", "process_id", "report_count", "status_id", "total_files", "trust_time"]
    CLIENTREPORTVERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_LINE_FIELD_NUMBER: _ClassVar[int]
    COUNT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    COUNT_PENDING_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC1_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC2_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC3_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC4_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC5_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    FILE_REPORT_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_LAUNCH_DATA_FIELD_NUMBER: _ClassVar[int]
    OSVERSION_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    TRUST_TIME_FIELD_NUMBER: _ClassVar[int]
    client_time: int
    clientreportversion: int
    command_line: str
    count_completed: int
    count_pending: int
    diagnostic1: int
    diagnostic2: int
    diagnostic3: int
    diagnostic4: int
    diagnostic5: int
    diagnostics: _containers.RepeatedCompositeFieldContainer[CVDiagnostic]
    file_report: str
    internal_error: int
    last_launch_data: str
    osversion: int
    process_id: int
    report_count: int
    status_id: int
    total_files: int
    trust_time: int
    def __init__(self, file_report: _Optional[str] = ..., command_line: _Optional[str] = ..., total_files: _Optional[int] = ..., internal_error: _Optional[int] = ..., trust_time: _Optional[int] = ..., count_pending: _Optional[int] = ..., count_completed: _Optional[int] = ..., process_id: _Optional[int] = ..., osversion: _Optional[int] = ..., clientreportversion: _Optional[int] = ..., status_id: _Optional[int] = ..., diagnostic1: _Optional[int] = ..., diagnostic2: _Optional[int] = ..., diagnostic3: _Optional[int] = ..., last_launch_data: _Optional[str] = ..., report_count: _Optional[int] = ..., client_time: _Optional[int] = ..., diagnostic4: _Optional[int] = ..., diagnostic5: _Optional[int] = ..., diagnostics: _Optional[_Iterable[_Union[CVDiagnostic, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestJoinFriendData(_message.Message):
    __slots__ = ["account_id", "errormsg", "join_ipp", "join_token", "res", "version"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    JOIN_IPP_FIELD_NUMBER: _ClassVar[int]
    JOIN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    errormsg: str
    join_ipp: int
    join_token: int
    res: CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    version: int
    def __init__(self, version: _Optional[int] = ..., account_id: _Optional[int] = ..., join_token: _Optional[int] = ..., join_ipp: _Optional[int] = ..., res: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve, _Mapping]] = ..., errormsg: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestJoinServerData(_message.Message):
    __slots__ = ["account_id", "errormsg", "res", "server_ip", "server_port", "serverid", "version"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    errormsg: str
    res: CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    server_ip: int
    server_port: int
    serverid: int
    version: int
    def __init__(self, version: _Optional[int] = ..., account_id: _Optional[int] = ..., serverid: _Optional[int] = ..., server_ip: _Optional[int] = ..., server_port: _Optional[int] = ..., res: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve, _Mapping]] = ..., errormsg: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestOffers(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestPlayersProfile(_message.Message):
    __slots__ = ["account_id", "account_ids__deprecated", "request_id__deprecated", "request_level"]
    ACCOUNT_IDS__DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID__DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    account_ids__deprecated: _containers.RepeatedScalarFieldContainer[int]
    request_id__deprecated: int
    request_level: int
    def __init__(self, request_id__deprecated: _Optional[int] = ..., account_ids__deprecated: _Optional[_Iterable[int]] = ..., account_id: _Optional[int] = ..., request_level: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestSouvenir(_message.Message):
    __slots__ = ["eventid", "itemid", "matchid"]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    itemid: int
    matchid: int
    def __init__(self, itemid: _Optional[int] = ..., matchid: _Optional[int] = ..., eventid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestWatchInfoFriends(_message.Message):
    __slots__ = ["account_ids", "client_launcher", "data_center_pings", "matchid", "request_id", "serverid"]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    DATA_CENTER_PINGS_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    client_launcher: int
    data_center_pings: _containers.RepeatedCompositeFieldContainer[DataCenterPing]
    matchid: int
    request_id: int
    serverid: int
    def __init__(self, request_id: _Optional[int] = ..., account_ids: _Optional[_Iterable[int]] = ..., serverid: _Optional[int] = ..., matchid: _Optional[int] = ..., client_launcher: _Optional[int] = ..., data_center_pings: _Optional[_Iterable[_Union[DataCenterPing, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientSubmitSurveyVote(_message.Message):
    __slots__ = ["survey_id", "vote"]
    SURVEY_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    survey_id: int
    vote: int
    def __init__(self, survey_id: _Optional[int] = ..., vote: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientToGCChat(_message.Message):
    __slots__ = ["match_id", "text"]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    text: str
    def __init__(self, match_id: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientToGCRequestElevate(_message.Message):
    __slots__ = ["stage"]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    stage: int
    def __init__(self, stage: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientToGCRequestTicket(_message.Message):
    __slots__ = ["authorized_public_ip", "authorized_steam_id", "gameserver_sdr_routing", "gameserver_steam_id"]
    AUTHORIZED_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    GAMESERVER_SDR_ROUTING_FIELD_NUMBER: _ClassVar[int]
    GAMESERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    authorized_public_ip: int
    authorized_steam_id: int
    gameserver_sdr_routing: str
    gameserver_steam_id: int
    def __init__(self, authorized_steam_id: _Optional[int] = ..., authorized_public_ip: _Optional[int] = ..., gameserver_steam_id: _Optional[int] = ..., gameserver_sdr_routing: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientVarValueNotificationInfo(_message.Message):
    __slots__ = ["choked_blocks", "server_addr", "server_port", "value_int", "value_name"]
    CHOKED_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    VALUE_INT_FIELD_NUMBER: _ClassVar[int]
    VALUE_NAME_FIELD_NUMBER: _ClassVar[int]
    choked_blocks: _containers.RepeatedScalarFieldContainer[str]
    server_addr: int
    server_port: int
    value_int: int
    value_name: str
    def __init__(self, value_name: _Optional[str] = ..., value_int: _Optional[int] = ..., server_addr: _Optional[int] = ..., server_port: _Optional[int] = ..., choked_blocks: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Fantasy(_message.Message):
    __slots__ = ["event_id", "teams"]
    class FantasySlot(_message.Message):
        __slots__ = ["itemid", "pick", "type"]
        ITEMID_FIELD_NUMBER: _ClassVar[int]
        PICK_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        itemid: int
        pick: int
        type: int
        def __init__(self, type: _Optional[int] = ..., pick: _Optional[int] = ..., itemid: _Optional[int] = ...) -> None: ...
    class FantasyTeam(_message.Message):
        __slots__ = ["sectionid", "slots"]
        SECTIONID_FIELD_NUMBER: _ClassVar[int]
        SLOTS_FIELD_NUMBER: _ClassVar[int]
        sectionid: int
        slots: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Fantasy.FantasySlot]
        def __init__(self, sectionid: _Optional[int] = ..., slots: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Fantasy.FantasySlot, _Mapping]]] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    teams: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Fantasy.FantasyTeam]
    def __init__(self, event_id: _Optional[int] = ..., teams: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Fantasy.FantasyTeam, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientInitSystem(_message.Message):
    __slots__ = ["cookie", "key_data", "load", "load_system", "manifest", "name", "outputname", "sha_hash", "system_package"]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    LOAD_FIELD_NUMBER: _ClassVar[int]
    LOAD_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUTNAME_FIELD_NUMBER: _ClassVar[int]
    SHA_HASH_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    cookie: int
    key_data: bytes
    load: bool
    load_system: bool
    manifest: str
    name: str
    outputname: str
    sha_hash: bytes
    system_package: bytes
    def __init__(self, load: bool = ..., name: _Optional[str] = ..., outputname: _Optional[str] = ..., key_data: _Optional[bytes] = ..., sha_hash: _Optional[bytes] = ..., cookie: _Optional[int] = ..., manifest: _Optional[str] = ..., system_package: _Optional[bytes] = ..., load_system: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientInitSystem_Response(_message.Message):
    __slots__ = ["aux_system1", "aux_system2", "diagnostic", "einit_result", "error_code1", "error_code2", "handle", "response", "sha_hash", "success"]
    AUX_SYSTEM1_FIELD_NUMBER: _ClassVar[int]
    AUX_SYSTEM2_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_FIELD_NUMBER: _ClassVar[int]
    EINIT_RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE1_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE2_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SHA_HASH_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    aux_system1: int
    aux_system2: int
    diagnostic: str
    einit_result: EInitSystemResult
    error_code1: int
    error_code2: int
    handle: int
    response: int
    sha_hash: bytes
    success: bool
    def __init__(self, success: bool = ..., diagnostic: _Optional[str] = ..., sha_hash: _Optional[bytes] = ..., response: _Optional[int] = ..., error_code1: _Optional[int] = ..., error_code2: _Optional[int] = ..., handle: _Optional[int] = ..., einit_result: _Optional[_Union[EInitSystemResult, str]] = ..., aux_system1: _Optional[int] = ..., aux_system2: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientRefuseSecureMode(_message.Message):
    __slots__ = ["file_report", "files_prevented_trusted", "kick_user", "offer_insecure_mode", "offer_secure_mode", "show_trusted_ui", "show_unsigned_ui", "show_warning_not_trusted", "show_warning_not_trusted_2"]
    FILES_PREVENTED_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    FILE_REPORT_FIELD_NUMBER: _ClassVar[int]
    KICK_USER_FIELD_NUMBER: _ClassVar[int]
    OFFER_INSECURE_MODE_FIELD_NUMBER: _ClassVar[int]
    OFFER_SECURE_MODE_FIELD_NUMBER: _ClassVar[int]
    SHOW_TRUSTED_UI_FIELD_NUMBER: _ClassVar[int]
    SHOW_UNSIGNED_UI_FIELD_NUMBER: _ClassVar[int]
    SHOW_WARNING_NOT_TRUSTED_2_FIELD_NUMBER: _ClassVar[int]
    SHOW_WARNING_NOT_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    file_report: str
    files_prevented_trusted: str
    kick_user: bool
    offer_insecure_mode: bool
    offer_secure_mode: bool
    show_trusted_ui: bool
    show_unsigned_ui: bool
    show_warning_not_trusted: bool
    show_warning_not_trusted_2: bool
    def __init__(self, file_report: _Optional[str] = ..., offer_insecure_mode: bool = ..., offer_secure_mode: bool = ..., show_unsigned_ui: bool = ..., kick_user: bool = ..., show_trusted_ui: bool = ..., show_warning_not_trusted: bool = ..., show_warning_not_trusted_2: bool = ..., files_prevented_trusted: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientRequestValidation(_message.Message):
    __slots__ = ["full_report", "module"]
    FULL_REPORT_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    full_report: bool
    module: str
    def __init__(self, full_report: bool = ..., module: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientTextMsg(_message.Message):
    __slots__ = ["id", "payload", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    payload: bytes
    type: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientTournamentInfo(_message.Message):
    __slots__ = ["eventid", "game_type", "stageid", "teamids"]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    STAGEID_FIELD_NUMBER: _ClassVar[int]
    TEAMIDS_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    game_type: int
    stageid: int
    teamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, eventid: _Optional[int] = ..., stageid: _Optional[int] = ..., game_type: _Optional[int] = ..., teamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ServerReservationUpdate(_message.Message):
    __slots__ = ["viewers_external_steam", "viewers_external_total"]
    VIEWERS_EXTERNAL_STEAM_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_EXTERNAL_TOTAL_FIELD_NUMBER: _ClassVar[int]
    viewers_external_steam: int
    viewers_external_total: int
    def __init__(self, viewers_external_total: _Optional[int] = ..., viewers_external_steam: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_GCToClientChat(_message.Message):
    __slots__ = ["account_id", "text"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    text: str
    def __init__(self, account_id: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_GetEventFavorites_Request(_message.Message):
    __slots__ = ["all_events"]
    ALL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    all_events: bool
    def __init__(self, all_events: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_GetEventFavorites_Response(_message.Message):
    __slots__ = ["all_events", "json_favorites", "json_featured"]
    ALL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    JSON_FAVORITES_FIELD_NUMBER: _ClassVar[int]
    JSON_FEATURED_FIELD_NUMBER: _ClassVar[int]
    all_events: bool
    json_favorites: str
    json_featured: str
    def __init__(self, all_events: bool = ..., json_favorites: _Optional[str] = ..., json_featured: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_GiftsLeaderboardRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgGCCStrike15_v2_GiftsLeaderboardResponse(_message.Message):
    __slots__ = ["entries", "servertime", "time_period_seconds", "total_gifts_given", "total_givers"]
    class GiftLeaderboardEntry(_message.Message):
        __slots__ = ["accountid", "gifts"]
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        GIFTS_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        gifts: int
        def __init__(self, accountid: _Optional[int] = ..., gifts: _Optional[int] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SERVERTIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GIFTS_GIVEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GIVERS_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_GiftsLeaderboardResponse.GiftLeaderboardEntry]
    servertime: int
    time_period_seconds: int
    total_gifts_given: int
    total_givers: int
    def __init__(self, servertime: _Optional[int] = ..., time_period_seconds: _Optional[int] = ..., total_gifts_given: _Optional[int] = ..., total_givers: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_GiftsLeaderboardResponse.GiftLeaderboardEntry, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchEndRewardDropsNotification(_message.Message):
    __slots__ = ["iteminfo"]
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    iteminfo: CEconItemPreviewDataBlock
    def __init__(self, iteminfo: _Optional[_Union[CEconItemPreviewDataBlock, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchEndRunRewardDrops(_message.Message):
    __slots__ = ["match_end_quest_data", "serverinfo"]
    MATCH_END_QUEST_DATA_FIELD_NUMBER: _ClassVar[int]
    SERVERINFO_FIELD_NUMBER: _ClassVar[int]
    match_end_quest_data: CMsgGC_ServerQuestUpdateData
    serverinfo: CMsgGCCStrike15_v2_MatchmakingServerReservationResponse
    def __init__(self, serverinfo: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingServerReservationResponse, _Mapping]] = ..., match_end_quest_data: _Optional[_Union[CMsgGC_ServerQuestUpdateData, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchList(_message.Message):
    __slots__ = ["accountid", "matches", "msgrequestid", "servertime", "streams", "tournamentinfo"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    MSGREQUESTID_FIELD_NUMBER: _ClassVar[int]
    SERVERTIME_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENTINFO_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    matches: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_MatchInfo]
    msgrequestid: int
    servertime: int
    streams: _containers.RepeatedCompositeFieldContainer[TournamentTeam]
    tournamentinfo: CDataGCCStrike15_v2_TournamentInfo
    def __init__(self, msgrequestid: _Optional[int] = ..., accountid: _Optional[int] = ..., servertime: _Optional[int] = ..., matches: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_MatchInfo, _Mapping]]] = ..., streams: _Optional[_Iterable[_Union[TournamentTeam, _Mapping]]] = ..., tournamentinfo: _Optional[_Union[CDataGCCStrike15_v2_TournamentInfo, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestFullGameInfo(_message.Message):
    __slots__ = ["matchid", "outcomeid", "token"]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    OUTCOMEID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    matchid: int
    outcomeid: int
    token: int
    def __init__(self, matchid: _Optional[int] = ..., outcomeid: _Optional[int] = ..., token: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestLiveGameForUser(_message.Message):
    __slots__ = ["accountid"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    def __init__(self, accountid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestRecentUserGames(_message.Message):
    __slots__ = ["accountid"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    def __init__(self, accountid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestTournamentGames(_message.Message):
    __slots__ = ["eventid"]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    def __init__(self, eventid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListTournamentOperatorMgmt(_message.Message):
    __slots__ = ["eventid", "matches"]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    matches: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_MatchInfo]
    def __init__(self, eventid: _Optional[int] = ..., matches: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_MatchInfo, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingClient2GCHello(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingClient2ServerPing(_message.Message):
    __slots__ = ["data_center_pings", "final_batch", "gameserverpings", "max_ping", "offset_index", "test_token"]
    DATA_CENTER_PINGS_FIELD_NUMBER: _ClassVar[int]
    FINAL_BATCH_FIELD_NUMBER: _ClassVar[int]
    GAMESERVERPINGS_FIELD_NUMBER: _ClassVar[int]
    MAX_PING_FIELD_NUMBER: _ClassVar[int]
    OFFSET_INDEX_FIELD_NUMBER: _ClassVar[int]
    TEST_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_center_pings: _containers.RepeatedCompositeFieldContainer[DataCenterPing]
    final_batch: int
    gameserverpings: _containers.RepeatedCompositeFieldContainer[GameServerPing]
    max_ping: int
    offset_index: int
    test_token: int
    def __init__(self, gameserverpings: _Optional[_Iterable[_Union[GameServerPing, _Mapping]]] = ..., offset_index: _Optional[int] = ..., final_batch: _Optional[int] = ..., data_center_pings: _Optional[_Iterable[_Union[DataCenterPing, _Mapping]]] = ..., max_ping: _Optional[int] = ..., test_token: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon(_message.Message):
    __slots__ = ["abandoned_match", "account_id", "penalty_reason", "penalty_seconds"]
    ABANDONED_MATCH_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PENALTY_REASON_FIELD_NUMBER: _ClassVar[int]
    PENALTY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    abandoned_match: CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    account_id: int
    penalty_reason: int
    penalty_seconds: int
    def __init__(self, account_id: _Optional[int] = ..., abandoned_match: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve, _Mapping]] = ..., penalty_seconds: _Optional[int] = ..., penalty_reason: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ClientHello(_message.Message):
    __slots__ = ["account_id", "activity", "commendation", "global_stats", "medals", "my_current_event", "my_current_event_stages", "my_current_event_teams", "my_current_team", "ongoingmatch", "penalty_reason", "penalty_seconds", "player_cur_xp", "player_level", "player_xp_bonus_flags", "ranking", "rankings", "survey_vote", "vac_banned"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    COMMENDATION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_STATS_FIELD_NUMBER: _ClassVar[int]
    MEDALS_FIELD_NUMBER: _ClassVar[int]
    MY_CURRENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    MY_CURRENT_EVENT_STAGES_FIELD_NUMBER: _ClassVar[int]
    MY_CURRENT_EVENT_TEAMS_FIELD_NUMBER: _ClassVar[int]
    MY_CURRENT_TEAM_FIELD_NUMBER: _ClassVar[int]
    ONGOINGMATCH_FIELD_NUMBER: _ClassVar[int]
    PENALTY_REASON_FIELD_NUMBER: _ClassVar[int]
    PENALTY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_CUR_XP_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_XP_BONUS_FLAGS_FIELD_NUMBER: _ClassVar[int]
    RANKINGS_FIELD_NUMBER: _ClassVar[int]
    RANKING_FIELD_NUMBER: _ClassVar[int]
    SURVEY_VOTE_FIELD_NUMBER: _ClassVar[int]
    VAC_BANNED_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    activity: AccountActivity
    commendation: PlayerCommendationInfo
    global_stats: GlobalStatistics
    medals: PlayerMedalsInfo
    my_current_event: TournamentEvent
    my_current_event_stages: _containers.RepeatedCompositeFieldContainer[TournamentEvent]
    my_current_event_teams: _containers.RepeatedCompositeFieldContainer[TournamentTeam]
    my_current_team: TournamentTeam
    ongoingmatch: CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    penalty_reason: int
    penalty_seconds: int
    player_cur_xp: int
    player_level: int
    player_xp_bonus_flags: int
    ranking: PlayerRankingInfo
    rankings: _containers.RepeatedCompositeFieldContainer[PlayerRankingInfo]
    survey_vote: int
    vac_banned: int
    def __init__(self, account_id: _Optional[int] = ..., ongoingmatch: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve, _Mapping]] = ..., global_stats: _Optional[_Union[GlobalStatistics, _Mapping]] = ..., penalty_seconds: _Optional[int] = ..., penalty_reason: _Optional[int] = ..., vac_banned: _Optional[int] = ..., ranking: _Optional[_Union[PlayerRankingInfo, _Mapping]] = ..., commendation: _Optional[_Union[PlayerCommendationInfo, _Mapping]] = ..., medals: _Optional[_Union[PlayerMedalsInfo, _Mapping]] = ..., my_current_event: _Optional[_Union[TournamentEvent, _Mapping]] = ..., my_current_event_teams: _Optional[_Iterable[_Union[TournamentTeam, _Mapping]]] = ..., my_current_team: _Optional[_Union[TournamentTeam, _Mapping]] = ..., my_current_event_stages: _Optional[_Iterable[_Union[TournamentEvent, _Mapping]]] = ..., survey_vote: _Optional[int] = ..., activity: _Optional[_Union[AccountActivity, _Mapping]] = ..., player_level: _Optional[int] = ..., player_cur_xp: _Optional[int] = ..., player_xp_bonus_flags: _Optional[int] = ..., rankings: _Optional[_Iterable[_Union[PlayerRankingInfo, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve(_message.Message):
    __slots__ = ["direct_udp_ip", "direct_udp_port", "map", "reservation", "reservationid", "server_address", "serverid"]
    DIRECT_UDP_IP_FIELD_NUMBER: _ClassVar[int]
    DIRECT_UDP_PORT_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    RESERVATIONID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    direct_udp_ip: int
    direct_udp_port: int
    map: str
    reservation: CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve
    reservationid: int
    server_address: str
    serverid: int
    def __init__(self, serverid: _Optional[int] = ..., direct_udp_ip: _Optional[int] = ..., direct_udp_port: _Optional[int] = ..., reservationid: _Optional[int] = ..., reservation: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve, _Mapping]] = ..., map: _Optional[str] = ..., server_address: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate(_message.Message):
    __slots__ = ["error", "failping_account_id_sessions", "failready_account_id_sessions", "global_stats", "insecure_account_id_sessions", "insufficientlevel_sessions", "launcher_mismatch_sessions", "matchmaking", "notes", "ongoingmatch_account_id_sessions", "penalty_account_id_sessions", "penalty_account_id_sessions_green", "server_ipaddress_mask", "vacbanned_account_id_sessions", "vsncheck_account_id_sessions", "waiting_account_id_sessions"]
    class Note(_message.Message):
        __slots__ = ["distance", "region_id", "region_r", "type"]
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_R_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        distance: float
        region_id: int
        region_r: float
        type: int
        def __init__(self, type: _Optional[int] = ..., region_id: _Optional[int] = ..., region_r: _Optional[float] = ..., distance: _Optional[float] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FAILPING_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    FAILREADY_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_STATS_FIELD_NUMBER: _ClassVar[int]
    INSECURE_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    INSUFFICIENTLEVEL_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_MISMATCH_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    MATCHMAKING_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    ONGOINGMATCH_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    PENALTY_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    PENALTY_ACCOUNT_ID_SESSIONS_GREEN_FIELD_NUMBER: _ClassVar[int]
    SERVER_IPADDRESS_MASK_FIELD_NUMBER: _ClassVar[int]
    VACBANNED_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    VSNCHECK_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    WAITING_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    error: str
    failping_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    failready_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    global_stats: GlobalStatistics
    insecure_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    insufficientlevel_sessions: _containers.RepeatedScalarFieldContainer[int]
    launcher_mismatch_sessions: _containers.RepeatedScalarFieldContainer[int]
    matchmaking: int
    notes: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate.Note]
    ongoingmatch_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    penalty_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    penalty_account_id_sessions_green: _containers.RepeatedScalarFieldContainer[int]
    server_ipaddress_mask: IpAddressMask
    vacbanned_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    vsncheck_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    waiting_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, matchmaking: _Optional[int] = ..., waiting_account_id_sessions: _Optional[_Iterable[int]] = ..., error: _Optional[str] = ..., ongoingmatch_account_id_sessions: _Optional[_Iterable[int]] = ..., global_stats: _Optional[_Union[GlobalStatistics, _Mapping]] = ..., failping_account_id_sessions: _Optional[_Iterable[int]] = ..., penalty_account_id_sessions: _Optional[_Iterable[int]] = ..., failready_account_id_sessions: _Optional[_Iterable[int]] = ..., vacbanned_account_id_sessions: _Optional[_Iterable[int]] = ..., server_ipaddress_mask: _Optional[_Union[IpAddressMask, _Mapping]] = ..., notes: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate.Note, _Mapping]]] = ..., penalty_account_id_sessions_green: _Optional[_Iterable[int]] = ..., insufficientlevel_sessions: _Optional[_Iterable[int]] = ..., vsncheck_account_id_sessions: _Optional[_Iterable[int]] = ..., launcher_mismatch_sessions: _Optional[_Iterable[int]] = ..., insecure_account_id_sessions: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm(_message.Message):
    __slots__ = ["exchange", "stamp", "token"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    STAMP_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    exchange: int
    stamp: int
    token: int
    def __init__(self, token: _Optional[int] = ..., stamp: _Optional[int] = ..., exchange: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve(_message.Message):
    __slots__ = ["account_ids", "encryption_key", "encryption_key_pub", "flags", "game_type", "match_id", "party_ids", "pre_match_data", "rankings", "rtime32_event_start", "server_version", "tournament_casters_account_ids", "tournament_event", "tournament_teams", "tv_control", "tv_master_steamid", "tv_relay_steamid", "whitelist"]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_PUB_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    PARTY_IDS_FIELD_NUMBER: _ClassVar[int]
    PRE_MATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    RANKINGS_FIELD_NUMBER: _ClassVar[int]
    RTIME32_EVENT_START_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_CASTERS_ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_TEAMS_FIELD_NUMBER: _ClassVar[int]
    TV_CONTROL_FIELD_NUMBER: _ClassVar[int]
    TV_MASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_STEAMID_FIELD_NUMBER: _ClassVar[int]
    WHITELIST_FIELD_NUMBER: _ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    encryption_key: int
    encryption_key_pub: int
    flags: int
    game_type: int
    match_id: int
    party_ids: _containers.RepeatedScalarFieldContainer[int]
    pre_match_data: CPreMatchInfoData
    rankings: _containers.RepeatedCompositeFieldContainer[PlayerRankingInfo]
    rtime32_event_start: int
    server_version: int
    tournament_casters_account_ids: _containers.RepeatedScalarFieldContainer[int]
    tournament_event: TournamentEvent
    tournament_teams: _containers.RepeatedCompositeFieldContainer[TournamentTeam]
    tv_control: int
    tv_master_steamid: int
    tv_relay_steamid: int
    whitelist: _containers.RepeatedCompositeFieldContainer[IpAddressMask]
    def __init__(self, account_ids: _Optional[_Iterable[int]] = ..., game_type: _Optional[int] = ..., match_id: _Optional[int] = ..., server_version: _Optional[int] = ..., flags: _Optional[int] = ..., rankings: _Optional[_Iterable[_Union[PlayerRankingInfo, _Mapping]]] = ..., encryption_key: _Optional[int] = ..., encryption_key_pub: _Optional[int] = ..., party_ids: _Optional[_Iterable[int]] = ..., whitelist: _Optional[_Iterable[_Union[IpAddressMask, _Mapping]]] = ..., tv_master_steamid: _Optional[int] = ..., tournament_event: _Optional[_Union[TournamentEvent, _Mapping]] = ..., tournament_teams: _Optional[_Iterable[_Union[TournamentTeam, _Mapping]]] = ..., tournament_casters_account_ids: _Optional[_Iterable[int]] = ..., tv_relay_steamid: _Optional[int] = ..., pre_match_data: _Optional[_Union[CPreMatchInfoData, _Mapping]] = ..., rtime32_event_start: _Optional[int] = ..., tv_control: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGCOperationalStats(_message.Message):
    __slots__ = ["namekeys", "packetid", "packets"]
    NAMEKEYS_FIELD_NUMBER: _ClassVar[int]
    PACKETID_FIELD_NUMBER: _ClassVar[int]
    PACKETS_FIELD_NUMBER: _ClassVar[int]
    namekeys: _containers.RepeatedCompositeFieldContainer[OperationalStatisticDescription]
    packetid: int
    packets: _containers.RepeatedCompositeFieldContainer[OperationalStatisticsPacket]
    def __init__(self, packetid: _Optional[int] = ..., namekeys: _Optional[_Iterable[_Union[OperationalStatisticDescription, _Mapping]]] = ..., packets: _Optional[_Iterable[_Union[OperationalStatisticsPacket, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate(_message.Message):
    __slots__ = ["main_post_url"]
    MAIN_POST_URL_FIELD_NUMBER: _ClassVar[int]
    main_post_url: str
    def __init__(self, main_post_url: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingServerReservationResponse(_message.Message):
    __slots__ = ["flags", "gc_reservation_sent", "idle_player_accounts", "legacy_steamdatagram_port", "map", "reservation", "reservationid", "reward_drop_list", "reward_item_attr_def_idx", "reward_item_attr_reward_idx", "reward_item_attr_value", "reward_player_accounts", "server_version", "steamdatagram_routing", "test_token", "tournament_tag", "tv_info"]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    GC_RESERVATION_SENT_FIELD_NUMBER: _ClassVar[int]
    IDLE_PLAYER_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    LEGACY_STEAMDATAGRAM_PORT_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    RESERVATIONID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    REWARD_DROP_LIST_FIELD_NUMBER: _ClassVar[int]
    REWARD_ITEM_ATTR_DEF_IDX_FIELD_NUMBER: _ClassVar[int]
    REWARD_ITEM_ATTR_REWARD_IDX_FIELD_NUMBER: _ClassVar[int]
    REWARD_ITEM_ATTR_VALUE_FIELD_NUMBER: _ClassVar[int]
    REWARD_PLAYER_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    STEAMDATAGRAM_ROUTING_FIELD_NUMBER: _ClassVar[int]
    TEST_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_TAG_FIELD_NUMBER: _ClassVar[int]
    TV_INFO_FIELD_NUMBER: _ClassVar[int]
    flags: int
    gc_reservation_sent: int
    idle_player_accounts: _containers.RepeatedScalarFieldContainer[int]
    legacy_steamdatagram_port: int
    map: str
    reservation: CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve
    reservationid: int
    reward_drop_list: int
    reward_item_attr_def_idx: int
    reward_item_attr_reward_idx: int
    reward_item_attr_value: int
    reward_player_accounts: _containers.RepeatedScalarFieldContainer[int]
    server_version: int
    steamdatagram_routing: int
    test_token: int
    tournament_tag: str
    tv_info: ServerHltvInfo
    def __init__(self, reservationid: _Optional[int] = ..., reservation: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve, _Mapping]] = ..., map: _Optional[str] = ..., gc_reservation_sent: _Optional[int] = ..., server_version: _Optional[int] = ..., tv_info: _Optional[_Union[ServerHltvInfo, _Mapping]] = ..., reward_player_accounts: _Optional[_Iterable[int]] = ..., idle_player_accounts: _Optional[_Iterable[int]] = ..., reward_item_attr_def_idx: _Optional[int] = ..., reward_item_attr_value: _Optional[int] = ..., reward_item_attr_reward_idx: _Optional[int] = ..., reward_drop_list: _Optional[int] = ..., tournament_tag: _Optional[str] = ..., legacy_steamdatagram_port: _Optional[int] = ..., steamdatagram_routing: _Optional[int] = ..., test_token: _Optional[int] = ..., flags: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingServerRoundStats(_message.Message):
    __slots__ = ["assists", "b_switched_teams", "confirm", "deaths", "drop_info", "enemy_2ks", "enemy_3ks", "enemy_4ks", "enemy_5ks", "enemy_headshots", "enemy_kills", "enemy_kills_agg", "kills", "map", "match_duration", "match_result", "max_rounds", "mvps", "pings", "player_spawned", "reservation", "reservation_stage", "reservationid", "round", "round_result", "scores", "spectators_count", "spectators_count_lnk", "spectators_count_tv", "team_scores", "team_spawn_count"]
    class DropInfo(_message.Message):
        __slots__ = ["account_mvp"]
        ACCOUNT_MVP_FIELD_NUMBER: _ClassVar[int]
        account_mvp: int
        def __init__(self, account_mvp: _Optional[int] = ...) -> None: ...
    ASSISTS_FIELD_NUMBER: _ClassVar[int]
    B_SWITCHED_TEAMS_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    DEATHS_FIELD_NUMBER: _ClassVar[int]
    DROP_INFO_FIELD_NUMBER: _ClassVar[int]
    ENEMY_2KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_3KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_4KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_5KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_HEADSHOTS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_KILLS_AGG_FIELD_NUMBER: _ClassVar[int]
    ENEMY_KILLS_FIELD_NUMBER: _ClassVar[int]
    KILLS_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    MATCH_DURATION_FIELD_NUMBER: _ClassVar[int]
    MATCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    MAX_ROUNDS_FIELD_NUMBER: _ClassVar[int]
    MVPS_FIELD_NUMBER: _ClassVar[int]
    PINGS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SPAWNED_FIELD_NUMBER: _ClassVar[int]
    RESERVATIONID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_STAGE_FIELD_NUMBER: _ClassVar[int]
    ROUND_FIELD_NUMBER: _ClassVar[int]
    ROUND_RESULT_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_COUNT_LNK_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_COUNT_TV_FIELD_NUMBER: _ClassVar[int]
    TEAM_SCORES_FIELD_NUMBER: _ClassVar[int]
    TEAM_SPAWN_COUNT_FIELD_NUMBER: _ClassVar[int]
    assists: _containers.RepeatedScalarFieldContainer[int]
    b_switched_teams: bool
    confirm: CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm
    deaths: _containers.RepeatedScalarFieldContainer[int]
    drop_info: CMsgGCCStrike15_v2_MatchmakingServerRoundStats.DropInfo
    enemy_2ks: _containers.RepeatedScalarFieldContainer[int]
    enemy_3ks: _containers.RepeatedScalarFieldContainer[int]
    enemy_4ks: _containers.RepeatedScalarFieldContainer[int]
    enemy_5ks: _containers.RepeatedScalarFieldContainer[int]
    enemy_headshots: _containers.RepeatedScalarFieldContainer[int]
    enemy_kills: _containers.RepeatedScalarFieldContainer[int]
    enemy_kills_agg: _containers.RepeatedScalarFieldContainer[int]
    kills: _containers.RepeatedScalarFieldContainer[int]
    map: str
    match_duration: int
    match_result: int
    max_rounds: int
    mvps: _containers.RepeatedScalarFieldContainer[int]
    pings: _containers.RepeatedScalarFieldContainer[int]
    player_spawned: _containers.RepeatedScalarFieldContainer[int]
    reservation: CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve
    reservation_stage: int
    reservationid: int
    round: int
    round_result: int
    scores: _containers.RepeatedScalarFieldContainer[int]
    spectators_count: int
    spectators_count_lnk: int
    spectators_count_tv: int
    team_scores: _containers.RepeatedScalarFieldContainer[int]
    team_spawn_count: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, reservationid: _Optional[int] = ..., reservation: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve, _Mapping]] = ..., map: _Optional[str] = ..., round: _Optional[int] = ..., kills: _Optional[_Iterable[int]] = ..., assists: _Optional[_Iterable[int]] = ..., deaths: _Optional[_Iterable[int]] = ..., scores: _Optional[_Iterable[int]] = ..., pings: _Optional[_Iterable[int]] = ..., round_result: _Optional[int] = ..., match_result: _Optional[int] = ..., team_scores: _Optional[_Iterable[int]] = ..., confirm: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm, _Mapping]] = ..., reservation_stage: _Optional[int] = ..., match_duration: _Optional[int] = ..., enemy_kills: _Optional[_Iterable[int]] = ..., enemy_headshots: _Optional[_Iterable[int]] = ..., enemy_3ks: _Optional[_Iterable[int]] = ..., enemy_4ks: _Optional[_Iterable[int]] = ..., enemy_5ks: _Optional[_Iterable[int]] = ..., mvps: _Optional[_Iterable[int]] = ..., spectators_count: _Optional[int] = ..., spectators_count_tv: _Optional[int] = ..., spectators_count_lnk: _Optional[int] = ..., enemy_kills_agg: _Optional[_Iterable[int]] = ..., drop_info: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingServerRoundStats.DropInfo, _Mapping]] = ..., b_switched_teams: bool = ..., enemy_2ks: _Optional[_Iterable[int]] = ..., player_spawned: _Optional[_Iterable[int]] = ..., team_spawn_count: _Optional[_Iterable[int]] = ..., max_rounds: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingStart(_message.Message):
    __slots__ = ["account_ids", "client_version", "game_type", "lobby_id", "prime_only", "ticket_data", "tournament_match", "tv_control"]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIME_ONLY_FIELD_NUMBER: _ClassVar[int]
    TICKET_DATA_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_MATCH_FIELD_NUMBER: _ClassVar[int]
    TV_CONTROL_FIELD_NUMBER: _ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    client_version: int
    game_type: int
    lobby_id: int
    prime_only: bool
    ticket_data: str
    tournament_match: TournamentMatchSetup
    tv_control: int
    def __init__(self, account_ids: _Optional[_Iterable[int]] = ..., game_type: _Optional[int] = ..., ticket_data: _Optional[str] = ..., client_version: _Optional[int] = ..., tournament_match: _Optional[_Union[TournamentMatchSetup, _Mapping]] = ..., prime_only: bool = ..., tv_control: _Optional[int] = ..., lobby_id: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingStop(_message.Message):
    __slots__ = ["abandon"]
    ABANDON_FIELD_NUMBER: _ClassVar[int]
    abandon: int
    def __init__(self, abandon: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Party_Invite(_message.Message):
    __slots__ = ["accountid", "lobbyid"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    lobbyid: int
    def __init__(self, accountid: _Optional[int] = ..., lobbyid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Party_Register(_message.Message):
    __slots__ = ["apr", "ark", "game_type", "grp", "id", "launcher", "nby", "slots", "ver"]
    APR_FIELD_NUMBER: _ClassVar[int]
    ARK_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    NBY_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    VER_FIELD_NUMBER: _ClassVar[int]
    apr: int
    ark: int
    game_type: int
    grp: int
    id: int
    launcher: int
    nby: int
    slots: int
    ver: int
    def __init__(self, id: _Optional[int] = ..., ver: _Optional[int] = ..., apr: _Optional[int] = ..., ark: _Optional[int] = ..., nby: _Optional[int] = ..., grp: _Optional[int] = ..., slots: _Optional[int] = ..., launcher: _Optional[int] = ..., game_type: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Party_Search(_message.Message):
    __slots__ = ["apr", "ark", "game_type", "grps", "launcher", "ver"]
    APR_FIELD_NUMBER: _ClassVar[int]
    ARK_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRPS_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    VER_FIELD_NUMBER: _ClassVar[int]
    apr: int
    ark: int
    game_type: int
    grps: _containers.RepeatedScalarFieldContainer[int]
    launcher: int
    ver: int
    def __init__(self, ver: _Optional[int] = ..., apr: _Optional[int] = ..., ark: _Optional[int] = ..., grps: _Optional[_Iterable[int]] = ..., launcher: _Optional[int] = ..., game_type: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Party_SearchResults(_message.Message):
    __slots__ = ["entries"]
    class Entry(_message.Message):
        __slots__ = ["accountid", "apr", "ark", "game_type", "grp", "id", "loc"]
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        APR_FIELD_NUMBER: _ClassVar[int]
        ARK_FIELD_NUMBER: _ClassVar[int]
        GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
        GRP_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOC_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        apr: int
        ark: int
        game_type: int
        grp: int
        id: int
        loc: int
        def __init__(self, id: _Optional[int] = ..., grp: _Optional[int] = ..., game_type: _Optional[int] = ..., apr: _Optional[int] = ..., ark: _Optional[int] = ..., loc: _Optional[int] = ..., accountid: _Optional[int] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Party_SearchResults.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Party_SearchResults.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment(_message.Message):
    __slots__ = ["caseid", "caseurl", "fractionid", "fractionrounds", "numrounds", "reason", "streakconvictions", "suspectid", "throttleseconds", "timestamp", "verdict"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    CASEURL_FIELD_NUMBER: _ClassVar[int]
    FRACTIONID_FIELD_NUMBER: _ClassVar[int]
    FRACTIONROUNDS_FIELD_NUMBER: _ClassVar[int]
    NUMROUNDS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    STREAKCONVICTIONS_FIELD_NUMBER: _ClassVar[int]
    SUSPECTID_FIELD_NUMBER: _ClassVar[int]
    THROTTLESECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    caseid: int
    caseurl: str
    fractionid: int
    fractionrounds: int
    numrounds: int
    reason: int
    streakconvictions: int
    suspectid: int
    throttleseconds: int
    timestamp: int
    verdict: int
    def __init__(self, caseid: _Optional[int] = ..., caseurl: _Optional[str] = ..., verdict: _Optional[int] = ..., timestamp: _Optional[int] = ..., throttleseconds: _Optional[int] = ..., suspectid: _Optional[int] = ..., fractionid: _Optional[int] = ..., numrounds: _Optional[int] = ..., fractionrounds: _Optional[int] = ..., streakconvictions: _Optional[int] = ..., reason: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_PlayerOverwatchCaseStatus(_message.Message):
    __slots__ = ["caseid", "statusid"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    STATUSID_FIELD_NUMBER: _ClassVar[int]
    caseid: int
    statusid: int
    def __init__(self, caseid: _Optional[int] = ..., statusid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate(_message.Message):
    __slots__ = ["caseid", "fractionid", "reason", "rpt_aimbot", "rpt_speedhack", "rpt_teamharm", "rpt_wallhack", "suspectid"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    FRACTIONID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RPT_AIMBOT_FIELD_NUMBER: _ClassVar[int]
    RPT_SPEEDHACK_FIELD_NUMBER: _ClassVar[int]
    RPT_TEAMHARM_FIELD_NUMBER: _ClassVar[int]
    RPT_WALLHACK_FIELD_NUMBER: _ClassVar[int]
    SUSPECTID_FIELD_NUMBER: _ClassVar[int]
    caseid: int
    fractionid: int
    reason: int
    rpt_aimbot: int
    rpt_speedhack: int
    rpt_teamharm: int
    rpt_wallhack: int
    suspectid: int
    def __init__(self, caseid: _Optional[int] = ..., suspectid: _Optional[int] = ..., fractionid: _Optional[int] = ..., rpt_aimbot: _Optional[int] = ..., rpt_wallhack: _Optional[int] = ..., rpt_speedhack: _Optional[int] = ..., rpt_teamharm: _Optional[int] = ..., reason: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_PlayersProfile(_message.Message):
    __slots__ = ["account_profiles", "request_id"]
    ACCOUNT_PROFILES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    account_profiles: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_MatchmakingGC2ClientHello]
    request_id: int
    def __init__(self, request_id: _Optional[int] = ..., account_profiles: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientHello, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Predictions(_message.Message):
    __slots__ = ["event_id", "group_match_team_picks"]
    class GroupMatchTeamPick(_message.Message):
        __slots__ = ["groupid", "index", "itemid", "sectionid", "teamid"]
        GROUPID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        ITEMID_FIELD_NUMBER: _ClassVar[int]
        SECTIONID_FIELD_NUMBER: _ClassVar[int]
        TEAMID_FIELD_NUMBER: _ClassVar[int]
        groupid: int
        index: int
        itemid: int
        sectionid: int
        teamid: int
        def __init__(self, sectionid: _Optional[int] = ..., groupid: _Optional[int] = ..., index: _Optional[int] = ..., teamid: _Optional[int] = ..., itemid: _Optional[int] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_MATCH_TEAM_PICKS_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    group_match_team_picks: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Predictions.GroupMatchTeamPick]
    def __init__(self, event_id: _Optional[int] = ..., group_match_team_picks: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Predictions.GroupMatchTeamPick, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Server2GCClientValidate(_message.Message):
    __slots__ = ["accountid"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    def __init__(self, accountid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ServerNotificationForUserPenalty(_message.Message):
    __slots__ = ["account_id", "communication_cooldown", "reason", "seconds"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_COOLDOWN_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    communication_cooldown: bool
    reason: int
    seconds: int
    def __init__(self, account_id: _Optional[int] = ..., reason: _Optional[int] = ..., seconds: _Optional[int] = ..., communication_cooldown: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_ServerVarValueNotificationInfo(_message.Message):
    __slots__ = ["accountid", "type", "userdata", "viewangles"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    VIEWANGLES_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    type: int
    userdata: _containers.RepeatedScalarFieldContainer[int]
    viewangles: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, accountid: _Optional[int] = ..., viewangles: _Optional[_Iterable[int]] = ..., type: _Optional[int] = ..., userdata: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCCStrike15_v2_SetEventFavorite(_message.Message):
    __slots__ = ["eventid", "is_favorite"]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    IS_FAVORITE_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    is_favorite: bool
    def __init__(self, eventid: _Optional[int] = ..., is_favorite: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_WatchInfoUsers(_message.Message):
    __slots__ = ["account_ids", "extended_timeout", "request_id", "watchable_match_infos"]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    WATCHABLE_MATCH_INFOS_FIELD_NUMBER: _ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    extended_timeout: int
    request_id: int
    watchable_match_infos: _containers.RepeatedCompositeFieldContainer[WatchableMatchInfo]
    def __init__(self, request_id: _Optional[int] = ..., account_ids: _Optional[_Iterable[int]] = ..., watchable_match_infos: _Optional[_Iterable[_Union[WatchableMatchInfo, _Mapping]]] = ..., extended_timeout: _Optional[int] = ...) -> None: ...

class CMsgGCCstrike15_v2_ClientRedeemMissionReward(_message.Message):
    __slots__ = ["campaign_id", "expected_cost", "redeem_id", "redeemable_balance"]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_COST_FIELD_NUMBER: _ClassVar[int]
    REDEEMABLE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    REDEEM_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: int
    expected_cost: int
    redeem_id: int
    redeemable_balance: int
    def __init__(self, campaign_id: _Optional[int] = ..., redeem_id: _Optional[int] = ..., redeemable_balance: _Optional[int] = ..., expected_cost: _Optional[int] = ...) -> None: ...

class CMsgGCCstrike15_v2_ClientRequestNewMission(_message.Message):
    __slots__ = ["campaign_id", "mission_id"]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: int
    mission_id: int
    def __init__(self, mission_id: _Optional[int] = ..., campaign_id: _Optional[int] = ...) -> None: ...

class CMsgGCCstrike15_v2_GC2ServerNotifyXPRewarded(_message.Message):
    __slots__ = ["account_id", "current_level", "current_xp", "operation_points_awarded", "upgraded_defidx", "xp_progress_data"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_XP_FIELD_NUMBER: _ClassVar[int]
    OPERATION_POINTS_AWARDED_FIELD_NUMBER: _ClassVar[int]
    UPGRADED_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    XP_PROGRESS_DATA_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    current_level: int
    current_xp: int
    operation_points_awarded: int
    upgraded_defidx: int
    xp_progress_data: _containers.RepeatedCompositeFieldContainer[XpProgressData]
    def __init__(self, xp_progress_data: _Optional[_Iterable[_Union[XpProgressData, _Mapping]]] = ..., account_id: _Optional[int] = ..., current_xp: _Optional[int] = ..., current_level: _Optional[int] = ..., upgraded_defidx: _Optional[int] = ..., operation_points_awarded: _Optional[int] = ...) -> None: ...

class CMsgGCToClientSteamDatagramTicket(_message.Message):
    __slots__ = ["serialized_ticket"]
    SERIALIZED_TICKET_FIELD_NUMBER: _ClassVar[int]
    serialized_ticket: bytes
    def __init__(self, serialized_ticket: _Optional[bytes] = ...) -> None: ...

class CMsgGC_GlobalGame_Play(_message.Message):
    __slots__ = ["gametimems", "msperpoint", "ticket"]
    GAMETIMEMS_FIELD_NUMBER: _ClassVar[int]
    MSPERPOINT_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    gametimems: int
    msperpoint: int
    ticket: int
    def __init__(self, ticket: _Optional[int] = ..., gametimems: _Optional[int] = ..., msperpoint: _Optional[int] = ...) -> None: ...

class CMsgGC_GlobalGame_Subscribe(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: int
    def __init__(self, ticket: _Optional[int] = ...) -> None: ...

class CMsgGC_GlobalGame_Unsubscribe(_message.Message):
    __slots__ = ["timeleft"]
    TIMELEFT_FIELD_NUMBER: _ClassVar[int]
    timeleft: int
    def __init__(self, timeleft: _Optional[int] = ...) -> None: ...

class CMsgGC_ServerQuestUpdateData(_message.Message):
    __slots__ = ["binary_data", "missionlbsdata", "mm_game_mode", "player_quest_data"]
    BINARY_DATA_FIELD_NUMBER: _ClassVar[int]
    MISSIONLBSDATA_FIELD_NUMBER: _ClassVar[int]
    MM_GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_QUEST_DATA_FIELD_NUMBER: _ClassVar[int]
    binary_data: bytes
    missionlbsdata: ScoreLeaderboardData
    mm_game_mode: int
    player_quest_data: _containers.RepeatedCompositeFieldContainer[PlayerQuestData]
    def __init__(self, player_quest_data: _Optional[_Iterable[_Union[PlayerQuestData, _Mapping]]] = ..., binary_data: _Optional[bytes] = ..., mm_game_mode: _Optional[int] = ..., missionlbsdata: _Optional[_Union[ScoreLeaderboardData, _Mapping]] = ...) -> None: ...

class CMsgLegacySource1ClientWelcome(_message.Message):
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
    location: CMsgLegacySource1ClientWelcome.Location
    outofdate_subscribed_caches: _containers.RepeatedCompositeFieldContainer[_gcsdk_gcmessages_pb2.CMsgSOCacheSubscribed]
    rtime32_gc_welcome_timestamp: int
    txn_country_code: str
    uptodate_subscribed_caches: _containers.RepeatedCompositeFieldContainer[_gcsdk_gcmessages_pb2.CMsgSOCacheSubscriptionCheck]
    version: int
    def __init__(self, version: _Optional[int] = ..., game_data: _Optional[bytes] = ..., outofdate_subscribed_caches: _Optional[_Iterable[_Union[_gcsdk_gcmessages_pb2.CMsgSOCacheSubscribed, _Mapping]]] = ..., uptodate_subscribed_caches: _Optional[_Iterable[_Union[_gcsdk_gcmessages_pb2.CMsgSOCacheSubscriptionCheck, _Mapping]]] = ..., location: _Optional[_Union[CMsgLegacySource1ClientWelcome.Location, _Mapping]] = ..., game_data2: _Optional[bytes] = ..., rtime32_gc_welcome_timestamp: _Optional[int] = ..., currency: _Optional[int] = ..., balance: _Optional[int] = ..., balance_url: _Optional[str] = ..., txn_country_code: _Optional[str] = ...) -> None: ...

class CPreMatchInfoData(_message.Message):
    __slots__ = ["draft", "predictions_pct", "stats", "wins"]
    class TeamStats(_message.Message):
        __slots__ = ["match_info_idxtxt", "match_info_teams", "match_info_txt"]
        MATCH_INFO_IDXTXT_FIELD_NUMBER: _ClassVar[int]
        MATCH_INFO_TEAMS_FIELD_NUMBER: _ClassVar[int]
        MATCH_INFO_TXT_FIELD_NUMBER: _ClassVar[int]
        match_info_idxtxt: int
        match_info_teams: _containers.RepeatedScalarFieldContainer[str]
        match_info_txt: str
        def __init__(self, match_info_idxtxt: _Optional[int] = ..., match_info_txt: _Optional[str] = ..., match_info_teams: _Optional[_Iterable[str]] = ...) -> None: ...
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    PREDICTIONS_PCT_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    draft: CDataGCCStrike15_v2_TournamentMatchDraft
    predictions_pct: int
    stats: _containers.RepeatedCompositeFieldContainer[CPreMatchInfoData.TeamStats]
    wins: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, predictions_pct: _Optional[int] = ..., draft: _Optional[_Union[CDataGCCStrike15_v2_TournamentMatchDraft, _Mapping]] = ..., stats: _Optional[_Iterable[_Union[CPreMatchInfoData.TeamStats, _Mapping]]] = ..., wins: _Optional[_Iterable[int]] = ...) -> None: ...

class CSOAccountRecurringSubscription(_message.Message):
    __slots__ = ["time_initiated", "time_next_cycle"]
    TIME_INITIATED_FIELD_NUMBER: _ClassVar[int]
    TIME_NEXT_CYCLE_FIELD_NUMBER: _ClassVar[int]
    time_initiated: int
    time_next_cycle: int
    def __init__(self, time_next_cycle: _Optional[int] = ..., time_initiated: _Optional[int] = ...) -> None: ...

class CSOAccountSeasonalOperation(_message.Message):
    __slots__ = ["mission_id", "missions_completed", "premium_tiers", "redeemable_balance", "season_pass_time", "season_value", "tier_unlocked"]
    MISSIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_TIERS_FIELD_NUMBER: _ClassVar[int]
    REDEEMABLE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    SEASON_PASS_TIME_FIELD_NUMBER: _ClassVar[int]
    SEASON_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIER_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    mission_id: int
    missions_completed: int
    premium_tiers: int
    redeemable_balance: int
    season_pass_time: int
    season_value: int
    tier_unlocked: int
    def __init__(self, season_value: _Optional[int] = ..., tier_unlocked: _Optional[int] = ..., premium_tiers: _Optional[int] = ..., mission_id: _Optional[int] = ..., missions_completed: _Optional[int] = ..., redeemable_balance: _Optional[int] = ..., season_pass_time: _Optional[int] = ...) -> None: ...

class CSOEconCoupon(_message.Message):
    __slots__ = ["defidx", "entryid", "expiration_date"]
    DEFIDX_FIELD_NUMBER: _ClassVar[int]
    ENTRYID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    defidx: int
    entryid: int
    expiration_date: int
    def __init__(self, entryid: _Optional[int] = ..., defidx: _Optional[int] = ..., expiration_date: _Optional[int] = ...) -> None: ...

class CSOPersonaDataPublic(_message.Message):
    __slots__ = ["commendation", "elevated_state", "player_level"]
    COMMENDATION_FIELD_NUMBER: _ClassVar[int]
    ELEVATED_STATE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    commendation: PlayerCommendationInfo
    elevated_state: bool
    player_level: int
    def __init__(self, player_level: _Optional[int] = ..., commendation: _Optional[_Union[PlayerCommendationInfo, _Mapping]] = ..., elevated_state: bool = ...) -> None: ...

class CSOQuestProgress(_message.Message):
    __slots__ = ["bonus_points", "points_remaining", "questid"]
    BONUS_POINTS_FIELD_NUMBER: _ClassVar[int]
    POINTS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    QUESTID_FIELD_NUMBER: _ClassVar[int]
    bonus_points: int
    points_remaining: int
    questid: int
    def __init__(self, questid: _Optional[int] = ..., points_remaining: _Optional[int] = ..., bonus_points: _Optional[int] = ...) -> None: ...

class CVDiagnostic(_message.Message):
    __slots__ = ["extended", "id", "string_value", "value"]
    EXTENDED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    extended: int
    id: int
    string_value: str
    value: int
    def __init__(self, id: _Optional[int] = ..., extended: _Optional[int] = ..., value: _Optional[int] = ..., string_value: _Optional[str] = ...) -> None: ...

class DataCenterPing(_message.Message):
    __slots__ = ["data_center_id", "ping"]
    DATA_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    data_center_id: int
    ping: int
    def __init__(self, data_center_id: _Optional[int] = ..., ping: _Optional[int] = ...) -> None: ...

class DeepPlayerMatchEvent(_message.Message):
    __slots__ = ["accountid", "b_playing_ct", "event_data", "event_id", "event_type", "match_id", "other_defidx", "other_pos_x", "other_pos_y", "other_pos_z", "user_defidx", "user_pos_x", "user_pos_y", "user_pos_z"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    B_PLAYING_CT_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    OTHER_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    OTHER_POS_X_FIELD_NUMBER: _ClassVar[int]
    OTHER_POS_Y_FIELD_NUMBER: _ClassVar[int]
    OTHER_POS_Z_FIELD_NUMBER: _ClassVar[int]
    USER_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    USER_POS_X_FIELD_NUMBER: _ClassVar[int]
    USER_POS_Y_FIELD_NUMBER: _ClassVar[int]
    USER_POS_Z_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    b_playing_ct: bool
    event_data: int
    event_id: int
    event_type: int
    match_id: int
    other_defidx: int
    other_pos_x: int
    other_pos_y: int
    other_pos_z: int
    user_defidx: int
    user_pos_x: int
    user_pos_y: int
    user_pos_z: int
    def __init__(self, accountid: _Optional[int] = ..., match_id: _Optional[int] = ..., event_id: _Optional[int] = ..., event_type: _Optional[int] = ..., b_playing_ct: bool = ..., user_pos_x: _Optional[int] = ..., user_pos_y: _Optional[int] = ..., user_pos_z: _Optional[int] = ..., user_defidx: _Optional[int] = ..., other_pos_x: _Optional[int] = ..., other_pos_y: _Optional[int] = ..., other_pos_z: _Optional[int] = ..., other_defidx: _Optional[int] = ..., event_data: _Optional[int] = ...) -> None: ...

class DeepPlayerStatsEntry(_message.Message):
    __slots__ = ["accountid", "b_starting_ct", "enemy_2ks", "enemy_3ks", "enemy_4ks", "enemy_headshots", "enemy_kills", "engagements_1v1_count", "engagements_1v1_wins", "engagements_1v2_count", "engagements_1v2_wins", "engagements_entry_count", "engagements_entry_wins", "flash_count", "flash_success", "mapid", "match_id", "match_outcome", "mates", "mm_game_mode", "rounds_lost", "rounds_won", "stat_deaths", "stat_mvps", "stat_score", "total_damage", "utility_count", "utility_success"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    B_STARTING_CT_FIELD_NUMBER: _ClassVar[int]
    ENEMY_2KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_3KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_4KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_HEADSHOTS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_KILLS_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENTS_1V1_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENTS_1V1_WINS_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENTS_1V2_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENTS_1V2_WINS_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENTS_ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENTS_ENTRY_WINS_FIELD_NUMBER: _ClassVar[int]
    FLASH_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLASH_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    MATES_FIELD_NUMBER: _ClassVar[int]
    MM_GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    ROUNDS_LOST_FIELD_NUMBER: _ClassVar[int]
    ROUNDS_WON_FIELD_NUMBER: _ClassVar[int]
    STAT_DEATHS_FIELD_NUMBER: _ClassVar[int]
    STAT_MVPS_FIELD_NUMBER: _ClassVar[int]
    STAT_SCORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DAMAGE_FIELD_NUMBER: _ClassVar[int]
    UTILITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    UTILITY_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    b_starting_ct: bool
    enemy_2ks: int
    enemy_3ks: int
    enemy_4ks: int
    enemy_headshots: int
    enemy_kills: int
    engagements_1v1_count: int
    engagements_1v1_wins: int
    engagements_1v2_count: int
    engagements_1v2_wins: int
    engagements_entry_count: int
    engagements_entry_wins: int
    flash_count: int
    flash_success: int
    mapid: int
    match_id: int
    match_outcome: int
    mates: _containers.RepeatedScalarFieldContainer[int]
    mm_game_mode: int
    rounds_lost: int
    rounds_won: int
    stat_deaths: int
    stat_mvps: int
    stat_score: int
    total_damage: int
    utility_count: int
    utility_success: int
    def __init__(self, accountid: _Optional[int] = ..., match_id: _Optional[int] = ..., mm_game_mode: _Optional[int] = ..., mapid: _Optional[int] = ..., b_starting_ct: bool = ..., match_outcome: _Optional[int] = ..., rounds_won: _Optional[int] = ..., rounds_lost: _Optional[int] = ..., stat_score: _Optional[int] = ..., stat_deaths: _Optional[int] = ..., stat_mvps: _Optional[int] = ..., enemy_kills: _Optional[int] = ..., enemy_headshots: _Optional[int] = ..., enemy_2ks: _Optional[int] = ..., enemy_3ks: _Optional[int] = ..., enemy_4ks: _Optional[int] = ..., total_damage: _Optional[int] = ..., engagements_entry_count: _Optional[int] = ..., engagements_entry_wins: _Optional[int] = ..., engagements_1v1_count: _Optional[int] = ..., engagements_1v1_wins: _Optional[int] = ..., engagements_1v2_count: _Optional[int] = ..., engagements_1v2_wins: _Optional[int] = ..., utility_count: _Optional[int] = ..., utility_success: _Optional[int] = ..., flash_count: _Optional[int] = ..., flash_success: _Optional[int] = ..., mates: _Optional[_Iterable[int]] = ...) -> None: ...

class DetailedSearchStatistic(_message.Message):
    __slots__ = ["game_type", "players_searching", "search_time_avg"]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_SEARCHING_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TIME_AVG_FIELD_NUMBER: _ClassVar[int]
    game_type: int
    players_searching: int
    search_time_avg: int
    def __init__(self, game_type: _Optional[int] = ..., search_time_avg: _Optional[int] = ..., players_searching: _Optional[int] = ...) -> None: ...

class GameServerPing(_message.Message):
    __slots__ = ["instances", "ip", "ping"]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    instances: int
    ip: int
    ping: int
    def __init__(self, ping: _Optional[int] = ..., ip: _Optional[int] = ..., instances: _Optional[int] = ...) -> None: ...

class GlobalStatistics(_message.Message):
    __slots__ = ["active_survey_id", "active_tournament_eventid", "main_post_url", "ongoing_matches", "players_online", "players_searching", "pricesheet_version", "required_appid_version", "required_appid_version2", "rtime32_cur", "rtime32_event_start", "search_statistics", "search_time_avg", "servers_available", "servers_online", "twitch_streams_version"]
    ACTIVE_SURVEY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TOURNAMENT_EVENTID_FIELD_NUMBER: _ClassVar[int]
    MAIN_POST_URL_FIELD_NUMBER: _ClassVar[int]
    ONGOING_MATCHES_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_SEARCHING_FIELD_NUMBER: _ClassVar[int]
    PRICESHEET_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPID_VERSION2_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPID_VERSION_FIELD_NUMBER: _ClassVar[int]
    RTIME32_CUR_FIELD_NUMBER: _ClassVar[int]
    RTIME32_EVENT_START_FIELD_NUMBER: _ClassVar[int]
    SEARCH_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TIME_AVG_FIELD_NUMBER: _ClassVar[int]
    SERVERS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SERVERS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    TWITCH_STREAMS_VERSION_FIELD_NUMBER: _ClassVar[int]
    active_survey_id: int
    active_tournament_eventid: int
    main_post_url: str
    ongoing_matches: int
    players_online: int
    players_searching: int
    pricesheet_version: int
    required_appid_version: int
    required_appid_version2: int
    rtime32_cur: int
    rtime32_event_start: int
    search_statistics: _containers.RepeatedCompositeFieldContainer[DetailedSearchStatistic]
    search_time_avg: int
    servers_available: int
    servers_online: int
    twitch_streams_version: int
    def __init__(self, players_online: _Optional[int] = ..., servers_online: _Optional[int] = ..., players_searching: _Optional[int] = ..., servers_available: _Optional[int] = ..., ongoing_matches: _Optional[int] = ..., search_time_avg: _Optional[int] = ..., search_statistics: _Optional[_Iterable[_Union[DetailedSearchStatistic, _Mapping]]] = ..., main_post_url: _Optional[str] = ..., required_appid_version: _Optional[int] = ..., pricesheet_version: _Optional[int] = ..., twitch_streams_version: _Optional[int] = ..., active_tournament_eventid: _Optional[int] = ..., active_survey_id: _Optional[int] = ..., rtime32_cur: _Optional[int] = ..., rtime32_event_start: _Optional[int] = ..., required_appid_version2: _Optional[int] = ...) -> None: ...

class IpAddressMask(_message.Message):
    __slots__ = ["a", "b", "bits", "c", "d", "token"]
    A_FIELD_NUMBER: _ClassVar[int]
    BITS_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    bits: int
    c: int
    d: int
    token: int
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ..., c: _Optional[int] = ..., d: _Optional[int] = ..., bits: _Optional[int] = ..., token: _Optional[int] = ...) -> None: ...

class MatchEndItemUpdates(_message.Message):
    __slots__ = ["item_attr_defidx", "item_attr_delta_value", "item_id"]
    ITEM_ATTR_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    ITEM_ATTR_DELTA_VALUE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_attr_defidx: int
    item_attr_delta_value: int
    item_id: int
    def __init__(self, item_id: _Optional[int] = ..., item_attr_defidx: _Optional[int] = ..., item_attr_delta_value: _Optional[int] = ...) -> None: ...

class OperationalStatisticDescription(_message.Message):
    __slots__ = ["idkey", "name"]
    IDKEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    idkey: int
    name: str
    def __init__(self, name: _Optional[str] = ..., idkey: _Optional[int] = ...) -> None: ...

class OperationalStatisticElement(_message.Message):
    __slots__ = ["idkey", "values"]
    IDKEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    idkey: int
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, idkey: _Optional[int] = ..., values: _Optional[_Iterable[int]] = ...) -> None: ...

class OperationalStatisticsPacket(_message.Message):
    __slots__ = ["mstimestamp", "packetid", "values"]
    MSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PACKETID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    mstimestamp: int
    packetid: int
    values: _containers.RepeatedCompositeFieldContainer[OperationalStatisticElement]
    def __init__(self, packetid: _Optional[int] = ..., mstimestamp: _Optional[int] = ..., values: _Optional[_Iterable[_Union[OperationalStatisticElement, _Mapping]]] = ...) -> None: ...

class PlayerCommendationInfo(_message.Message):
    __slots__ = ["cmd_friendly", "cmd_leader", "cmd_teaching"]
    CMD_FRIENDLY_FIELD_NUMBER: _ClassVar[int]
    CMD_LEADER_FIELD_NUMBER: _ClassVar[int]
    CMD_TEACHING_FIELD_NUMBER: _ClassVar[int]
    cmd_friendly: int
    cmd_leader: int
    cmd_teaching: int
    def __init__(self, cmd_friendly: _Optional[int] = ..., cmd_teaching: _Optional[int] = ..., cmd_leader: _Optional[int] = ...) -> None: ...

class PlayerDecalDigitalSignature(_message.Message):
    __slots__ = ["accountid", "creationtime", "endpos", "entindex", "equipslot", "hitbox", "left", "normal", "rtime", "signature", "startpos", "tint_id", "trace_id", "tx_defidx"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CREATIONTIME_FIELD_NUMBER: _ClassVar[int]
    ENDPOS_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    EQUIPSLOT_FIELD_NUMBER: _ClassVar[int]
    HITBOX_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    RTIME_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    STARTPOS_FIELD_NUMBER: _ClassVar[int]
    TINT_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    TX_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    creationtime: float
    endpos: _containers.RepeatedScalarFieldContainer[float]
    entindex: int
    equipslot: int
    hitbox: int
    left: _containers.RepeatedScalarFieldContainer[float]
    normal: _containers.RepeatedScalarFieldContainer[float]
    rtime: int
    signature: bytes
    startpos: _containers.RepeatedScalarFieldContainer[float]
    tint_id: int
    trace_id: int
    tx_defidx: int
    def __init__(self, signature: _Optional[bytes] = ..., accountid: _Optional[int] = ..., rtime: _Optional[int] = ..., endpos: _Optional[_Iterable[float]] = ..., startpos: _Optional[_Iterable[float]] = ..., left: _Optional[_Iterable[float]] = ..., tx_defidx: _Optional[int] = ..., entindex: _Optional[int] = ..., hitbox: _Optional[int] = ..., creationtime: _Optional[float] = ..., equipslot: _Optional[int] = ..., trace_id: _Optional[int] = ..., normal: _Optional[_Iterable[float]] = ..., tint_id: _Optional[int] = ...) -> None: ...

class PlayerMedalsInfo(_message.Message):
    __slots__ = ["display_items_defidx", "featured_display_item_defidx"]
    DISPLAY_ITEMS_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    FEATURED_DISPLAY_ITEM_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    display_items_defidx: _containers.RepeatedScalarFieldContainer[int]
    featured_display_item_defidx: int
    def __init__(self, display_items_defidx: _Optional[_Iterable[int]] = ..., featured_display_item_defidx: _Optional[int] = ...) -> None: ...

class PlayerQuestData(_message.Message):
    __slots__ = ["item_updates", "mm_game_mode", "operation_points_eligible", "quest_item_data", "quester_account_id", "time_played", "userstatchanges", "xp_progress_data"]
    class QuestItemData(_message.Message):
        __slots__ = ["quest_bonus_points_earned", "quest_id", "quest_normal_points_earned"]
        QUEST_BONUS_POINTS_EARNED_FIELD_NUMBER: _ClassVar[int]
        QUEST_ID_FIELD_NUMBER: _ClassVar[int]
        QUEST_NORMAL_POINTS_EARNED_FIELD_NUMBER: _ClassVar[int]
        quest_bonus_points_earned: int
        quest_id: int
        quest_normal_points_earned: int
        def __init__(self, quest_id: _Optional[int] = ..., quest_normal_points_earned: _Optional[int] = ..., quest_bonus_points_earned: _Optional[int] = ...) -> None: ...
    ITEM_UPDATES_FIELD_NUMBER: _ClassVar[int]
    MM_GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_POINTS_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    QUESTER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_ITEM_DATA_FIELD_NUMBER: _ClassVar[int]
    TIME_PLAYED_FIELD_NUMBER: _ClassVar[int]
    USERSTATCHANGES_FIELD_NUMBER: _ClassVar[int]
    XP_PROGRESS_DATA_FIELD_NUMBER: _ClassVar[int]
    item_updates: _containers.RepeatedCompositeFieldContainer[MatchEndItemUpdates]
    mm_game_mode: int
    operation_points_eligible: bool
    quest_item_data: _containers.RepeatedCompositeFieldContainer[PlayerQuestData.QuestItemData]
    quester_account_id: int
    time_played: int
    userstatchanges: _containers.RepeatedCompositeFieldContainer[CMsgCsgoSteamUserStatChange]
    xp_progress_data: _containers.RepeatedCompositeFieldContainer[XpProgressData]
    def __init__(self, quester_account_id: _Optional[int] = ..., quest_item_data: _Optional[_Iterable[_Union[PlayerQuestData.QuestItemData, _Mapping]]] = ..., xp_progress_data: _Optional[_Iterable[_Union[XpProgressData, _Mapping]]] = ..., time_played: _Optional[int] = ..., mm_game_mode: _Optional[int] = ..., item_updates: _Optional[_Iterable[_Union[MatchEndItemUpdates, _Mapping]]] = ..., operation_points_eligible: bool = ..., userstatchanges: _Optional[_Iterable[_Union[CMsgCsgoSteamUserStatChange, _Mapping]]] = ...) -> None: ...

class PlayerRankingInfo(_message.Message):
    __slots__ = ["account_id", "rank_change", "rank_id", "rank_type_id", "tv_control", "wins"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RANK_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    TV_CONTROL_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    rank_change: float
    rank_id: int
    rank_type_id: int
    tv_control: int
    wins: int
    def __init__(self, account_id: _Optional[int] = ..., rank_id: _Optional[int] = ..., wins: _Optional[int] = ..., rank_change: _Optional[float] = ..., rank_type_id: _Optional[int] = ..., tv_control: _Optional[int] = ...) -> None: ...

class ScoreLeaderboardData(_message.Message):
    __slots__ = ["accountentries", "matchentries", "quest_id", "score"]
    class AccountEntries(_message.Message):
        __slots__ = ["accountid", "entries"]
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        entries: _containers.RepeatedCompositeFieldContainer[ScoreLeaderboardData.Entry]
        def __init__(self, accountid: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[ScoreLeaderboardData.Entry, _Mapping]]] = ...) -> None: ...
    class Entry(_message.Message):
        __slots__ = ["tag", "val"]
        TAG_FIELD_NUMBER: _ClassVar[int]
        VAL_FIELD_NUMBER: _ClassVar[int]
        tag: int
        val: int
        def __init__(self, tag: _Optional[int] = ..., val: _Optional[int] = ...) -> None: ...
    ACCOUNTENTRIES_FIELD_NUMBER: _ClassVar[int]
    MATCHENTRIES_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    accountentries: _containers.RepeatedCompositeFieldContainer[ScoreLeaderboardData.AccountEntries]
    matchentries: _containers.RepeatedCompositeFieldContainer[ScoreLeaderboardData.Entry]
    quest_id: int
    score: int
    def __init__(self, quest_id: _Optional[int] = ..., score: _Optional[int] = ..., accountentries: _Optional[_Iterable[_Union[ScoreLeaderboardData.AccountEntries, _Mapping]]] = ..., matchentries: _Optional[_Iterable[_Union[ScoreLeaderboardData.Entry, _Mapping]]] = ...) -> None: ...

class ServerHltvInfo(_message.Message):
    __slots__ = ["flags", "game_map", "game_mapgroup", "game_type", "tv_clients", "tv_local_clients", "tv_local_proxies", "tv_local_slots", "tv_master_steamid", "tv_proxies", "tv_relay_address", "tv_relay_clients", "tv_relay_port", "tv_relay_proxies", "tv_relay_slots", "tv_relay_steamid", "tv_slots", "tv_time", "tv_udp_port", "tv_watch_key"]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    GAME_MAPGROUP_FIELD_NUMBER: _ClassVar[int]
    GAME_MAP_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    TV_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    TV_LOCAL_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    TV_LOCAL_PROXIES_FIELD_NUMBER: _ClassVar[int]
    TV_LOCAL_SLOTS_FIELD_NUMBER: _ClassVar[int]
    TV_MASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    TV_PROXIES_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_PORT_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_PROXIES_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_SLOTS_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_STEAMID_FIELD_NUMBER: _ClassVar[int]
    TV_SLOTS_FIELD_NUMBER: _ClassVar[int]
    TV_TIME_FIELD_NUMBER: _ClassVar[int]
    TV_UDP_PORT_FIELD_NUMBER: _ClassVar[int]
    TV_WATCH_KEY_FIELD_NUMBER: _ClassVar[int]
    flags: int
    game_map: str
    game_mapgroup: str
    game_type: int
    tv_clients: int
    tv_local_clients: int
    tv_local_proxies: int
    tv_local_slots: int
    tv_master_steamid: int
    tv_proxies: int
    tv_relay_address: int
    tv_relay_clients: int
    tv_relay_port: int
    tv_relay_proxies: int
    tv_relay_slots: int
    tv_relay_steamid: int
    tv_slots: int
    tv_time: int
    tv_udp_port: int
    tv_watch_key: int
    def __init__(self, tv_udp_port: _Optional[int] = ..., tv_watch_key: _Optional[int] = ..., tv_slots: _Optional[int] = ..., tv_clients: _Optional[int] = ..., tv_proxies: _Optional[int] = ..., tv_time: _Optional[int] = ..., game_type: _Optional[int] = ..., game_mapgroup: _Optional[str] = ..., game_map: _Optional[str] = ..., tv_master_steamid: _Optional[int] = ..., tv_local_slots: _Optional[int] = ..., tv_local_clients: _Optional[int] = ..., tv_local_proxies: _Optional[int] = ..., tv_relay_slots: _Optional[int] = ..., tv_relay_clients: _Optional[int] = ..., tv_relay_proxies: _Optional[int] = ..., tv_relay_address: _Optional[int] = ..., tv_relay_port: _Optional[int] = ..., tv_relay_steamid: _Optional[int] = ..., flags: _Optional[int] = ...) -> None: ...

class TournamentEvent(_message.Message):
    __slots__ = ["active_section_id", "event_id", "event_name", "event_public", "event_stage_id", "event_stage_name", "event_tag", "event_time_end", "event_time_start"]
    ACTIVE_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    EVENT_STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TAG_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_END_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_START_FIELD_NUMBER: _ClassVar[int]
    active_section_id: int
    event_id: int
    event_name: str
    event_public: int
    event_stage_id: int
    event_stage_name: str
    event_tag: str
    event_time_end: int
    event_time_start: int
    def __init__(self, event_id: _Optional[int] = ..., event_tag: _Optional[str] = ..., event_name: _Optional[str] = ..., event_time_start: _Optional[int] = ..., event_time_end: _Optional[int] = ..., event_public: _Optional[int] = ..., event_stage_id: _Optional[int] = ..., event_stage_name: _Optional[str] = ..., active_section_id: _Optional[int] = ...) -> None: ...

class TournamentMatchSetup(_message.Message):
    __slots__ = ["event_id", "event_stage_id", "team_id_ct", "team_id_t"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_CT_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_T_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    event_stage_id: int
    team_id_ct: int
    team_id_t: int
    def __init__(self, event_id: _Optional[int] = ..., team_id_ct: _Optional[int] = ..., team_id_t: _Optional[int] = ..., event_stage_id: _Optional[int] = ...) -> None: ...

class TournamentPlayer(_message.Message):
    __slots__ = ["account_id", "player_desc", "player_dob", "player_flag", "player_location", "player_name", "player_nick"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DESC_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DOB_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FLAG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NICK_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    player_desc: str
    player_dob: int
    player_flag: str
    player_location: str
    player_name: str
    player_nick: str
    def __init__(self, account_id: _Optional[int] = ..., player_nick: _Optional[str] = ..., player_name: _Optional[str] = ..., player_dob: _Optional[int] = ..., player_flag: _Optional[str] = ..., player_location: _Optional[str] = ..., player_desc: _Optional[str] = ...) -> None: ...

class TournamentTeam(_message.Message):
    __slots__ = ["players", "team_flag", "team_id", "team_name", "team_tag"]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    TEAM_FLAG_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_TAG_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[TournamentPlayer]
    team_flag: str
    team_id: int
    team_name: str
    team_tag: str
    def __init__(self, team_id: _Optional[int] = ..., team_tag: _Optional[str] = ..., team_flag: _Optional[str] = ..., team_name: _Optional[str] = ..., players: _Optional[_Iterable[_Union[TournamentPlayer, _Mapping]]] = ...) -> None: ...

class WatchableMatchInfo(_message.Message):
    __slots__ = ["cl_decryptdata_key", "cl_decryptdata_key_pub", "game_map", "game_mapgroup", "game_type", "match_id", "reservation_id", "server_id", "server_ip", "tv_port", "tv_spectators", "tv_time", "tv_watch_password"]
    CL_DECRYPTDATA_KEY_FIELD_NUMBER: _ClassVar[int]
    CL_DECRYPTDATA_KEY_PUB_FIELD_NUMBER: _ClassVar[int]
    GAME_MAPGROUP_FIELD_NUMBER: _ClassVar[int]
    GAME_MAP_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    TV_PORT_FIELD_NUMBER: _ClassVar[int]
    TV_SPECTATORS_FIELD_NUMBER: _ClassVar[int]
    TV_TIME_FIELD_NUMBER: _ClassVar[int]
    TV_WATCH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    cl_decryptdata_key: int
    cl_decryptdata_key_pub: int
    game_map: str
    game_mapgroup: str
    game_type: int
    match_id: int
    reservation_id: int
    server_id: int
    server_ip: int
    tv_port: int
    tv_spectators: int
    tv_time: int
    tv_watch_password: bytes
    def __init__(self, server_ip: _Optional[int] = ..., tv_port: _Optional[int] = ..., tv_spectators: _Optional[int] = ..., tv_time: _Optional[int] = ..., tv_watch_password: _Optional[bytes] = ..., cl_decryptdata_key: _Optional[int] = ..., cl_decryptdata_key_pub: _Optional[int] = ..., game_type: _Optional[int] = ..., game_mapgroup: _Optional[str] = ..., game_map: _Optional[str] = ..., server_id: _Optional[int] = ..., match_id: _Optional[int] = ..., reservation_id: _Optional[int] = ...) -> None: ...

class XpProgressData(_message.Message):
    __slots__ = ["xp_category", "xp_points"]
    XP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    XP_POINTS_FIELD_NUMBER: _ClassVar[int]
    xp_category: int
    xp_points: int
    def __init__(self, xp_points: _Optional[int] = ..., xp_category: _Optional[int] = ...) -> None: ...

class ECsgoGCMsg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECsgoSteamUserStat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EClientReportingVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EInitSystemResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
