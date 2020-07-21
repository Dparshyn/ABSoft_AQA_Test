import pytest
from pages.mailbox import Mailbox

@pytest.fixture
def prepare_email_elements(browser):
   mail_box = Mailbox(browser)
   mail_box.go_to_site()
   mail_box.open_message()
   return mail_box.mailbox_content()


def test_email_not_empty(prepare_email_elements):
   assert prepare_email_elements > 0