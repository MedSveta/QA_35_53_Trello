from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    def open(self) -> 'HomePage':
        self.driver.get("https://trello.com/")
        return self