from enum import Enum


class AllureEpic(str, Enum):
    """Enum, представляющий эпики в виде строковых перечислений."""

    VACANCIES = "Страница вакансий"
    NAVIGATION = "Навигация по сайту"
