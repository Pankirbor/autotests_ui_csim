from playwright.sync_api import Page, expect
from src.ui.components.base_component import BaseComponent
from src.ui.elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Контейнер пустого состояния
        self.container = page.locator(".not_found")

        # Элементы пустого состояния
        self.title = Text.by_xpath(
            page=page,
            xpath="//div[@class='not_found']//h3",
            name="Заголовок пустого состояния",
        )

        self.description = Text.by_xpath(
            page=page,
            xpath="//div[@class='not_found']//p",
            name="Описание пустого состояния",
        )

    # Базовые проверки
    def should_be_visible(self):
        """Проверяет что компонент пустого состояния видим"""
        expect(self.container).to_be_visible()
        return self

    def should_not_be_visible(self):
        """Проверяет что компонент пустого состояния не видим"""
        expect(self.container).to_be_hidden()
        return self

    # Проверка содержимого
    def should_have_title(self, expected_title: str = None):
        """Проверяет заголовок пустого состояния"""
        expect(self.title.locator).to_be_visible()
        if expected_title:
            expect(self.title.locator).to_have_text(expected_title)
        return self

    def should_have_description(self, expected_description: str = None):
        """Проверяет описание пустого состояния"""
        expect(self.description.locator).to_be_visible()
        if expected_description:
            expect(self.description.locator).to_contain_text(expected_description)
        return self

    def should_contain_text(self, text: str):
        """Проверяет что компонент содержит текст"""
        expect(self.container).to_contain_text(text)
        return self

    # Получение данных
    def get_title_text(self) -> str:
        """Возвращает текст заголовка"""
        return self.title.get_text() if self.title.locator.count() > 0 else ""

    def get_description_text(self) -> str:
        """Возвращает текст описания"""
        return (
            self.description.get_text() if self.description.locator.count() > 0 else ""
        )

    def get_full_text(self) -> str:
        """Возвращает полный текст компонента"""
        return self.container.inner_text() if self.container.count() > 0 else ""

    # Проверки состояния
    def is_displayed(self) -> bool:
        """Проверяет отображается ли компонент пустого состояния"""
        return self.container.is_visible()

    def take_screenshot(self, name: str = "empty_state"):
        """Делает скриншот пустого состояния"""
        if self.is_displayed():
            self.container.screenshot(path=f"{name}.png")
        return self

    def verify_complete_empty_state(
        self, expected_title: str = None, expected_description: str = None
    ):
        """Комплексная проверка пустого состояния"""
        self.should_be_visible().should_have_title(
            expected_title
        ).should_have_description(expected_description)
        return self
