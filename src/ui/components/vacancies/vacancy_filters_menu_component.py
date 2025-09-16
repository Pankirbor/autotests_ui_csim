from typing import Self
import allure
from playwright.sync_api import Page, expect

from src.ui.components.base_component import BaseComponent
from src.ui.elements.container import Container
from src.ui.elements.button import Button
from src.ui.elements.checkbox import Checkbox
from src.ui.locators import VacancyFiltersMenuLocators
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class VacancyFiltersMenuComponent(BaseComponent):
    """
    Компонент меню фильтров вакансий.

    Предоставляет методы для взаимодействия с чекбоксами фильтров, кнопками "Сбросить" и "Применить",
    а также для проверки состояния и содержимого меню.
    """

    def __init__(self, page: Page):
        """
        Инициализирует компонент меню фильтров.

        Args:
            page (Page): Экземпляр страницы Playwright.
        """
        super().__init__(page)
        self.container = Container.by_xpath(page, *VacancyFiltersMenuLocators.CONTAINER)
        self._checkboxes_cache: dict[str, list[Checkbox]] = {}
        self._all_checkboxes_by_label: dict[str, Checkbox] | None = None
        self.reset_btn = Button.by_xpath(page, *VacancyFiltersMenuLocators.RESET_BUTTON)
        self.apply_btn = Button.by_xpath(page, *VacancyFiltersMenuLocators.APPLY_BUTTON)

    @property
    def experience_checkboxes(self) -> list[Checkbox]:
        """
        Возвращает список чекбоксов из группы "Опыт работы".

        Returns:
            list[Checkbox]: Список чекбоксов.
        """
        return self._create_checkboxes_by_group("Опыт работы")

    @property
    def employment_checkboxes(self) -> list[Checkbox]:
        """
        Возвращает список чекбоксов из группы "Занятость".

        Returns:
            list[Checkbox]: Список чекбоксов.
        """
        return self._create_checkboxes_by_group("Занятость")

    @property
    def schedule_checkboxes(self) -> list[Checkbox]:
        """
        Возвращает список чекбоксов из группы "График работы".

        Returns:
            list[Checkbox]: Список чекбоксов.
        """
        return self._create_checkboxes_by_group("График работы")

    @property
    def all_checkboxes_by_label(self) -> dict[str, Checkbox]:
        """
        Возвращает словарь всех чекбоксов, где ключ — текст метки (aria-label).

        Returns:
            dict[str, Checkbox]: Словарь чекбоксов.
        """
        if self._all_checkboxes_by_label is None:
            all_checkboxes = [
                *self.employment_checkboxes,
                *self.experience_checkboxes,
                *self.schedule_checkboxes,
            ]
            self._all_checkboxes_by_label = {
                checkbox.get_label_text(): checkbox for checkbox in all_checkboxes
            }
        return self._all_checkboxes_by_label

    def _create_checkboxes_by_group(self, group_title: str) -> list[Checkbox]:
        """
        Создаёт список чекбоксов для указанной группы.

        Args:
            group_title (str): Название группы (например, "Опыт работы").

        Returns:
            list[Checkbox]: Список чекбоксов в группе.
        """
        if group_title not in self._checkboxes_cache:

            filter_group = self.page.locator(
                VacancyFiltersMenuLocators.CHECKBOX_GROUP_BY_TITLE.selector.format(
                    group_title=group_title
                )
            )
            checkbox_elements = filter_group.locator(
                VacancyFiltersMenuLocators.CHECKBOX_ITEMS.selector
            ).all()
            checkbox_path, checkbox_name = VacancyFiltersMenuLocators.CHECKBOX_ITEM
            checkboxes = []
            for index, element in enumerate(checkbox_elements, start=1):
                label_text = element.inner_text().strip()
                checkbox = Checkbox.by_xpath(
                    self.page,
                    checkbox_path.format(group_title=group_title, index=index),
                    checkbox_name.format(
                        group_title=group_title,
                        label=label_text,
                    ),
                )
                checkboxes.append(checkbox)

            self._checkboxes_cache[group_title] = checkboxes

        return self._checkboxes_cache[group_title]

    def get_checkbox_by_label(self, label: str) -> Checkbox:
        """
        Возвращает чекбокс по тексту его метки (aria-label).

        Args:
            label (str): Текст метки чекбокса (например, "От 1 года до 3 лет").

        Returns:
            Checkbox: Найденный чекбокс.

        Raises:
            ValueError: Если чекбокс с указанной меткой не найден.
        """
        if label in self.all_checkboxes_by_label:
            return self.all_checkboxes_by_label[label]

        available_labels = ", ".join(self.all_checkboxes_by_label.keys())
        raise ValueError(
            f"Чекбокс с меткой '{label}' не найден. Доступные метки: {available_labels}."
        )

    @allure.step("Проверка отображения меню фильтров")
    def check_visible(self, nth: int = 0, **kwargs):
        """
        Проверяет, что меню фильтров отображается.
        """
        self.container.get_locator(nth, **kwargs).wait_for(
            state="visible", timeout=10000
        )
        self.container.check_visible()
        self.check_expected_checkboxes()
        return self

    def check_not_visible(self):
        """
        Проверяет, что меню фильтров не отображается.
        """
        logger.info("Проверка, что меню фильтров не отображается")
        expect(self.container.get_locator()).not_to_be_visible()

    @allure.step("Проверка отображения чекбоксов меню фильтров")
    def check_expected_checkboxes(self):
        checkboxes = [
            *self.employment_checkboxes,
            *self.experience_checkboxes,
            *self.schedule_checkboxes,
        ]
        employment_labels = ["Полная", "Частичная"]
        experience_labels = [
            "Нет опыта",
            "От 1 года до 3 лет",
            "От 3 до 6 лет",
            "Более 6 лет",
        ]
        schdule_labels = ["Полный день", "Удаленная работа", "Гибкий график"]
        labels = [*employment_labels, *experience_labels, *schdule_labels]
        for i in range(len(labels)):
            checkboxes[i].check_visible().check_contain_text(labels[i])

    @allure.step("Выбор фильтров по лейблам {filters}")
    def select_filters(self, filters: list[str]) -> Self:
        for label in filters:
            checkbox = self.get_checkbox_by_label(label)
            checkbox.check()

        return self

    @allure.step("Проверка, что выбраны фильтры: {filters}")
    def are_filters_selected(self, filters: list[str]) -> Self:
        """
        Проверяет, что указанные чекбоксы отмечены.
        Args:
            filters (list[str]): Список меток чекбоксов (например, ["Полная", "От 1 года до 3 лет"]).

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        for label in filters:
            checkbox = self.get_checkbox_by_label(label)
            checkbox.is_checked()

        return self

    @allure.step("Проверка отмены фильтров кнопкой 'Сбросить'")
    def check_filter_reset(self) -> Self:
        """
        Сбрасывает все чекбоксы и проверяет, что они сняты.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        for checkbox in self.all_checkboxes_by_label.values():
            checkbox.is_not_checked()

        return self
