from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_items = (By.CSS_SELECTOR, 'div.cart_items')
        self.checkout_button = (By.CSS_SELECTOR, 'button.checkout')

    def open_cart(self):
        """Открытие страницы корзины."""
        self.driver.get('https://www.traektoria.ru/cart')

    def is_cart_empty(self):
        """Проверка, что корзина пуста."""
        return len(self.driver.find_elements(*self.cart_items)) == 0

    def proceed_to_checkout(self):
        """Переход к оформлению заказа."""
        self.click(self.checkout_button)
