from src.ui.components.base_component import BaseComponent
from src.ui.elements.icon import Icon
from src.ui.elements.input import Input
from src.ui.elements.label import Label
from src.ui.locators import NavBarLocators


class SearchComponent(BaseComponent):

    def __init__(self, page):
        super().__init__(page)

        self.search_tab = Label.by_xpath(page, NavBarLocators.SEARCH_TAB, "Поиск")
        self.icon = Icon.by_xpath(page, NavBarLocators.SEARCH_ICON, "Иконка поиска")
        self.input = Input.by_xpath(
            page, NavBarLocators.SEARCH_INPUT, "Поле ввода поиска"
        )
        self.inter_icon = Icon.by_xpath(
            page, NavBarLocators.SEARCH_ENTER_ICON, "Иконка стрелки вправо"
        )

    def check_visible(self):
        self.search_tab.check_visible()
        self.icon.check_visible()
