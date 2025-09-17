from src.ui.locators.base import UILocator


class VacancyItemLocators:
    """Локаторы для элементов вакансии."""

    CONTAINER = UILocator(
        selector="//article[contains(@class, 'vacancy')]",
        description="Контейнер детальной страницы вакансии",
    )
    VACANCY_NAME = UILocator(
        selector="//h1[contains(@class, 'vacancy__title')]",
        description="Название вакансии",
    )
    PUBLICATION_DATE = UILocator(
        selector="//div[contains(@class, 'header')]//time",
        description="Дата публикации вакансии",
    )
    TAGS_CONTAINER = UILocator(
        selector="//div[contains(@class, 'vacancy__tags')]",
        description="Контейнер тегов вакансии",
    )
    EMPLOYMENT_TAG = UILocator(
        selector="//button[contains(@class, 'tag') and .//span[text()='Занятость:']]",
        description="Тег 'Занятость'",
    )
    EXPERIENCE_TAG = UILocator(
        selector="//button[contains(@class, 'tag') and .//span[contains(text(), 'Опыт:')]]",
        description="Тег с указанием опыта работы",
    )
    SCHEDULE_TAG = UILocator(
        selector="//button[contains(@class, 'tag') and .//span[contains(text(), 'График работы:')]]",
        description="Тег с указанием графика работы",
    )
    TASKS_SECTION = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Задачи']/following-sibling::ul[1]",
        description="Список задач вакансии",
    )
    TASKS_ITEMS = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Задачи']/following-sibling::ul[1]/li",
        description="Элементы списка задач",
    )
    REQUIREMENTS_SECTION = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Ожидаем от кандидата']/following-sibling::ul[1]",
        description="Список требований к кандидату",
    )
    REQUIREMENTS_TITLE = UILocator(
        selector="//h2[text()='Ожидаем от кандидата']",
        description="Заголовок секции 'Ожидаем от кандидата'",
    )
    REQUIREMENTS_ITEMS = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Ожидаем от кандидата']/following-sibling::ul[1]/li",
        description="Элементы списка требований",
    )
    PLUS_SECTION = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Будет плюсом']/following-sibling::ul[1]",
        description="Список желательных навыков (плюсов)",
    )
    PLUS_TITLE = UILocator(
        selector="//h2[text()='Будет плюсом']",
        description="Заголовок секции 'Будет плюсом'",
    )
    PLUS_ITEMS = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Будет плюсом']/following-sibling::ul[1]/li",
        description="Элементы списка плюсов",
    )
    CONDITIONS_SECTION = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Условия']/following-sibling::ul[1]",
        description="Список условий работы",
    )
    CONDITIONS_ITEMS = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Условия']/following-sibling::ul[1]/li",
        description="Элементы списка условий",
    )
    RESPONSE_BUTTON = UILocator(
        selector="//div[contains(@class, 'vacancy__actions')]//button[.//span[text()='Откликнуться на вакансию']]",
        description="Кнопка 'Откликнуться на вакансию'",
    )
    DESCRIPTION_AFTER_TASKS = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Задачи']/following-sibling::p[1]",
        description="Описание после секции 'Задачи'",
    )
    DESCRIPTION_AFTER_PLUS = UILocator(
        selector="//div[contains(@class, 'post')]//h2[text()='Будет плюсом']/following-sibling::p[1]",
        description="Описание после секции 'Будет плюсом'",
    )
