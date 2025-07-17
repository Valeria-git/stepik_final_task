from .base_page import BasePage
from .locators import LoginPageLocators
from test_data import LOGIN_PAGE_LINK

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        actual_url = self.browser.current_url
        expected_url = LOGIN_PAGE_LINK
        assert actual_url == expected_url, f"Expected URL to be {expected_url}, but got {actual_url}"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESS_MESSAGE), "Registration was not perfromed"
    