import pytest
from source import send_mail
from pages.mailbox import Mailbox
from source.animal_api import *

@py.fixture(scope="session")
def test_email_valid(@py.fixture):
   variables = your_fixture
   assert is_email_valid(variables["email"])

