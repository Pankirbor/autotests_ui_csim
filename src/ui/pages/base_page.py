import os
from datetime import datetime
from typing import Pattern

import allure

from playwright.sync_api import Page, expect
import pytest
from src.utils.logger import get_logger


logger = get_logger(__name__.upper())


class BasePage:
    """
    Базовый класс для всех страниц веб-приложения.

    Этот класс содержит общие методы, такие как переход на страницу,
    перезагрузка страницы и проверки видимости элементов и их содержимого.

    Attributes:
        page (Page): Экземпляр страницы браузера.

    Methods:
        visit: Переходит на указанную URL-адрес.
        reload: Перезагружает текущую страницу.
        check_current_url: Проверяет, что текущий URL соответствует ожидаемому.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализирует базовый класс страницы.

        Args:
            page (Page): Экземпляр страницы браузера.
        """
        self.page = page

    # todo убрать локаторы в файл locators.py
    def accept_cookies_if_present(self) -> None:
        """Принимает куки, если диалог виден."""
        cookies_dialog = self.page.locator(".cookie-dialog")
        accept_button = self.page.locator(".cookie-dialog button:has-text('Принять')")

        cookies_dialog.wait_for(state="visible", timeout=10000)
        if cookies_dialog.is_visible():
            if accept_button.is_visible():
                accept_button.click()
                logger.info("Куки приняты")
                self.page.wait_for_timeout(1000)

    def visit(self, url: str) -> None:
        """
        Открывает указанную URL-страницу и ждет завершения загрузки.

        Args:
            url (str): Адрес страницы, на которую нужно перейти.
        """
        step = f"Переход на страницу: '{url}'"
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle", timeout=50000)

            # Проверяем CAPTCHA
            # captcha_type = self.debug_captcha_type()

            # # Если это сложная CAPTCHA — пропускаем тест
            # if captcha_type in [
            #     "yandex_smart_captcha",
            #     "recaptcha",
            #     "hcaptcha",
            #     "unknown",
            # ]:
            #     pytest.skip(f"CAPTCHA detected ({captcha_type}) — skipping test in CI")
            self.accept_cookies_if_present()

    def reload(self) -> None:
        """
        Перезагружает текущую страницу и ждет загрузки контента DOM.
        """
        step = f"Обновление страницы: '{self.page.url}'"
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]) -> None:
        """
        Проверяет, что текущий URL совпадает с ожидаемым.

        Args:
            expected_url (Pattern[str]): Регулярное выражение или строка ожидаемого URL.
        """
        step = f"Checking that current url matches pattern '{expected_url.pattern}'"
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)

    def debug_captcha_type(self):
        """
        Определяет тип CAPTCHA на странице и пытается обработать простые случаи.
        Для сложных CAPTCHA — логирует и сохраняет артефакты для дебага.
        """
        page = self.page

        # 1. Проверяем Yandex SmartCaptcha (по твоим локаторам)
        smart_captcha_container = "//div[contains(@class, 'smart-captcha')]"
        smart_captcha_iframe = "//iframe[@data-testid='backend-iframe']"

        if (
            page.locator(smart_captcha_container).count() > 0
            or page.locator(smart_captcha_iframe).count() > 0
        ):
            print("⚠️ Yandex SmartCaptcha detected — cannot bypass by clicking")
            self._save_captcha_artifacts("yandex_smart_captcha")
            return "yandex_smart_captcha"

        # 2. Google reCAPTCHA
        if page.locator("iframe[src*='google.com/recaptcha']").count() > 0:
            print("⚠️ reCAPTCHA detected — cannot bypass by clicking")
            self._save_captcha_artifacts("recaptcha")
            return "recaptcha"

        # 3. hCaptcha
        if page.locator("iframe[src*='hcaptcha']").count() > 0:
            print("⚠️ hCaptcha detected — cannot bypass by clicking")
            self._save_captcha_artifacts("hcaptcha")
            return "hcaptcha"

        # 4. Простая галочка (если есть — пробуем кликнуть)
        simple_selectors = [
            "input#human-verify",
            "label:has-text('not a robot')",
            "input[name='robot_check']",
            "#simple-human-check",
            "input[type='checkbox'][id*='robot']",
        ]

        for selector in simple_selectors:
            if page.locator(selector).count() > 0:
                try:
                    page.locator(selector).check(timeout=3000)
                    print(f"✅ Simple CAPTCHA checkbox clicked: {selector}")
                    return "simple_checkbox"
                except Exception as e:
                    print(f"❌ Failed to click simple CAPTCHA {selector}: {e}")

        # 5. Неизвестная CAPTCHA — сохраняем артефакты
        print("❓ Unknown CAPTCHA — saving page state for debugging")
        self._save_captcha_artifacts("unknown")

        return "unknown"

    def _save_captcha_artifacts(self, captcha_type: str):
        """
        Сохраняет скриншот, HTML и логи при обнаружении CAPTCHA.
        Артефакты можно скачать из GitHub Actions.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        artifact_dir = "artifacts/captcha"
        os.makedirs(artifact_dir, exist_ok=True)

        # Имя файла на основе типа CAPTCHA и времени
        prefix = f"{artifact_dir}/{captcha_type}_{timestamp}"

        try:
            # 1. Скриншот всей страницы
            screenshot_path = f"{prefix}_screenshot.png"
            self.page.screenshot(path=screenshot_path, full_page=True)
            print(f"📸 Screenshot saved: {screenshot_path}")

            # 2. HTML-фрагмент всей страницы (первые 10К символов для лога)
            html = self.page.content()
            print(f"📄 Page HTML fragment (first 2000 chars):\n{html[:2000]}")

            # 3. Сохраняем полный HTML в файл (если нужно)
            html_path = f"{prefix}_page.html"
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"💾 Full HTML saved: {html_path}")

            # 4. Логируем URL и заголовок
            print(f"🌐 Page URL: {self.page.url}")
            print(f"🔖 Page Title: {self.page.title()}")

        except Exception as e:
            print(f"❌ Failed to save artifacts: {e}")
