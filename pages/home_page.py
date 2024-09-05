from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.traektoria.ru/'
        self.search_box = (By.NAME, 'q')
        self.search_button = (By.CSS_SELECTOR, 'button.search_button')
        self.logo = (By.CSS_SELECTOR, 'div.logo')
        self.category_menu = (By.CSS_SELECTOR, 'ul.category_menu')

    def open(self):
        """Открытие главной страницы."""
        self.driver.get(self.url)

    def search(self, query):
        """Поиск по ключевому слову."""
        self.send_keys(self.search_box, query)
        self.click(self.search_button)

    def is_logo_visible(self):
        """Проверка видимости логотипа."""
        return self.is_visible(self.logo)

    def is_category_menu_visible(self):
        """Проверка видимости меню категорий."""
        return self.is_visible(self.category_menu)
