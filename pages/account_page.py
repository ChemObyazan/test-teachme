from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
import allure

class AccountPage(BasePage, AccountPageLocators):

    @allure.step("Открываю страницу аккаунта")
    def open_account_page(self):
        self.click(self.BUTTON_ACCOUNT)
        self.click(self.BUTTON_ENTER)

    @allure.step("Ввожу email")
    def set_email(self, email):
        self.fill(self.FIELD_EMAIL, email)

    @allure.step("Ввожу пароль")
    def set_password(self, password):
        self.fill(self.FIELD_PASSW, password)

    @allure.step("Кликаю кнопку войти")
    def click_submit(self):
        self.click(self.BUTTON_SUBMIT)

