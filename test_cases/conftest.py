import time
import pytest
from playwright.sync_api import Playwright
from page_objects.home_page import HomePage
from page_objects.lobby_page import LobbyPage
from page_objects.menu.menu import Menu
from page_objects.menu.my_account.edit_profile import EditProfile
from page_objects.menu.my_account.my_account_dialog import MyAccountDialog
from utilities import manage_page
from utilities.common_ops import get_data


@pytest.fixture(scope="function")
def init_web_driver(request, playwright: Playwright):
    browser_type = get_data('Browser').lower()
    slow_mo = int(get_data('Slow_mo'))
    browser_launchers = {
        'chrome': playwright.chromium.launch,
        'firefox': playwright.firefox.launch,
        'edge': playwright.chromium.launch
    }
    channel = 'msedge' if browser_type == 'edge' else browser_type

    if browser_type in browser_launchers:
        manage_page.browser = browser_launchers[browser_type](headless=False, channel=channel, slow_mo=slow_mo)
    manage_page.context = manage_page.browser.new_context()
    manage_page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    manage_page.page = manage_page.context.new_page()
    manage_page.page.set_viewport_size({"width": 1920, "height": 1080})
    manage_page.page.goto(get_data('URL'))

    # Initialize page object
    manage_page.home_page = HomePage(manage_page.page)
    manage_page.lobby_page = LobbyPage(manage_page.page)
    manage_page.menu = Menu(manage_page.page)
    manage_page.my_account_dialog = MyAccountDialog(manage_page.page)
    manage_page.edit_profile = EditProfile(manage_page.page)

    yield
    time.sleep(5)
    manage_page.context.tracing.stop(path="../trace/trace.zip")
    manage_page.context.close()
    manage_page.browser.close()


