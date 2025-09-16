from src.ui.locators.base import UILocator


class CookiesLocators:
    """
    Локаторы для диалога согласия на использование cookies.
    """

    CONTAINER = UILocator(selector=".cookie-dialog", description="Контейнер с куками")
    ACCEPT_BUTTON = UILocator(
        selector=".cookie-dialog button:has-text('Принять')",
        description="Кнопка 'Принять'",
    )
