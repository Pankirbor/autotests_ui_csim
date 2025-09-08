from playwright.sync_api import Page, expect
from src.ui.components.base_component import BaseComponent
from src.ui.elements.container import Container
from src.ui.elements.text import Text
from src.ui.locators import VacanciesListLocators


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = Container.by_xpath(page, *VacanciesListLocators.CONTAINER)
        self.title = Text.by_xpath(page, *VacanciesListLocators.EMPTY_VIEW_TITLE)
        self.description = Text.by_xpath(
            page, *VacanciesListLocators.EMPTY_VIEW_DESCRIPTION
        )

    # Базовые проверки
    def should_be_visible(self):
        """Проверяет что компонент пустого состояния видим"""
        self.container.check_visible()
        return self

    def should_not_be_visible(self):
        """Проверяет что компонент пустого состояния не видим"""
        expect(self.container).to_be_hidden()
        return self

    # Проверка содержимого
    def should_have_title(self, expected_title: str = None):
        """Проверяет заголовок пустого состояния"""
        self.title.check_visible()
        if expected_title:
            self.title.check_contain_text(expected_title)
        return self

    def should_have_description(self, expected_description: str = None):
        """Проверяет описание пустого состояния"""
        self.description.check_visible()
        if expected_description:
            self.description.check_contain_text(expected_description)
        return self

    def should_contain_text(self, text: str):
        """Проверяет что компонент содержит текст"""
        expect(self.container).to_contain_text(text)
        return self

    # Получение данных
    def get_title_text(self) -> str:
        """Возвращает текст заголовка"""
        return (
            self.title.get_locator().get_text()
            if self.title.get_locator().count() > 0
            else ""
        )

    def get_description_text(self) -> str:
        """Возвращает текст описания"""
        return (
            self.description.get_locator().get_text()
            if self.description.get_locator().count() > 0
            else ""
        )

    def get_full_text(self) -> str:
        """Возвращает полный текст компонента"""
        return (
            self.container.get_locator().inner_text()
            if self.container.get_locator().count() > 0
            else ""
        )

    # Проверки состояния
    def is_displayed(self) -> bool:
        """Проверяет отображается ли компонент пустого состояния"""
        return self.container.get_locator().is_visible()

    def take_screenshot(self, name: str = "empty_state"):
        """Делает скриншот пустого состояния"""
        if self.is_displayed():
            self.container.get_locator().screenshot(path=f"{name}.png")
        return self

    def verify_complete_empty_state(
        self, expected_title: str = None, expected_description: str = None
    ):
        """Комплексная проверка пустого состояния"""
        (
            self.should_be_visible()
            .should_have_title(expected_title)
            .should_have_description(expected_description)
        )
        return self
