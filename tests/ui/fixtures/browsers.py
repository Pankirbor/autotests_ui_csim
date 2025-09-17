from collections.abc import Iterator

from playwright.sync_api import Page, Playwright
import pytest

from config import settings
from integrations.playwright.page_builder import playwright_page_builder


@pytest.fixture(params=settings.ui.browsers)
def chromium_page(
    request: pytest.FixtureRequest,
    playwright: Playwright,
) -> Iterator[Page]:
    """Фикстура для создания страницы Chromium без предварительно загруженного состояния.

    Эта фикстура использует `playwright_page_builder` для настройки и запуска страницы
    в браузере Chromium. Имя теста автоматически извлекается из `request.node.name`.
    Используется для запуска тестов без сохраненного состояния браузера.

    Args:
        request (pytest.FixtureRequest): Объект запроса Pytest, используется для
                                         получения имени текущего теста.
        playwright (Playwright): Объект Playwright для управления браузером.

    Yields:
        Iterator[Page]: Генератор, возвращающий объект страницы Playwright.

    Returns:
        None: Ресурсы управляются через генератор.
    """
    yield from playwright_page_builder(
        playwright=playwright,
        browser_type=request.param,
        test_name=request.node.name,
    )


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    """Фикстура для инициализации браузера и сохранения состояния после регистрации.

    Эта фикстура запускается один раз за сессию тестирования. Она открывает браузер,
    сохраняет состояние контекста в файл `browser-state.json`,
    чтобы использовать его в последующих тестах.

    Аргументы:
        playwright (Playwright): Объект Playwright для управления браузером.

    Возвращает:
        None
    """
    browser = playwright.chromium.launch(headless=settings.ui.headless)
    context = browser.new_context(base_url=settings.get_ui_base_url())
    context.storage_state(path=settings.ui.browser_state_file)
    browser.close()


@pytest.fixture(params=settings.ui.browsers)
def chromium_page_with_state(
    request: pytest.FixtureRequest,
    initialize_browser_state,
    playwright: Playwright,
) -> Iterator[Page]:
    """Фикстура для создания страницы Chromium с предварительно загруженным состоянием браузера.

    Эта фикстура использует `playwright_page_builder` для настройки и запуска страницы
    в браузере Chromium. Используется состояние браузера из файла `browser-state.json`,
    что позволяет сохранить авторизацию или другие данные между тестами.
    Также имя теста автоматически извлекается из `request.node.name`.

    Args:
        request (pytest.FixtureRequest): Объект запроса Pytest, используется для
                                         получения имени текущего теста.
        initialize_browser_state: Дополнительная фикстура, используемая для
                                  инициализации состояния браузера перед тестом.
        playwright (Playwright): Объект Playwright для управления браузером.

    Yields:
        Iterator[Page]: Генератор, возвращающий объект страницы Playwright.

    Returns:
        None: Ресурсы управляются через генератор.
    """
    yield from playwright_page_builder(
        playwright=playwright,
        browser_type=request.param,
        test_name=request.node.name,
        state=settings.ui.browser_state_file,
    )
