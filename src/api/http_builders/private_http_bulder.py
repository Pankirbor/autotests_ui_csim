from httpx import AsyncClient, Client

from api.event_hooks import (
    curl_event_hook,
    log_request_event_hook,
    log_response_event_hook,
)
from config import settings


def get_public_http_client() -> Client:
    """Функция создаёт экземпляр httpx.Client с базовыми настройками.

    Returns:
        Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout=settings.HTTP_CLIENT.TIMEOUT,
        base_url=settings.HTTP_CLIENT.url_as_string,
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],
            "response": [log_response_event_hook],
        },
    )


def get_public_async_http_client() -> AsyncClient:
    """Функция создаёт экземпляр httpx.AsyncClient с базовыми настройками.

    Returns:
        Готовый к использованию объект httpx.AsyncClient.
    """
    return AsyncClient(
        timeout=settings.HTTP_CLIENT.TIMEOUT,
        base_url=settings.HTTP_CLIENT.url_as_string,
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],
            "response": [log_response_event_hook],
        },
    )
