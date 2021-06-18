# def test_button(browser):
#     try:
#         assert  browser.find_elements_by_css_selector('button.btn:nth-child(3)'), 'Кнопка не найдена'
#     finally:
#         browser.quit()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()