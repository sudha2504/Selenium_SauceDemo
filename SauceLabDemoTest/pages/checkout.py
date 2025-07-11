from faker import Faker
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utilities.base_element import BaseElement
from utilities.locator import Locator

class CheckoutPage(BasePage):

    def details_element(self, detail):
        locator = Locator(By.CSS_SELECTOR, f'input#{detail}')
        return BaseElement(self.driver, locator)

    @property
    def continue_checkout(self):
        locator = Locator(By.CSS_SELECTOR, 'input#continue')
        return BaseElement(self.driver, locator)

    def add_details(self):
        fake = Faker()
        name = fake.name().split(" ")
        details_dict = {'first-name': name[0], 'last-name': name[1], 'postal-code': fake.postcode()}
        for i in ['first-name', 'last-name', 'postal-code']:
            details_element = self.details_element(i)
            details_element.input_text(details_dict[i])

        print("Added Checkout Details successfully")




