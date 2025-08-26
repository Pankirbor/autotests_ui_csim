from enum import Enum
from typing import Any, Self, Optional, List
from pydantic import BaseModel, EmailStr, DirectoryPath, HttpUrl, FilePath, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Browser(str, Enum):
    """
    Перечисление, представляющее поддерживаемые браузеры.

    Каждый элемент перечисления представлен в виде строки, что позволяет использовать
    значения напрямую при выборе браузера для запуска тестов или других действий.

    Members:
        WEBKIT (str): Браузер WebKit.
        CHROMIUM (str): Браузер Chromium.
        FIREFOX (str): Браузер Firefox.
    """

    WEBKIT = "webkit"
    CHROMIUM = "chromium"
    FIREFOX = "firefox"


class Environment(str, Enum):
    """
    Перечисление для окружений.
    """

    LOCAL = "local"
    DEV = "dev"
    STAGING = "staging"
    PROD = "production"


class TestUser(BaseModel):
    """
    Модель данных, представляющая тестового пользователя.

    Используется для валидации и хранения информации о пользователе,
    необходимой для тестирования. Включает обязательные поля: имя пользователя,
    адрес электронной почты и пароль.

    Attributes:
        username (str): Имя пользователя.
        email (EmailStr): Адрес электронной почты, валидированный как корректный email.
        password (str): Пароль пользователя.
    """

    username: str
    email: EmailStr
    password: str


class HTTPClientConfig(BaseModel):
    """
    Класс для хранения настроек HTTP-клиента.
    """

    base_url: HttpUrl
    timeout: float = Field(default=30.0)
    follow_redirects: bool = Field(default=True)

    @property
    def url_as_string(self) -> str:
        return f"{self.base_url}"


class TestData(BaseModel):
    """
    Класс для хранения доступа к тестовым данным.
    """

    image_jpeg_file: FilePath
    test_users_file: Optional[FilePath] = None


class UISettings(BaseModel):
    """
    Настройки для UI тестирования.
    """

    app_url: HttpUrl
    headless: bool = Field(default=True)
    browsers: List[Browser] = Field(default=[Browser.CHROMIUM])
    default_browser: Browser = Field(default=Browser.CHROMIUM)
    viewport_width: int = Field(default=1920)
    viewport_height: int = Field(default=1080)
    # slow_mo: int = Field(default=0)  # Замедление действий в ms
    videos_path: DirectoryPath
    tracing_path: DirectoryPath
    browser_state_file: FilePath
    # snapshots_tests: Optional[List[str]] = None


class APISettings(BaseModel):
    """
    Настройки для API тестирования.
    """

    http_client: HTTPClientConfig
    internal_host: HttpUrl
    api_version: str = Field(default="/api/v1")


class ReportingSettings(BaseModel):
    """
    Настройки для отчетности.
    """

    allure_api_results_dir: DirectoryPath
    allure_ui_results_dir: DirectoryPath
    video_recording: bool = Field(default=False)
    trace_recording: bool = Field(default=False)


class FrameworkSettings(BaseSettings):
    """
    Единый класс настроек для всего тестового фреймворка.
    """

    model_config = SettingsConfigDict(
        env_file=".env.example",
        env_file_encoding="utf-8",
        extra="ignore",
        env_nested_delimiter="__",
    )

    # Основные настройки
    environment: Environment = Field(default=Environment.LOCAL)
    debug: bool = Field(default=False)
    log_level: str = Field(default="INFO")

    # UI настройки
    ui: UISettings

    # API настройки
    api: APISettings

    # Тестовые данные
    test_data: TestData

    # Отчетность
    reporting: ReportingSettings

    # Пользователи
    test_user: TestUser

    @classmethod
    def initialize(cls) -> Self:
        """
        Инициализирует настройки и создает необходимые директории.

        Returns:
            Self: Экземпляр класса настроек.
        """
        # Создаем базовые директории если их нет
        base_dirs = [
            "./videos",
            "./tracing",
            "./allure-api-results",
            "./allure-ui-results",
            "./logs",
        ]

        for dir_path in base_dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)

        # Создаем файл состояния браузера если его нет
        browser_state_file = Path("browser_state.json")
        browser_state_file.touch(exist_ok=True)

        return cls()

    def get_ui_base_url(self) -> str:
        """
        Возвращает базовый URL для UI.

        Returns:
            str: Базовый URL для UI.
        """
        return f"{self.ui.app_url}/"

    def get_api_base_url(self) -> str:
        """
        Возвращает полный базовый URL для API.

        Returns:
            str: Полный базовый URL для API.
        """
        return f"{self.api.base_url}{self.api.api_version}"

    def get_env_properties(self) -> dict[str, Any]:
        """
        Возвращает свойства окружения для Allure.

        Returns:
            dict: Словарь с настройками окружения.
        """
        return {
            "Environment": self.environment.value,
            "UI_URL": self.get_ui_base_url(),
            "API_URL": self.get_api_base_url(),
            "Headless": str(self.ui.headless),
            "Browsers": ", ".join([b.value for b in self.ui.browsers]),
            "Debug": str(self.debug),
            "Log_Level": self.log_level,
        }

    def print_settings(self):
        """Печатает текущие настройки."""
        from src.utils.console_output_formatter import print_dict

        print_dict(self.model_dump(exclude={"test_user", "auth_token"}))


# Глобальный экземпляр настроек
settings = FrameworkSettings.initialize()
settings.print_settings()
