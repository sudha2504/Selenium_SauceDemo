import options
from  selenium import webdriver
from pytest import fixture
import json

from selenium.webdriver.common.by import By

data_path = "config/test_data.json"

def load_data(path):
    with open(path) as f:
        return json.load(f)

@fixture(params=load_data(data_path))
def test_data_load(request):
    data = request.param
    return data

# # @fixture(params=[webdriver.Chrome])
# @fixture(params=[ webdriver.Firefox])
@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request, env):

    driver = request.param
    if driver == webdriver.Chrome:
        options = webdriver.ChromeOptions()
        prefs = {
            "profile.password_manager_leak_detection": False  # 👈 This is key
        }
        options.add_experimental_option("prefs", prefs)
    elif driver == webdriver.Firefox:
        options= webdriver.FirefoxOptions()
        options.set_preference("signon.rememberSignons", False)  # Disable saving passwords
        options.set_preference("signon.autofillForms", False)  # Disable autofill
        options.set_preference("signon.management.page.breachAlert.enabled", False)  # Disable breach alerts

    options.add_argument("--user-data-dir=/tmp/temporary-profile")
    drvr = driver(options=options)
    drvr.maximize_window()

    yield drvr

    drvr.get("https://www.saucedemo.com/inventory.html")
    elements = drvr.find_elements(By.XPATH, "//button[contains(@id,'remove')]")
    for element in elements:
        element.click()
    drvr.quit()

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     help="The environment to run the tests on")

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")