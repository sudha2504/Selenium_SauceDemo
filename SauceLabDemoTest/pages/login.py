from pages.basepage import BasePage
from utilities.locator import Locator
from selenium.webdriver.common.by import By
from utilities.base_element import BaseElement

class LoginPage(BasePage):

    url = "https://www.saucedemo.com/"

    @property
    def login_username(self):
        locator = Locator(By.CSS_SELECTOR, 'input#user-name')
        return BaseElement(self.driver, locator)

    @property
    def login_password(self):
        locator = Locator(By.CSS_SELECTOR, 'input#password')
        return BaseElement(self.driver, locator)

    @property
    def submit_login_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input#login-button')
        return BaseElement(self.driver, locator)

    def enter_login_details(self, username, password):
        self.login_username.input_text(username)
        self.login_password.input_text(password)
        self.submit_login_button.click()





