from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://getnada.com"

    def go_to_site(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((locator)))
        except TimeoutException:
            return False
        return element

    def click_element(self, locator, time=15):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable((locator)))
        except TimeoutException:
            return False
        return element