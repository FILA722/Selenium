from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time

class LoginPage(BasePage):
    @pytest.fixture(scope="function", autouse=True)
    def login_new_user(self):
        self.register_new_user()
        self.should_be_authorized_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert driver.current_url == self.url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        login = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login.click()
        email = self.browser.find_element(*BasePageLocators.INSERT_EMAIL)
        email.send_keys(f'{time.time()}@fakemail.com')
        password = self.browser.find_element(*BasePageLocators.INSERT_PASSWORD)
        password_phrase = f'{time.time()}qpoijfq'
        password.send_keys(password_phrase)
        confirm_password = self.browser.find_element(*BasePageLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys(password_phrase)
        register_button = self.browser.find_element(*BasePageLocators.REGISTER_BUTTON)
        register_button.click()
