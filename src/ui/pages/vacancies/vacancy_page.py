import allure
from playwright.sync_api import Page

from src.ui.elements.container import Container
from src.ui.elements.text import Text
from src.ui.pages.base_page import BasePage
from src.ui.components.header_component import HeaderComponent
from src.ui.components.footer_component import FooterComponent
from src.ui.components.navigation.navbar_component import NavbarComponent
from src.ui.components.navigation.breadcrambs_component import BreadcrumbsComponent
from src.ui.components.vacancies.vacancy_response_form_component import (
    VacancyResponseFormComponent,
)
from src.ui.locators import VacancyItemLocators


class VacancyDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.breadcrumbs = BreadcrumbsComponent(page, count_of_elements=3)
        # self.header = HeaderComponent(page, location="Вакансия")
        self.footer = FooterComponent(page)
        self.container = Container.by_xpath(page, *VacancyItemLocators.CONTAINER)
        self.vacancy_name = Text.by_xpath(page, *VacancyItemLocators.VACANCY_NAME)
        self.requirements_heading = Text.by_xpath(
            page, *VacancyItemLocators.REQUIREMENTS_TITLE
        )
        self.expectations_heading = Text.by_xpath(page, *VacancyItemLocators.PLUS_TITLE)
        self.vacancy_response_form = VacancyResponseFormComponent(page)

    @property
    def requirements(self):
        return self.page.locator(VacancyItemLocators.REQUIREMENTS_ITEMS[0])

    @property
    def expectations(self):
        return self.page.locator(VacancyItemLocators.PLUS_ITEMS[0])

    @allure.step("Проверка отображения страницы вакансии")
    def check_visible(self) -> None:
        page_name = self.vacancy_name.get_locator().text_content()
        self.navbar.check_visible()
        self.breadcrumbs.check_visible(page_name)
        self.footer.check_visible()
        self.container.check_visible()
        self.vacancy_response_form.check_visible()

    @allure.step("Проверка заголовка вакансии")
    def check_vacancy_title(self, vacancy_title: str) -> None:
        self.vacancy_name.check_contain_text(vacancy_title)
