import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage

@pytest.mark.usefixtures("driver")
def test_basket_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open()

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    
    basket_page.assert_basket_is_empty()
