# Тестирование сайта Траектория
https://www.traektoria.ru/

## Структура проекта

Проект  написан по методологии Page Object Model 


- `pages/` - содержит страницы сайта и методы для взаимодействия с элементами этой страницы.
  - `base_page.py` - базовая страница, содержит общие методы для всех страниц.
  - `home_page.py` - главная страница.
  - `category_page.py` - страница категорий.
  - `product_page.py` - продукта.
  - `cart_page.py` - корзина.
  - `checkout_page.py` - оформление заказа.
  - `login_page.py` - страница входа.
  - `profile_page.py` - профил пользователя.
  - `about_page.py` - страница "О нас".
  - `contacts_page.py` - страница "Контакты".
- `tests/` - содержит тесты для каждой страницы.
  - `test_home_page.py` - тесты для главной страницы.
  - `test_category_page.py` - тесты для страницы категорий.
  - `test_product_page.py` - тесты для страницы продукта.
  - `test_cart_page.py` - тесты для страницы корзины.
  - `test_checkout_page.py` - тесты для страницы оформления заказа.
  - `test_login_page.py` - тесты для страницы входа.
  - `test_profile_page.py` - тесты для страницы профиля пользователя.
  - `test_about_page.py` - тесты для страницы "О нас".
  - `test_contacts_page.py` - тесты для страницы "Контакты".
- `conftest.py` - содержит фикстуры для Pytest.
- `pytest.ini` - конфигурационный файл для Pytest.

## Установка зависимостей
pip install -r requirements.txt

##Запаск тестов
pytest

##Подготовка отчётов
allure serve /path/to/your/report/directory