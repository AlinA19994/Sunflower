from playwright.sync_api import Page
from functions.functions import Functions

class EditProfile:

    def __init__(self, page: Page):
        self.page = page
        self.nickname_field = self.page.get_by_test_id("nicknameInput")
        self.avatars_images = self.page.locator('img[alt="Avatar Image "]')
        self.apply_button = self.page.locator('[class="button button--main"]')

    def change_nickname(self, newNickname):
        """
        Insert value to the nickname field
        """
        self.nickname_field.fill(newNickname)

    def change_avatar(self):
        """
        click on the avatar from the random index
        """
        inx = Functions.random_number_between_range(self.avatars_images)
        self.avatars_images.nth(inx).click()

    def submit(self):
        """
        press on apply button
        """
        self.apply_button.nth(1).click()




