from typing import Literal, TypedDict


# OpenAI
OpenAIRole = Literal["system", "assistant", "user"]
OpenAIContent = str
OpenAIMessage = TypedDict(
    "Message",
    {
        "role": OpenAIRole,
        "content": OpenAIContent,
    },
)
OpenAIMessages = list[OpenAIMessage]


# Get request from WhatsApp
WhatsAppText = TypedDict("WhatsappText", {"body": str})
WhatsAppMessage = TypedDict(
    "WhatsappMessage",
    {
        "from": str,
        "id": str,
        "timestamp": int,
        "text": WhatsAppText,
        "type": str,
    },
)
WhatsAppMessages = list[WhatsAppMessage]
WhatsAppProfile = TypedDict(
    "WhatsappProfile",
    {
        "name": str,
    },
)
WhatsAppContact = TypedDict(
    "WhatsappContact",
    {
        "profile": WhatsAppProfile,
        "wa_id": str,
    },
)
WhatsAppContacts = list[WhatsAppContact]
WhatsAppMetadata = TypedDict(
    "WhatsappMetadata",
    {
        "display_phone_number": str,
        "phone_number_id": str,
    },
)
WhatsAppMessagingProduct = str
WhatsAppValue = TypedDict(
    "WhatsappValue",
    {
        "messaging_product": WhatsAppMessagingProduct,
        "metadata": WhatsAppMetadata,
        "contacts": WhatsAppContacts,
        "messages": WhatsAppMessages,
    },
)
WhatsAppChange = TypedDict(
    "WhatsappChange",
    {
        "value": WhatsAppValue,
        "field": str,
    },
)
WhatsAppChanges = list[WhatsAppChange]
WhatsAppID = str
WhatsAppEntry = TypedDict(
    "WhatsappEntry",
    {
        "id": WhatsAppID,
        "changes": WhatsAppChanges,
    },
)
WhatsAppEntries = list[WhatsAppEntry]
WhatsAppObject = str
WhatsAppData = TypedDict(
    "WhatsappData",
    {
        "object": WhatsAppObject,
        "entry": WhatsAppEntries,
    },
)

# Send message to WhatsApp
WhatsAppRequestTextBody = TypedDict(
    "WhatsAppRequestTextBody",
    {
        "body": str,
        "preview_url": bool,
    },
)
WhatsAppRequest = TypedDict(
    "WhatsAppRequest",
    {
        "message_product": Literal["whatsapp"],
        "recipient_type": Literal["individual"],
        "to": str,
        "type": Literal["text"],
        "text": WhatsAppRequestTextBody,
    },
)
