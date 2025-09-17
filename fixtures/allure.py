from collections.abc import Iterator

import pytest

from integrations.allure.environment import create_allure_environment


@pytest.fixture(scope="session", autouse=True)
def save_allure_environment() -> Iterator[None]:
    """Фикстура, автоматически сохраняющая информацию об окружении в файл Allure.

    Используется для сбора и сохранения данных о тестовом окружении (например, версии браузера,
    URL приложения, конфигурации) после завершения всех тестов. Фикстура имеет сессионный
    уровень (`scope="session"`) и автоматически применяется (`autouse=True`).

    Yields:
        None: Не возвращает значение напрямую, но управляет жизненным циклом через yield.
    """
    yield
    create_allure_environment()
