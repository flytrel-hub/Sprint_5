from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from conftest import WAIT_TIMEOUT


class TestLogin:
    def test_login_from_main_page(self, driver, perform_login):
        login_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        )
        login_button.click()

        perform_login()

        order_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )

        assert order_button.text == "Оформить заказ", "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_from_personal_account(self, driver, perform_login):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        perform_login()

        order_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )

        assert order_button.text == "Оформить заказ", "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_via_registration_page(self, driver, perform_login):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        register_link_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        )
        register_link_button.click()

        login_link_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK)
        )
        login_link_button.click()

        perform_login()

        order_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )

        assert order_button.text == "Оформить заказ", "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_via_password_recovery(self, driver, perform_login):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        recover_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.RECOVER_PASSWORD_LINK)
        )
        recover_button.click()

        login_link_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK)
        )
        login_link_button.click()

        perform_login()

        order_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )

        assert order_button.text == "Оформить заказ", "Кнопка 'Оформить заказ' не отображается после входа"