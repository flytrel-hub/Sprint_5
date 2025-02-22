from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators
from conftest import WAIT_TIMEOUT


class TestRegistration:
    def test_valid_registration(self, driver):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        register_link_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        )
        register_link_button.click()

        name_input = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.NAME_REGISTRATION_INPUT)
        )
        name_input.send_keys(Data.VALID_REGISTER_NAME)

        email_input = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.EMAIL_REGISTRATION_INPUT)
        )
        email_input.send_keys(Data.VALID_REGISTER_EMAIL)

        password_input = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PASSWORD_REGISTRATION_INPUT)
        )
        password_input.send_keys(Data.VALID_REGISTER_PASSWORD)

        register_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        register_button.click()

        login_title = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.LOGIN_TITLE)
        )

        assert login_title.text == "Вход"


    def test_invalid_registration(self, driver):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        register_link_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        )
        register_link_button.click()

        name_input = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.NAME_REGISTRATION_INPUT)
        )
        name_input.send_keys(Data.VALID_REGISTER_NAME)

        email_input = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.EMAIL_REGISTRATION_INPUT)
        )
        email_input.send_keys(Data.VALID_REGISTER_EMAIL)

        password_input = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PASSWORD_REGISTRATION_INPUT)
        )
        password_input.send_keys(Data.INVALID_REGISTER_PASSWORD)

        register_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        register_button.click()

        error_message = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.ERROR_MESSAGE)
        )

        assert error_message.text == "Некорректный пароль"
