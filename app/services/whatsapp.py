import logging

from ...config import (
    WHATSAPP_LOCAL_TOKEN,
    WhatsAppData,
    WhatsAppChange,
    WhatsAppChanges,
    WhatsAppMessage,
    WhatsAppMessages,
    WhatsAppRequest,
)
from ..integrations.whatsapp import post_message

logger = logging.getLogger(__name__)


def authenticate_token(hub_mode: str | None, hub_verify_token: str | None) -> bool:
    return hub_mode == "subscribe" and hub_verify_token == WHATSAPP_LOCAL_TOKEN


def _retrieve_whatsapp_changes(data: WhatsAppData) -> WhatsAppChanges:
    changes: WhatsAppChanges = []

    if len(data.get("entry")) > 0:
        for entry in data.get("entry"):
            changes.extend(entry.get("changes"))

    return changes


def _retrieve_whatsapp_messages(change: WhatsAppChange) -> WhatsAppMessages:
    messages: WhatsAppMessages = []

    if change.get("field") == "messages":
        for message in change.get("value").get("messages"):
            messages.append(message)

    return messages


def get_whatsapp_messages(data: WhatsAppData) -> WhatsAppMessages:
    try:
        changes = _retrieve_whatsapp_changes(data)
        messages: WhatsAppMessages = []

        for change in changes:
            messages.extend(_retrieve_whatsapp_messages(change))

        return messages
    except Exception as e:
        raise Exception("Error retrieving WhatsApp messages from json body") from e


def get_user_id_from_whatsapp_message(message: WhatsAppMessage) -> str:
    return message.get("from")


def get_content_from_whatsapp_message(message: WhatsAppMessage) -> str:
    return message.get("text").get("body")


def send_whatsapp_message(user_id: str, message: str):
    payload: WhatsAppRequest = {
        "message_product": "whatsapp",
        "recipient_type": "individual",
        "to": user_id,
        "type": "text",
        "text": {
            "body": message,
            "preview_url": False,
        },
    }
    try:
        response = post_message(payload)
        return response
    except Exception as e:
        raise Exception("Error sending message to WhatsApp") from e
