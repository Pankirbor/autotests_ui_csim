import allure
from playwright.sync_api import Page

from src.ui.components.empty_view_component import EmptyViewComponent
from src.ui.components.filters.filter_component import FilterVacanciesComponent
from src.ui.components.footer_component import FooterComponent
from src.ui.components.header_component import HeaderComponent
from src.ui.components.navigation.breadcrambs_component import BreadcrumbsComponent
from src.ui.components.navigation.navbar_component import NavbarComponent
from src.ui.components.vacancies.vacancies_list_component import VacanciesListComponent
from src.ui.locators import VacanciesListLocators
from src.ui.pages.base_page import BasePage
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class VacanciesPage(BasePage):
    """Страница списка вакансий."""

    def __init__(self, page: Page) -> None:
        """Инициализирует страницу вакансии.

        Args:
            page (Page): Экземпляр страницы браузера.
        """
        super().__init__(page)
        self.nav_bar = NavbarComponent(page)
        self.header = HeaderComponent(page, location="Вакансии")
        self.breadcrumbs = BreadcrumbsComponent(page, count_of_elements=2)

        self.filter_bar = FilterVacanciesComponent(page)
        self.vacancies_list = VacanciesListComponent(page)
        self.empty_view = EmptyViewComponent(page)
        self.footer = FooterComponent(page)

    @allure.step("Проверка сброса фильтров в меню кнопки 'Фильтр'")
    def verify_filter_reset_functionality(self, checkboxes_to_choose: list[str]):
        """Проверяет, что выбранные фильтры корректно сбрасываются при нажатии кнопки "Сбросить".

        Args:
            checkboxes_to_choose (list[str]): Список меток чекбоксов для выбора.

        """
        filter_menu = self.filter_bar.filter_menu
        filter_menu.check_not_visible()
        self.filter_bar.filter_menu_btn.click()
        (
            filter_menu.check_visible()
            .select_filters(checkboxes_to_choose)
            .are_filters_selected(checkboxes_to_choose)
            .reset_btn.click()
        )
        filter_menu.check_not_visible()
        self.filter_bar.filter_menu_btn.click()
        filter_menu.check_visible().check_filter_reset()

    @allure.step("Проверка применения фильтров в меню кнопки 'Фильтр'")
    def apply_specified_filters_and_verify(self, checkboxes_to_choose: list[str]):
        """Применяет указанные фильтры и проверяет, что они отображаются в меню фильтров.

        Args:
            checkboxes_to_choose (list[str]): Список меток чекбоксов для выбора.
        """
        initial_count_of_vacancies = self.vacancies_list.get_vacancies_count()

        filter_menu = self.filter_bar.filter_menu
        try:
            filter_menu.check_not_visible()
            self.filter_bar.filter_menu_btn.click()
        except AssertionError:
            logger.warning("Меню фильтров уже открыто.")

        (
            filter_menu.check_visible()
            .select_filters(checkboxes_to_choose)
            .are_filters_selected(checkboxes_to_choose)
            .apply_btn.click()
        )
        filter_menu.check_not_visible()
        self.vacancies_list.container.check_less_or_equal_count_elements(
            VacanciesListLocators.VACANCY_CARDS[0], initial_count_of_vacancies
        )

    @allure.step("Проверка фильтрации вакансий при переключении по всем вкладкам категорий")
    def verify_filtering_by_all_category_tabs(self):
        """Проверяет фильтрацию вакансий при переключении по всем вкладкам категорий."""
        initial_count = self.vacancies_list.get_vacancies_count()

        for tab in self.filter_bar.tabs:
            with allure.step(f"Применяем фильтр: {tab.name}"):
                tab.click()
                tab.is_active()
                self.vacancies_list.container.check_less_or_equal_count_elements(
                    VacanciesListLocators.VACANCY_CARDS[0], initial_count
                )
