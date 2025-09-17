from functools import cache

from httpx import AsyncClient, Client

from src.api.schemas.authentication import AuthenticationUserSchema


@cache
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    Args:
        user (AuthenticationUserSchema): Данные пользователя для входа.

    Returns:
        Client: Объект httpx.Client с настроенным заголовком авторизации.
    """


@cache
def get_private_async_http_client(user: AuthenticationUserSchema) -> AsyncClient:
    """Функция создаёт экземпляр httpx.AsyncClient с аутентификацией пользователя.

    Args:
        user (AuthenticationUserSchema): Данные пользователя для входа.

    Returns:
        AsyncClient: Объект httpx.AsyncClient с настроенным заголовком авторизации.
    """
