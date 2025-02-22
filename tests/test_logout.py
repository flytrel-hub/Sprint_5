from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from conftest import WAIT_TIMEOUT


class TestLogout:
    def test_logout_from_personal_account(self, driver, authorization):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        logout_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()

        submit_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.SUBMIT_BUTTON)
        )
        current_url = driver.current_url

        assert submit_button.text == "Войти", "Выход из аккаунта не выполнен"
        assert "/login" in current_url, "URL не соответствует странице логина после выхода"
