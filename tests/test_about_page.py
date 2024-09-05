import pytest
from pages.about_page import AboutPage

@pytest.fixture
def about_page(driver):
    return AboutPage(driver)

def test_about_page_content_visibility(about_page):
    """Проверка видимости контента страницы 'О нас'."""
    about_page.open()
    assert about_page.is_about_content_visible()
