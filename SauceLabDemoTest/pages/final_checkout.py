from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.listing import PageWithListings
from utilities.base_element import BaseElement
from utilities.locator import Locator


class FinalCheckout(BasePage):

     url = "https://www.saucedemo.com/checkout-step-two.html"

     @property
     def finish_button(self):
         locator = Locator(By.CSS_SELECTOR, "button#finish")
         return BaseElement(self.driver, locator)

     def verify_checkout_detail(self):
         page_listing = PageWithListings(self.driver.page_source)
         total_price_of_product = page_listing.get_total_price_of_products_checkout()
         checkout_price_details = page_listing.get_price_details_checkout()

         if total_price_of_product == checkout_price_details['summary_subtotal_label']:
             tax_amount = round(total_price_of_product*(0.08),2)
             if  tax_amount == checkout_price_details['summary_tax_label']:
                 print("Checkout Tax Details are correct")
             else:
                 print("Tax details are not correctly computed Expected: {} Found: {}".format(round(total_price_of_product*(0.08),2),
                                                                                     checkout_price_details['summary_tax_label']))
         else:
             print("Total amount is incorrect. Expected: {},  Found: {}".format(total_price_of_product, checkout_price_details['summary_subtotal_label']))

         print("Checkout details are correct")

     def finish_order_button(self):
         locator = Locator(By.CSS_SELECTOR, 'button[id="finish"]')
         return BaseElement(self.driver, locator)


