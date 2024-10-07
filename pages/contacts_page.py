from locators.contacts_page_locators import ContactsPageLocators
from pages.base_page import BasePage
import allure

class ContactsPage(BasePage, ContactsPageLocators):

    @allure.step("Открываю страницу контактов")
    def assert_contact_page_is_open(self):
        self.assertions.assert_that_element_is_visible(self.FEEDBACK_FORM)

    @allure.step("Заполняю форму обратной связи")
    def fill_feedback_form(self, name, email, message):
        self.fill(self.FEEDBACK_FORM, name)
        self.fill(self.FEEDBACK_FORM, email)
        self.fill(self.FEEDBACK_FORM, message)

    @allure.step("Отправляю форму обратной связи")
    def submit_feedback_form(self):
        self.click(self.BUTTON_SUBMIT_FEEDBACK)

    @allure.step("Проверяю успешную отправку формы")
    def assert_feedback_form_submission_success(self):
        self.assertions.assert_that_element_is_visible(self.SUCCESS_MESSAGE)


