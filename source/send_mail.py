from pages.base_app import BasePage
from pages.page_locators import SearchLocators
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from source.animal_api import animal_request


class MailAddress(BasePage):
    def create_message(self):
        msg = MIMEMultipart()
        receiver = self.find_element(SearchLocators.E_MAIL).text
        sender = "absofttest67@gmail.com"
        password = input("Please input your password to mailbox absofttest67@gmail.com: ")
        message = f'{animal_request()}'
        msg['Subject'] = "TEST LINKS"
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print(f"Your email was successfully send to {receiver}. Congrats!")