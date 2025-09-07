import allure
from playwright.sync_api import Page, expect

from src.ui.components.base_component import BaseComponent
from src.ui.elements.text import Text
from src.ui.elements.link import Link
from src.ui.locators import BreadcrumbsLocators


class BreadcrumbsComponent(BaseComponent):

    def __init__(self, page: Page, count_of_elements: int, page_name: str):
        super().__init__(page)

        self.count_of_elements = (count_of_elements,)
        self.page_name = page_name
        self.container = page.locator(BreadcrumbsLocators.CONTAINER)
        self.items = page.locator(BreadcrumbsLocators.ITEMS)

        # Основные элементы
        self.home_link = Link.by_xpath(
            page=page,
            xpath=BreadcrumbsLocators.HOME_LINK,
            name="Ссылка на главную",
        )

        self.current_page = Text.by_xpath(
            page=page,
            xpath=BreadcrumbsLocators.CURRENT_PAGE,
            name="Текущая страница",
        )

    #! проверка гипотезы
    @allure.step("Проверка наличия всех элементов хлебных крошек {self.page_name}")
    def check_visible(self):
        (
            self.should_be_visible()
            .should_contain_home_link()
            .should_have_items_count(self.count_of_elements)
            .should_contain_current_page(self.page_name)
        )

    def should_be_visible(self):
        expect(self.container).to_be_visible()
        return self

    def get_all_items(self):
        """Возвращает все элементы хлебных крошек"""
        return self.items.all()

    def get_items_text(self):
        """Возвращает текст всех элементов"""
        return [item.inner_text().strip() for item in self.get_all_items()]

    def should_have_items_count(self, count):
        """Проверяет количество элементов"""
        expect(self.items).to_have_count(count)
        return self

    def should_contain_home_link(self):
        """Проверяет наличие ссылки на главную"""
        self.home_link.check_visible().check_contain_text("Главная")
        return self

    def should_contain_current_page(self, page_name):
        """Проверяет текущую страницу"""
        self.current_page.check_visible().check_contain_text(page_name)
        return self
