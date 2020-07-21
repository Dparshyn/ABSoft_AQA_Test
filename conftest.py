import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Opera()
    yield driver
    driver.quit()