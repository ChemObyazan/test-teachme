from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.CSS_SELECTOR, 'button.add_to_cart')
        self.product_name = (By.CSS_SELECTOR, 'h1.product_name')
        self.product_price = (By.CSS_SELECTOR, 'div.product_price')

    def add_to_cart(self):
        """Добавление товара в корзину."""
        self.click(self.add_to_cart_button)

    def get_product_name(self):
        """Получение названия товара."""
        return self.get_text(self.product_name)

    def get_product_price(self):
        """Получение цены товара."""
        return self.get_text(self.product_price)
