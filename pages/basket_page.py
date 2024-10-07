from locators.basket_page_locators import BasketPageLocators
from pages.base_page import BasePage
import allure

class BasketPage(BasePage, BasketPageLocators):

    @allure.step("Открываю корзину")
    def open_basket(self):
        self.click(self.BUTTON_BASKET)

    @allure.step("Проверяю, что корзина пуста")
    def assert_basket_is_empty(self):
        self.assertions.assert_that_text_is_the_same(self.BASKET_IS_EMPTY, "Корзина пока пуста")

    @allure.step("Проверяю, что корзина не пуста")
    def assert_basket_is_not_empty(self):
        self.assertions.assert_that_element_doesnt_exist(self.BASKET_IS_EMPTY)

    @allure.step("Применяю промокод")
    def apply_promo_code(self, code):
        self.fill(self.PROMO_CODE, code)
        self.click(self.BUTTON_USE_PROMO_CODE)

    @allure.step("Проверяю, что промокод недействителен")
    def assert_invalid_promo_code(self):
        self.assertions.assert_that_element_is_visible(self.PROMO_CODE_IS_INVALID)
