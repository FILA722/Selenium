from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPageLocators
import pytest
import time
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.locators import BasketPageLocators
from .pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By

class TestUserAddToBasketFromProductPage():
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        try:
            assert page.is_not_element_present(*BasketPageLocators.ITEM_ADD_TO_BASKET_NOTIFY) == True
        finally:
            browser.quit()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)
        page.open()
        NameItem = browser.find_element(By.CSS_SELECTOR, 'div.col-sm-6:nth-child(2) > h1:nth-child(1)').text
        page.should_be_product_link()
        page.press_buy()
        page.solve_quiz_and_get_code()
        assert NameItem == browser.find_element(By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)').text
        time.sleep(1)
        page.go_to_basket_page()
        page.should_be_product_add_to_basket()
        time.sleep(1)
        browser.quit()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    try:
        page.press_buy()
        page.solve_quiz_and_get_code()
        # time.sleep(1)
        assert page.is_not_element_present(*BasketPageLocators.ITEM_ADD_TO_BASKET_NOTIFY) == False
    finally:
        browser.quit()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    NameItem = browser.find_element(By.CSS_SELECTOR, 'div.col-sm-6:nth-child(2) > h1:nth-child(1)').text
    page.should_be_product_link()
    page.press_buy()
    page.solve_quiz_and_get_code()
    assert NameItem == browser.find_element(By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)').text
    time.sleep(1)
    page.go_to_basket_page()
    page.should_be_product_add_to_basket()
    time.sleep(1)
    browser.quit()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    try:
        page.press_buy()
        page.solve_quiz_and_get_code()
        # time.sleep(1)
        assert page.is_disappeared(*BasketPageLocators.ITEM_ADD_TO_BASKET_NOTIFY) == False
    finally:
        browser.quit()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    try:
        page.should_be_login_link()
    finally:
        browser.quit()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    try:
        page.go_to_login_page()
        assert page.is_element_present(*LoginPageLocators.LOGIN_FORM) == True, 'Login Form not foubnded.'
        assert page.is_element_present(*LoginPageLocators.REGISTER_FORM) == True, 'Register Form not founded.'
    finally:
        browser.quit()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    try:
        page.go_to_basket_page()
        time.sleep(1)
        assert page.is_this_a_basket_page() == True, 'Not basket page.'
        assert page.is_basket_empty() == False, 'Basket not empty.'
    finally:
        browser.quit()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    try:
        page.go_to_basket_page()
        time.sleep(1)
        assert page.is_this_a_basket_page() == True, 'Not basket page.'
        assert page.is_basket_empty() == True, 'Basket not empty.'
    finally:
        browser.quit()

