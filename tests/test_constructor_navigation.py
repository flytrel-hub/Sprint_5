from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from conftest import WAIT_TIMEOUT


class TestConstructorNavigation:
    def test_go_to_constructor_from_personal_account(self, driver, authorization):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        constructor_link = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)
        )
        constructor_link.click()

        order_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )

        assert order_button.text == "Оформить заказ", "Переход в конструктор не выполнен" 

    def test_go_to_constructor_via_logo(self, driver, authorization):
        personal_account_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_button.click()

        logo_link = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.LOGO)
        )
        logo_link.click()

        order_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )

        assert order_button.text == "Оформить заказ", "Переход в конструктор не выполнен"