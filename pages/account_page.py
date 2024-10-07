from pages.base_page import BasePage
from locators.account_locators import AccountPageLocators

class AccountPage(BasePage, AccountPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_account_page(self):
        self.click(self.BUTTON_ACCOUNT)
        self.click(self.BUTTON_ENTER)

    def login(self, email, password):
        self.fill(self.FIELD_EMAIL, email)
        self.fill(self.FIELD_PASSWORD, password)
        self.click(self.BUTTON_SUBMIT)

    def assert_error_message(self):
        self.assertions.assert_that_element_is_visible(self.ERROR_MESSAGE)
