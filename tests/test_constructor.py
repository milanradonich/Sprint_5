import time
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class TestConstructor:
    def test_active_menu_sauces(self, driver_setup):
        """
        тест проверяет переход в меню конструктор
        :return:
        """
        self.driver = driver_setup
        self.driver.find_element(By.XPATH, LINK_HEADER_MENU_SAUCES).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, LINK_HEADER_MENU_SAUCES))
        )
        new_class = self.driver.find_element(By.XPATH, LINK_HEADER_MENU_SAUCES)
        assert CLASS_LOCATOR in new_class.get_attribute("class")

        self.driver.find_element(By.XPATH, LINK_HEADER_MENU_FILLINGS).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, LINK_HEADER_MENU_FILLINGS))
        )
        new_class = self.driver.find_element(By.XPATH, LINK_HEADER_MENU_FILLINGS)
        assert CLASS_LOCATOR in new_class.get_attribute("class")

        self.driver.find_element(By.XPATH, LINK_HEADER_MENU_BUNS).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, LINK_HEADER_MENU_BUNS))
        )
        new_class = self.driver.find_element(By.XPATH, LINK_HEADER_MENU_BUNS)
        assert CLASS_LOCATOR in new_class.get_attribute("class")
