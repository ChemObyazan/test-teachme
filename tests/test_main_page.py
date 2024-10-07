import pytest
from pages.main_page import MainPage
import allure


@allure.title("Тест на отклонение куки")
def test_reject_cookies(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_reject_cookies()
    main_page.assert_that_banner_is_displayed()


@allure.title("Тест на принятие куки")
def test_accept_cookies(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.assert_that_banner_is_displayed()


@allure.title("Тест на поиск товара")
def test_search_product(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search("сноуборд")
    main_page.assert_that_search_results_are_displayed()
