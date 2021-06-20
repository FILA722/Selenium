from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time
from .pages.base_page import BasePage
from .pages.locators import BasketPageLocators
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer9"])

# def test_guest_can_add_to_basket(browser):

def test_guest_can_add_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0'
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