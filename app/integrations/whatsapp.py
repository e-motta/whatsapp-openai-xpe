import requests

from ..config import WhatsAppRequest, WHATSAPP_API_URL
from .utils import exponential_backoff_retry


@exponential_backoff_retry(max_retries=3)
def post_message(payload: WhatsAppRequest) -> requests.models.Response:
    headers = {
        "Content-Type": "application/json",
    }

    return requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
