from typing import Self

import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from src.ui.elements.base_element import BaseElement
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class Button(BaseElement):
    """Класс, представляющий кнопку на веб-странице.

    Этот класс наследуется от BaseElement и добавляет специфичные методы
    для проверки состояния кнопки:
     - включено (enabled) или выключено (disabled).

    Методы:
        check_enabled: Проверяет, что кнопка доступна для взаимодействия.
        check_disabled: Проверяет, что кнопка недоступна для взаимодействия.
    """

    def check_enabled(self, nth: int = 0, **kwargs) -> Self:
        """Проверяет, что кнопка включена (доступна для нажатия).

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых кнопок.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Проверка, что  {self.type_of} '{self.name}' доступна для нажатия"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

        self.track_coverage(ActionType.ENABLED, nth, **kwargs)
        return self

    def check_disabled(self, nth: int = 0, **kwargs) -> Self:
        """Проверяет, что кнопка выключена (недоступна для нажатия).

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых кнопок.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Проверка, что {self.type_of} '{self.name}' недоступна для нажатия"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()

        self.track_coverage(ActionType.DISABLED, nth, **kwargs)
        return self
