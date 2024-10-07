from selenium.webdriver.common.by import By

class BasketPageLocators:
    BUTTON_BASKET = (By.CLASS_NAME, 'headerCart')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '[class="EmptyBasket_title__fTZV_ Title-module__title Title-module__h2"]')
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[@data-testid="basketConfirmation"]')
    PROMO_CODE = (By.XPATH, '//input[@placeholder="Введите промокод"]')
    BUTTON_USE_PROMO_CODE = (By.XPATH, '//button[@data-testid="promocodeConfirmation"]')
    PROMO_CODE_IS_INVALID = (By.CLASS_NAME, 'ErrorMessage-module__message')

