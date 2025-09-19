import re
from typing import Self

import allure
from playwright.sync_api import Page

from src.ui.components.base_component import BaseComponent
from src.ui.elements.icon import Icon
from src.ui.elements.link import Link
from src.ui.elements.text import Text
from src.ui.locators import FooterLocators


class FooterComponent(BaseComponent):
    """Класс компонента футера.

    Attributes:
        info (Text): Элемент, отображающий информацию о компании.
        user_agreement_link (Link): Ссылка на пользовательское соглашение.
        privacy_policy_link (Link): Ссылка на политику конфиденциальности.
        main_page_link (Link): Ссылка на главную страницу.
        footer_icon (Icon): Иконка футера.
    """

    def __init__(self, page: Page):
        """Инициализация компонента футера."""
        super().__init__(page)

        self.info = Text.by_xpath(page, *FooterLocators.INFO)
        self.user_agreement_link = Link.by_xpath(
            page, *FooterLocators.USER_AGREEMENT_LINK
        )
        self.privacy_policy_link = Link.by_xpath(
            page, *FooterLocators.PRIVACY_POLICY_LINK
        )
        self.main_page_link = Link.by_xpath(page, *FooterLocators.MAIN_PAGE_LINK)
        self.footer_icon = Icon.by_xpath(page, *FooterLocators.ICON)

    def should_contain_copyright(self, years="2018 - 2025") -> Self:
        """Проверяет наличие копирайта."""
        self.info.check_contain_text(f"© {years}")
        return self

    def should_contain_inn(self, inn="9709037529") -> Self:
        """Проверяет наличие ИНН."""
        self.info.check_contain_text(f"ИНН: {inn}")
        return self

    def should_have_all_links(self) -> Self:
        """Проверяет наличие всех ссылок."""
        self.user_agreement_link.check_visible()
        self.privacy_policy_link.check_visible()
        self.main_page_link.check_visible()
        return self

    def should_have_icon(self) -> Self:
        """Проверяет наличие иконки."""
        self.footer_icon.check_visible()
        self.footer_icon.check_visible()
        return self

    @allure.step("Проверка наличия всех элементов в футере")
    def check_visible(self) -> Self:
        """Проверяет, что все элементы футера видимы."""
        (
            self.should_contain_copyright()
            .should_contain_inn()
            .should_have_all_links()
            .should_have_icon()
        )

        return self

    @allure.step("Проверка перехода на главную страницу")
    def navigate_to_main_page(self):
        """Проверяет переход на главную страницу."""
        self.main_page_link.check_visible().click()
        self.check_current_url(re.compile("/"))

    @allure.step("Проверка скачивания файла политики конфиденциальности")
    def check_download_privacy_policy(
        self, file_name: str = "Политика конфиденциальности.pdf"
    ):
        self.privacy_policy_link.check_download_file(file_name)

    @allure.step("Проверка скачивания файла пользовательского соглашения")
    def check_download_user_agreement(
        self, file_name: str = "Пользовательское_соглашение.pdf"
    ):
        self.user_agreement_link.check_download_file(file_name)
