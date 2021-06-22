from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru')

@pytest.fixture(scope='function')
def browser(request):
    # language = request.config.getoption('language')
    browser = webdriver.Firefox()
    return browser