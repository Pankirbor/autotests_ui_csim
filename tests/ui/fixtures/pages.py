import pytest
from playwright.sync_api import Page

from src.ui.pages.vacancies.vacancies_page import VacanciesPage


@pytest.fixture
def vacancies_page(chromium_page_with_state: Page) -> VacanciesPage:
    """
    Фикстура для страницы вакансий

    Args:
        chromium_page_with_state (Page): страница с состоянием

    Returns:
        VacanciesPage: страница вакансий
    """
    return VacanciesPage(chromium_page_with_state)
