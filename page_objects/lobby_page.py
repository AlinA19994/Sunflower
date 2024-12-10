from playwright.sync_api import Page

class LobbyPage:

    def __init__(self, page: Page):
        self.page = page
        self.popup_subscribe_later_button = self.page.locator('[id= "onesignal-slidedown-cancel-button"]')
        self.menu_button = self.page.get_by_test_id("menuButton")
        self.coin_switch = self.page.locator('[class="game-type-switcher__coin"]')
        self.type_of_coin = self.page.locator('[class="balance-panel-left"]')
        self.balance = self.page.locator('[id="balance"]')

    def discard_alert(self):
        """
        On the alert - select later option
        """
        self.popup_subscribe_later_button.click()

    def open_menu(self):
        """
        click on button menu
        """
        self.menu_button.click()

    def switch_coin(self):
        """
        switch between coins
        """
        self.coin_switch.click()

    def get_balance(self):
        """
        get text from coin type and get text from  current balance
        :return: string coin type + balance
        """
        return self.type_of_coin.inner_text() +" " +(self.balance.inner_text())
