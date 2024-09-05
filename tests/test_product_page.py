import pytest
from pages.product_page import ProductPage

@pytest.fixture
def product_page(driver):
    return ProductPage(driver)

def test_add_product_to_cart(product_page):
    """Проверка добавления товара в корзину."""
    product_page.driver.get('https://www.traektoria.ru/product/slug')
    product_name = product_page.get_product_name()
    product_page.add_to_cart()
    assert product_name in product_page.driver.page_source

def test_product_page_price_visibility(product_page):
    """Проверка видимости цены товара на странице."""
    product_page.driver.get('https://www.traektoria.ru/product/slug')
    assert product_page.is_visible(product_page.product_price)
