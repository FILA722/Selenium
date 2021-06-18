import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_language', action='store', default='ru')

@pytest.fixture(scope='function')
def browser(request):
    browser_language = request.config.getoption('browser_language')
    browser = webdriver.Chrome()
    link = f'http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/'
    browser.get(link)
    return browser
    # browser.quit()
