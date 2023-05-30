import steammessages_pb2 as _steammessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
k_EGCItemCustomizationNotification_ActivateFanToken: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_ActivateOperationCoin: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_ApplyPatch: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_ApplySticker: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_CasketAdded: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_CasketContents: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_CasketInvFull: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_CasketRemoved: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_CasketTooFull: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_ClientRedeemMissionReward: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_GenerateSouvenir: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_GraffitiUnseal: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_NameBaseItem: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_NameItem: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_RemoveItemName: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_RemovePatch: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_RemoveSticker: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_StatTrakSwap: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_UnlockCrate: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_XRayItemClaim: EGCItemCustomizationNotification
k_EGCItemCustomizationNotification_XRayItemReveal: EGCItemCustomizationNotification
k_EGCMsgCommitUnfinalized: EGCMsgResponse
k_EGCMsgFailedToCreate: EGCMsgResponse
k_EGCMsgLimitExceeded: EGCMsgResponse
k_EGCMsgResponseDenied: EGCMsgResponse
k_EGCMsgResponseInvalid: EGCMsgResponse
k_EGCMsgResponseNoMatch: EGCMsgResponse
k_EGCMsgResponseNotLoggedOn: EGCMsgResponse
k_EGCMsgResponseOK: EGCMsgResponse
k_EGCMsgResponseServerError: EGCMsgResponse
k_EGCMsgResponseTimeout: EGCMsgResponse
k_EGCMsgResponseUnknownError: EGCMsgResponse
k_EMsgGCAddItemToSocketResponse_DEPRECATED: EGCItemMsg
k_EMsgGCAddItemToSocket_DEPRECATED: EGCItemMsg
k_EMsgGCAddSocketToBaseItem_DEPRECATED: EGCItemMsg
k_EMsgGCAddSocketToItemResponse_DEPRECATED: EGCItemMsg
k_EMsgGCAddSocketToItem_DEPRECATED: EGCItemMsg
k_EMsgGCAdjustItemEquippedState: EGCItemMsg
k_EMsgGCAdjustItemEquippedStateMulti: EGCItemMsg
k_EMsgGCApplyAutograph: EGCItemMsg
k_EMsgGCApplyConsumableEffects: EGCItemMsg
k_EMsgGCApplyEggEssence: EGCItemMsg
k_EMsgGCApplyPennantUpgrade: EGCItemMsg
k_EMsgGCApplySticker: EGCItemMsg
k_EMsgGCApplyStrangePart: EGCItemMsg
k_EMsgGCBackpackSortFinished: EGCItemMsg
k_EMsgGCBannedWordListRequest: EGCItemMsg
k_EMsgGCBannedWordListResponse: EGCItemMsg
k_EMsgGCBase: EGCItemMsg
k_EMsgGCCasketItemAdd: EGCItemMsg
k_EMsgGCCasketItemExtract: EGCItemMsg
k_EMsgGCCasketItemLoadContents: EGCItemMsg
k_EMsgGCClientDisplayNotification: EGCItemMsg
k_EMsgGCClientVersionUpdated: EGCItemMsg
k_EMsgGCCollectItem: EGCItemMsg
k_EMsgGCConsumableExhausted: EGCItemMsg
k_EMsgGCCraft: EGCItemMsg
k_EMsgGCCraftResponse: EGCItemMsg
k_EMsgGCCustomizeItemTexture: EGCItemMsg
k_EMsgGCCustomizeItemTextureResponse: EGCItemMsg
k_EMsgGCDelete: EGCItemMsg
k_EMsgGCDeliverGift: EGCItemMsg
k_EMsgGCDeliverGiftResponseGiver: EGCItemMsg
k_EMsgGCDeliverGiftResponseReceiver: EGCItemMsg
k_EMsgGCDev_NewItemRequest: EGCItemMsg
k_EMsgGCDev_NewItemRequestResponse: EGCItemMsg
k_EMsgGCDev_PaintKitDropItem: EGCItemMsg
k_EMsgGCGiftWrapItem: EGCItemMsg
k_EMsgGCGiftWrapItemResponse: EGCItemMsg
k_EMsgGCGiftedItems: EGCItemMsg
k_EMsgGCGiftedItems_DEPRECATED: EGCItemMsg
k_EMsgGCGoldenWrenchBroadcast: EGCItemMsg
k_EMsgGCItemAcknowledged: EGCItemMsg
k_EMsgGCItemAcknowledged__DEPRECATED: EGCItemMsg
k_EMsgGCItemCustomizationNotification: EGCItemMsg
k_EMsgGCItemPreviewCheckStatus: EGCItemMsg
k_EMsgGCItemPreviewExpire: EGCItemMsg
k_EMsgGCItemPreviewExpireNotification: EGCItemMsg
k_EMsgGCItemPreviewItemBoughtNotification: EGCItemMsg
k_EMsgGCItemPreviewRequest: EGCItemMsg
k_EMsgGCItemPreviewRequestResponse: EGCItemMsg
k_EMsgGCItemPreviewStatusResponse: EGCItemMsg
k_EMsgGCLookupAccount: EGCItemMsg
k_EMsgGCLookupAccountName: EGCItemMsg
k_EMsgGCLookupAccountNameResponse: EGCItemMsg
k_EMsgGCLookupAccountResponse: EGCItemMsg
k_EMsgGCMOTDRequest: EGCItemMsg
k_EMsgGCMOTDRequestResponse: EGCItemMsg
k_EMsgGCModifyItemAttribute: EGCItemMsg
k_EMsgGCNameBaseItem: EGCItemMsg
k_EMsgGCNameBaseItemResponse: EGCItemMsg
k_EMsgGCNameEggEssenceResponse: EGCItemMsg
k_EMsgGCNameItem: EGCItemMsg
k_EMsgGCNameItemNotification: EGCItemMsg
k_EMsgGCPaintItem: EGCItemMsg
k_EMsgGCPaintItemResponse: EGCItemMsg
k_EMsgGCPaintKitBaseItem: EGCItemMsg
k_EMsgGCPaintKitItem: EGCItemMsg
k_EMsgGCPaintKitItemResponse: EGCItemMsg
k_EMsgGCRecurringSubscriptionStatus: EGCItemMsg
k_EMsgGCRemoveCustomTexture: EGCItemMsg
k_EMsgGCRemoveCustomTextureResponse: EGCItemMsg
k_EMsgGCRemoveItemName: EGCItemMsg
k_EMsgGCRemoveItemPaint: EGCItemMsg
k_EMsgGCRemoveMakersMark: EGCItemMsg
k_EMsgGCRemoveMakersMarkResponse: EGCItemMsg
k_EMsgGCRemoveSocketItemResponse_DEPRECATED: EGCItemMsg
k_EMsgGCRemoveSocketItem_DEPRECATED: EGCItemMsg
k_EMsgGCRemoveUniqueCraftIndex: EGCItemMsg
k_EMsgGCRemoveUniqueCraftIndexResponse: EGCItemMsg
k_EMsgGCRequestAnnouncements: EGCItemMsg
k_EMsgGCRequestAnnouncementsResponse: EGCItemMsg
k_EMsgGCRequestPassportItemGrant: EGCItemMsg
k_EMsgGCSaxxyBroadcast: EGCItemMsg
k_EMsgGCServerBrowser_BlacklistServer: EGCItemMsg
k_EMsgGCServerBrowser_FavoriteServer: EGCItemMsg
k_EMsgGCServerRentalsBase: EGCItemMsg
k_EMsgGCServerVersionUpdated: EGCItemMsg
k_EMsgGCSetItemPosition: EGCItemMsg
k_EMsgGCSetItemPositions: EGCItemMsg
k_EMsgGCSetItemStyle: EGCItemMsg
k_EMsgGCShowItemsPickedUp: EGCItemMsg
k_EMsgGCSortItems: EGCItemMsg
k_EMsgGCStatTrakSwap: EGCItemMsg
k_EMsgGCStoreGetUserData: EGCItemMsg
k_EMsgGCStoreGetUserDataResponse: EGCItemMsg
k_EMsgGCStorePurchaseCancel: EGCItemMsg
k_EMsgGCStorePurchaseCancelResponse: EGCItemMsg
k_EMsgGCStorePurchaseFinalize: EGCItemMsg
k_EMsgGCStorePurchaseFinalizeResponse: EGCItemMsg
k_EMsgGCStorePurchaseInit: EGCItemMsg
k_EMsgGCStorePurchaseInitResponse: EGCItemMsg
k_EMsgGCStorePurchaseInitResponse_DEPRECATED: EGCItemMsg
k_EMsgGCStorePurchaseInit_DEPRECATED: EGCItemMsg
k_EMsgGCStorePurchaseQueryTxn: EGCItemMsg
k_EMsgGCStorePurchaseQueryTxnResponse: EGCItemMsg
k_EMsgGCToGCBannedWordListBroadcast: EGCItemMsg
k_EMsgGCToGCBannedWordListUpdated: EGCItemMsg
k_EMsgGCToGCBroadcastConsoleCommand: EGCItemMsg
k_EMsgGCToGCDirtyMultipleSDOCache: EGCItemMsg
k_EMsgGCToGCDirtySDOCache: EGCItemMsg
k_EMsgGCToGCIsTrustedServer: EGCItemMsg
k_EMsgGCToGCIsTrustedServerResponse: EGCItemMsg
k_EMsgGCToGCUpdateSQLKeyValue: EGCItemMsg
k_EMsgGCToGCWebAPIAccountChanged: EGCItemMsg
k_EMsgGCTradingBase: EGCItemMsg
k_EMsgGCTrading_CancelSession: EGCItemMsg
k_EMsgGCTrading_ConfirmOffer: EGCItemMsg
k_EMsgGCTrading_InitiateTradeRequest: EGCItemMsg
k_EMsgGCTrading_InitiateTradeResponse: EGCItemMsg
k_EMsgGCTrading_ReadinessResponse: EGCItemMsg
k_EMsgGCTrading_RemoveItem: EGCItemMsg
k_EMsgGCTrading_SessionClosed: EGCItemMsg
k_EMsgGCTrading_SetItem: EGCItemMsg
k_EMsgGCTrading_SetReadiness: EGCItemMsg
k_EMsgGCTrading_StartSession: EGCItemMsg
k_EMsgGCTrading_TradeChatMsg: EGCItemMsg
k_EMsgGCTrading_TradeTypingChatMsg: EGCItemMsg
k_EMsgGCTrading_UpdateTradeInfo: EGCItemMsg
k_EMsgGCUnlockCrate: EGCItemMsg
k_EMsgGCUnlockCrateResponse: EGCItemMsg
k_EMsgGCUnlockItemStyle: EGCItemMsg
k_EMsgGCUnlockItemStyleResponse: EGCItemMsg
k_EMsgGCUnwrapGiftRequest: EGCItemMsg
k_EMsgGCUnwrapGiftResponse: EGCItemMsg
k_EMsgGCUpdateItemSchema: EGCItemMsg
k_EMsgGCUseItemRequest: EGCItemMsg
k_EMsgGCUseItemResponse: EGCItemMsg
k_EMsgGCUsedClaimCodeItem: EGCItemMsg
k_EMsgGCUserTrackTimePlayedConsecutively: EGCItemMsg
k_EMsgGCVerifyCacheSubscription: EGCItemMsg
k_EMsgGC_IncrementKillCountAttribute: EGCItemMsg
k_EMsgGC_IncrementKillCountResponse: EGCItemMsg
k_EMsgGC_ReportAbuse: EGCItemMsg
k_EMsgGC_ReportAbuseResponse: EGCItemMsg
k_EMsgGC_RevolvingLootList_DEPRECATED: EGCItemMsg
k_UnlockStyle_Failed_CantAfford: EUnlockStyle
k_UnlockStyle_Failed_CantAffordAttrib: EUnlockStyle
k_UnlockStyle_Failed_CantCommit: EUnlockStyle
k_UnlockStyle_Failed_CantLockCache: EUnlockStyle
k_UnlockStyle_Failed_PreReq: EUnlockStyle
k_UnlockStyle_Succeeded: EUnlockStyle

class CAttribute_String(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class CMsgApplyAutograph(_message.Message):
    __slots__ = ["autograph_item_id", "item_item_id"]
    AUTOGRAPH_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    autograph_item_id: int
    item_item_id: int
    def __init__(self, autograph_item_id: _Optional[int] = ..., item_item_id: _Optional[int] = ...) -> None: ...

class CMsgCasketItem(_message.Message):
    __slots__ = ["casket_item_id", "item_item_id"]
    CASKET_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    casket_item_id: int
    item_item_id: int
    def __init__(self, casket_item_id: _Optional[int] = ..., item_item_id: _Optional[int] = ...) -> None: ...

class CMsgGCGiftedItems(_message.Message):
    __slots__ = ["accountid", "giftdefindex", "max_gifts_possible", "num_eligible_recipients", "recipients_accountids"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    GIFTDEFINDEX_FIELD_NUMBER: _ClassVar[int]
    MAX_GIFTS_POSSIBLE_FIELD_NUMBER: _ClassVar[int]
    NUM_ELIGIBLE_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    giftdefindex: int
    max_gifts_possible: int
    num_eligible_recipients: int
    recipients_accountids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, accountid: _Optional[int] = ..., giftdefindex: _Optional[int] = ..., max_gifts_possible: _Optional[int] = ..., num_eligible_recipients: _Optional[int] = ..., recipients_accountids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCItemCustomizationNotification(_message.Message):
    __slots__ = ["item_id", "request"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    item_id: _containers.RepeatedScalarFieldContainer[int]
    request: int
    def __init__(self, item_id: _Optional[_Iterable[int]] = ..., request: _Optional[int] = ...) -> None: ...

class CMsgGCUserTrackTimePlayedConsecutively(_message.Message):
    __slots__ = ["state"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: int
    def __init__(self, state: _Optional[int] = ...) -> None: ...

class EGCItemMsg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EGCMsgResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EUnlockStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EGCItemCustomizationNotification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
