import time
import requests
from functools import wraps
from typing import Any, Callable
import logging

logger = logging.getLogger(__name__)


def exponential_backoff_retry(max_retries: int = 3):
    def decorator(func: Callable[..., Any]):
        @wraps(func)
        def retry_with_backoff(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            while retries <= max_retries:
                try:
                    response = func(*args, **kwargs)
                    if isinstance(response, requests.models.Response):
                        response.raise_for_status()
                    return response
                except Exception as e:
                    logger.error(f"Error making request: {str(e)}")
                    retries += 1
                    wait_time = 2**retries
                    if retries <= max_retries:
                        logger.info(f"Retrying in {wait_time} seconds...")
                        time.sleep(wait_time)
            raise Exception("Max retries reached")

        return retry_with_backoff

    return decorator
