from selenium.webdriver.common.by import By

class BasketPageLocators:
    BUTTON_BASKET = (By.CLASS_NAME, 'headerCart')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '[class="EmptyBasket_title__fTZV_ '
                                        'Title-module__title Title-module__h2"]')
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[@data-testid="basketConfirmation"]')
    PROMO_CODE_INPUT = (By.CSS_SELECTOR, 'input[name="promoCode"]')
    APPLY_PROMO_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="applyPromo"]')
