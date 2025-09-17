from re import Pattern

import allure
from playwright.sync_api import Page, expect
import pytest

from src.ui.locators.cookies import CookiesLocators
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class BasePage:
    """Базовый класс для всех страниц веб-приложения.

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
        """Инициализирует базовый класс страницы.

        Args:
            page (Page): Экземпляр страницы браузера.
        """
        self.page = page

    def accept_cookies_if_present(self) -> None:
        """Принимает куки, если диалог виден."""
        cookies_dialog = self.page.locator(CookiesLocators.CONTAINER.selector)
        accept_button = self.page.locator(CookiesLocators.ACCEPT_BUTTON.selector)

        cookies_dialog.wait_for(state="visible", timeout=10000)
        if cookies_dialog.is_visible():
            if accept_button.is_visible():
                accept_button.click()
                logger.info("Куки приняты")
                self.page.wait_for_timeout(1000)

    def visit(self, url: str) -> None:
        """Открывает указанную URL-страницу и ждет завершения загрузки.

        Args:
            url (str): Адрес страницы, на которую нужно перейти.
        """
        step = f"Переход на страницу: '{url}'"
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle", timeout=50000)
            self._check_for_captcha_page()
            self.accept_cookies_if_present()

    def reload(self) -> None:
        """Перезагружает текущую страницу и ждет загрузки контента DOM."""
        step = f"Обновление страницы: '{self.page.url}'"
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]) -> None:
        """Проверяет, что текущий URL совпадает с ожидаемым.

        Args:
            expected_url (Pattern[str]): Регулярное выражение или строка ожидаемого URL.
        """
        step = f"Checking that current url matches pattern '{expected_url.pattern}'"
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)

    def _check_for_captcha_page(self) -> None:
        """
        Проверяет, открылась ли страница защиты от ботов (CAPTCHA).

        Если обнаружена — пропускает тест с понятным сообщением и прикрепляет скриншот кAllure.
        """
        # Получаем содержимое страницы
        page_content = self.page.content()

        # Ищем ключевые фразы
        captcha_patterns = [
            "Checking your browser before accessing cism-ms.ru",
            "Sorry, we could not verify your browser automatically",
            "Complete the manual check to continue",
        ]

        if any(pattern in page_content for pattern in captcha_patterns):
            logger.warning("⚠️ Обнаружена CAPTCHA-страница")
            screenshot = self.page.screenshot()
            allure.attach(
                screenshot,
                name="CAPTCHA PageDetected",
                attachment_type=allure.attachment_type.PNG,
            )
            pytest.skip(
                "Тест пропущен: обнаружена страница защиты от ботов. "
                "Сайт блокирует автоматизированные запросы с IP GitHub Actions. "
            )
