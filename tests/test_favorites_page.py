import pytest
from pages.favorites_page import FavoritesPage
from pages.main_page import MainPage
import allure


@allure.title("Тест на пустое избранное")
def test_favorites_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open()

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()
    favorites_page.assert_favorites_is_empty()


@allure.title("Тест на добавление товара в избранное")
def test_add_to_favorites(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search("сноуборд")
    main_page.select_product_by_index(0)

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()
    favorites_page.assert_favorites_is_not_empty()


