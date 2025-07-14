from pages.main_page import MainPage
import pytest
from test_data import MAIN_PAGE_LINK



       
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.should_be_login_link()


