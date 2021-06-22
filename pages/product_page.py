from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators
from .locators import BasketPageLocators
import pytest
import time

class ProductPage(BasePage):
    def product_page_tests(self):
        self.go_to_basket_page()
        # self.should_be_product_link()
        # self.should_be_product_add_to_basket()


    def press_buy(self):
        basket_page = self.browser.find_element(By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
        basket_page.click()

    def go_to_basket_page(self):
        basket_page = self.browser.find_element(By.CSS_SELECTOR, "a.btn-info:nth-child(1)")
        basket_page.click()

    def should_be_product_link(self):
        assert self.browser.current_url == self.url

    def should_be_product_add_to_basket(self):
        assert self.find_element(*BasketPageLocators.BASKET_ADD) == self.find_element(*BasketPageLocators.BASKET_TOTAL)
