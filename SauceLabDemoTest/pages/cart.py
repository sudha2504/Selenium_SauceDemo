from utilities.base_element import BaseElement
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utilities.locator import Locator
from pages.product_listing import ProductListing

class CartPage(BasePage):

    url = "https://www.saucedemo.com/cart.html"

    @property
    def continue_shopping_button(self):
        locator = Locator(By.CSS_SELECTOR, "button#continue-shopping")
        return BaseElement(self.driver, locator)

    @property
    def checkout_button(self):
        locator = Locator(By.CSS_SELECTOR, "button#checkout")
        return BaseElement(self.driver, locator)

    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()

        if self.driver.current_url  == ProductListing.url:
            return True
        else:
            return False






