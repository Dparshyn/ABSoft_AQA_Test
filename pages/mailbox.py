from pages.baseApp import *
from pages.pageLocators import SearchLocators


class Mailbox(BasePage):
    def open_message(self):
        element = self.click_element(*SearchLocators.GO_TO_EMAIL_BOX)
        element.click()

    def mailbox_content(self):
        elements = len(self.driver.find_elements(*SearchLocators.E_MAIL_CONTENT))
        assert elements > 0