from src.ui.locators.base import UILocator


class FilterVacanciesLocators:
    """Локаторы для элементов фильтрации на странице вакансий."""

    FILTER_CONTAINER = UILocator(
        selector="//div[contains(@class,'post__bar')]", description="Контейнер фильтров"
    )
    FILTERS_TABS = UILocator(
        selector=".q-tabs", description="Контейнер вкладок фильтров"
    )
    ALL_TABS = UILocator(
        selector="//div[contains(@role, 'tablist')]//div[contains(@role, 'tab')]",
        description="Все вкладки фильтров",
    )
    SORT = UILocator(
        selector="//button[contains(@class, 'btn_sort')]",
        description="Кнопка сортировки",
    )
    ICON_SORTING_UP = UILocator(
        selector="//button[contains(@class, 'btn_sort')]//i[contains(@class, 'icon-sorting-up')]",
        description="Иконка сортировки по возрастанию",
    )
    ICON_SORTING_DOWN = UILocator(
        selector="//button[contains(@class, 'btn_sort')]//i[contains(@class, 'icon-sorting-down')]",
        description="Иконка сортировки по убыванию",
    )
    FILTER_BTN = UILocator(
        selector="//button[contains(@class, 'btn_filters')]",
        description="Кнопка 'Фильтр'",
    )
    TAB = UILocator(
        selector="(//div[contains(@role, 'tablist')]//div[contains(@role, 'tab')])[{index}]",
        description="Вкладка {title}",
    )
    TAB_ALL_VACANCIES = UILocator(
        selector="//div[contains(@class, 'q-tab')]//div[contains(text(), 'Все')]",
        description="Вкладка 'Все'",
    )
