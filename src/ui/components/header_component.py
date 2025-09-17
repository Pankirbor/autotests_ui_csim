from playwright.sync_api import Page

from src.ui.components.base_component import BaseComponent
from src.ui.elements.text import Text
from src.ui.locators import HeaderPageLocators


class HeaderComponent(BaseComponent):
    """Класс представления компонента заголовка страницы.

    Attributes:
        title (Text): заголовок страницы
        subtitle (Text): подзаголовок страницы
    """

    def __init__(self, page: Page, location: str):
        """Инициализация компонента заголовка страницы."""
        super().__init__(page)

        self.title = Text.by_xpath(
            page,
            *HeaderPageLocators.TITLE.format(location=location),
        )
        self.subtitle = Text.by_xpath(
            page,
            *HeaderPageLocators.SUBTITLE.format(location=location),
        )

    def check_visible(self):
        """Проверяет, что компонент видим."""
        super().check_visible()
        self.title.check_visible()
        self.subtitle.check_visible()
