import config

class Test_change_profile_photo:
    def test_change_profile_photo(self, go_boards_page):
        profile = go_boards_page.open_my_account_atlassian_page()
        profile.change_profile_photo(config.PROFILE_PHOTO_PATH_CAT)