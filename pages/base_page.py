from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

from helpers.assertions import Assertions

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.assertions = Assertions(driver)

    @allure.step("Открываю страницу")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Кликаю на элемент")
    def click(self, selector):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(selector)
            ).click()
        except (TimeoutException, NoSuchElementException):
            assert False, f"Элемент {selector} не найден"

    @allure.step("Заполняю поле")
    def fill(self, selector, text):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(selector)
        )
        element.send_keys(text)

    @allure.step("Проверяю, что элемент существует")
    def check_element_is_exist(self, selector):
        return self.driver.find_elements(*selector)
