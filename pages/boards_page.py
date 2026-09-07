from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BoardsPage(BasePage):
    CREATE_NEW_BOARD_BTN = (By.XPATH, "//button[@data-testid='create-board-tile']")
    CREATE_BOARD = (By.XPATH, "//button[@data-testid='create-board-button']")
    INPUT_BOARD_TITLE = (By.XPATH, "//input[@data-testid='create-board-title-input']")

    def create_new_board(self):
        self.click(self.CREATE_NEW_BOARD_BTN)
        self.click(self.CREATE_BOARD)
