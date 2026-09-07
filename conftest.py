import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from faker import Faker
import config as cfg

from models.user import User


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("lang=en")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    time.sleep(2)
    driver.quit()

@pytest.fixture
def user() -> User:
    return cfg.STANDARD_USER

@pytest.fixture
def go_boards_page(driver, user):
    return HomePage(driver).open().goto_login_page().login(user)