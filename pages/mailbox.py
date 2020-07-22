from pages.base_app import BasePage
from pages.page_locators import SearchLocators


class Mailbox(BasePage):
    def open_message(self):
        element = self.click_element(SearchLocators.GO_TO_EMAIL_BOX)
        element.click()

    def mailbox_content(self):
        elements = self.driver.find_element(*SearchLocators.E_MAIL_CONTENT)
        print(elements)
        return elements
