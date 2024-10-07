import pytest
from pages.contact_page import ContactPage

@pytest.mark.usefixtures("driver")
def test_send_message_via_contact_form(driver):
    contact_page = ContactPage(driver)
    
    # Заполняем форму обратной связи
    contact_page.fill_contact_form("Test User", "test@example.com", "Тестовое сообщение")
    
    # Проверяем, что сообщение было успешно отправлено
    contact_page.assert_success_message()
