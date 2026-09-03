import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("lang=en")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    time.sleep(2)
    driver.quit()