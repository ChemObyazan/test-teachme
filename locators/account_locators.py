from selenium.webdriver.common.by import By

class AccountPageLocators:
    BUTTON_ACCOUNT = (By.CSS_SELECTOR, '[class="styles_userToolsToggler__c2aHe"]')
    BUTTON_ENTER = (By.CSS_SELECTOR, '[data-testid="loginButton"]')
    # Добавляем новые элементы, если нужно
    FIELD_EMAIL = (By.XPATH, '//input[@label="Электронная почта"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@label="Пароль"]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '[data-testid="loginSubmit"]')
    ERROR_MESSAGE = (By.CLASS_NAME, 'ErrorMessage-module__message')
