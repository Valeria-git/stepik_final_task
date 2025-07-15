from test_data import PRODUCT_PAGE
from test_data import PRODUCT_PAGE_CODERS
from test_data import PRODUCT_PAGE_PROMO
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest
import time

@pytest.mark.skip(reason="Just skip for testing another cases")
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_added_to_busket()
    page.should_be_solved_quiz()
    page.should_be_successful_message()
    page.should_be_the_same_products()
    page.should_be_the_same_price()



@pytest.mark.xfail(reason="as message is presented for now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_PROMO)
    page.open()
    page.should_be_be_added_thing_in_basket_with_success()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_PAGE_PROMO)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="as message is presented for now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_PROMO)
    page.open()
    page.should_be_be_added_thing_in_basket_with_success()
    page.success_message_should_disappear()