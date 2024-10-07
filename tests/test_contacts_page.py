import pytest
from pages.contacts_page import ContactsPage
from pages.main_page import MainPage
import allure


@allure.title("Тест загрузки страницы контактов")
def test_contact_page_loads(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.go_to_contacts()  # Переход на страницу контактов
    contacts_page = ContactsPage(driver)
    contacts_page.assert_contact_page_is_open()


@allure.title("Тест отправки формы обратной связи")
def test_feedback_form_submission(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.go_to_contacts()

    contacts_page = ContactsPage(driver)
    contacts_page.fill_feedback_form("Иван Иванов", "ivan@example.com", "Сообщение")
    contacts_page.submit_feedback_form()

    contacts_page.assert_feedback_form_submission_success()


