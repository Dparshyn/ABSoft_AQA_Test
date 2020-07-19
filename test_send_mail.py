import pytest
from source.send_mail import *
from pages.mailbox import Mailbox
from source.animal_api import *


@pytest.fixture()
def test_send_mail(browser):
    link = 'https://getnada.com/'
    page = MailAddress.create_message(browser, link)
    page.open()
    mail_box = Mailbox(browser)
    mail_box.open_message()
    mail_box.mailbox_content()
    animal_request()
