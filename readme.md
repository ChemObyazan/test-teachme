# Проект автоматизации тестирования для сайта Траектория

## Описание
Проект автоматизации тестирования, включающий UI и API тесты для сайта [Траектория](https://www.traektoria.ru/). Проект реализован с использованием Page Object Model (POM).

### Структура проекта:
- `locators/` — Локаторы для страниц
- `pages/` — Реализация страниц
- `tests/` — Тесты для страниц и API
- `conftest.py` — Настройки драйвера и фикстур
- `Makefile` — Скрипты для запуска тестов
- `requirements.txt` — Зависимости проекта

### Установка и запуск:
1. Клонировать репозиторий:
```bash
git clone <repository-url>

2. Установка зависимостей:
pip install -r requirements.txt

3. Запустить все тесты.
make test_all

4. Запустить UI тесты:
make test_ui

5. Запустить API тесты:
make test_api

6. Сгенерировать отчёт Allure
make allure_report

6.1 **Организация работы с Allure**:
Для генерации отчетов Allure, нужно убедиться, что Allure установлен в системе.

#### Установка Allure:
```bash
choco install allure  # для Windows