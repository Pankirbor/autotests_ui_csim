from playwright.sync_api import Page
import pytest

from src.ui.pages.vacancies.vacancies_page import VacanciesPage
from src.ui.pages.vacancies.vacancy_page import VacancyDetailPage


@pytest.fixture
def vacancies_page(chromium_page_with_state: Page) -> VacanciesPage:
    """Фикстура для страницы вакансий.

    Args:
        chromium_page_with_state (Page): страница с состоянием

    Returns:
        VacanciesPage: страница вакансий
    """
    return VacanciesPage(chromium_page_with_state)


@pytest.fixture
def vacancy_detail_page(chromium_page_with_state: Page) -> VacancyDetailPage:
    """Фикстура для страницы детальной информации овакансии.

    Args:
        chromium_page_with_state (Page): страница с состоянием

    Returns:
        VacanciesPage: страница вакансии
    """
    return VacancyDetailPage(chromium_page_with_state)
