from playwright.sync_api import Page

class MyAccountDialog:

    def __init__(self, page: Page):
        self.page = page
        self.displayed_nickName = self.page.get_by_test_id("nicknameDisplay")
        self.edit_profile_button = self.page.locator('[class="_pen_a31cg_31"]')

    def press_on_edit_button(self):
        """
        press on edit button
        """
        self.edit_profile_button.click()

    def get_nickname_text(self):
        """
        get text from the nickname field
        :return: string
        """
        return self.displayed_nickName.inner_text()

