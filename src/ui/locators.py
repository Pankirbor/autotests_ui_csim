class NavBarLocators:
    ABOUT_US_TAB = "//a[@role='tab' and @href='/']"
    MATERIALS_TAB = "//a[@role='tab' and @href='/poleznye-materialy']"
    NEWS_TAB = "//a[@role='tab' and @href='/novosti']"
    VACANCIES_TAB = "//a[@role='tab' and @href='/vakansii']"
    CONTACT_TAB = "//a[@role='tab' and @href='/#feedback']"
    SEARCH_TAB = "//header//div[@class='input_search__wrapp']"
    SEARCH_ICON = ".input_search__icon_search"
    SEARCH_INPUT = "//div[contains(@class, 'input_search__wrapp')]//input"
    SEARCH_ENTER_ICON = (
        "i[role='presentation']"  # q-icon icon-move-right cursor-pointer
    )
    LOGO = "//div[contains(@class, 'q-avatar')]//img"


class HeaderPageLocators:
    TITLE = "//h1[contains(@class, 'post__title')] | //h1"
    SUBTITLE = "//h3[contains(@class, 'post__subtitle')] | //section[contains(@class, 'header__inner')]//p"


class BreadcrumbsLocators:
    CONTAINER = ("//div[contains(@class, 'q-breadcrumbs')]", "Контейнер хлебных крошек")
    ITEMS = ".q-breadcrumbs__el"
    HOME_LINK = (
        "//div[contains(@class, 'q-breadcrumbs')]//a[@href='/']",
        "Ссылка на главную",
    )
    CURRENT_PAGE = (
        "//div[contains(@class, 'q-breadcrumbs')]//span[contains(@class, 'q-breadcrumbs__el')]",
        "Текущая страница",
    )


class FilterLocators:
    """Локаторы для элементов фильтрации на странице"""

    # Контейнер фильтров
    FILTER_CONTAINER = ".post__bar"

    # Контейнер вкладок
    TABS_CONTAINER = ".category_tabs.period"

    # Все вкладки периода
    PERIOD_TABS = ".q-tab.period__year"
    ALL_TABS = ".q-tab"  # Все вкладки включая календарь

    # Конкретные вкладки по классам
    TAB_ALL = ".q-tab.period__year:has(.q-tab__label:text('Все'))"
    TAB_2025 = ".q-tab.period__year:has(.q-tab__label:text('2025'))"
    TAB_2024 = ".q-tab.period__year:has(.q-tab__label:text('2024'))"
    TAB_CUSTOM_PERIOD = ".q-tab.period__calendar"

    # Активная/неактивная вкладка
    ACTIVE_TAB = ".q-tab.q-tab--active"
    INACTIVE_TAB = ".q-tab.q-tab--inactive"

    # Элементы вкладок
    TAB_LABEL = ".q-tab__label"
    TAB_INDICATOR = ".q-tab__indicator"

    # Селект сортировки
    SORT_SELECT = ".period_select__sort"
    SORT_SELECT_CONTROL = ".period_select__sort .q-field__control"
    SORT_SELECT_VALUE = ".period_select__sort span"
    SORT_DROPDOWN_ICON = ".q-field__inner .q-select__dropdown-icon"
    SORT_OPTIONS = "[role='option']"

    # Кнопка фильтра по тегам
    TAGS_FILTER_BUTTON = ".btn_filters"
    TAGS = "checkbox__tags"

    # Кнопки формата показа
    VIEW_BUTTONS_CONTAINER = ".post__btns_view"
    VIEW_BUTTON = ".post__btns_view .q-btn"
    TILE_VIEW_BUTTON = ".post__btns_view .icon-tile"
    LIST_VIEW_BUTTON = ".post__btns_view .icon-list"
    ACTIVE_VIEW_BUTTON = ".post__btns_view .q-btn.active"

    # Иконки
    CALENDAR_ICON = ".icon-calendar"
    CHEVRON_DOWN_ICON = ".icon-chevron-down"

    # Внутренние элементы календарной вкладки
    CALENDAR_INNER = ".period__calendar_inner"
    CALENDAR_VIEW = "[role='menu']"
    # Портал с календарем (меню)
    CALENDAR_PORTAL = "#q-portal--menu--1"

    # Сам календарь внутри портала
    CALENDAR_MENU = "[id^='q-portal--menu--'] [role='menu']"
    CALENDAR_DATE = "[id^='q-portal--menu--'] .q-date"

    # Элементы календаря
    CALENDAR_HEADER = "[id^='q-portal--menu--'] .q-date__navigation"
    CALENDAR_DAYS = (
        "[id^='q-portal--menu--'] .q-date__calendar-days.q-date__calendar-item--in"
    )
    CALENDAR_BUTTONS = "[id^='q-portal--menu--'] .period__btn"


class FilterVacanciesLocators:
    """Локаторы для элементов фильтрации на странице вакансий"""

    FILTER_CONTAINER = ("//div[contains(@class,'post__bar')]", "Контейнер фильтров")
    FILTERS_TABS = ".q-tabs"
    ALL_TABS = ".q-tab"
    SORT = ("//div[contains(@class, 'btn_sort')]//button", "Кнопка сортировки")
    FILTER_BTN = ("//div[contains(@class, 'btn_filters')]//button", "Кнопка 'Фильтр'")
    TAB = ("//div[contains(@class, 'q-tab')][{index}]", "Вкладка {title}")


class VacanciesListLocators:
    CONTAINER = ("//div[contains(@class, 'row')]", "Блок со списком вакансий")
    VACANCY_CARDS = ("//article[contains(@class, 'vacancy_card')]", "Список вакансий")
    CARD_TITLE = ("//h3[contains(@class, 'vacancy_card__title')]", "Название вакансии")
    CARD_DATE = ("//time", "Дата публикации")
    CARD_LINK = ("//a[contains(@class, 'vacancy_card__link')]", "Ссылка на вакансию")
    CARD_ICON = (
        "//i[contains(@class, 'vacancy_card__icon')]",
        "Иконка ссылки на вакансию",
    )
    EMPTY_VIEW_CONTAINER = (
        "//div[contains(@class, 'not_found')]",
        "Контейнер пустого состояния",
    )
    EMPTY_VIEW_TITLE = ("//div[@class='not_found']//h3", "Заголовок пустого состояния")
    EMPTY_VIEW_DESCRIPTION = (
        "//div[@class='not_found']//p",
        "Описание пустого состояния",
    )


class FooterLocators:
    """Локаторы для элементов футера"""

    FOOTER_CONTAINER = "footer.container"
    INFO = "//footer[contains(@class, 'footer')]//div[contains(@class, 'footer__info')]"
    PRIVACY_POLICY_LINK = "//footer[contains(@class, 'footer')]//a[contains(@href, 'Политика конфиденциальности')"
    USER_AGREEMENT_LINK = "//footer[contains(@class, 'footer')]//a[contains(@href, 'Пользовательское_соглашение')]"
    MAIN_PAGE_LINK = "//footer[contains(@class, 'footer')]//a[@href='/']"
    ICON = "//footer[contains(@class, 'footer')]//img[@alt='logo']"


class UsefulMaterialsLocators:
    BREADCRUMBS = ".q-breadcrumbs__el"
    PAGE_TITLE = "h1"
    MATERIAL_CARDS = ".post_card"
    PAGINATION_ITEMS = ".pagination_page button"
    CURRENT_PAGE = ".pagination_page button[aria-current='true']"
    SORT_SELECT = ".sort-select"
