from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.profile_info = (By.CSS_SELECTOR, 'div.profile_info')

    def is_profile_info_visible(self):
        """Проверка видимости информации профиля."""
        return self.is_visible(self.profile_info)
