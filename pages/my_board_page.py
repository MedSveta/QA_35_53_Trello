import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MyBoardPage(BasePage):

    MENU_DOTS = (By.XPATH, "//button[@aria-label='Show menu']")
    CLOSE_BOARD = (By.XPATH, "//div[text()='Close board']")
    CLOSE_BTN = (By.XPATH, "//button[@data-testid='popover-close-board-confirm']")
    DELETE_BOARD = (By.XPATH, "//button[@data-testid='close-board-delete-board-button']")
    DELETE_BTN = (By.XPATH, "//button[@data-testid='close-board-delete-board-confirm-button']")


    def delete_board(self):
        from pages.boards_page import BoardsPage
        self.click(self.MENU_DOTS)
        self.click(self.CLOSE_BOARD)
        self.click(self.CLOSE_BTN)
        self.click(self.MENU_DOTS)
        self.click(self.DELETE_BOARD)
        self.click(self.DELETE_BTN)
        return BoardsPage(self.driver)


