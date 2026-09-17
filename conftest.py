import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from models.board import Board
from pages.home_page import HomePage
from pages.boards_page import BoardsPage
from faker import Faker
import config as cfg

from models.user import User

fake = Faker()


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


@pytest.fixture
def new_board() -> Board:
    return Board(f"qa-{fake.random_int(0, 999)}")

@pytest.fixture
def board_created(go_boards_page, new_board):
    my_board = go_boards_page.create_new_board(new_board).submit_board()
    return my_board
