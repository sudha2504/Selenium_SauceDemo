from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import by
from selenium.webdriver.support.wait import WebDriverWait

class BaseElement:

    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator
        self.webElement = None
        self.findElement(self.locator)

    def findElement(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.locator)))
        self.webElement = element
        return None

    def click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator)).click()
        return None

    def input_text(self, txt):
        self.webElement.send_keys(txt)
        return None

    @property
    def text(self):
        text = self.webElement.text
        return text
