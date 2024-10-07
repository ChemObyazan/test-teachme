from locators.favorites_page_locators import FavoritesPageLocators
from pages.base_page import BasePage
import allure

class FavoritesPage(BasePage, FavoritesPageLocators):

    @allure.step("Открываю избранное")
    def open_favorites(self):
        self.click(self.BUTTON_FAVORITES)

    @allure.step("Проверяю, что избранное пусто")
    def assert_favorites_is_empty(self):
        self.assertions.assert_that_text_is_the_same(self.FAVORITES_ARE_EMPTY, "Нет избранных товаров")

    @allure.step("Проверяю, что избранное не пусто")
    def assert_favorites_is_not_empty(self):
        self.assertions.assert_that_text_is_the_same(self.FAVORITES_ARE_EMPTY, "Избранные товары")
