import pytest
from pages.category_page import CategoryPage

@pytest.fixture
def category_page(driver):
    return CategoryPage(driver)

def test_category_page_product_list(category_page):
    """Проверка видимости списка товаров на странице категории."""
    category_page.open_category('https://www.traektoria.ru/category/skateboards/')
    assert category_page.is_product_list_visible()

def test_category_page_click_first_product(category_page):
    """Проверка перехода на страницу товара при клике на первый товар."""
    category_page.open_category('https://www.traektoria.ru/category/skateboards/')
    category_page.click_first_product()
    assert "product" in category_page.driver.current_url
