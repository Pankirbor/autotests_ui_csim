import re

import allure
from ui_coverage_tool import ActionType
from playwright.sync_api import expect

from src.ui.elements.base_element import BaseElement
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class Tab(BaseElement):
    """
    Класс превставления элемента таба на веб-странице.
    """

    def is_active(self, nth: int = 0, **kwargs) -> bool:
        """
        Проверяет, что элемент таба является активным (имеет класс 'q-tab--active').

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых элементов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            bool: True, если таб активен, иначе False.
        """
        step_description = (
            f"Проверка: таб '{self.name}' активен (имеет класс 'q-tab--active')."
        )

        with allure.step(step_description):
            locator = self.get_locator(nth, **kwargs)

            try:
                logger.info(f"{step_description}")
                expect(locator).to_have_class(
                    re.compile(r"q-tab--active"), timeout=5000
                )
                is_selected = True
            except AssertionError:
                is_selected = False
                logger.warning(f"⚠️ {step_description} — таб НЕ активен.")

        self.track_coverage(ActionType.CHECKED, nth, **kwargs)
        return is_selected
