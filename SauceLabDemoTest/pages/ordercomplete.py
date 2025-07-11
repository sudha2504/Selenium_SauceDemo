from pages.basepage import BasePage
from utilities.base_element import BaseElement
from utilities.locator import Locator
from selenium.webdriver.common.by import By


class OrderCompletePage(BasePage):

    @property
    def success_message(self):
        locator = Locator(By.XPATH, '//h2[contains(text(),"Thank you for your order")]')
        return BaseElement(self.driver, locator)

    def check_order_success(self):
        if self.success_message == None:
            print("Order unsuccessful")
        else:
            print("Order Successful")