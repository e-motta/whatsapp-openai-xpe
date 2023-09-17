from typing import Any
import openai

from ..config import OPENAI_API_KEY, OpenAIMessages
from .utils import exponential_backoff_retry

openai.api_key = OPENAI_API_KEY


@exponential_backoff_retry(max_retries=3)
def generate_chat_completion(messages: OpenAIMessages) -> dict[Any, Any]:
    return openai.ChatCompletion.create(  # type: ignore
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
    )
