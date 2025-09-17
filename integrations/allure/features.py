from enum import Enum


class AllureFeature(str, Enum):
    """Enum, представляющий фичи в виде строковых перечислений."""

    VACANCY_LIST = "Список вакансий и карточки"
    CATEGORY_FILTERS = "Фильтрация по категориям (табы и селект)"
    ADVANCED_FILTERS = "Расширенные фильтры (опыт, занятость, график)"
    SORTING = "Сортировка вакансий"
    FOOTER = "Футер"
    HEADER_NAVIGATION = "Навигация в шапке"
    HEADER_SEARCH = "Поиск по сайту в шапке"
