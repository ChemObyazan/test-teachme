from selenium.webdriver.common.by import By

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button[data-test-id="add-to-basket"]')
    BUTTON_ADD_TO_FAVORITES = (By.CSS_SELECTOR, 'button[data-test-id="add-to-favorites"]')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, 'div[data-test-id="product-description"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span[data-test-id="product-price"]')
    PRODUCT_IMAGES = (By.CSS_SELECTOR, 'img[data-test-id="product-image"]')

