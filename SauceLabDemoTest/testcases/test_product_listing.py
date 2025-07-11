import pytest
from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.final_checkout import FinalCheckout
from pages.ordercomplete import OrderCompletePage
from pages.product_listing import ProductListing
from pages.login import LoginPage
import time

@pytest.mark.skip
def test_check_product(browser,test_data_load):
    login_page = LoginPage(browser)
    product_page = ProductListing(browser)

    login_page.go(LoginPage.url)
    login_page.enter_login_details(test_data_load['username'], test_data_load['password'])

    product_page.find_item('Sauce Labs Backpack')
    product_page.modify_item_in_cart("Sauce Labs Backpack", action='add')

    product_page.find_item('Sauce Labs Fleece Jacket')
    product_page.modify_item_in_cart("Sauce Labs Fleece Jacket", action='add')
    time.sleep(2)

    product_page.modify_item_in_cart('Sauce Labs Fleece Jacket', action='remove')
    product_page.modify_item_in_cart('Sauce Labs Backpack', action='remove')
    time.sleep(5)


test_data = [
    ("item_name", "az", False),
    ("item_name", "za", True),
    ("item_price", "lohi", False),
    ("item_price", "hilo", True)
]

@pytest.mark.product
@pytest.mark.parametrize("based_on, filter_criteria, reverse", test_data)
def test_check_filter_working_correctly(browser,test_data_load,based_on,filter_criteria,reverse):
    login_page = LoginPage(browser)
    product_page = ProductListing(browser)

    login_page.go(LoginPage.url)
    login_page.enter_login_details(test_data_load['username'], test_data_load['password'])

    product_page.filter_item(filter_criteria)
    time.sleep(2)

    if product_page.check_product_listing_order(reverse=reverse, based_on=based_on):
        print(f"Items are correctly Ordered as per the criteria - {filter_criteria}")
    else:
        print(f"Items are not correctly ordered as per the criteria - {filter_criteria}")

@pytest.mark.product
def test_go_to_cart(browser,test_data_load):
    login_page = LoginPage(browser)
    product_page = ProductListing(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)
    final_checkout = FinalCheckout(browser)
    order_complete = OrderCompletePage(browser)

    login_page.go(LoginPage.url)
    login_page.enter_login_details(test_data_load['username'], test_data_load['password'])

    product_page.find_item('Sauce Labs Backpack')
    product_page.modify_item_in_cart("Sauce Labs Backpack", action='add')

    product_page.find_item('Sauce Labs Bolt T-Shirt')
    product_page.modify_item_in_cart("Sauce Labs Bolt T-Shirt", action='add')

    product_page.shopping_cart.click()
    cart_page.modify_item_in_cart("Sauce Labs Backpack", action='remove')

    cart_page.click_continue_shopping_button()
    product_page.find_item('Sauce Labs Bike Light')
    product_page.modify_item_in_cart("Sauce Labs Bike Light", action='add')

    product_page.shopping_cart.click()

    cart_page.checkout_button.click()
    checkout_page.add_details()
    checkout_page.continue_checkout.click()
    final_checkout.verify_checkout_detail()
    final_checkout.finish_button.click()

    order_complete.check_order_success()













