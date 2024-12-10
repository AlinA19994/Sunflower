import time
import pytest
from workflows.web_workflows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    def test_01_Verify_change_users_nickname(self):
        WebFlows.sign_in_with_correct_credentials()
        WebFlows.alert()
        WebFlows.navigate_to_my_account()
        WebFlows.edit_nickname_and_avatar()
        WebFlows.verify_update_nickname()

    def test_02_Print_Balance(self):
        WebFlows.sign_in_with_correct_credentials()
        WebFlows.alert()
        time.sleep(2)
        WebFlows.get_value_by_account_balance()







