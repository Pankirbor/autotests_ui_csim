from src.ui.components.base_component import BaseComponent
from src.ui.elements.icon import Icon
from src.ui.elements.input import Input
from src.ui.elements.label import Label
from src.ui.locators import NavBarLocators


class SearchComponent(BaseComponent):
    """Класс превставления компонента поиска.

    Atributes:
        search_tab (Label): ссылка на таб "Поиск"
        icon (Icon): иконка поиска
        input (Input): поле ввода поиска
        inter_icon (Icon): иконка "ввод"
    """

    def __init__(self, page):
        """Инициализация компонента поиска."""
        super().__init__(page)

        self.search_tab = Label.by_xpath(page, *NavBarLocators.SEARCH_TAB)
        self.icon = Icon.by_xpath(page, *NavBarLocators.SEARCH_ICON)
        self.input = Input.by_xpath(page, *NavBarLocators.SEARCH_INPUT)
        self.inter_icon = Icon.by_xpath(page, *NavBarLocators.SEARCH_ENTER_ICON)

    def check_visible(self):
        """Проверка, что компонент поиска видим."""
        self.search_tab.check_visible()
        self.icon.check_visible()
