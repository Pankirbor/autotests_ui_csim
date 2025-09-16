import typing

import allure
from playwright.sync_api import Playwright, Page
from playwright_stealth import stealth

from config import settings, Browser
from integrations.playwright.mocks import mock_static_resources


def playwright_page_builder(
    playwright: Playwright,
    browser_type: Browser,
    test_name: str,
    state: str | None = None,
) -> typing.Iterator[Page]:
    """
    Генератор для создания и настройки страницы Playwright в указанном браузере.

    Функция запускает браузер, заданный через `browser_type`, создает новый контекст с
    указанием начального состояния (state), записью видео и трассировкой выполнения.
    После завершения работы браузер закрывается, а трассировка и видео прикрепляются
    к отчету Allure.

    Args:
        playwright (Playwright): Объект Playwright для управления браузером.
        browser_type (Browser): Тип браузера (webkit, chromium, firefox).
        test_name (str): Имя теста, используется для формирования путей файлов.
        state (str | None, optional): Путь к файлу состояния браузера. Defaults to None.

    Yields:
        Iterator[Page]: Генератор, возвращающий объект страницы Playwright.

    Returns:
        None: Ресурсы управляются внутри генератора.
    """
    browser = playwright[browser_type].launch(headless=settings.ui.headless)
    context = browser.new_context(
        storage_state=state,
        record_video_dir=settings.ui.videos_path,
        base_url=settings.get_ui_base_url(),
    )
    context.tracing.start(
        name=test_name, screenshots=True, snapshots=True, sources=True
    )
    page = context.new_page()
    mock_static_resources(page)
    stealth(page)
    page.mouse.move(10, 10)
    page.wait_for_timeout(1000)

    yield page

    context.tracing.stop(path=settings.ui.tracing_path / f"{test_name}.zip")
    browser.close()

    allure.attach.file(
        source=settings.ui.tracing_path / f"{test_name}.zip",
        name="trace",
        extension="zip",
    )
    allure.attach.file(
        source=page.video.path(),
        name="video",
        attachment_type=allure.attachment_type.WEBM,
    )
