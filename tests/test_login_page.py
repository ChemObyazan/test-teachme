import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def test_login_valid_credentials(login_page):
    """Проверка входа с корректными учетными данными."""
    login_page.driver.get('https://www.traektoria.ru/login')
    login_page.login('valid@example.com', 'valid_password')
    assert "dashboard" in login_page.driver.current_url

def test_login_invalid_credentials(login_page):
    """Проверка входа с некорректными учетными данными."""
    login_page.driver.get('https://www.traektoria.ru/login')
    login_page.login('invalid@example.com', 'invalid_password')
    assert "error" in login_page.driver.page_source
