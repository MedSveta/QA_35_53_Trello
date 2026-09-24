from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path

from pages.base_page import BasePage

class AtlassianPage(BasePage):
    PROFILE_PHOTO = (By.XPATH, "//button[@aria-label='Profile photo options']")
    CHANGE_PROFILE_PHOTO = (By.XPATH, "//button[@data-testid='change-avatar']")
    INPUT_UPLOAD_PHOTO = (By.XPATH, "//input[@data-testid='image-navigator-input-file']")
    BTN_SUBMIT = (By.XPATH, "//button[@type='submit' and @class='css-1yaki22']")

    def change_profile_photo(self, photo_path: str| Path) -> None:
        #self.click(self.PROFILE_PHOTO)
        (ActionChains(self.driver)
         .move_to_element(self.find(self.PROFILE_PHOTO))
         .click()
         .perform()
         )
        self.click(self.CHANGE_PROFILE_PHOTO)
        self.find(self.INPUT_UPLOAD_PHOTO).send_keys(str(photo_path))
        self.click(self.BTN_SUBMIT)