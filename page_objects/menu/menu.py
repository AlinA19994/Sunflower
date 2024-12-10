from playwright.sync_api import Page

class Menu:

    def __init__(self, page: Page):
        self.page = page
        self.my_account = self.page.locator('//button[@class="side-menu__action" and text()="My Account"]')

    def select_my_account_option(self):
        """
        select My account in menu
        """
        self.my_account.click()
