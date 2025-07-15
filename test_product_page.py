from test_data import PRODUCT_PAGE
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    page.should_be_product_added_to_busket()
    page.should_be_solved_quiz()
    #time.sleep(100)
    page.should_be_successful_message()
    page.should_be_the_same_products()
    page.should_be_the_same_price()


