from typing import Any

import allure
from httpx import AsyncClient, Response, QueryParams, URL


class AsyncApiClient:
    """Асинхронный клиент для взаимодействия с внешним API."""

    def __init__(self, client: AsyncClient):
        """
        Инициализирует экземпляр класса AsyncApiClient.

        Args:
            client (AsyncClient): Асинхронный клиент HTTP.
        """
        self.client = client

    @allure.step("Отправляем GET-запрос на {url}")
    async def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Асинхронно отправляет HTTP GET-запрос на указанный URL.

        Args:
            url (URL | str): Адрес, по которому выполняется запрос.
            params (QueryParams | None): Параметры запроса.

        Returns:
            Response: Ответ сервера в виде объекта Response.
        """
        return await self.client.get(url=url, params=params)

    @allure.step("Отправляем POST-запрос на {url}")
    async def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: Any | None = None,
        files: Any | None = None,
    ) -> Response:
        """
        Асинхронно отправляет HTTP POST-запрос на указанный URL.

        Args:
            url (URL | str): Адрес, по которому выполняется запрос.
            json: Any | None: Данные в формате JSON.
            data: RequestData | None: Форматированные данные формы (например, application/x-www-form-urlencoded).
            files: RequestFile | None: Файлы для загрузки на сервер.

        Returns:
            Response: Ответ сервера в виде объекта Response.
        """
        return await self.client.post(url=url, json=json, data=data, files=files)

    @allure.step("Отправляем PATCH-запрос на {url}")
    async def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Асинхронно отправляет HTTP PATCH-запрос на указанный URL.

        Args:
            url (URL | str): Адрес, по которому выполняется запрос.
            json: Any | None: Данные для обновления в формате JSON.

        Returns:
            Response: Ответ сервера в виде объекта Response.
        """

        return await self.client.patch(url=url, json=json)

    @allure.step("Отправляем DELETE-запрос на {url}")
    async def delete(self, url: URL | str) -> Response:
        """
        Асинхронно отправляет HTTP DELETE-запрос на указанный URL.

        Args:
            url (URL | str): Адрес, по которому выполняется запрос.

        Returns:
            Response: Ответ сервера в виде объекта Response.
        """

        return await self.client.delete(url=url)
