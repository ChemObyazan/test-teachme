from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage
import allure

class ProductPage(BasePage, ProductPageLocators):

    @allure.step("Проверяю, что страница товара открыта")
    def assert_product_page_is_open(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_DESCRIPTION)

    @allure.step("Добавляю товар в корзину")
    def add_to_basket(self):
        self.click(self.BUTTON_ADD_TO_BASKET)

    @allure.step("Добавляю товар в избранное")
    def add_to_favorites(self):
        self.click(self.BUTTON_ADD_TO_FAVORITES)

    @allure.step("Проверяю отображение изображений товара")
    def assert_product_images_displayed(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_IMAGES)
    
    @allure.step("Проверяю детали товара")
    def assert_product_details_displayed(self):
        self.assertions.assert_that_element_is_visible(self.PRODUCT_DESCRIPTION)
        self.assertions.assert_that_element_is_visible(self.PRODUCT_PRICE)

