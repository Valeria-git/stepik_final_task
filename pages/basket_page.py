from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
from .locators import BasketPageLocators
from test_data import LOGIN_PAGE_LINK


class BasketPage(BasePage):


    def should_be_basket_empty(self):       
        actual = self.browser.find_elements(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert len(actual) == 1,  "Basket is not empty"


        
        