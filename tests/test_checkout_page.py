import pytest
from pages.checkout_page import CheckoutPage

@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)

def test_checkout_form_visibility(checkout_page):
    """Проверка видимости формы оформления заказа."""
    checkout_page.driver.get('https://www.traektoria.ru/checkout')
    assert checkout_page.is_checkout_form_visible()
