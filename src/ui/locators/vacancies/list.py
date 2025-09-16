from src.ui.locators.base import UILocator


class VacanciesListLocators:
    CONTAINER = UILocator(
        selector="//article[@class='post']//div[@class='row']",
        description="Блок со списком вакансий",
    )
    VACANCY_CARDS = UILocator(
        selector="//article[contains(@class, 'vacancy_card')]",
        description="Список карточек вакансий",
    )
    CARD_TITLE = UILocator(
        selector="//h3[contains(@class, 'vacancy_card__title')]",
        description="Название вакансии",
    )
    CARD_DATE = UILocator(selector="//time", description="Дата публикации")
    CARD_LINK = UILocator(
        selector="//a[contains(@class, 'vacancy_card__link')]",
        description="Ссылка на вакансию",
    )
    CARD_ICON = UILocator(
        selector="//i[contains(@class, 'vacancy_card__icon')]",
        description="Иконка ссылки на вакансию",
    )
    EMPTY_VIEW_CONTAINER = UILocator(
        selector="//div[contains(@class, 'not_found')]",
        description="Контейнер пустого состояния",
    )
    EMPTY_VIEW_TITLE = UILocator(
        selector="//div[@class='not_found']//h3",
        description="Заголовок пустого состояния",
    )
    EMPTY_VIEW_DESCRIPTION = UILocator(
        selector="//div[@class='not_found']//p",
        description="Описание пустого состояния",
    )
