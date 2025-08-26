import logging


def get_logger(name: str) -> logging.Logger:
    """
    Создает и настраивает логгер с выводом в консоль.

    Формат логов включает дату и время, имя логгера, уровень лога и само сообщение.
    Логгер выводит сообщения уровня DEBUG и выше. Используется для отладки и мониторинга работы приложения.

    Returns:
        logging.Logger: Настроенный объект логгера.
    """
    logger = logging.getLogger(name)
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(funcName)s | %(levelname)s | %(message)s"
    )
    console_handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    return logger
