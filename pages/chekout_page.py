from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_form = (By.CSS_SELECTOR, 'form.checkout_form')

    def is_checkout_form_visible(self):
        """Проверка видимости формы оформления заказа."""
        return self.is_visible(self.checkout_form)
