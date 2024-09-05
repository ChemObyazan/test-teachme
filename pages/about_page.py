from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.traektoria.ru/about/'
        self.about_content = (By.CSS_SELECTOR, 'div.about_content')

    def open(self):
        """Открытие страницы 'О нас'."""
        self.driver.get(self.url)

    def is_about_content_visible(self):
        """Проверка видимости контента страницы 'О нас'."""
        return self.is_visible(self.about_content)
