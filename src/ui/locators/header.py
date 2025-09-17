from src.ui.locators.base import UILocator


class HeaderPageLocators:
    """Локаторы для шапки страницы."""

    TITLE = UILocator(
        selector="//h1[contains(@class, 'post__title')] | //h1",
        description="Заголовок страницы {location}",
    )
    SUBTITLE = UILocator(
        selector="//h3[contains(@class, 'post__subtitle')] | //section[contains(@class, 'header__inner')]//p",
        description="Подзаголовок страницы {location}",
    )
