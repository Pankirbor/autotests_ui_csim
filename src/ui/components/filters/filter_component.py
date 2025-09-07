from playwright.sync_api import Page

from src.ui.components.base_component import BaseComponent
from src.ui.elements.button import Button
from src.ui.elements.tab import Tab
from src.ui.locators import FilterVacanciesLocators


class FilteVacanciesComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.tabs = self._get_filters_tabs()
        self.sort_btn = Button.by_xpath(
            self.page, FilterVacanciesLocators.SORT, "Кнопка сортировки"
        )
        self.filter_menu = Button.by_xpath(
            self.page, FilterVacanciesLocators.FILTER_BTN, "Кнопка Фильтр"
        )

    def _get_filters_tabs(self):
        return [
            Tab(
                self.page, f"//div[@class='q-tab'][{i + 1}]", f"Tab {item.inner_text()}"
            )
            for i, item in enumerate(
                self.page.locator(FilterVacanciesLocators.TAB).all()
            )
        ]
