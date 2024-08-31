import time
import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class TestConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        """
        фикстура получения двайвера
        :param driver_setup:
        :return:
        """
        self.driver = driver_setup
        yield self.driver

    def test_active_menu_sauces(self):
        """
        тест проверяет переход в меню конструктор
        :return:
        """
        div_element = self.driver.find_element(By.XPATH, LINK_HEADER_MENU_SAUCES)
        div_element.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "tab_tab_type_current__2BEPc"))
        )
        assert "tab_tab_type_current__2BEPc" in div_element.get_attribute("class")

        div_element = self.driver.find_element(By.XPATH, LINK_HEADER_MENU_FILLINGS)
        div_element.click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "tab_tab_type_current__2BEPc"))
        )
        assert "tab_tab_type_current__2BEPc" in div_element.get_attribute("class")

        div_element = self.driver.find_element(By.XPATH, LINK_HEADER_MENU_BUNS)
        div_element.click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "tab_tab_type_current__2BEPc"))
        )
        assert "tab_tab_type_current__2BEPc" in div_element.get_attribute("class")
