from enum import Enum


class AllureStoryApi(str, Enum):
    LOGIN = "Login"

    GET_ENTITY = "Get entity"
    GET_ENTITIES = "Get entities"
    CREATE_ENTITY = "Create entity"
    UPDATE_ENTITY = "Update entity"
    DELETE_ENTITY = "Delete entity"
    VALIDATE_ENTITY = "Validate entity"


class AllureStoryUi(str, Enum):
    PAGE_LOADS_CORRECTLY = (
        "Страница загружается корректно и отображает все ключевые элементы"
    )
    # Глобальная Навигация (шапка)
    CLICK_HEADER_LOGO = "Клик по логотипу в шапке ведет на главную"
    NAVIGATE_TO_PAGES = "Переход на страницы  через навигацию"
    USE_GLOBAL_SEARCH = "Использование глобального поиска по сайту в шапке"
    # Страница Вакансий: Список
    CLICK_VACANCY_CARD = "Клик по карточке вакансии для перехода на детальную страницу"
    DISPLAY_VACANCY_CARD = "Отображение карточки вакансии"
    # Страница Вакансий: Фильтрация по категориям
    CLICK_CATEGORY_TAB = "Клик по вкладке категории (например, 'Разработка')"
    SELECT_CATEGORY_FROM_DROPDOWN = "Выбор категории из выпадающего списка (селекта)"
    # Страница Вакансий: Расширенные фильтры
    OPEN_ADVANCED_FILTERS = "Открытие панели расширенных фильтров"
    APPLY_EXPERIENCE_FILTER = (
        "Применение фильтра по опыту работы (например, 'От 3 до 6 лет')"
    )
    APPLY_EMPLOYMENT_FILTER = "Применение фильтра по занятости (например, 'Полная')"
    APPLY_SCHEDULE_FILTER = (
        "Применение фильтра по графику работы (например, 'Удаленная работа')"
    )
    EXTENDED_FILTER_FUNCTIONALITY = "Проверка функциональности расширенных фильтров"
    # Страница Вакансий: Сортировка
    CLICK_SORT_BUTTON = "Клик по кнопке сортировки 'Сначала новые'"
    INITIAL_SORT = "Сортировка по умолчанию (Сначала новые)"
    # Футер
    CLICK_FOOTER_AGREEMENT = "Клик по ссылке 'Пользовательское соглашение' в футере"
    CLICK_FOOTER_PRIVACY = "Клик по ссылке 'Политика конфиденциальности' в футере"
    BREADCRUMBS = "Функционал навигации по страницам (хлебные крошки)"
