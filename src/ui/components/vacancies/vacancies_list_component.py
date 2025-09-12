from datetime import datetime
from typing import List, Dict

import allure
from playwright.sync_api import Page, expect

from src.ui.components.base_component import BaseComponent
from src.ui.elements.container import Container
from src.ui.elements.icon import Icon
from src.ui.elements.link import Link
from src.ui.elements.text import Text
from src.ui.locators import VacanciesListLocators
from src.utils.logger import get_logger, console

logger = get_logger(__name__.upper())


class VacanciesListComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Контейнер списка
        self.container = Container.by_xpath(self.page, *VacanciesListLocators.CONTAINER)

        # Карточки вакансий
        # self.vacancy_cards = page.locator(VacanciesListLocators.VACANCY_CARDS[0])

        # Элементы карточки
        self.card_title = Text.by_xpath(self.page, *VacanciesListLocators.CARD_TITLE)
        self.card_date = Text.by_xpath(self.page, *VacanciesListLocators.CARD_DATE)
        self.card_link = Link.by_xpath(self.page, *VacanciesListLocators.CARD_LINK)
        self.card_icon = Icon.by_xpath(self.page, *VacanciesListLocators.CARD_ICON)

    @property
    def vacancy_cards(self):
        return self.page.locator(VacanciesListLocators.VACANCY_CARDS[0])

    # Базовые проверки
    def check_visible(self):
        self.container.check_visible()
        return self

    def should_have_vacancies(self, min_count=1):
        """Проверяет что есть вакансии"""
        expect(self.vacancy_cards).to_have_count(min_count, timeout=10000)
        return self

    # Работа с карточками
    def get_all_vacancies(self):
        """Возвращает все карточки вакансий"""
        return self.vacancy_cards.all()

    def get_vacancies_count(self):
        """Возвращает количество вакансий"""
        return self.vacancy_cards.count()

    def get_vacancy_by_index(self, index: int):
        """Возвращает карточку по индексу"""
        return self.vacancy_cards.nth(index)

    def get_vacancy_by_title(self, title: str):
        """Возвращает карточку по названию"""
        return self.vacancy_cards.filter(has_text=title).first

    # Получение данных
    def get_vacancy_data(self, index: int = 0) -> Dict:
        """Возвращает данные вакансии по индексу"""
        vacancy = self.get_vacancy_by_index(index)
        return {
            "title": self.card_title.get_locator(nth=index).inner_text().strip(),
            "date": self.card_date.get_locator(nth=index).get_attribute("datetime")
            or self.card_date.get_locator(nth=index).inner_text().strip(),
            "link": self.card_link.get_locator(nth=index).get_attribute("href"),
            "element": vacancy,
        }

    def get_all_vacancies_data(self) -> List[Dict]:
        """Возвращает данные всех вакансий"""
        vacancies_data = []
        for i in range(self.get_vacancies_count()):
            vacancies_data.append(self.get_vacancy_data(i))
        return vacancies_data

    def get_vacancies_titles(self) -> List[str]:
        """Возвращает список названий вакансий"""
        return [
            self.card_title.get_locator(nth=ind).inner_text().strip()
            for ind in range(self.get_vacancies_count())
        ]

    @allure.step(
        "Проверяем, что при наведении на карточку вакансии меняется цвет фона и текста"
    )
    def check_hover_on_vacancy(self, index: int = 1):
        vacancy = self.get_vacancy_by_index(index)
        bg_before = vacancy.evaluate(
            "el => window.getComputedStyle(el).backgroundColor"
        )
        color_before = vacancy.evaluate("el => window.getComputedStyle(el).color")

        vacancy.hover()
        self.page.wait_for_timeout(1000)
        bg_after = vacancy.evaluate("el => window.getComputedStyle(el).backgroundColor")
        color_after = vacancy.evaluate("el => window.getComputedStyle(el).color")
        logger.info(
            "Проверяем, что цвет текста и фон карточки вакансии меняется при наведении"
        )
        assert (
            bg_before != bg_after
        ), f"Цвет фона карточки вакансии не изменился. {bg_before} == {bg_after}"
        assert (
            color_before != color_after
        ), f"Цвет текста карточки вакансии не изменился. {color_before} == {color_after}"

    @allure.step("Проверяем, что вакансии отсортированы по дате публикации: {order}")
    def check_vacansies_sorted_by_date(self, order: str = "desc"):
        self.container.check_visible()
        vacancies_data = self.get_all_vacancies_data()
        dates = [
            datetime.strptime(vacancy["date"], "%d.%m.%Y")
            for vacancy in vacancies_data
            if vacancy["date"]
        ]
        if order == "desc":
            is_sorted = all([dates[i] >= dates[i + 1] for i in range(len(dates) - 1)])
        elif order == "asc":
            is_sorted = all([dates[i] <= dates[i + 1] for i in range(len(dates) - 1)])
        else:
            ValueError("order должен быть 'desc' или 'asc'")

        logger.info(
            f"Проверяем, что вакансии отсортированы по дате публикации: '{order}'"
        )
        assert is_sorted, f"Вакансии не отсортированы в соответствии с порядком {order}"
