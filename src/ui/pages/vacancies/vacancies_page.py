from playwright.sync_api import Page

from src.ui.pages.base_page import BasePage
from src.ui.components.navigation.navbar_component import NavbarComponent
from src.ui.components.empty_view_component import EmptyViewComponent
from src.ui.components.filters.filter_component import FilteVacanciesComponent
from src.ui.components.footer_component import FooterComponent
from src.ui.components.header_component import HeaderComponent
from src.ui.components.vacancies.vacancies_list_component import VacanciesListComponent


class VacanciesPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.nav_bar = NavbarComponent(page)
        self.header = HeaderComponent(page, location="Вакансии")
        self.filter_bar = FilteVacanciesComponent(page)
        self.vacancies_list = VacanciesListComponent(page)
        self.empty_view = EmptyViewComponent(page)
        self.footer = FooterComponent(page)
