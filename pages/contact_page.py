from pages.base_page import BasePage
from locators.contact_page_locators import ContactPageLocators

class ContactPage(BasePage, ContactPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_contact_form(self, name, email, message):
        self.fill(self.CONTACT_NAME, name)
        self.fill(self.CONTACT_EMAIL, email)
        self.fill(self.CONTACT_MESSAGE, message)
        self.click(self.SEND_MESSAGE_BUTTON)

    def assert_success_message(self):
        self.assertions.assert_that_element_is_visible(self.SUCCESS_MESSAGE)

    def get_phone_number(self):
        return self.get_text(self.PHONE_NUMBER)
