from typing import Self

import allure
from ui_coverage_tool import ActionType

from src.ui.elements.base_element import BaseElement
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class Container(BaseElement):
    """Класс превставления контейнера на веб-странице."""

    def check_less_or_equal_count_elements(
        self, inner_item_path: str, expected_max_count: int, nth: int = 0, **kwargs
    ) -> Self:
        """Проверяет, что количество дочерних элементов контейнера МЕНЬШЕ ИЛИ РАВНО ожидаемому.

        Используется, например, для проверки фильтрации:
        количество отфильтрованных элементов не может превышать общее количество.

        Args:
            inner_item_path (str): Путь к дочерним элементам внутри контейнера.
            expected_max_count (int): Максимально допустимое количество элементов.
            nth (int): Индекс экземпляра контейнера (если их несколько).
            **kwargs: Параметры для форматирования локатора.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.

        Raises:
            AssertionError: Если фактическое количество элементов больше ожидаемого максимума.
        """
        step_description = (
            f"Проверка: в контейнере {self.name} количество элементов"
            f" не должно превышать {expected_max_count}"
        )

        with allure.step(step_description):
            container = self.get_locator(nth, **kwargs)
            container.page.wait_for_timeout(5000)
            actual_count = container.locator(inner_item_path).count()
            logger.info(
                step_description + f", актуальное количество элементов: {actual_count}"
            )

            try:
                message = (
                    f"Ошибка фильтрации: в контейнере '{self.name}' "
                    f"найдено {actual_count} элементов, "
                    f"что БОЛЬШЕ ожидаемого максимума ({expected_max_count})."
                )

                assert actual_count <= expected_max_count, message
            except AssertionError as e:
                logger.error(e)
                raise

        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)
        return self
