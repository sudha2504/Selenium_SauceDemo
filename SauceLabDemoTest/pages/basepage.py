from selenium.webdriver.common.by import By

from utilities.base_element import BaseElement


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver
        # self.url = {
        #     'dev': 'http://localhost:8000',
        #     'qa': 'https://www.saucedemo.com/'
        # }[env]

    def go(self, url):
        self.driver.get(url)

    def modify_item_in_cart(self, item_name, action='add'):
        item_to_be_modified = item_name.lower().replace(" ", '-')
        if action == 'add':
             id = "add-to-cart-" + item_to_be_modified
        else:
            id = "remove-" + item_to_be_modified
        locator = (By.CSS_SELECTOR, f"button[id='{id}']")
        item_to_be_modified_element = BaseElement(self.driver, locator)
        item_to_be_modified_element.click()
        print("{} {} is done".format(action, item_name))