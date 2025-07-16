from pages.main_page import MainPage
from pages.basket_page import BasketPage
import pytest
from test_data import MAIN_PAGE_LINK


@pytest.mark.login_guest
class TestLoginFromMainPage():   

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.should_be_view_basket_button()
    page.go_to_basket_page()
    page.should_be_basket_empty()


