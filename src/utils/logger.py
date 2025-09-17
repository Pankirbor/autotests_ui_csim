import logging

from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme

# Опционально: кастомная цветовая тема
custom_theme = Theme(
    {
        "logging.level.debug": "blue",
        "logging.level.info": "green",
        "logging.level.warning": "yellow",
        "logging.level.error": "bold red",
        "logging.level.critical": "bold white on red",
    }
)
console = Console(theme=custom_theme)


def get_logger(name: str) -> logging.Logger:
    """Создает и настраивает логгер с выводом в консоль.

    Формат логов включает дату и время, имя логгера, уровень лога и само сообщение.
    Логгер выводит сообщения уровня DEBUG и выше. Используется для отладки и мониторинга работы приложения.

    Returns:
        logging.Logger: Настроенный объект логгера.
    """
    logger = logging.getLogger(name)
    console_handler = RichHandler(
        rich_tracebacks=True,
        show_time=False,
        markup=True,
        console=console,
    )
    formatter = logging.Formatter("%(asctime)s | %(name)s | [plum1]%(funcName)s[/] | %(message)s")
    console_handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    return logger
