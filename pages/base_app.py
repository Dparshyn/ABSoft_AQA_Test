from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from pages.page_locators import SearchLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://getnada.com"

    def go_to_site(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(locator))
        return element

    def click_element(self, locator, time=15):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator))
        return element
