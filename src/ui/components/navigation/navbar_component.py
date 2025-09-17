import re

from src.ui.components.base_component import BaseComponent
from src.ui.components.navigation.search_component import SearchComponent
from src.ui.elements.icon import Icon
from src.ui.elements.tab import Tab
from src.ui.locators import NavBarLocators
from src.ui.routes import AppRoute


class NavbarComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.logo = Icon.by_xpath(page, *NavBarLocators.LOGO)
        self.about_tab = Tab.by_xpath(page, *NavBarLocators.ABOUT_US_TAB)
        self.materials_tab = Tab.by_xpath(page, *NavBarLocators.MATERIALS_TAB)
        self.news_tab = Tab.by_xpath(page, *NavBarLocators.NEWS_TAB)
        self.vacancies_tab = Tab.by_xpath(page, *NavBarLocators.VACANCIES_TAB)
        self.contacts_tab = Tab.by_xpath(page, *NavBarLocators.CONTACT_TAB)
        self.search = SearchComponent(page)

    def check_visible(self):
        for component in [
            self.logo,
            self.about_tab,
            self.materials_tab,
            self.news_tab,
            self.vacancies_tab,
            self.contacts_tab,
            self.search,
        ]:
            component.check_visible()

    def click_about_tab(self) -> None:
        """Кликает по табу "О Нас" и проверяет, что пользователь перешел на главную страницу."""
        self.about_tab.check_visible().click()
        self.check_current_url(re.compile(rf".*{AppRoute.ABOUT}"))
