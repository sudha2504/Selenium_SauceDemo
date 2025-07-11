from selenium.webdriver.support.ui import Select
from pages.listing import PageWithListings
from utilities.locator import Locator
from selenium.webdriver.common.by import By


from pages.basepage import BasePage
from utilities.base_element import BaseElement


class ProductListing(BasePage):

    url = "https://www.saucedemo.com/inventory.html"

    def find_item(self, item_name):
        locator = Locator(By.XPATH, f"//div[contains(text(), '{item_name}')]")
        return BaseElement(self.driver, locator)

    @property
    def filter_dropdownelement(self):
        locator = Locator(By.CSS_SELECTOR, 'select')
        return BaseElement(self.driver, locator)

    @property
    def shopping_cart(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
        return BaseElement(self.driver, locator)

    def filter_item(self, criteria):
        select_criteria = Select(self.filter_dropdownelement.webElement)
        select_criteria.select_by_value(criteria)
        pass

    def check_product_listing_order(self, reverse=False, based_on='item_name'):
        product_listing = PageWithListings(self.driver.page_source)
        list_products = product_listing.get_product_listings(based_on)

        if product_listing.check_product_order(list_products, reverse=reverse):
            return True
        else:
            return False
