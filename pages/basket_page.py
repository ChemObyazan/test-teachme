from pages.base_page import BasePage
from locators.basket_locators import BasketPageLocators

class BasketPage(BasePage, BasketPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_basket(self):
        self.click(self.BUTTON_BASKET)

    def assert_basket_is_empty(self):
        self.assertions.assert_that_text_is_the_same(self.BASKET_IS_EMPTY, 'Корзина пуста')

    def apply_promo_code(self, promo_code):
        self.fill(self.PROMO_CODE_INPUT, promo_code)
        self.click(self.APPLY_PROMO_BUTTON)

    def make_order(self):
        self.click(self.BUTTON_MAKE_ORDER)
