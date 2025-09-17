from datetime import datetime
from typing import Any, Self

import allure
from playwright.sync_api import Locator, Page, expect

from src.ui.components.base_component import BaseComponent
from src.ui.elements.container import Container
from src.ui.elements.icon import Icon
from src.ui.elements.link import Link
from src.ui.elements.text import Text
from src.ui.locators import VacanciesListLocators
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class VacanciesListComponent(BaseComponent):
    """Класс представления компонента списка вакансий.

    Attributes:
        container (Container): контейнер списка вакансий
        vacancy_cards (Locator): локатор для карточек вакансий
        card_title (Text): заголовок карточки вакансии
        card_date (Text): дата публикации карточки вакансии
        card_link (Link): ссылка на карточку вакансии
        card_icon (Icon): иконка карточки вакансии
    """

    def __init__(self, page: Page):
        """Инициализирует компонент списка вакансий."""
        super().__init__(page)

        # Контейнер списка
        self.container = Container.by_xpath(self.page, *VacanciesListLocators.CONTAINER)

        # Элементы карточки
        self.card_title = Text.by_xpath(self.page, *VacanciesListLocators.CARD_TITLE)
        self.card_date = Text.by_xpath(self.page, *VacanciesListLocators.CARD_DATE)
        self.card_link = Link.by_xpath(self.page, *VacanciesListLocators.CARD_LINK)
        self.card_icon = Icon.by_xpath(self.page, *VacanciesListLocators.CARD_ICON)

    @property
    def vacancy_cards(self) -> list[Locator]:
        """Возвращает локатор для карточек вакансий."""
        return self.page.locator(VacanciesListLocators.VACANCY_CARDS.selector)

    # Базовые проверки
    def check_visible(self) -> Self:
        """Проверяет, что компонент списка вакансий виден."""
        self.container.check_visible()
        return self

    def should_have_vacancies(self, min_count=1) -> Self:
        """Проверяет что есть вакансии."""
        expect(self.vacancy_cards).to_have_count(min_count, timeout=10000)
        return self

    # Работа с карточками
    def get_all_vacancies(self) -> list[Locator]:
        """Возвращает все карточки вакансий."""
        return self.vacancy_cards.all()

    def get_vacancies_count(self) -> int:
        """Возвращает количество вакансий."""
        return self.vacancy_cards.count()

    def get_vacancy_by_index(self, index: int) -> Locator:
        """Возвращает карточку по индексу."""
        return self.vacancy_cards.nth(index)

    def get_vacancy_by_title(self, title: str) -> Locator:
        """Возвращает карточку по названию."""
        return self.vacancy_cards.filter(has_text=title).first

    # Получение данных
    def get_vacancy_data(self, index: int = 0) -> dict[str, Any]:
        """Возвращает данные вакансии по индексу."""
        vacancy = self.get_vacancy_by_index(index)
        return {
            "title": self.card_title.get_locator(nth=index).inner_text().strip(),
            "date": self.card_date.get_locator(nth=index).get_attribute("datetime")
            or self.card_date.get_locator(nth=index).inner_text().strip(),
            "link": self.card_link.get_locator(nth=index).get_attribute("href"),
            "element": vacancy,
        }

    def get_all_vacancies_data(self) -> list[dict[str, Any]]:
        """Возвращает данные всех вакансий."""
        vacancies_data = []
        for i in range(self.get_vacancies_count()):
            vacancies_data.append(self.get_vacancy_data(i))
        return vacancies_data

    def get_vacancies_titles(self) -> list[str]:
        """Возвращает список названий вакансий."""
        return [
            self.card_title.get_locator(nth=ind).inner_text().strip()
            for ind in range(self.get_vacancies_count())
        ]

    @allure.step(
        "Проверяем, что при наведении на карточку вакансии меняется цвет фона и текста"
    )
    def check_hover_on_vacancy(self, index: int = 1) -> None:
        """Проверяет, что при наведении на карточку вакансии меняется цвет фона и текста."""
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
    def check_vacancies_sorted_by_date(self, order: str = "desc") -> None:
        """Проверяет, что список вакансий отсортирован по дате публикации в указанном порядке.

        Args:
            order (str): Порядок сортировки — "asc" (по возрастанию) или "desc" (по убыванию).

        Raises:
            AssertionError: Если вакансии не отсортированы в указанном порядке.
        """
        self.container.check_visible()
        vacancies_data = self.get_all_vacancies_data()
        dates = self._extract_dates(vacancies_data)

        logger.info(
            f"Проверяем, что вакансии отсортированы по дате публикации: '{order}'"
        )
        try:
            assert self._is_sorted(
                dates, order
            ), f"Вакансии не отсортированы в соответствии с порядком {order}"

        except AssertionError as e:

            current_order = "\n".join(
                f"{i}) {vcancy['title']} - {vcancy['date']}"
                for i, vcancy in enumerate(vacancies_data, start=1)
            )

            error_msg = (
                f"Вакансии не отсортированы в порядке '{order}'.\n"
                f"Текущий порядок:\n{current_order}"
            )
            logger.error(error_msg)
            raise e

    def _is_sorted(self, dates: list[datetime], order: str) -> bool:
        """Проверяет, отсортирован ли список дат в заданном порядке.

        Args:
            dates: Список дат для проверки.
            order: Порядок сортировки — "asc" (возрастание) или "desc" (убывание).

        Returns:
            bool: True, если список отсортирован правильно, иначе False.

        Raises:
            ValueError: Если order не "asc" или "desc".
        """
        if order == "desc":
            return all(dates[i] >= dates[i + 1] for i in range(len(dates) - 1))
        elif order == "asc":
            return all(dates[i] <= dates[i + 1] for i in range(len(dates) - 1))
        else:
            raise ValueError(
                f"Некорректное значение order: '{order}'. Ожидается 'asc' или 'desc'."
            )

    def _extract_dates(self, vacancies_data: list[dict[str, Any]]) -> list[datetime]:
        """Извлекает и парсит даты из данных вакансий."""
        dates = []
        for vacancy in vacancies_data:
            date_str = vacancy.get("date")
            if date_str:
                try:
                    parsed_date = datetime.strptime(date_str, "%d.%m.%Y")
                    dates.append(parsed_date)

                except ValueError:
                    err_msg = (
                        f"Некорректный формат даты: {date_str}"
                        f" в вакансии {vacancy.get('title', 'N/A')}"
                    )
                    logger.warning(err_msg)
        return dates
