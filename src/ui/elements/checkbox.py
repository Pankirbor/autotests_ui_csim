from typing import Self

import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from src.ui.elements.base_element import BaseElement
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class Checkbox(BaseElement):
    """Класс, представляющий чекбокс на веб-странице.

    Расширяет BaseElement и предоставляет методы для взаимодействия с чекбоксами:
    установка/снятие галочки, проверка состояния, проверка атрибутов.

    Методы:
        check: Устанавливает галочку в чекбоксе.
        uncheck: Снимает галочку с чекбокса.
        is_checked: Проверяет, что чекбокс отмечен.
        is_not_checked: Проверяет, что чекбокс не отмечен.
        get_label_text: Возвращает текст метки чекбокса.
        has_aria_checked: Проверяет значение ARIA-атрибута aria-checked.
        hover: Наводит курсор на чекбокс.
        focus: Фокусирует чекбокс.
    """

    def is_checked(self, nth: int = 0, **kwargs) -> Self:
        """Проверяет, что чекбокс отмечен (галочка установлена).

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых чекбоксов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Проверка, что {self.type_of} '{self.name}' выбран"
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_be_checked()

        return self

    def is_not_checked(self, nth: int = 0, **kwargs) -> Self:
        """Проверяет, что чекбокс не отмечен (галочка снята).

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых чекбоксов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Проверка, что {self.type_of} '{self.name}' не выбран"
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).not_to_be_checked()

        return self

    def check(self, nth: int = 0, **kwargs) -> Self:
        """Устанавливает галочку в чекбоксе.

        Если чекбокс уже отмечен — ничего не делает (Playwright сам проверяет состояние).

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых чекбоксов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Выбор {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).check()

        self.track_coverage(ActionType.CHECKED, nth, **kwargs)
        return self

    def uncheck(self, nth: int = 0, **kwargs) -> Self:
        """Снимает галочку с чекбокса.

        Если чекбокс уже не отмечен — ничего не делает.

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых чекбоксов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Снятие выбора с {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).uncheck()
        self.track_coverage(ActionType.UNCHECKED, nth, **kwargs)
        return self

    def get_label_text(self, nth: int = 0, **kwargs) -> str:
        """Возвращает текст метки, связанной с чекбоксом.

        Предполагается, что метка находится рядом или внутри (зависит от реализации).
        В твоём случае — ищет .q-checkbox__label внутри текущего элемента.

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых чекбоксов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            str: Текст метки чекбокса.
        """
        step = f"Получение текста метки для {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            text = self.get_locator(nth, **kwargs).get_attribute("aria-label").strip()
            logger.info(f"Текст метки: '{text}'")
            return text

    def has_aria_checked(self, expected_value: str, nth: int = 0, **kwargs) -> Self:
        """Проверяет значение ARIA-атрибута aria-checked (полезно для кастомных чекбоксов).

        Args:
            expected_value (str): Ожидаемое значение ('true', 'false', 'mixed').
            nth (int): Индекс элемента, если на странице несколько одинаковых чекбоксов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = (
            f"Проверка ARIA-атрибута aria-checked='{expected_value}' у {self.type_of} '{self.name}'"
        )
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_have_attribute(
                "aria-checked", expected_value
            )
        return self

    def hover(self, nth: int = 0, **kwargs) -> Self:
        """Наводит курсор на чекбокс (может изменить стиль или показать тултип).

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых чекбоксов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Наведение курсора на {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).hover()
        return self

    def focus(self, nth: int = 0, **kwargs) -> Self:
        """Фокусирует чекбокс (например, для проверки стилей :focus).

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых чекбоксов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Фокусировка на {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).focus()
        return self
