class LocatorError(Exception):
    """Базовое исключение для ошибок локаторов."""

    pass


class LocatorNotFoundError(LocatorError):
    """Исключение когда локатор не найден на странице."""

    pass


class LocatorFormatError(LocatorError):
    """Исключение когда не удается отформатировать путь локатора."""

    pass


class ElementInteractionError(LocatorError):
    """Исключение при взаимодействии с элементом."""

    pass
