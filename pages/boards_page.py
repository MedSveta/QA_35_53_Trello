import time

from models.board import Board
from pages.base_page import BasePage
from pages.my_board_page import MyBoardPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BoardsPage(BasePage):
    CREATE_NEW_BOARD_BTN = (By.XPATH, "//button[@data-testid='create-board-tile']")
    CREATE_BOARD = (By.XPATH, "//button[@data-testid='create-board-button']")
    INPUT_BOARD_TITLE = (By.XPATH, "//input[@data-testid='create-board-title-input']")
    CREATE_BTN = (By.XPATH, "//button[@data-testid='create-board-submit-button']")
    DELETE_MESSAGE = (By.XPATH, "//*[text()='Board deleted.']")


    def create_new_board(self, board: Board) -> 'BoardsPage':
        self.click(self.CREATE_NEW_BOARD_BTN)
        self.click(self.CREATE_BOARD)
        self.fill(self.INPUT_BOARD_TITLE, board.board_title)
        return self

    def submit_board(self) ->MyBoardPage:
        self.click(self.CREATE_BTN)
        return MyBoardPage(self.driver)

    def is_create_btn_clickable(self) -> bool:
        return self.is_not_clickable(self.CREATE_BTN)

    #def is_board_deleted_message(self, text: str) -> bool:
    #   return self.is_text_present(self.DELETE_MESSAGE, text)

    def is_board_deleted_message(self, text):
        element = self.wait.until(EC.visibility_of_element_located(self.DELETE_MESSAGE))
        return text in element.text


