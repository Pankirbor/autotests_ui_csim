from typing import Pattern

import allure

from playwright.sync_api import Page, expect
from src.utils.logger import get_logger


logger = get_logger(__name__.upper())


class BasePage:
    """
    Базовый класс для всех страниц веб-приложения.

    Этот класс содержит общие методы, такие как переход на страницу,
    перезагрузка страницы и проверки видимости элементов и их содержимого.

    Attributes:
        page (Page): Экземпляр страницы браузера.

    Methods:
        visit: Переходит на указанную URL-адрес.
        reload: Перезагружает текущую страницу.
        check_current_url: Проверяет, что текущий URL соответствует ожидаемому.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализирует базовый класс страницы.

        Args:
            page (Page): Экземпляр страницы браузера.
        """
        self.page = page

    # todo убрать локаторы в файл locators.py
    def accept_cookies_if_present(self) -> None:
        """Принимает куки, если диалог виден."""
        cookies_dialog = self.page.locator(".cookie-dialog")
        accept_button = self.page.locator(".cookie-dialog button:has-text('Принять')")

        cookies_dialog.wait_for(state="visible", timeout=10000)
        if cookies_dialog.is_visible():
            if accept_button.is_visible():
                accept_button.click()
                logger.info("Куки приняты")
                self.page.wait_for_timeout(1000)

    def visit(self, url: str) -> None:
        """
        Открывает указанную URL-страницу и ждет завершения загрузки.

        Args:
            url (str): Адрес страницы, на которую нужно перейти.
        """
        step = f"Opening the url: '{url}'"
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle", timeout=50000)
            self.accept_cookies_if_present()

    def reload(self) -> None:
        """
        Перезагружает текущую страницу и ждет загрузки контента DOM.
        """
        step = f"Reload page with url: '{self.page.url}'"
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]) -> None:
        """
        Проверяет, что текущий URL совпадает с ожидаемым.

        Args:
            expected_url (Pattern[str]): Регулярное выражение или строка ожидаемого URL.
        """
        step = f"Checking that current url matches pattern '{expected_url.pattern}'"
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
