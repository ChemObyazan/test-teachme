import pytest
from pages.product_page import ProductPage
from pages.main_page import MainPage
import allure


@allure.title("Тест открытия страницы продукта")
def test_open_product_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search("сноуборд")
    main_page.select_product_by_index(0)

    product_page = ProductPage(driver)
    product_page.assert_product_page_is_open()


@allure.title("Тест добавления товара в корзину")
def test_add_to_basket(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search("сноуборд")
    main_page.select_product_by_index(0)

    product_page = ProductPage(driver)
    product_page.add_to_basket()
    product_page.assert_product_added_to_basket()


@allure.title("Тест добавления товара в избранное")
def test_add_to_favorites(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search("сноуборд")
    main_page.select_product_by_index(0)

    product_page = ProductPage(driver)
    product_page.add_to_favorites()
    product_page.assert_product_added_to_favorites()


