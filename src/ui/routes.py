from enum import Enum


class AppRoute(str, Enum):
    """Перечисление маршрутов приложения.

    Представляет собой пути к различным страницам веб-приложения в виде строк.
    Используется для удобного обращения к URL внутри тестов или логики приложения.

    Members:
    """

    ABOUT = "/"
    MATERIALS = "/poleznye-materialy"
    NEWS = "/novosti"
    VACANCIES = "/vakansii"
    CONTACTS = "/#feedback"
