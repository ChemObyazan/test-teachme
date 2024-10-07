from selenium.webdriver.common.by import By

class ContactsPageLocators:
    FEEDBACK_FORM = (By.CSS_SELECTOR, 'form[data-test-id="feedback-form"]')
    BUTTON_SUBMIT_FEEDBACK = (By.CSS_SELECTOR, 'button[type="submit"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div[data-test-id="feedback-success"]')
    SOCIAL_MEDIA_LINKS = (By.CSS_SELECTOR, 'a[data-test-id="social-media-link"]')


