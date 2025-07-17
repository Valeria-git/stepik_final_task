from test_data import LOGIN_PAGE_LINK, MAIN_PAGE_LINK
from .pages.login_page import LoginPage

# from test_data import MAIN_PAGE_LINK
# from pages.login_page import LoginPage
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, LOGIN_PAGE_LINK)
    page.open()
    page.should_be_login_form()
    

def test_guest_should_see_registration_form(browser):
    page = LoginPage(browser, LOGIN_PAGE_LINK)
    page.open()
    page.should_be_register_form()


