from src.ui.locators.base import UILocator


class VacancyResponseFormLocators:
    """
    Локаторы для формы отклика на вакансию.
    """

    FULL_NAME_INPUT = UILocator(
        selector="//input[@aria-label='Представьтесь, пожалуйста']",
        description="Поле ввода 'Имя'",
    )
    PHONE_INPUT = UILocator(
        selector="//input[@aria-label='Ваш номер телефона']",
        description="Поле ввода 'Телефон'",
    )
    EMAIL_INPUT = UILocator(
        selector="//input[@aria-label='Ваш Email']", description="Поле ввода 'Email'"
    )
    RESUME_LINK_INPUT = UILocator(
        selector="//input[@aria-label='Ваше резюме']",
        description="Поле ввода 'Ссылка на резюме'",
    )
    SUBMIT_BUTTON = UILocator(
        selector="//form[contains(@class, 'vacancy_form')]//button[@type='submit' and .//span[text()='Отправить']]",
        description="Кнопка 'Отправить'",
    )
    ATTACH_FILE_LINK = UILocator(
        selector="//span[contains(@class, 'file-link') and text()='прикрепите файл']",
        description="Ссылка 'прикрепите файл'",
    )
    FORM_CONTAINER = UILocator(
        selector="//form[contains(@class, 'vacancy_form')]",
        description="Контейнер формы отклика",
    )
    FOOTER_TEXT = UILocator(
        selector="//div[contains(@class, 'vacancy_form__footer')]",
        description="Футер формы с согласием на обработку данных",
    )
    FULL_NAME_ERROR = UILocator(
        selector="//input[@aria-label='Представьтесь, пожалуйста']/ancestor::label//div[@role='alert']",
        description="Сообщение об ошибке под полем 'Имя'",
    )
    PHONE_ERROR = UILocator(
        selector="//input[@aria-label='Ваш номер телефона']/ancestor::label//div[@role='alert']",
        description="Сообщение об ошибке под полем 'Телефон'",
    )
    EMAIL_ERROR = UILocator(
        selector="//input[@aria-label='Ваш Email']/ancestor::label//div[@role='alert']",
        description="Сообщение об ошибке под полем 'Email'",
    )
    RESUME_LINK_ERROR = UILocator(
        selector="//input[@aria-label='Ваше резюме']/ancestor::label//div[@role='alert']",
        description="Сообщение об ошибке под полем 'Резюме'",
    )
    SMART_CAPTCHA_CONTAINER = UILocator(
        selector="//div[contains(@class, 'smart-captcha')]",
        description="Контейнер Yandex SmartCaptcha",
    )
    SMART_CAPTCHA_IFRAME = UILocator(
        selector="//iframe[@data-testid='backend-iframe']", description="Iframe капчи"
    )
    SUCCESS_MESSAGE = UILocator(
        selector="//div[contains(text(), 'успешно') or contains(text(), 'отправлен') or contains(@class, 'success')]",
        description="Сообщение об успешной отправке формы",
    )
