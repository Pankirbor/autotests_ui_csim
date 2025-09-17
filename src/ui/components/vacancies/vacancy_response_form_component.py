from typing import Self

import allure
from playwright.sync_api import Page, expect

from src.ui.components.base_component import BaseComponent
from src.ui.elements.button import Button
from src.ui.elements.input import Input
from src.ui.elements.text import Text
from src.ui.locators import VacancyResponseFormLocators
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class VacancyResponseFormComponent(BaseComponent):
    """Компонент формы отклика на вакансию.

    Attributes:
        page (Page): Экземпляр страницы Playwright.
        name_input (Input): Поле ввода имени.
        email_input (Input): Поле ввода email.
        phone_input (Input): Поле ввода телефона.
        resume_link_input (Input): Поле ввода ссылки на резюме.
        submit_button (Button): Кнопка отправки формы.
        fill_name_error_message (Text): Текст ошибки под полем 'Имя'.
        fill_email_error_message (Text): Текст ошибки под полем 'Email'.
        fill_phone_error_message (Text): Текст ошибки под полем 'Телефон'.
        fill_resume_link_error_message (Text): Текст ошибки под полем 'Ссылка на резюме'.
    """

    def __init__(self, page: Page):
        """Инициализирует компонент формы отклика на вакансию."""
        super().__init__(page)

        self.name_input = Input.by_xpath(
            page, *VacancyResponseFormLocators.FULL_NAME_INPUT
        )
        self.email_input = Input.by_xpath(
            page, *VacancyResponseFormLocators.EMAIL_INPUT
        )
        self.phone_input = Input.by_xpath(
            page, *VacancyResponseFormLocators.PHONE_INPUT
        )
        self.resume_link_input = Input.by_xpath(
            page, *VacancyResponseFormLocators.RESUME_LINK_INPUT
        )
        self.submit_button = Button.by_xpath(
            page, *VacancyResponseFormLocators.SUBMIT_BUTTON
        )
        self.fill_name_error_message = Text.by_xpath(
            page, *VacancyResponseFormLocators.FULL_NAME_ERROR
        )
        self.fill_email_error_message = Text.by_xpath(
            page, *VacancyResponseFormLocators.EMAIL_ERROR
        )
        self.fill_phone_error_message = Text.by_xpath(
            page, *VacancyResponseFormLocators.PHONE_ERROR
        )
        self.fill_resume_link_error_message = Text.by_xpath(
            page, *VacancyResponseFormLocators.RESUME_LINK_ERROR
        )

    def fill_phone(self, value: str) -> Self:
        """Заполняет поле номера телефона."""
        self.phone_input.fill(value)
        return self

    def fill_email(self, value: str) -> Self:
        """Заполняет поле email."""
        self.email_input.fill(value)
        return self

    def fill_resume_link(self, value: str) -> Self:
        """Заполняет поле со ссылкой на резюме."""
        self.resume_link_input.fill(value)
        return self

    def submit(self) -> None:
        """Отправляет форму отклика на вакансию."""
        step = "Отправка формы отклика на вакансию"
        with allure.step(step):
            logger.info(step)
            self.submit_button.click()

    @allure.step("Проверка, что форма отклика на вакансию видима")
    def check_visible(self) -> None:
        """Проверяет, что форма отклика видима."""
        self.name_input.check_visible()
        self.phone_input.check_visible()
        self.email_input.check_visible()
        self.resume_link_input.check_visible()
        self.submit_button.check_visible()

    @allure.step("Проверка, что все поля формы пустые.")
    def check_all_fields_are_empty(self) -> None:
        """Проверяет, что все поля формы пустые."""
        self.name_input.check_have_value("")
        self.phone_input.check_have_value("")
        self.email_input.check_have_value("")
        self.resume_link_input.check_have_value("")

    def fill_form(
        self, full_name: str, phone: str, email: str, resume_link: str = ""
    ) -> Self:
        """Заполняет форму отклика на вакансию.

        Args:
            full_name (str): Имя кандидата.
            phone (str): Телефон.
            email (str): Email.
            resume_link (str): Ссылка на резюме (опционально).

        Returns:
            Self: Экземпляр компонента.
        """
        step = "Заполнение формы отклика на вакансию"
        with allure.step(step):
            logger.info(step)
            self.fill_full_name(full_name)
            self.fill_phone(phone)
            self.fill_email(email)
            if resume_link:
                self.fill_resume_link(resume_link)
        return self

    def wait_for_captcha_iframe(self, timeout: float = 10000) -> None:
        """Ожидает появления iframe капчи (если используется в тестах с обходом капчи)."""
        step = "Waiting for Yandex SmartCaptcha iframe to load"
        with allure.step(step):
            logger.info(step)
            expect(
                self.page.frame_locator(
                    VacancyResponseFormLocators.SMART_CAPTCHA_IFRAME
                )
            ).to_be_visible(timeout=timeout)

    def check_full_name_error_message(self, expected_text: str) -> None:
        """Проверяет текст ошибки под полем 'Имя'."""
        step = (
            f"Проверка сообщения об ошибке под полем '{self.full_name_input.name}'"
            f": '{expected_text}'"
        )
        with allure.step(step):
            logger.info(step)
            self.check_full_name_error_message.check_visible().check_have_text(
                expected_text
            )

    def check_email_error_message(self, expected_text: str) -> None:
        """Проверяет текст ошибки под полем 'Email'."""
        step = (
            f"Проверка сообщения об ошибке под полем '{self.email_input.name}'"
            f": '{expected_text}'"
        )
        with allure.step(step):
            logger.info(step)
            self.fill_email_error_message.check_visible().check_have_text(expected_text)

    def check_phone_error_message(self, expected_text: str) -> None:
        """Проверяет текст ошибки под полем 'Телефон'."""
        step = (
            f"Проверка сообщения об ошибке под полем '{self.phone_input.name}'"
            f": '{expected_text}'"
        )
        with allure.step(step):
            logger.info(step)
            self.fill_phone_error_message.check_visible().check_have_text(expected_text)

    def check_resume_link_error_message(self, expected_text: str) -> None:
        """Проверяет текст ошибки под полем 'Ссылка на резюме'."""
        step = (
            f"Проверка сообщения об ошибке под полем '{self.resume_link_input.name}'"
            f": '{expected_text}'"
        )
        with allure.step(step):
            logger.info(step)
            self.resume_link_input.check_visible().check_contain_text(expected_text)
