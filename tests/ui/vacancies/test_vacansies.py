import re

import allure
from allure_commons.types import Severity
import pytest

from integrations.allure import AllureEpic, AllureFeature, AllureStoryUi, AllureTagUi
from src.ui.pages.vacancies.vacancies_page import VacanciesPage
from src.ui.pages.vacancies.vacancy_page import VacancyDetailPage
from src.ui.routes import AppRoute


@pytest.mark.UI
@allure.epic(AllureEpic.VACANCIES)
@allure.feature(AllureFeature.VACANCY_LIST)
class TestVacancyList:
    @allure.title("Проверка, что страница вакансий загружается корректно")
    @allure.story(AllureStoryUi.PAGE_LOADS_CORRECTLY)
    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTagUi.UI, AllureTagUi.SMOKE)
    def test_vacancies_page_loads_and_displays_all_critical_elements(
        self, vacancies_page: VacanciesPage
    ):
        """Тест: Проверка, что страница вакансий загружается корректно.

        Что тестируется:
            - После перехода на страницу '/vakansii' должны быть видимы:
                1. Глобальная навигационная панель (шапка).
                2. Хлебные крошки с текстом "Все вакансии".
                3. Заголовок страницы с текстом "Присоединяйся к команде Центра".
                4. Панель фильтров (категории, поиск, сортировка).
                5. Список карточек вакансий.
            - Это базовый smoke-тест, гарантирующий, что страница не "сломана".
        """
        vacancies_page.visit(AppRoute.VACANCIES)
        vacancies_page.nav_bar.check_visible()
        vacancies_page.breadcrumbs.check_visible("Все вакансии")
        vacancies_page.header.check_visible()
        vacancies_page.header.title.check_contain_text("Присоединяйся к команде Центра")
        vacancies_page.header.subtitle.check_contain_text(
            "Развивайся вместе с нами, создавай нейросети и двигай технологические процессы"
        )
        vacancies_page.filter_bar.check_visible()
        vacancies_page.vacancies_list.check_visible()

    @allure.title(
        "Проверка корректного отображения, состояний и функциональности хлебных крошек"
        " на странице вакансий"
    )
    @allure.story(AllureStoryUi.BREADCRUMBS)
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTagUi.UI, AllureTagUi.POSITIVE)
    def test_vacancies_page_breadcrumbs(self, vacancies_page: VacanciesPage):
        """Тест: Проверка корректной работы хлебных крошек на странице вакансий.

        Предусловия:
            - Страница вакансий загружена.
        Шаги:
            1. Проверить, что блок хлебных крошек отображается на странице.
            2. Проверить текстовое содержимое крошек:
                - Первая крошка (родительская): "Главная" (является кликабельной ссылкой).
                - Вторая крошка (текущая): "Все вакансии" (не является ссылкой).
            3. Проверить состояние ссылки "Главная":
                b. Ссылка должна быть активной (иметь атрибут `href="/"`, не быть disabled).
            4. Проверить функциональность:
                a. Кликнуть по ссылке "Главная".
                b. Убедиться, что произошел переход на главную страницу (URL заканчивается на '/').
                c. Убедиться, что главная страница загрузилась корректно
                   (например, отображается герой-секция или навигация).
        Ожидаемый результат:
            - Блок хлебных крошек отображается корректно.
            - Текст крошек: "Главная | Все вакансии".
            - Ссылка "Главная" ведет на главную страницу при клике.
            - Текущая крошка "Все вакансии" не является кликабельной.
        """
        vacancies_page.visit(AppRoute.VACANCIES)
        vacancies_page.nav_bar.vacancies_tab.is_active()
        vacancies_page.breadcrumbs.should_current_page_not_be_clickable()
        vacancies_page.breadcrumbs.check_visible("Все вакансии")
        vacancies_page.breadcrumbs.home_link.check_enabled()
        vacancies_page.breadcrumbs.home_link.click()
        vacancies_page.check_current_url(re.compile(r".*/"))
        vacancies_page.nav_bar.about_tab.is_active()

    @allure.title(
        "Проверка, что клик по карточке вакансии открывает детальную страницу"
    )
    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStoryUi.CLICK_VACANCY_CARD)
    @allure.tag(AllureTagUi.UI, AllureTagUi.POSITIVE)
    def test_click_on_vacancy_card(
        self, vacancies_page: VacanciesPage, vacancy_detail_page: VacancyDetailPage
    ):
        """Тест: Проверка, что клик по карточке вакансии открывает детальную страницу.

        Предусловия:
            - Пользователь находится на странице '/vakansii'.
            - Список вакансий содержит как минимум одну карточку.
        Шаги:
            1. Получить данные первой вакансии в списке (название, дата, URL).
            2. Навести курсор на карточку вакансии (проверить hover-состояние, если применимо).
            3. Кликнуть по карточке вакансии.
            4. Дождаться полной загрузки детальной страницы вакансии.
            5. Проверить, что URL страницы соответствует ожидаемому (на основе href карточки).
            6. Проверить, что на детальной странице отображается:
                - Заголовок вакансии, идентичный названию в карточке.
                - Дата публикации вакансии.
                - Блок "Обязанности".
                - Блок "Требования".
                - Блок "Условия".
                - Кнопка "Откликнуться" (или аналогичная).
            7. Проверить, что хлебные крошки на детальной странице содержат путь:
                "Главная | Все вакансии | [Название вакансии]".

        Ожидаемый результат:
            - Пользователь успешно переходит на детальную страницу выбранной вакансии.
            - Все ключевые элементы интерфейса и контент отображаются корректно.
            - Информация на детальной странице соответствует данным из карточки в списке.
        """
        vacancies_page.visit(AppRoute.VACANCIES)
        vacancies_page.vacancies_list.check_visible()
        vacancies_page.vacancies_list.check_hover_on_vacancy()
        first_vacancy = vacancies_page.vacancies_list.get_vacancy_by_index(index=1)
        first_vacancy_data = vacancies_page.vacancies_list.get_vacancy_data(index=1)
        first_vacancy.click()
        vacancy_detail_page.check_current_url(
            re.compile(rf".*{first_vacancy_data['link']}")
        )
        vacancy_detail_page.check_visible()
        vacancy_detail_page.check_vacancy_title(first_vacancy_data["title"])


@pytest.mark.UI
@allure.epic(AllureEpic.VACANCIES)
@allure.feature(AllureFeature.CATEGORY_FILTERS)
@allure.severity(Severity.NORMAL)
@allure.tag(AllureTagUi.UI, AllureTagUi.POSITIVE)
class TestVacancyFilters:
    @allure.title(
        "Проверка, что при клике на вкладку категории в фильтре, "
        "список карточек вакансий обновляется"
    )
    @allure.story(AllureStoryUi.CLICK_CATEGORY_TAB)
    def test_click_category_tab(self, vacancies_page: VacanciesPage):
        """Тест: Проверка, что при клике на вкладку категории в фильтре,список вакансий обновляется.

        Предусловия:
            - Страница вакансий загружена.
        Шаги:
            1. Нажать на вкладку категории в фильтре.
            2. Проверить, что список карточек вакансий обновился.
        Ожидаемый результат:
            - Список карточек вакансий должен обновиться с учетом выбранной категории.
        """
        vacancies_page.visit(AppRoute.VACANCIES)
        vacancies_page.vacancies_list.check_visible()
        vacancies_page.verify_filtering_by_all_category_tabs()

    @allure.title("Проверка функциональности расширенного фильтра")
    @allure.story(AllureStoryUi.EXTENDED_FILTER_FUNCTIONALITY)
    def test_filter_menu_reset_and_apply_functionality(
        self, vacancies_page: VacanciesPage
    ):
        """Тест: Проверка функциональности кнопки "Фильтры".

        Предусловия:
            - Страница вакансий загружена.
            - Меню фильтров не отображается.
        Шаги:
            1. Нажать на кнопку "Фильтры".
            2. Проверить, что меню фильтров открылось и содержит все ожидаемые чекбоксы.
            3. Выбрать один или несколько чекбоксов.
            4. Нажать на кнопку "Сбросить".
            5. Проверить, что выбранные чекбоксы были сброшены.
            6. Выбрать один чекбокс (например, "Удаленная работа").
            7. Нажать на кнопку "Применить".
            8. Убедиться, что меню фильтров закрылось и список карточек вакансий обновился
              с учетом выбранных фильтров.
        Ожидаемый результат:
            - Меню фильтров открылось и содержит все ожидаемые чекбоксы.
            - Выбранные чекбоксы отображаются в меню фильтров.
            - При сбросе фильтров выбранные чекбоксы должны быть сняты.
            - При применении фильтров список карточек вакансий должен обновиться
            с учетом выбранных фильтров.
        """
        vacancies_page.visit(AppRoute.VACANCIES)
        vacancies_page.verify_filter_reset_functionality(
            ["От 1 года до 3 лет", "Удаленная работа"]
        )
        vacancies_page.apply_specified_filters_and_verify(["От 1 года до 3 лет"])

    @allure.title("Проверка начальной сортировки вакансий: 'Сначала новые'")
    @allure.story(AllureStoryUi.INITIAL_SORT)
    def test_initial_sort_order_is_newest_first(self, vacancies_page: VacanciesPage):
        """Проверяет, что вакансии отсортированы по убыванию даты.

        Предусловия:
            - Страница вакансий загружена.
            - Отображены вакансии по категории "Все".
            - Вакансии отсортированы по дате публикации "Сначала новые".
        Шаги:
            1. Проверить, что вакансии отсортированы по дате публикации "Сначала новые".
            2. Проверить, что вакансии отсортированы по дате публикации от новых к старым.

        Ожидаемый результат:
            - Вакансии отсортированы по дате публикации "Сначала новые".
        """
        vacancies_page.visit(AppRoute.VACANCIES)
        vacancies_page.filter_bar.sort_btn.check_contain_text("Сначала новые")
        vacancies_page.vacancies_list.check_vacancies_sorted_by_date(order="desc")

    @allure.title("Проверка переключения сортировки на 'Сначала старые'")
    @allure.story(AllureStoryUi.CLICK_SORT_BUTTON)
    def test_switch_sort_order_to_oldest_first(self, vacancies_page: VacanciesPage):
        """Проверяет пересортировку вакансий по возрастанию даты.

        Предусловия:
            - Страница вакансий загружена.
            - Отображены вакансии по категории "Все".
            - Вакансии отсортированы по дате публикации "Сначала новые".
        Шаги:
            1. Нажать на кнопку "Сначала новые".
            5. Иконка стрелочка вниз активна и отображает текст "Сначала старые".
            6. Проверить, что вакансии отсортированы по дате публикации от старых к новым.

        Ожидаемый результат:
            - Нажатие на таб "Сначала новые" обновляет список вакансий и сортирует их
            по дате публикации от старых к новым.
            - Иконка стрелочка вниз активна и отображает текст "Сначала старые".
        """
        vacancies_page.visit(AppRoute.VACANCIES)
        vacancies_page.filter_bar.sort_btn.click()
        vacancies_page.filter_bar.sort_btn.check_contain_text("Сначала старые")
        vacancies_page.vacancies_list.check_vacancies_sorted_by_date(order="asc")
