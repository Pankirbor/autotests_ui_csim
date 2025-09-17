from src.ui.locators.base import UILocator


class FooterLocators:
    """Локаторы для элементов футера."""

    FOOTER_CONTAINER = UILocator(
        selector="footer.container", description="Контейнер футера"
    )
    INFO = UILocator(
        selector="//footer[contains(@class, 'footer')]//div[contains(@class, 'footer__info')]",
        description="Блок информации в футере",
    )
    PRIVACY_POLICY_LINK = UILocator(
        selector="//footer[contains(@class, 'footer')]//a[contains(@href, 'Политика конфиденциальности.pdf')]",
        description="Ссылка на Политику конфиденциальности",
    )
    USER_AGREEMENT_LINK = UILocator(
        selector="//footer[contains(@class, 'footer')]//a[contains(@href, 'Пользовательское_соглашение.pdf')]",
        description="Ссылка на Пользовательское соглашение",
    )
    MAIN_PAGE_LINK = UILocator(
        selector="//footer[contains(@class, 'footer')]//a[@href='/']",
        description="Ссылка на главную страницу",
    )
    ICON = UILocator(
        selector="//footer[contains(@class, 'footer')]//img[@alt='logo']",
        description="Логотип в футере",
    )
