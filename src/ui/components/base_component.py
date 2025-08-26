from typing import Pattern

import allure
from playwright.sync_api import expect, Locator, Page
from src.utils.logger import get_logger


logger = get_logger(__name__.upper())


class BaseComponent:
    """
    Базовый класс для всех компонентов пользовательского интерфейса.

    Этот класс предоставляет общие методы для проверки видимости элементов,
    их текстового содержимого, значения ввода и текущего URL страницы.

    Attributes:
        page (Page): Экземпляр страницы браузера.

    Methods:
        check_current_url: Проверяет, что текущий URL соответствует ожидаемому.
        check_locator: Проверяет видимость локатора и его текстовое содержимое.
        check_input_locator: Проверяет видимость поля ввода и его значение.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализирует базовый компонент.

        Args:
            page (Page): Экземпляр страницы браузера.
        """
        self.page = page

    def check_current_url(self, url: Pattern[str]) -> None:
        """
        Проверяет, что текущий URL совпадает с ожидаемым.

        Args:
            url (Pattern[str]): Регулярное выражение или строка ожидаемого URL.
        """
        step = f"Checking that current url matches pattern '{url.pattern}'"
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(url)

    def check_locator(self, locator: Locator, text: str | None = None) -> None:
        """
        Проверяет видимость элемента и его текстовое содержимое.

        Args:
            locator (Locator): Локатор элемента на странице.
            text (str | None): Ожидаемый текст элемента. Если None — только проверяется видимость.
        """
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_text(text)

    def check_input_locator(self, locator: Locator, text: str | None) -> None:
        """
        Проверяет видимость поля ввода и его значение.

        Args:
            locator (Locator): Локатор поля ввода.
            value (str): Ожидаемое значение в поле ввода.
        """
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_value(text)
