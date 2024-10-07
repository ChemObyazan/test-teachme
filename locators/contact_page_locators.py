from selenium.webdriver.common.by import By

class ContactPageLocators:
    CONTACT_FORM = (By.CSS_SELECTOR, 'form.contact-form')
    CONTACT_EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    CONTACT_NAME = (By.CSS_SELECTOR, 'input[name="name"]')
    CONTACT_MESSAGE = (By.CSS_SELECTOR, 'textarea[name="message"]')
    SEND_MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.success-message')
    PHONE_NUMBER = (By.CSS_SELECTOR, '.contact-phone')
