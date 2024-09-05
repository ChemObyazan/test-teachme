import pytest
from pages.home_page import HomePage

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

def test_home_page_title(home_page):
    """Проверка заголовка главной страницы."""
    home_page.open()
    assert "Траектория" in home_page.get_title()

def test_home_page_search(home_page):
    """Проверка поиска по ключевому слову."""
    home_page.open()
    home_page.search("Скейтборд")
    assert "Скейтборд" in home_page.driver.page_source

def test_home_page_logo_visibility(home_page):
    """Проверка видимости логотипа на главной странице."""
    home_page.open()
    assert home_page.is_logo_visible()

def test_home_page_category_menu_visibility(home_page):
    """Проверка видимости меню категорий на главной странице."""
    home_page.open()
    assert home_page.is_category_menu_visible()

