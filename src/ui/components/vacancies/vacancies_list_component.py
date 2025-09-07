from typing import List, Dict

from playwright.sync_api import Page, expect

from src.ui.components.base_component import BaseComponent
from src.ui.elements.link import Link
from src.ui.elements.text import Text


class VacanciesListComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Контейнер списка
        self.container = page.locator(".row")

        # Карточки вакансий
        self.vacancy_cards = page.locator("article.vacancy_card")

        # Элементы карточки
        self.card_title = Text.by_xpath(
            self.page, "h3.vacancy_card__title", name="Название вакансии"
        )
        self.card_date = page.locator("time")
        self.card_link = Link.by_xpath(
            self.page, "a.vacancy_card__link", name="Ссылка на вакансию"
        )
        self.card_icon = page.locator(".vacancy_card__icon")

    # Базовые проверки
    def should_be_visible(self):
        expect(self.container).to_be_visible()
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
            "title": vacancy.locator("h3.vacancy_card__title").inner_text().strip(),
            "date": vacancy.locator("time").get_attribute("datetime")
            or vacancy.locator("time").inner_text().strip(),
            "link": vacancy.locator("a.vacancy_card__link").get_attribute("href"),
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
            card.locator("h3.vacancy_card__title").inner_text().strip()
            for card in self.get_all_vacancies()
        ]
