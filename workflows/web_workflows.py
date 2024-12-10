
from functions.functions import Functions
from utilities import manage_page as page
from functions.verifications import Verifications
import os

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

nickname = None

class WebFlows:
    @staticmethod
    def sign_in_with_correct_credentials():
        """
        step: Log in to the account with the correct credentials
        :argument: Email + Password - from environment variables
        """
        page.home_page.sign_in(EMAIL, PASSWORD)

    @staticmethod
    def alert():
        """
        step: - Clicking "later" on the alert pop up after the login
        """
        page.lobby_page.discard_alert()

    @staticmethod
    def navigate_to_my_account():
        """
        step: - Press on menu button and navigate to "my account"
        """
        page.lobby_page.open_menu()
        page.menu.select_my_account_option()

    @staticmethod
    def edit_nickname_and_avatar():
        """
        steps:
        1. Press on edit option in my account
        2. Create randon nickname and save it in global "nickname" variable
        3. Choose Random avatar
        4. Press on apply - to save changes
        """
        page.my_account_dialog.press_on_edit_button()
        random_nickname = Functions.random_name()
        globals()['nickname'] = random_nickname
        page.edit_profile.change_nickname(random_nickname)
        page.edit_profile.change_avatar()
        page.edit_profile.submit()

    @staticmethod
    def verify_update_nickname():
        """
        steps:
        1. Get text from my account dialog - nickname field and save it as actual variable
        2. Saved value from nickname variable in expect variable
        3. Verify with assert between the variables
        """
        actual = page.my_account_dialog.get_nickname_text()
        expect = nickname
        Verifications.verify_equals(actual, expect)

    @staticmethod
    def get_value_by_account_balance():
        """
        steps:
        1. Print current coin type with balance
        2. switch to the other coin
        3. Print other coin type with balance
        """

        print(page.lobby_page.get_balance())
        page.lobby_page.switch_coin()
        print(page.lobby_page.get_balance())







