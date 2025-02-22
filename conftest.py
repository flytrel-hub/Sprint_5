import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from locators import Locators

WAIT_TIMEOUT = 10


@pytest.fixture(scope='function')
def driver():
    try:
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()
        chrome_driver.get(Data.STELLAR_BURGERS_URL)
        yield chrome_driver
    except Exception as e:
        raise Exception(f"Ошибка запуска браузера: {e}")
    finally:
        chrome_driver.quit()


@pytest.fixture(scope='function')
def perform_login(driver):
    def _login(email=Data.AUTH_EMAIL, password=Data.AUTH_PASSWORD):
        email_input = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.EMAIL_LOGIN_INPUT)
        )
        email_input.send_keys(email)

        password_input = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.PASSWORD_LOGIN_INPUT)
        )
        password_input.send_keys(password)

        submit_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)
        )
        submit_button.click()
    return _login


@pytest.fixture(scope='function')
def authorization(driver, perform_login):
    login_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
    )
    login_button.click()

    perform_login()

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.presence_of_element_located(Locators.ORDER_BUTTON)
    )

    assert "/login" not in driver.current_url, "Авторизация не выполнена"
