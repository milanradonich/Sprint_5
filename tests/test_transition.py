import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import login_execution
from locators import *


class TestTransition:
    def test_transition_to_constructor_success(self, driver_setup):
        """
        Переход из личного кабинета в конструктор
        :return:
        """
        self.driver = driver_setup
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_ENTER_IN_ACC))
        ).click()
        login_execution(self)
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_PERSONAL_ACCOUNT))
        ).click()
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LINK_CONSTRACTION))
        ).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/')
        )
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transition_to_logo_success(self, driver_setup):
        """
        Переход из личного кабинета на главную
        :return:
        """
        self.driver = driver_setup
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_ENTER_IN_ACC))
        ).click()
        login_execution(self)
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_PERSONAL_ACCOUNT))
        ).click()
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LINK_LOGO))
        ).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/')
        )
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'
