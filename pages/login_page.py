from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = (By.NAME, 'email')
        self.password_field = (By.NAME, 'password')
        self.login_button = (By.CSS_SELECTOR, 'button.login')

    def login(self, email, password):
        """Ввод учетных данных и нажатие кнопки входа."""
        self.send_keys(self.email_field, email)
        self.send_keys(self.password_field, password)
        self.click(self.login_button)
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = (By.NAME, 'email')
        self.password_field = (By.NAME, 'password')
        self.login_button = (By.CSS_SELECTOR, 'button.login')

    def login(self, email, password):
        """Ввод учетных данных и нажатие кнопки входа."""
        self.send_keys(self.email_field, email)
        self.send_keys(self.password_field, password)
        self.click(self.login_button)
