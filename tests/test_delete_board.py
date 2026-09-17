

class TestDeleteBoard:
    def test_delete_board(self, board_created):
        boards_page = board_created.delete_board()
        #assert boards_page.is_board_deleted_message("Board deleted.")