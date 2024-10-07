from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import allure


class Assertions:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверяю, что текст совпадает')
    def assert_that_text_is_the_same(self, selector, text):
        assert WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element(selector, text)
        )

    @allure.step('Проверяю, что элемент виден')
    def assert_that_element_is_visible(self, selector):
        assert WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(selector)
        )

    @allure.step('Проверяю, что элемента нет на странице')
    def assert_that_element_doesnt_exist(self, selector):
        time.sleep(1)
        assert not self.driver.find_elements(*selector)
