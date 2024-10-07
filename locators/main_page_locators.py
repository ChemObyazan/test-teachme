from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_WINDOW = (By.CSS_SELECTOR, '[class="AgreementCookie_modal__x3nra"]')
    BUTTON_REJECT_COOKIES = (By.CSS_SELECTOR, '[class="Button-module__button '
                                              'AgreementCookie_reject__f5oqP '
                                              'Button-module__gray-secondary"]')
    BANNER = (By.CSS_SELECTOR, '[class="Carousel_swiperContainer__uZrl1"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, '[class="Search_searchInput__RoV1W"]')
    BUTTON_SEARCH = (By.CSS_SELECTOR, '[aria-label="Найти"]')
    
