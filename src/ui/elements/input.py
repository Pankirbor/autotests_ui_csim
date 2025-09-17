from typing import Self

import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from src.ui.elements.base_element import BaseElement
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class Input(BaseElement):
    """Класс, представляющий поле ввода на веб-странице.

    Этот класс расширяет BaseElement и предоставляет методы для взаимодействия с полями ввода:
    заполнение, очистка, проверка значения и ввод текста с задержкой.

    Методы:
        fill: Заполняет поле указанным значением.
        check_have_value: Проверяет, что значение в поле соответствует ожидаемому.
        clear: Очищает поле ввода.
        type_text: Вводит текст в поле с возможностью задания параметров.
    """

    def fill(self, value: str, nth: int = 0, **kwargs) -> Self:
        """Заполняет поле ввода указанным значением.

        Аргументы:
            value (str): Значение, которое будет введено.
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Заполняем {self.type_of} '{self.name}' значением: '{value}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).fill(value)

        self.track_coverage(ActionType.FILL, nth, **kwargs)
        return self

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """Проверяет, что поле ввода содержит указанное значение.

        Аргументы:
            value (str): Ожидаемое значение в поле ввода.
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Проверка, что {self.type_of} '{self.name}' имеет значение '{value}'"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)

        self.track_coverage(ActionType.VALUE, nth, **kwargs)

    def clear(self, nth: int = 0, **kwargs) -> Self:
        """Очищает поле ввода.

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Очищение {self.type_of} '{self.name}' от содержимого"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.clear()

        return self

    def type_text(
        self,
        text: str,
        nth: int = 0,
        delay: int | None = None,
        timeout: float | None = None,
        no_wait_after: bool | None = None,
        **kwargs,
    ) -> Self:
        """Вводит текст в поле ввода с возможностью задания параметров.

        Аргументы:
            text (str): Текст, который будет введен.
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            delay (int | None): Задержка между нажатиями клавиш в миллисекундах.
            timeout (float | None): Максимальное время ожидания завершения действия.
            no_wait_after (bool | None): Если True, не ждать завершения после ввода.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Заполнение {self.type_of} '{self.name}' значением {text} с задержкой {delay}"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.type(
                text,
                delay=delay,
                timeout=timeout,
                no_wait_after=no_wait_after,
            )

        self.track_coverage(ActionType.TYPE, nth, **kwargs)
        return self
