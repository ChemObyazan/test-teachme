from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_list = (By.CSS_SELECTOR, 'div.product_list')
        self.first_product = (By.CSS_SELECTOR, 'div.product_list div.product_item:first-child a')

    def open_category(self, url):
        """Открытие страницы категории товаров."""
        self.driver.get(url)

    def is_product_list_visible(self):
        """Проверка видимости списка товаров."""
        return self.is_visible(self.product_list)

    def click_first_product(self):
        """Нажатие на первый товар в списке."""
        self.click(self.first_product)
