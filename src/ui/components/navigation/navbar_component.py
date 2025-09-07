from src.ui.components.base_component import BaseComponent
from src.ui.components.navigation.search_component import SearchComponent
from src.ui.elements.icon import Icon
from src.ui.elements.link import Link
from src.ui.locators import NavBarLocators


class NavbarComponent(BaseComponent):

    def __init__(self, page):
        super().__init__(page)

        self.logo = Icon.by_xpath(page, NavBarLocators.LOGO, "Логотип сайта")
        self.about_tab = Icon.by_xpath(page, NavBarLocators.ABOUT_US_TAB, "О нас")
        self.materials_tab = Link.by_xpath(
            page, NavBarLocators.MATERIALS_TAB, "Материалы"
        )
        self.news_tab = Link.by_xpath(page, NavBarLocators.NEWS_TAB, "Новости")
        self.vacancies_tab = Link.by_xpath(
            page, NavBarLocators.VACANCIES_TAB, "Вакансии"
        )
        self.contacts_tab = Link.by_xpath(page, NavBarLocators.CONTACT_TAB, "Контакты")
        self.search = SearchComponent(page)
