from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, timeout=10):
        """Ожидание видимости элемента на странице."""
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        """Нажатие на элемент."""
        self.wait_for_element(by_locator)
        self.driver.find_element(*by_locator).click()

    def send_keys(self, by_locator, text):
        """Ввод текста в элемент."""
        self.wait_for_element(by_locator)
        self.driver.find_element(*by_locator).send_keys(text)

    def get_text(self, by_locator):
        """Получение текста из элемента."""
        self.wait_for_element(by_locator)
        return self.driver.find_element(*by_locator).text

    def is_visible(self, by_locator):
        """Проверка видимости элемента."""
        self.wait_for_element(by_locator)
        return self.driver.find_element(*by_locator).is_displayed()

    def get_title(self):
        """Получение заголовка страницы."""
        return self.driver.title
