from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
from .locators import BasketPageLocators
from test_data import LOGIN_PAGE_LINK


class BasketPage(BasePage):


    def should_be_basket_empty(self):       
        actual = self.browser.find_elements(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert len(actual) == 1,  "Basket is not empty"

    def should_not_be_basket_empty(self):    
        assert self.browser.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE),  "Basket is empty"


    def busket_should_become_not_empty(self):
        assert self.is_disappeared(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
       "Basket should have item, but it's empty"
        



        
        