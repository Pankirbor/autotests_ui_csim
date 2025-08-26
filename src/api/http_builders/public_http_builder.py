from functools import lru_cache

from httpx import AsyncClient, Client

from api.event_hooks import (
    curl_event_hook,
    log_request_event_hook,
    log_response_event_hook,
)
from config import settings
from src.api.schemas.authentication import AuthenticationUserSchema


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    Args:
        user (AuthenticationUserSchema): Данные пользователя для входа.

    Returns:
        Client: Объект httpx.Client с настроенным заголовком авторизации.
    """


@lru_cache(maxsize=None)
def get_private_async_http_client(user: AuthenticationUserSchema) -> AsyncClient:
    """
    Функция создаёт экземпляр httpx.AsyncClient с аутентификацией пользователя.

    Args:
        user (AuthenticationUserSchema): Данные пользователя для входа.

    Returns:
        AsyncClient: Объект httpx.AsyncClient с настроенным заголовком авторизации.
    """
