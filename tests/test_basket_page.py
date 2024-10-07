import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage
import allure


@allure.title("Тест на пустую корзину")
def test_basket_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open()

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.assert_basket_is_empty()


@allure.title("Тест добавления товара в корзину")
def test_add_product_to_basket(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search("сноуборд")
    main_page.select_product_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.assert_basket_is_not_empty()


@allure.title("Тест промокода")
@pytest.mark.parametrize("promo_code", ["INVALID", "12345"])
def test_invalid_promo_code(driver, promo_code):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search("сноуборд")
    main_page.select_product_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.apply_promo_code(promo_code)
    basket_page.assert_invalid_promo_code()

