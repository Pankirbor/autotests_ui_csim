from typing import Self

import allure
from playwright.sync_api import Download, expect
from ui_coverage_tool import ActionType

from src.ui.elements.base_element import BaseElement
from src.utils.logger import get_logger

logger = get_logger(__name__.upper())


class Link(BaseElement):
    """Класс превставления ссылки на веб-странице."""

    def check_enabled(self, nth: int = 0, **kwargs) -> Self:
        """Проверяет, что ссылка активна (доступна для нажатия).

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
        """Проверяет, что ссылка неактивна (недоступна для нажатия).

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

    def check_download_file(self, file_name: str, nth: int = 0, **kwargs) -> Download:
        """Скачивает файл по ссылке.

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых ссылок.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        with self.page.expect_download() as download_info:
            self.click(nth, **kwargs)

        download: Download = download_info.value
        downloaded_file_name = download.suggested_filename
        logger.info(f"Файл '{downloaded_file_name}' загружен")

        check_file_name_step = (
            f"Проверяем соответствие имени файла ожидаемому '{file_name}'"
        )
        with allure.step(check_file_name_step):
            logger.info(check_file_name_step)
            assert (
                file_name == downloaded_file_name
            ), f"Название '{downloaded_file_name}' не соответствует ожидаемому '{file_name}'"

        is_empty_file_step = f"Проверяем, что файл '{downloaded_file_name}' не пустой"
        with allure.step(is_empty_file_step):
            logger.info(is_empty_file_step)
            file_path = download.path()
            file_size = file_path.stat().st_size
            assert file_size > 0, f"Скачанный файл '{downloaded_file_name}' пустой"
