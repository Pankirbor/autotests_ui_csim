from typing import Self
from playwright.sync_api import Page

from src.ui.components.base_component import BaseComponent
from src.ui.elements.button import Button
from src.ui.elements.container import Container
from src.ui.elements.tab import Tab
from src.ui.locators import FilterVacanciesLocators


class FilterVacanciesComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.tabs = self._get_filters_tabs()
        self.container = Container.by_xpath(
            page, *FilterVacanciesLocators.FILTER_CONTAINER
        )
        self.sort_btn = Button.by_xpath(page, *FilterVacanciesLocators.SORT)
        self.filter_menu = Button.by_xpath(page, *FilterVacanciesLocators.FILTER_BTN)

    def should_be_visible(self) -> Self:
        self.container.check_visible()
        return self

    def _get_filters_tabs(self) -> list[Tab]:
        xpath, name = FilterVacanciesLocators.TAB
        return [
            Tab(self.page, xpath.format(index=i), name.format(title=item.inner_text()))
            for i, item in enumerate(
                self.page.locator(FilterVacanciesLocators.ALL_TABS).all()
            )
        ]
