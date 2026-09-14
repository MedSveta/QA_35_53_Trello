
class TestDeleteBoard:

    def test_delete_board(self, board_created):
        delete_board = board_created.delete_board()