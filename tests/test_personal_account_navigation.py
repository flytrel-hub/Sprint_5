from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from conftest import WAIT_TIMEOUT


class TestPersonalAccountNavigation:
    def test_go_to_personal_account(self, driver, authorization):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        order_history_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(Locators.ORDER_HISTORY_LINK)
        )
        current_url = driver.current_url

        assert order_history_button.text == "История заказов", "Кнопка 'История заказов' не отображается в личном кабинете"
        assert "/account" in current_url, "URL не соответствует странице личного кабинета"
