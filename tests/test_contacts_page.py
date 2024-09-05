import pytest
from pages.contacts_page import ContactsPage

@pytest.fixture
def contacts_page(driver):
    return ContactsPage(driver)

def test_contacts_page_content_visibility(contacts_page):
    """Проверка видимости контента страницы 'Контакты'."""
    contacts_page.open()
    assert contacts_page.is_contacts_content_visible()
