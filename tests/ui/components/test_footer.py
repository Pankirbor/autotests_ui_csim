import allure
from allure_commons.types import Severity
import pytest

from integrations.allure.epic import AllureEpic
from integrations.allure.features import AllureFeature
from integrations.allure.stories import AllureStoryUi
from integrations.allure.tags import AllureTagUi
from src.ui.pages.vacancies.vacancies_page import VacanciesPage
from src.ui.routes import AppRoute


@pytest.mark.UI
@allure.epic(AllureEpic.CSIM)
@allure.feature(AllureFeature.FOOTER)
class TestFooterComponent:
    """Тесты компонента Footer."""

    @allure.title("Проверка отображения компонента Footer на странице Вакансии")
    @allure.severity(Severity.NORMAL)
    @allure.story(AllureStoryUi.FOOTER_VISIBILITY)
    @allure.tag(AllureTagUi.UI, AllureTagUi.POSITIVE, AllureTagUi.SMOKE)
    def test_footer_visibility_and_downloads(self, vacancies_page: VacanciesPage):
        """Тест: Проверка отображения компонента Footer на странице Вакансии.

        Предусловия:
            - Открыта любая страница, например, '/vakansii'.

        Шаги:
            1. Проверить, что все элементы футера видны(копирайт, ИНН, ссылки, логотип).
            2. Скачать файл "Политики конфиденциальности" - проверить название, формат и что файл не пустой.
            3. Скачать файл "Пользовательского соглашения" - проверить название, формат и что файл не пустой.
            4. Кликнуть на логотип - проверить переход на главную страницу, URL содержит '/'.

        Ожидаемый результат:
            - Все элементы футера отображаются корректно.
            - Юридические документы скачиваются, имеют корректный формат и не пустые.
            - Переход на главную страницу работает корректно.
        """
        vacancies_page.visit(AppRoute.VACANCIES)
        vacancies_page.footer.check_visible()
        vacancies_page.footer.check_download_privacy_policy()
        vacancies_page.footer.check_download_user_agreement()
        vacancies_page.footer.navigate_to_main_page()
