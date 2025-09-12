from typing import Self

import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from src.ui.elements.base_element import BaseElement
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class Link(BaseElement):
    """
    Класс превставления ссылки на веб-странице.
    """

    def check_enabled(self, nth: int = 0, **kwargs) -> Self:
        """
        Проверяет, что ссылка активна (доступна для нажатия).

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых ссылок.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Проверка, что {self.type_of} '{self.name}' активна"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

        self.track_coverage(ActionType.ENABLED, nth, **kwargs)
        return self

    def check_disabled(self, nth: int = 0, **kwargs) -> Self:
        """
        Проверяет, что ссылка неактивна (недоступна для нажатия).

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых ссылок.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Проверка, что {self.type_of} '{self.name}' неактивна"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()

        self.track_coverage(ActionType.DISABLED, nth, **kwargs)
        return self
