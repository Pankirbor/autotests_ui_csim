from enum import Enum


class AllureTagApi(str, Enum):
    """Enum, представляющий теги Allure для API-тестов."""

    API = "api"
    GET_ENTITY = "GET_ENTITY"
    GET_ENTITIES = "GET_ENTITIES"
    CREATE_ENTITY = "CREATE_ENTITY"
    UPDATE_ENTITY = "UPDATE_ENTITY"
    DELETE_ENTITY = "DELETE_ENTITY"
    VALIDATE_ENTITY = "VALIDATE_ENTITY"


class AllureTagUi(str, Enum):
    """Enum, представляющий теги Allure для UI-тестов."""

    UI = "ui"
    SMOKE = "smoke"
    REGRESSION = "regression"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    DESKTOP = "desktop"
    MOBILE = "mobile"
