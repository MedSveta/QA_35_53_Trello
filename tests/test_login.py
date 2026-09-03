
from pages.home_page import HomePage

class TestLogin:
    def test_login(self, driver):
        page = HomePage(driver).open()