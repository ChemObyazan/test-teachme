import pytest
from pages.account_page import AccountPage
from pages.main_page import MainPage
import allure


@allure.title("Тест на некорректный email")
def test_incorrect_email(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.set_email("invalidemail")
    account_page.set_password("password123")
    account_page.click_submit()

    account_page.assert_incorrect_email_message()


@allure.title("Тест на пустое поле пароля")
def test_empty_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.set_email("test@example.com")
    account_page.click_submit()

    account_page.assert_empty_password_message()

