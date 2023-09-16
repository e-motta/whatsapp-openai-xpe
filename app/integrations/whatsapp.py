import requests

from ..config import WhatsAppRequest, WHATSAPP_API_URL, WHATSAPP_BEARER_TOKEN
from .utils import exponential_backoff_retry


@exponential_backoff_retry(max_retries=0)
def post_message(payload: WhatsAppRequest) -> requests.models.Response:
    headers = {
        "Authorization": f"Bearer {WHATSAPP_BEARER_TOKEN}",
        "Content-Type": "application/json",
    }

    return requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
