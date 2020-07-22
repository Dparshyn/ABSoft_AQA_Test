from selenium.webdriver.common.by import By


class SearchLocators:
    E_MAIL = (By.CSS_SELECTOR, '.address.what_to_copy')
    GO_TO_EMAIL_BOX = (By.CSS_SELECTOR, '.msg_list .msg_item:first-child')
    E_MAIL_CONTENT = (By.TAG_NAME, 'a')
