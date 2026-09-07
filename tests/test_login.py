
from pages.home_page import HomePage

class TestLogin:
    def test_login(self, driver, user):
        page = HomePage(driver).open().goto_login_page().login(user)
        assert page.is_url_contains("boards")

    def test_login_negative(self, driver, user):
        page = HomePage(driver).open().goto_login_page().login(user)
        assert not page.is_url_contains("negative")