from src.ui.locators.base import UILocator


class BreadcrumbsLocators:
    """Локаторы для элементов хлебных крошек."""

    CONTAINER = UILocator(
        selector="//div[contains(@class, 'q-breadcrumbs')]",
        description="Контейнер хлебных крошек",
    )
    ITEMS = UILocator(
        selector=".q-breadcrumbs__el",
        description="Элементы хлебных крошек",
    )
    HOME_LINK = UILocator(
        selector="//div[contains(@class, 'q-breadcrumbs')]//a[@href='/']",
        description="Ссылка на главную",
    )
    CURRENT_PAGE = UILocator(
        selector="//div[contains(@class, 'q-breadcrumbs')]//span[contains(@class, 'q-breadcrumbs__el')]",
        description="Текущая страница",
    )
