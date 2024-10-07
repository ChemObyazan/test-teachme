import pytest
from pages.product_card_page import ProductCardPage

@pytest.mark.usefixtures("driver")
def test_add_product_to_cart(driver):
    product_page = ProductCardPage(driver)
    
    # Здесь нужно сначала открыть карточку продукта
    product_page.add_to_cart()

    assert "В корзине" in product_page.get_product_title()
