from pages.base_page import BasePage
from locators.product_card_locators import ProductCardLocators

class ProductCardPage(BasePage, ProductCardLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_product_card(self):
        # Метод для открытия карточки продукта, если нужно
        pass

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    def get_product_description(self):
        return self.get_text(self.PRODUCT_DESCRIPTION)

    def assert_product_has_reviews(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_REVIEWS)
