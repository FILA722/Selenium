from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket_page(self):
        basket = self.browser.find_element(*BasketPageLocators.GO_TO_BASKET_PAGE_BUTTON)
        basket.click()

    def is_this_a_basket_page(self):
        try:
            assert self.browser.find_element(*BasketPageLocators.THIS_IS_BASKET_PAGE).text == 'Basket', 'This is not basket page'
        except AssertionError:
            return False
        return True

    def is_basket_empty(self):
        try:
            assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text == 'Your basket is empty.', 'Basket is not empty'
        except AssertionError:
            return False
        return True

    def is_basket_not_empty(self):
        try:
            assert self.browser.find_element(*BasketPageLocators.NOT_EMPTY_BASKET).text == 'Items to buy now', 'Basket is empty'
        except AssertionError:
            return False
        return True