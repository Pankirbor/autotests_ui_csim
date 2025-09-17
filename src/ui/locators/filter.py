from src.ui.locators.base import UILocator


class FilterPageLocators:
    """Локаторы для элементов фильтрации на странице."""

    FILTER_CONTAINER = UILocator(
        selector=".post__bar", description="Контейнер фильтров"
    )
    TABS_CONTAINER = UILocator(
        selector=".category_tabs.period", description="Контейнер вкладок фильтрации"
    )
    PERIOD_TABS = UILocator(
        selector=".q-tab.period__year", description="Вкладки периода"
    )
    ALL_TABS = UILocator(
        selector=".q-tab", description="Все вкладки (включая календарь)"
    )
    TAB_ALL = UILocator(
        selector=".q-tab.period__year:has(.q-tab__label:text('Все'))",
        description="Вкладка 'Все'",
    )
    TAB_2025 = UILocator(
        selector=".q-tab.period__year:has(.q-tab__label:text('2025'))",
        description="Вкладка '2025'",
    )
    TAB_2024 = UILocator(
        selector=".q-tab.period__year:has(.q-tab__label:text('2024'))",
        description="Вкладка '2024'",
    )
    TAB_CUSTOM_PERIOD = UILocator(
        selector=".q-tab.period__calendar",
        description="Вкладка календаря (пользовательский период)",
    )
    ACTIVE_TAB = UILocator(
        selector=".q-tab.q-tab--active", description="Активная вкладка"
    )
    INACTIVE_TAB = UILocator(
        selector=".q-tab.q-tab--inactive", description="Неактивная вкладка"
    )
    TAB_LABEL = UILocator(selector=".q-tab__label", description="Текст вкладки")
    TAB_INDICATOR = UILocator(
        selector=".q-tab__indicator", description="Индикатор активной вкладки"
    )
    SORT_SELECT = UILocator(
        selector=".period_select__sort", description="Селект сортировки"
    )
    SORT_SELECT_CONTROL = UILocator(
        selector=".period_select__sort .q-field__control",
        description="Контрол селекта сортировки",
    )
    SORT_SELECT_VALUE = UILocator(
        selector=".period_select__sort span", description="Текущее значение сортировки"
    )
    SORT_DROPDOWN_ICON = UILocator(
        selector=".q-field__inner .q-select__dropdown-icon",
        description="Иконка раскрытия селекта",
    )
    SORT_OPTIONS = UILocator(selector="[role='option']", description="Опции сортировки")
    TAGS_FILTER_BUTTON = UILocator(
        selector=".btn_filters", description="Кнопка фильтра по тегам"
    )
    TAGS = UILocator(selector="checkbox__tags", description="Контейнер тегов")
    VIEW_BUTTONS_CONTAINER = UILocator(
        selector=".post__btns_view", description="Контейнер кнопок переключения вида"
    )
    VIEW_BUTTON = UILocator(
        selector=".post__btns_view .q-btn", description="Кнопка переключения вида"
    )
    TILE_VIEW_BUTTON = UILocator(
        selector=".post__btns_view .icon-tile", description="Кнопка вида 'Плитка'"
    )
    LIST_VIEW_BUTTON = UILocator(
        selector=".post__btns_view .icon-list", description="Кнопка вида 'Список'"
    )
    ACTIVE_VIEW_BUTTON = UILocator(
        selector=".post__btns_view .q-btn.active", description="Активная кнопка вида"
    )
    CALENDAR_ICON = UILocator(selector=".icon-calendar", description="Иконка календаря")
    CHEVRON_DOWN_ICON = UILocator(
        selector=".icon-chevron-down", description="Иконка раскрытия"
    )
    CALENDAR_INNER = UILocator(
        selector=".period__calendar_inner", description="Внутренний контейнер календаря"
    )
    CALENDAR_VIEW = UILocator(
        selector="[role='menu']", description="Вид календаря (меню)"
    )
    CALENDAR_PORTAL = UILocator(
        selector="#q-portal--menu--1", description="Портал календаря"
    )
    CALENDAR_MENU = UILocator(
        selector="[id^='q-portal--menu--'] [role='menu']",
        description="Меню календаря внутри портала",
    )
    CALENDAR_DATE = UILocator(
        selector="[id^='q-portal--menu--'] .q-date",
        description="Компонент даты в календаре",
    )
    CALENDAR_HEADER = UILocator(
        selector="[id^='q-portal--menu--'] .q-date__navigation",
        description="Шапка календаря",
    )
    CALENDAR_DAYS = UILocator(
        selector="[id^='q-portal--menu--'] .q-date__calendar-days.q-date__calendar-item--in",
        description="Дни календаря",
    )
    CALENDAR_BUTTONS = UILocator(
        selector="[id^='q-portal--menu--'] .period__btn",
        description="Кнопки в календаре",
    )
