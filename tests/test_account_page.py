import pytest
from pages.account_page import AccountPage
from pages.main_page import MainPage

@pytest.mark.usefixtures("driver")
def test_incorrect_login(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.login("incorrect_email@test.com", "incorrect_password")
    
    account_page.assert_error_message()

@pytest.mark.usefixtures("driver")
def test_incorrect_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.login("correct_email@test.com", "incorrect_password")

    account_page.assert_error_message()

@pytest.mark.usefixtures("driver")
def test_empty_email_field(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.login("", "somepassword")
    
    account_page.assert_error_message()

@pytest.mark.usefixtures("driver")
def test_empty_password_field(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.login("correct_email@test.com", "")
    
    account_page.assert_error_message()

@pytest.mark.usefixtures("driver")
def test_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.click_forgot_password()
    account_page.reset_password("correct_email@test.com")

    account_page.assert_success_reset_message()

@pytest.mark.usefixtures("driver")
def test_registration_incorrect_email(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.register("incorrect_email", "password")

    account_page.assert_error_message()

@pytest.mark.usefixtures("driver")
def test_registration_existing_user(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.register("existing_user@test.com", "password")

    account_page.assert_error_message()

@pytest.mark.usefixtures("driver")
def test_successful_registration(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.register("new_user@test.com", "new_password")

    account_page.assert_success_registration()

@pytest.mark.usefixtures("driver")
def test_successful_login(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.login("correct_email@test.com", "correct_password")
    
    account_page.assert_login_successful()

@pytest.mark.usefixtures("driver")
def test_logout(driver):
    main_page = MainPage(driver)
    main_page.open()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.login("correct_email@test.com", "correct_password")
    account_page.logout()

    account_page.assert_logged_out()
