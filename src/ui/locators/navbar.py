from src.ui.locators.base import UILocator


class NavBarLocators:
    ABOUT_US_TAB = UILocator(
        selector="//a[@role='tab' and @href='/']",
        description="Вкладка 'О нас' в навбаре",
    )
    MATERIALS_TAB = UILocator(
        selector="//a[@role='tab' and @href='/poleznye-materialy']",
        description="Вкладка 'Полезные материалы' в навбаре",
    )
    NEWS_TAB = UILocator(
        selector="//a[@role='tab' and @href='/novosti']",
        description="Вкладка 'Новости' в навбаре",
    )
    VACANCIES_TAB = UILocator(
        selector="//a[@role='tab' and @href='/vakansii']",
        description="Вкладка 'Вакансии' в навбаре",
    )
    CONTACT_TAB = UILocator(
        selector="//a[@role='tab' and @href='/#feedback']",
        description="Вкладка 'Контакты' в навбаре",
    )
    SEARCH_TAB = UILocator(
        selector="//header//div[@class='input_search__wrapp']",
        description="Контейнер поиска в навбаре",
    )
    SEARCH_ICON = UILocator(
        selector=".input_search__icon_search", description="Иконка поиска"
    )
    SEARCH_INPUT = UILocator(
        selector="//div[contains(@class, 'input_search__wrapp')]//input",
        description="Поле ввода поиска",
    )
    SEARCH_ENTER_ICON = UILocator(
        selector="i[role='presentation']", description="Иконка 'Enter' для поиска"
    )
    LOGO = UILocator(
        selector="//div[contains(@class, 'q-avatar')]//img",
        description="Логотип в навбаре",
    )
