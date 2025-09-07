from typing import Self

import allure

from playwright.sync_api import Page, Locator, expect
from ui_coverage_tool import ActionType, SelectorType

from src.ui.elements.ui_coverage import tracker
from src.core.exceptions import LocatorNotFoundError
from src.utils.logger import get_logger


logger = get_logger(__name__.upper())


class BaseElement:
    """
    Базовый класс для элементов пользовательского интерфейса.

    Этот класс предоставляет общие методы для взаимодействия с элементами на веб-странице:
    получение локатора, клик, проверка видимости и текстового содержимого.

    Attributes:
        page (Page): Экземпляр страницы браузера.
        locator_path (str): Шаблон пути локатора элемента.
        name (str): Название элемента (используется для идентификации).

    Methods:
        get_locator: Получает локатор элемента.
        click: Выполняет клик по элементу.
        check_visible: Проверяет видимость элемента.
        check_have_text: Проверяет, что элемент содержит ожидаемый текст.
    """

    def __init__(
        self, page: Page, locator_path: str, name: str, use_xpath: bool = False
    ) -> None:
        """
        Инициализирует базовый элемент.

        Args:
            page (Page): Экземпляр страницы браузера.
            locator_path (str): Путь к локатору элемента.
            name (str): Название элемента.
        """
        self.page = page
        self.locator_path = locator_path
        self.name = name
        self.use_xpath = use_xpath

    @classmethod
    def by_test_id(cls, page: Page, test_id: str, name: str) -> Self:
        """
        Создает элемент для поиска по data-testid.

        Args:
            page (Page): Экземпляр страницы браузера.
            test_id (str): data-testid атрибут элемента.
            name (str): Название элемента.

        Returns:
            Self: Экземпляр созданного элемента.
        """
        return cls(page=page, locator_path=test_id, name=name, use_xpath=False)

    @classmethod
    def by_xpath(cls, page: Page, xpath: str, name: str) -> Self:
        """
        Создает элемент для поиска по XPath.

        Args:
            page (Page): Экземпляр страницы браузера.
            xpath (str): XPath для поиска элемента.
            name (str): Название элемента.

        Returns:
            Self: Экземпляр созданного элемента.
        """
        return cls(page=page, locator_path=xpath, name=name, use_xpath=True)

    def type_of(self) -> str:
        """
        Возвращает тип элемента в нижнем регистре.

        Returns:
            str: Тип элемента в нижнем регистре.
        """
        return self.__class__.__name__

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Возвращает локатор элемента, используя переданные параметры для форматирования пути.

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых элементов.
            **kwargs: Параметры для форматирования локатора.

        Returns:
            Locator: Локатор элемента на странице.
        """
        formatted_selector = self.locator_path.format(**kwargs)
        step = f"Getting locator with '{formatted_selector}' at index' {nth}'"

        with allure.step(step):
            try:
                if self.use_xpath:
                    locator = self.page.locator(formatted_selector).nth(nth)
                else:
                    locator = self.page.get_by_test_id(locator).nth(nth)

                return locator

            except Exception as e:
                error_msg = f"Элемент '{self.name}' не найден по {formatted_selector}"
                logger.error(error_msg)
                logger.exception("Детали ошибки:")

                # Скриншот для отладки
                allure.attach(
                    self.page.screenshot(),
                    name=f"element_not_found_{self.name}",
                    attachment_type=allure.attachment_type.PNG,
                )

                raise LocatorNotFoundError(error_msg) from e

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        """
        Возвращает строковый путь локатора элемента.
        Если в локаторе есть переменные, они заменяются на значения из kwargs.

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых элементов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Returns:
            str: Строковый путь локатора.
        """
        formatted_selector = self.locator_path.format(**kwargs)

        if self.use_xpath:
            return formatted_selector

        return f"//*[@data-testid='{formatted_selector}'][{nth + 1}]"

    def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs) -> None:
        """
        Отправляет информацию о выполнении действия в трекер.

        Args:
            action_type (ActionType): Тип действия (клик, ввод, проверка).
            nth (int): Индекс элемента.
            **kwargs: Дополнительные аргументы для форматирования локатора.
        """
        tracker.track_coverage(
            selector=self.get_raw_locator(nth=nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH,
        )

    def click(self, nth: int = 0, **kwargs) -> None:
        """
        Выполняет клик по элементу.

        Args:
            nth (int): Индекс элемента, если на странице несколько одинаковых элементов.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Clicking {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).click()

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs) -> Self:
        """
        Проверяет, что элемент отображается на странице.

        Returns:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Checking that {self.type_of} '{self.name}' is visible"
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_be_visible()

        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)
        return self

    def check_contain_text(self, text: str, nth: int = 0, **kwargs) -> None:
        """
        Проверяет, что элемент содержит указанный текст.

        Args:
            text (str): Ожидаемый текст в элементе.
        """
        step = f"Checking that {self.type_of} '{self.name}' has text '{text}'"
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_contain_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)
