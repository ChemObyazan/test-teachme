from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.traektoria.ru/contacts/'
        self.contacts_content = (By.CSS_SELECTOR, 'div.contacts_content')

    def open(self):
        """Открытие страницы 'Контакты'."""
        self.driver.get(self.url)

    def is_contacts_content_visible(self):
        """Проверка видимости контента страницы 'Контакты'."""
        return self.is_visible(self.contacts_content)
