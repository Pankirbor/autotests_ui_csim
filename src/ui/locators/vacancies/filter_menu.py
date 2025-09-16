from src.ui.locators.base import UILocator


class VacancyFiltersMenuLocators:
    """
    Локаторы для выпадающего меню фильтров вакансий.
    """

    CONTAINER = UILocator(
        selector="//div[contains(@class,'q-menu')]",
        description="Контейнер выпадающего меню фильтров",
    )
    RESET_BUTTON = UILocator(
        selector="//button[contains(., 'Сбросить')]",
        description="Кнопка 'Сбросить' в меню фильтров",
    )
    APPLY_BUTTON = UILocator(
        selector="//button[contains(., 'Применить')]",
        description="Кнопка 'Применить' в меню фильтров",
    )
    CHECKBOX_ROOT = UILocator(
        selector=".//div[contains(@class, 'q-checkbox') and .//div[contains(@class, 'q-checkbox__label') and normalize-space() = '{label}']]",
        description="Корневой элемент чекбокса по тексту метки '{label}'",
    )
    CHECKBOX_ITEMS = UILocator(
        selector="//div[contains(@role, 'checkbox')]",
        description="Элементы чекбоксов в меню",
    )
    CHECKBOX_ITEM = UILocator(
        selector="(//div[normalize-space(text()) = '{group_title}']/following-sibling::div[@role='group'][1]//div[contains(@role, 'checkbox')])[{index}]",
        description="Чекбокс из группы {group_title}: {label}",
    )
    CHECKBOX_LABEL = UILocator(
        selector=".//div[contains(@class, 'q-checkbox__label')]",
        description="Текст метки чекбокса",
    )
    CHECKBOX_GROUP_BY_TITLE = UILocator(
        selector="//div[normalize-space(text()) = '{group_title}']/following-sibling::div[@role='group'][1]",
        description="Группа чекбоксов, следующая за заголовком '{group_title}'",
    )
