import allure
from playwright.sync_api import Page, expect

from src.ui.components.base_component import BaseComponent
from src.ui.elements.container import Container
from src.ui.elements.text import Text
from src.ui.elements.link import Link
from src.ui.locators import BreadcrumbsLocators
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class BreadcrumbsComponent(BaseComponent):
    def __init__(self, page: Page, count_of_elements: int):
        super().__init__(page)

        self.count_of_elements = count_of_elements
        self.items = page.locator(BreadcrumbsLocators.ITEMS)
        self.container = Container.by_xpath(page, *BreadcrumbsLocators.CONTAINER)
        self.home_link = Link.by_xpath(page, *BreadcrumbsLocators.HOME_LINK)
        self.current_page = Text.by_xpath(page, *BreadcrumbsLocators.CURRENT_PAGE)

    @allure.step("Проверка наличия всех элементов хлебных крошек {page_name}")
    def check_visible(self, page_name: str):
        (
            self.should_be_visible()
            .should_contain_home_link()
            .should_have_items_count(self.count_of_elements)
            .should_contain_current_page(page_name)
        )

    def should_be_visible(self):
        self.container.check_visible()
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
        self.current_page.check_visible()
        current_page_text = self.current_page.get_locator().inner_text().strip().lower()
        step = f"Проверка текста названия текущей страницы {current_page_text} c {page_name.lower()}"
        with allure.step(step):
            logger.info(step)
            assert (
                current_page_text == page_name.lower()
            ), f"Название текущей страницы ({current_page_text}) не соответсвует ожидаемому: {page_name}"
        return self

    @allure.step(
        "Проверка, что текущая страница в хлебных крошках не является кликабельной"
    )
    def should_current_page_not_be_clickable(self):
        """
        Проверяет, что элемент текущей страницы:
        - не является ссылкой (<a>)
        - не имеет атрибута href
        - не кликабелен (ожидаем, что click() вызовет исключение)
        """
        current_locator = self.current_page.get_locator()
        href_value = current_locator.get_attribute("href")
        logger.info("Проверка, атрибут 'href' елемента текущей хлебной крошки")
        assert (
            href_value is None
        ), f"Текущая страница имеет атрибут 'href' со значением: {href_value}"
        tag_name = current_locator.evaluate("el => el.tagName.toLowerCase()")

        logger.info("Проверка, что элемент текущей хлебной крошки не является ссылкой")
        assert (
            tag_name != "a"
        ), f"Текущая страница является ссылкой (<a>), что недопустимо. Тег: <{tag_name}>"
