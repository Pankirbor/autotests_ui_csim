from playwright.sync_api import Page

from src.ui.components.base_component import BaseComponent
from src.ui.elements.text import Text
from src.ui.locators import HeaderPageLocators


class HeaderComponent(BaseComponent):
    def __init__(self, page: Page, location: str):
        super().__init__(page)

        self.title = Text.by_xpath(
            page=page,
            xpath=HeaderPageLocators.TITLE,
            name=f"Заголовок страницы {location}",
        )
        self.subtitle = Text.by_xpath(
            page=page,
            xpath=HeaderPageLocators.SUBTITLE,
            name=f"Подзаголовок страницы {location}",
        )

    def check_visible(self):
        self.title.check_visible()
        self.subtitle.check_visible()
