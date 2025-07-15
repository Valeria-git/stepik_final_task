from selenium.webdriver.common.by import By



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():


    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR,"id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
  
    PRODUCT_ADDED_TO_BUSKET_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner")

    PRODUCT_NAME_IN_THE_PRODUCT_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main >h1")
    PRODUCT_NAME_IN_THE_BUSKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner strong")
 
    PRODUCT_COST = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    TOTAL_COST_BUSKET = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p strong")
