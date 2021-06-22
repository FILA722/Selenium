from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "li.active:nth-child(2)")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INSERT_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    INSERT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button:nth-child(7)')

class BasketPageLocators():
    BASKET_ADD = (By.CSS_SELECTOR, 'div.col-sm-1 > p:nth-child(1)')
    ITEM_ADD_TO_BASKET_NOTIFY = (By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2)')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.table > tbody:nth-child(1) > tr:nth-child(2) > th:nth-child(2)')
    BASKET_RULE = (By.CSS_SELECTOR, 'div.alert:nth-child(2) > div:nth-child(2)')
    PAGE_ITEM = (By.CSS_SELECTOR, 'div.col-sm-6:nth-child(2) > h1:nth-child(1)')
    BASKET_ITEM = (By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    GO_TO_BASKET_PAGE_BUTTON = (By.CSS_SELECTOR, '.btn-group > a:nth-child(1)')
    THIS_IS_BASKET_PAGE = (By.CSS_SELECTOR, '.page-header > h1:nth-child(1)')
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p:nth-child(1)')
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, 'h2.col-sm-6')