import pytest
from pages.cart_page import CartPage

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

def test_cart_empty(cart_page):
    """Проверка, что корзина пуста."""
    cart_page.open_cart()
    assert cart_page.is_cart_empty()

def test_proceed_to_checkout(cart_page):
    """Проверка перехода к оформлению заказа."""
    cart_page.open_cart()
    cart_page.proceed_to_checkout()
    assert "checkout" in cart_page.driver.current_url
v