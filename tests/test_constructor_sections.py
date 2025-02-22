from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from conftest import WAIT_TIMEOUT


class TestConstructorSections:
    def test_switch_to_buns_section(self, driver, authorization):
        buns_section = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(Locators.BUNS_SECTION)
        )
        sauces_section = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION)
        )

        sauces_section.click()
        WebDriverWait(driver, WAIT_TIMEOUT).until(
            lambda d: "current" in d.find_element(*Locators.SAUCES_SECTION).get_attribute("class")
        )

        driver.execute_script("arguments[0].scrollIntoView();", buns_section)
        buns_section.click()
        WebDriverWait(driver, WAIT_TIMEOUT).until(
            lambda d: "current" in d.find_element(*Locators.BUNS_SECTION).get_attribute("class")
        )

        assert "current" in buns_section.get_attribute("class"), "Переход к разделу 'Булки' не выполнен"

    def test_switch_to_sauces_section(self, driver, authorization):
        sauces_section = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION)
        )

        driver.execute_script("arguments[0].scrollIntoView();", sauces_section)
        sauces_section.click()

        WebDriverWait(driver, WAIT_TIMEOUT).until(
            lambda d: "current" in d.find_element(*Locators.SAUCES_SECTION).get_attribute("class")
        )

        assert "current" in sauces_section.get_attribute("class"), "Раздел 'Соусы' не подсвечен после клика"

    def test_switch_to_fillings_section(self, driver, authorization):
        fillings_section = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(Locators.FILLINGS_SECTION)
        )

        driver.execute_script("arguments[0].scrollIntoView();", fillings_section)
        fillings_section.click()

        WebDriverWait(driver, 10).until(
            lambda d: "current" in d.find_element(*Locators.FILLINGS_SECTION).get_attribute("class")
        )

        assert "current" in fillings_section.get_attribute("class"), "Раздел 'Начинки' не подсвечен после клика"
