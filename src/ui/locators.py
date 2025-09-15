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
    ALL_TABS = "//div[contains(@role, 'tablist')]//div[contains(@role, 'tab')]"
    SORT = ("//button[contains(@class, 'btn_sort')]", "Кнопка сортировки")
    ICON_SORTING_UP = (
        "//button[contains(@class, 'btn_sort')]//i[contains(@class, 'icon-sorting-up')]",
        "Иконка сортировки по возрастанию",
    )
    ICON_SORTING_DOWN = (
        "//button[contains(@class, 'btn_sort')]//i[contains(@class, 'icon-sorting-down')]",
        "Иконка сортировки по убыванию",
    )
    FILTER_BTN = ("//button[contains(@class, 'btn_filters')]", "Кнопка 'Фильтр'")
    TAB = (
        "(//div[contains(@role, 'tablist')]//div[contains(@role, 'tab')])[{index}]",
        "Вкладка {title}",
    )
    TAB_ALL_VACANCIES = (
        "//div[contains(@class, 'q-tab')]//div[contains(text(), 'Все')]",
        "Вкладка 'Все'",
    )


class VacancyFiltersMenuLocators:
    """
    Локаторы для выпадающего меню фильтров вакансий.
    """

    # --- Основные элементы ---
    CONTAINER = (
        "//div[contains(@class,'q-menu')]",
        "Контейнер выпадающего меню фильтров",
    )
    RESET_BUTTON = (
        "//button[contains(., 'Сбросить')]",
        "Кнопка 'Сбросить' в меню фильтров",
    )
    APPLY_BUTTON = (
        "//button[contains(., 'Применить')]",
        "Кнопка 'Применить' в меню фильтров",
    )

    # --- Чекбоксы ---
    # Шаблон: используется в Checkbox(BaseElement) — должен указывать на корневой элемент чекбокса (.q-checkbox)
    CHECKBOX_ROOT = (
        ".//div[contains(@class, 'q-checkbox') and .//div[contains(@class, 'q-checkbox__label') and normalize-space() = '{label}']]",
        "Корневой элемент чекбокса по тексту метки '{label}'",
    )

    CHECKBOX_ITEMS = "//div[contains(@role, 'checkbox')]"
    CHECKBOX_ITEM = (
        "(//div[normalize-space(text()) = '{group_title}']/following-sibling::div[@role='group'][1]//div[contains(@role, 'checkbox')])[{index}]",
        "Чекбокс из группы {group_title}: {label}",
    )

    # Локатор для получения текста метки (если нужно отдельно)
    CHECKBOX_LABEL = (
        ".//div[contains(@class, 'q-checkbox__label')]",
        "Текст метки чекбокса",
    )

    # --- Группы чекбоксов ---
    # Шаблон: находит группу чекбоксов по заголовку раздела
    CHECKBOX_GROUP_BY_TITLE = (
        "//div[normalize-space(text()) = '{group_title}']/following-sibling::div[@role='group'][1]",
        "Группа чекбоксов, следующая за заголовком '{group_title}'",
    )


class VacanciesListLocators:
    CONTAINER = (
        "//article[@class='post']//div[@class='row']",
        "Блок со списком вакансий",
    )
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


class VacancyItemLocators:
    """
    Локаторы для страницы детальной информации о вакансии.
    Каждый элемент — кортеж: (XPath, человекочитаемое название)
    """

    # --- Основной контейнер вакансии ---
    CONTAINER = (
        "//article[contains(@class, 'vacancy')]",
        "Контейнер детальной страницы вакансии",
    )

    # --- Заголовок и дата ---
    VACANCY_NAME = ("//h1[contains(@class, 'vacancy__title')]", "Название вакансии")
    PUBLICATION_DATE = (
        "//div[contains(@class, 'header')]//time",
        "Дата публикации вакансии",
    )

    # --- Теги (занятость, опыт, график) ---
    TAGS_CONTAINER = (
        "//div[contains(@class, 'vacancy__tags')]",
        "Контейнер тегов вакансии",
    )
    EMPLOYMENT_TAG = (
        "//button[contains(@class, 'tag') and .//span[text()='Занятость: Полная']]",
        "Тег 'Занятость: Полная'",
    )
    EXPERIENCE_TAG = (
        "//button[contains(@class, 'tag') and .//span[contains(text(), 'Опыт:')]]",
        "Тег с указанием опыта работы",
    )
    SCHEDULE_TAG = (
        "//button[contains(@class, 'tag') and .//span[contains(text(), 'График работы:')]]",
        "Тег с указанием графика работы",
    )

    # --- Секции контента: Задачи, Ожидания, Плюсы, Условия ---
    TASKS_SECTION = (
        "//div[contains(@class, 'post')]//h2[text()='Задачи']/following-sibling::ul[1]",
        "Список задач вакансии",
    )
    TASKS_ITEMS = (
        "//div[contains(@class, 'post')]//h2[text()='Задачи']/following-sibling::ul[1]/li",
        "Элементы списка задач",
    )

    REQUIREMENTS_SECTION = (
        "//div[contains(@class, 'post')]//h2[text()='Ожидаем от кандидата']/following-sibling::ul[1]",
        "Список требований к кандидату",
    )
    REQUIREMENTS_TITLE = (
        "//h2[text()='Ожидаем от кандидата']",
        "Заголовок секции 'Ожидаем от кандидата'",
    )
    REQUIREMENTS_ITEMS = (
        "//div[contains(@class, 'post')]//h2[text()='Ожидаем от кандидата']/following-sibling::ul[1]/li",
        "Элементы списка требований",
    )

    PLUS_SECTION = (
        "//div[contains(@class, 'post')]//h2[text()='Будет плюсом']/following-sibling::ul[1]",
        "Список желательных навыков (плюсов)",
    )
    PLUS_TITLE = ("//h2[text()='Будет плюсом']", "Заголовок секции 'Будет плюсом'")
    PLUS_ITEMS = (
        "//div[contains(@class, 'post')]//h2[text()='Будет плюсом']/following-sibling::ul[1]/li",
        "Элементы списка плюсов",
    )

    CONDITIONS_SECTION = (
        "//div[contains(@class, 'post')]//h2[text()='Условия']/following-sibling::ul[1]",
        "Список условий работы",
    )
    CONDITIONS_ITEMS = (
        "//div[contains(@class, 'post')]//h2[text()='Условия']/following-sibling::ul[1]/li",
        "Элементы списка условий",
    )

    # --- Кнопка "Откликнуться на вакансию" ---
    RESPONSE_BUTTON = (
        "//div[contains(@class, 'vacancy__actions')]//button[.//span[text()='Откликнуться на вакансию']]",
        "Кнопка 'Откликнуться на вакансию'",
    )

    # --- Описание (абзацы между списками) ---
    DESCRIPTION_AFTER_TASKS = (
        "//div[contains(@class, 'post')]//h2[text()='Задачи']/following-sibling::p[1]",
        "Описание после секции 'Задачи'",
    )
    DESCRIPTION_AFTER_PLUS = (
        "//div[contains(@class, 'post')]//h2[text()='Будет плюсом']/following-sibling::p[1]",
        "Описание после секции 'Будет плюсом'",
    )


class VacancyResponseFormLocators:
    """
    Локаторы для формы отклика на вакансию.
    Используются XPath + aria-label для стабильности.
    Каждый элемент — кортеж: (локатор, человекочитаемое название)
    """

    # --- Поля ввода ---
    FULL_NAME_INPUT = (
        "//input[@aria-label='Представьтесь, пожалуйста']",
        "Поле ввода 'Имя'",
    )
    PHONE_INPUT = ("//input[@aria-label='Ваш номер телефона']", "Поле ввода 'Телефон'")
    EMAIL_INPUT = ("//input[@aria-label='Ваш Email']", "Поле ввода 'Email'")
    RESUME_LINK_INPUT = (
        "//input[@aria-label='Ваше резюме']",
        "Поле ввода 'Ссылка на резюме'",
    )

    # --- Кнопки ---
    SUBMIT_BUTTON = (
        "//form[contains(@class, 'vacancy_form')]//button[@type='submit' and .//span[text()='Отправить']]",
        "Кнопка 'Отправить'",
    )
    ATTACH_FILE_LINK = (
        "//span[contains(@class, 'file-link') and text()='прикрепите файл']",
        "Ссылка 'прикрепите файл'",
    )

    # --- Контейнеры ---
    FORM_CONTAINER = (
        "//form[contains(@class, 'vacancy_form')]",
        "Контейнер формы отклика",
    )
    FOOTER_TEXT = (
        "//div[contains(@class, 'vacancy_form__footer')]",
        "Футер формы с согласием на обработку данных",
    )

    # --- Валидационные сообщения (ошибки) ---
    # Ищем <div role="alert"> внутри label того же поля
    FULL_NAME_ERROR = (
        "//input[@aria-label='Представьтесь, пожалуйста']/ancestor::label//div[@role='alert']",
        "Сообщение об ошибке под полем 'Имя'",
    )
    PHONE_ERROR = (
        "//input[@aria-label='Ваш номер телефона']/ancestor::label//div[@role='alert']",
        "Сообщение об ошибке под полем 'Телефон'",
    )
    EMAIL_ERROR = (
        "//input[@aria-label='Ваш Email']/ancestor::label//div[@role='alert']",
        "Сообщение об ошибке под полем 'Email'",
    )
    RESUME_LINK_ERROR = (
        "//input[@aria-label='Ваше резюме']/ancestor::label//div[@role='alert']",
        "Сообщение об ошибке под полем 'Резюме'",
    )

    # --- Капча ---
    SMART_CAPTCHA_CONTAINER = (
        "//div[contains(@class, 'smart-captcha')]",
        "Контейнер Yandex SmartCaptcha",
    )
    SMART_CAPTCHA_IFRAME = ("//iframe[@data-testid='backend-iframe']", "Iframe капчи")

    # --- Успешное сообщение (если появится — сейчас в HTML нет) ---
    SUCCESS_MESSAGE = (
        "//div[contains(text(), 'успешно') or contains(text(), 'отправлен') or contains(@class, 'success')]",
        "Сообщение об успешной отправке формы",
    )


class FooterLocators:
    """Локаторы для элементов футера"""

    FOOTER_CONTAINER = "footer.container"
    INFO = "//footer[contains(@class, 'footer')]//div[contains(@class, 'footer__info')]"
    PRIVACY_POLICY_LINK = "//footer[contains(@class, 'footer')]//a[contains(@href, 'Политика конфиденциальности.pdf')]"
    USER_AGREEMENT_LINK = "//footer[contains(@class, 'footer')]//a[contains(@href, 'Пользовательское_соглашение.pdf')]"
    MAIN_PAGE_LINK = "//footer[contains(@class, 'footer')]//a[@href='/']"
    ICON = "//footer[contains(@class, 'footer')]//img[@alt='logo']"


class UsefulMaterialsLocators:
    BREADCRUMBS = ".q-breadcrumbs__el"
    PAGE_TITLE = "h1"
    MATERIAL_CARDS = ".post_card"
    PAGINATION_ITEMS = ".pagination_page button"
    CURRENT_PAGE = ".pagination_page button[aria-current='true']"
    SORT_SELECT = ".sort-select"


class CookiesLocators:
    CONTAINER = (".cookie-dialog", "Контейнер с куками")
    ACCEPT_BUTTON = (".cookie-dialog button:has-text('Принять')", "Кнопка 'Принять'")
