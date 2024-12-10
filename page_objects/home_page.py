from playwright.sync_api import Page



class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.login_option = self.page.get_by_test_id("lobby-login-btn")
        self.email_fields = self.page.locator('[id="email"]')
        self.password_fields = self.page.locator('[id=password]')
        self.login_button = self.page.locator('button[type= "submit"]')

    def sign_in(self, username, password):
        """
        Sign in using provided username and password.
        1. Press on Log in button
        2. Insert email in the Email field
        3. Insert password in the Password field
        4. Press on "log in" button
        """
        self.login_option.click()
        self.email_fields.fill(username)
        self.password_fields.fill(password)
        self.login_button.click()






