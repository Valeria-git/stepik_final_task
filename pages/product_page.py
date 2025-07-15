from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.alert import Alert


class ProductPage(BasePage):


    def should_be_product_added_to_busket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        button.click()

    def should_be_solved_quiz(self):
        BasePage.solve_quiz_and_get_code(self)

    def should_be_successful_message(self):
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BUSKET_MESSAGE).text.strip()
        expected = "has been added to your basket."
        assert  expected in message, f"Expected message to be {expected}, but got {message}"

    def should_be_the_same_products(self):
        expected = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_THE_PRODUCT_PAGE).text.strip()
        actual = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_THE_BUSKET).text.strip()
        assert expected == actual, f"Expected product name to be {expected}, but got {actual}"    

    #in this case total == product_price
    def should_be_the_same_price(self):
        expected = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text.strip()
        actual = self.browser.find_element(*ProductPageLocators.TOTAL_COST_BUSKET).text.strip()
        assert expected in actual, f"Expected total price to be {expected}, but got {actual}"       
        
