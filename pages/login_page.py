from pages.base_page import BasePage
from pages.boards_page import BoardsPage
from models.user import User
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL = (By.XPATH, "//input[@data-testid='username']")
    CONTINUE = (By.ID, "login-submit")
    PASSWORD =(By.XPATH, "//input[@data-testid='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-testid='login-submit-idf-testid']")

    def login(self, user: User) -> BoardsPage:
        self.fill(self.EMAIL, user.email)
        self.click(self.CONTINUE)
        self.fill(self.PASSWORD, user.password)
        self.click(self.LOGIN_BUTTON)
        return BoardsPage(self.driver)