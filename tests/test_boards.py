from models.board import Board
import pytest

class TestBoard:

    @pytest.mark.smoke
    def test_create_new_board_positive(self, go_boards_page, new_board):
        my_board = go_boards_page.create_new_board(new_board).submit_board()
        assert my_board.is_url_contains(new_board.board_title)

    def test_create_new_board_negative_empty_board_title(self, go_boards_page):
        my_board = go_boards_page.create_new_board(Board(""))
        assert my_board.is_create_btn_clickable()