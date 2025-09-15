from typing import Self
import allure
from playwright.sync_api import Page, expect

from src.ui.components.base_component import BaseComponent
from src.ui.components.vacancies.vacancy_filters_menu_component import (
    VacancyFiltersMenuComponent,
)
from src.ui.elements.button import Button
from src.ui.elements.container import Container
from src.ui.elements.icon import Icon
from src.ui.elements.tab import Tab
from src.ui.locators import FilterVacanciesLocators
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class FilterVacanciesComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = Container.by_xpath(
            page, *FilterVacanciesLocators.FILTER_CONTAINER
        )
        self.tab_all = Tab(page, *FilterVacanciesLocators.TAB_ALL_VACANCIES)
        self.sort_btn = Button.by_xpath(page, *FilterVacanciesLocators.SORT)
        self.up_icon = Icon.by_xpath(page, *FilterVacanciesLocators.ICON_SORTING_UP)
        self.down_icon = Icon.by_xpath(page, *FilterVacanciesLocators.ICON_SORTING_DOWN)
        self.filter_menu_btn = Button.by_xpath(
            page, *FilterVacanciesLocators.FILTER_BTN
        )
        self.filter_menu = VacancyFiltersMenuComponent(page)

    @property
    def tabs(self) -> list[Tab]:
        """Ленивое свойство: возвращает список вкладок при каждом обращении."""
        return self._get_filters_tabs()

    @allure.step("Проверка видимости фильтра")
    def check_visible(self) -> Self:
        self.container.check_visible()
        return self

    def _get_filters_tabs(self) -> list[Tab]:
        xpath, name = FilterVacanciesLocators.TAB
        tab_elements = self.page.locator(FilterVacanciesLocators.ALL_TABS).all()
        # tab_elements = tabs.all()

        result = []
        for i, item in enumerate(tab_elements, start=1):
            tab_text = item.inner_text().strip()
            if tab_text != "Все":
                result.append(
                    Tab.by_xpath(
                        self.page, xpath.format(index=i), name.format(title=tab_text)
                    )
                )
        return result
