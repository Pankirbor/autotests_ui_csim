# 🛡️ UI-тесты для сайта ЦИСМ — Демонстрационный проект

> **ЦИСМ** — высокотехнологичная IT-компания, работающая на стыке психологии и разработки для анализа и мониторинга молодёжной цифровой среды.
> **Миссия:** Защита подрастающего поколения от воздействия деструктивного контента.
> **Цель:** Формирование безопасной цифровой среды для граждан России.

---

## 📌 О проекте

Это **демонстрационный репозиторий**, содержащий **автоматизированные UI-тесты** для страницы **"Вакансии"** сайта [cism-ms.ru](https://cism-ms.ru/).
Проект создан в образовательных и демонстрационных целях — **не является полным покрытием сайта**.

✅ Тесты проверяют:
- Фильтрацию вакансий
- Сортировку по дате
- Навигацию по карточкам

---

## 🚀 Технологии

| Категория       | Технология                                                                 |
|------------------|----------------------------------------------------------------------------|
| Язык             | ![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)      |
| Фреймворк тестов | ![Pytest](https://img.shields.io/badge/Pytest-7.x+-green?logo=pytest)      |
| Браузерный движок| ![Playwright](https://img.shields.io/badge/Playwright-1.40+-orange?logo=playwright) |
| Отчёты           | ![Allure](https://img.shields.io/badge/Allure_Report-2.29+-pink?logo=allure) |
| Линтер           | ![Ruff](https://img.shields.io/badge/Ruff-0.6.6+-black?logo=python)        |
| CI/CD            | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-blue?logo=github) |

---

## 📊 Отчёты и артефакты

### ▶️ Последний Allure-отчёт
[![Allure Report](https://img.shields.io/badge/Allure_Report-View_Online-red?logo=allure)](https://pankirbor.github.io/autotests_ui_csim/)

> 👉 [Открыть отчёт](https://pankirbor.github.io/autotests_ui_csim/)

### 📦 Артефакты последнего запуска (скриншоты, видео, HTML)
[![Artifacts](https://img.shields.io/badge/Download-Artifacts-orange?logo=github)](https://github.com/Pankirbor/autotests_ui_csim/actions)

> Зайдите в последний workflow → Artifacts → скачайте `allure-ui-results`, `coverage-report`

---

## ⚙️ Запуск локально

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Pankirbor/autotests_ui_csim.git
   cd autotests_ui_csim
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # или
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   playwright install --with-deps
   pytest -m UI --alluredir=./allure-ui-results

## 🧪 Запуск в CI
>Проект настроен на автоматический запуск в **GitHub Actions** при `push` в `main` или **открытии PR**.

>Тесты запускаются в **Chromium и Firefox**, генерируется **Allure-отчёт** и публикуется на **GitHub Pages**.

## 🤝 Цель проекта
*Этот репозиторий — демонстрация подхода к автоматизации UI-тестов.*

**Он показывает:**
- Интеграцию с **Allure и GitHub Pages**
- Настройку логирования и отладки
- Использование **Page Object Model**
- Работу с **Playwright и Pytest**