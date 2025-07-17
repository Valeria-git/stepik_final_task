from pages.product_page import ProductPage
from test_data import PRODUCT_PAGE_PROMO
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from utils.helper import generate_password, generate_email
import pytest


#! 
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_PROMO)
    page.open()
    page.should_be_product_added_to_busket()
    page.should_be_solved_quiz()
    page.should_be_successful_message()
    page.should_be_the_same_products()
    page.should_be_the_same_price()

#!
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_PROMO)
    page.open()
    page.should_be_view_basket_button()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()

#!
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_PROMO)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.xfail(reason="as message is presented for now")
def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_PROMO)
    page.open()
    page.should_be_be_added_thing_in_basket_with_success()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="Just skip for testing another cases")
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


@pytest.mark.skip(reason="Just skip for testing another cases")
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()



@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = generate_email()
        password = generate_password()
        page = ProductPage(browser, PRODUCT_PAGE_PROMO)
   
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email,password)
        login_page.should_be_authorized_user()

        page = ProductPage(browser, PRODUCT_PAGE_PROMO)
        page.open()

        self.link = PRODUCT_PAGE_PROMO



   #!
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_product_added_to_busket()
        page.should_be_solved_quiz()
        page.should_be_successful_message()
        page.should_be_the_same_products()
        page.should_be_the_same_price()

    @pytest.mark.skip(reason="Just skip for testing another cases")
    #@pytest.mark.xfail(reason="as message is presented for now")
    def test_user_can_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_be_added_thing_in_basket_with_success()








