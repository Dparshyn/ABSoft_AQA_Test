import pytest
from pages.mailbox import Mailbox
from source.send_mail import MailAddress


@pytest.fixture
def prepare_email_elements(browser):
    mail_box = Mailbox(browser)
    mail_box.go_to_site()
    mail_sending = MailAddress(browser)
    mail_sending.create_message()
    mail_box.open_message()
    return mail_box.mailbox_content()


def test_email_not_empty(prepare_email_elements):
    assert len(prepare_email_elements) > 0
