from selenium.webdriver.common.by import By

class ProductCardLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1.MuiTypography-root.MuiTypography-h1')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="add-to-cart-button"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h4')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, '.MuiBox-root p.MuiTypography-body1')
    PRODUCT_IMAGES = (By.CSS_SELECTOR, 'img[data-testid="product-image"]')
    PRODUCT_REVIEWS = (By.CSS_SELECTOR, '.reviews')
