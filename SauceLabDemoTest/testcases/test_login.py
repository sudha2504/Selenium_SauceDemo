from pages.login import LoginPage
import pytest

@pytest.mark.login
def test_check_login(browser,test_data_load):
    login_page = LoginPage(browser)
    login_page.go(LoginPage.url)
    print(test_data_load)
    print(browser.title)
    login_page.enter_login_details(test_data_load['username'], test_data_load['password'])

