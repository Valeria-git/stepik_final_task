from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_PAGE = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

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

    PRODUCT_ADDED_TO_BUSKET_MESSAGE = (By.XPATH, "//div[contains(@class, 'alertinner') and contains(., 'has been added')]")

    PRODUCT_NAME_IN_THE_PRODUCT_PAGE = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_NAME_IN_THE_BUSKET = (By.CSS_SELECTOR, ".breadcrumb .active")

    TOTAL_COST_BUSKET = (
        By.XPATH, 
        "//div[contains(@class,'alertinner')]//p[contains(., 'Your basket total is now')]/strong"
        )
    PRODUCT_COST = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")