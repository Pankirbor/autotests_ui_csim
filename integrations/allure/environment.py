from pathlib import Path
import platform
from pprint import pformat
import sys

from config import settings


def create_allure_environment():
    """Функция записывает в файл environment.properties."""
    properties_data = list(settings.get_env_properties().items())
    properties_data.extend(
        [
            ("OS_INFO", f"{platform.system()} {platform.version()}"),
            ("PYTHON_VERSION", sys.version),
        ]
    )
    properties_content = "\n".join([f"{key}={value}" for key, value in properties_data])
    # env_lines = []

    # data = settings.model_dump()

    # for key, value in data.items():
    #     if key in ("test_user", "auth_token"):  # Пропускаем чувствительные данные
    #         continue
    #     # Сериализуем значение в красивую строку
    #     serialized = pformat(value, indent=4, width=100, sort_dicts=False)
    #     env_lines.append(f"{key}={serialized}")

    # env_lines.extend(
    #     [
    #         f"OS_INFO={platform.system()} {platform.version()}",
    #         f"PYTHON_VERSION={sys.version}",
    #     ]
    # )

    # properties_content = "\n".join(env_lines)

    properties_path: Path = (
        settings.reporting.allure_results_dir / "environment.properties"
    )
    properties_path.write_text(properties_content, encoding="utf-8")
