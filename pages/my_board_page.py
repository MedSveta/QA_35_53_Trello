from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MyBoardPage(BasePage):

    MENU_DOTS = (By.XPATH, "//button[@aria-label='Show menu']")
    CLOSE_BOARD = (By.XPATH, "//div[text()='Close board']")
    CLOSE_BTN = (By.XPATH, "//button[@data-testid='popover-close-board-confirm']")

    def delete_board(self):
        self.click(self.MENU_DOTS)
        self.click(self.CLOSE_BOARD)
        self.click(self.CLOSE_BTN)
