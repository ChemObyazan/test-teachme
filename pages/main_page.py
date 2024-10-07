from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage, MainPageLocators):

    @allure.step("Открываю главную страницу")
    def open(self):
        self.open_page("https://www.traektoria.ru/")

    @allure.step("Отклоняю куки")
    def click_reject_cookies(self):
        self.click(self.BUTTON_REJECT_COOKIES)

    @allure.step("Принимаю куки")
    def click_agree_cookies(self):
        self.click(self.BUTTON_AGREE_COOKIES)

    @allure.step("Проверяю наличие баннера")
    def assert_that_banner_is_displayed(self):
        self.assertions.assert_that_element_is_visible(self.BANNER)

    @allure.step("Поиск товара")
    def search(self, query):
        self.fill(self.SEARCH_FIELD, query)
        self.click(self.SEARCH_FIELD)
    
    @allure.step("Проверяю наличие результатов поиска")
    def assert_that_search_results_are_displayed(self):
        self.assertions.assert_that_element_is_visible(self.SEARCH_RESULT)
