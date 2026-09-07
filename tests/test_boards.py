
class TestBoard:
    def test_create_new_board(self, go_boards_page):
        my_board = go_boards_page.create_new_board()