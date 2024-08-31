import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import login_execution
from locators import *


class TestTransition:
    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        """
        фикстура получения двайвера
        :param driver_setup:
        :return:
        """
        self.driver = driver_setup
        yield self.driver

    def test_transition_to_constructor_success(self):
        """
        Переход из личного кабинета в конструктор
        :return:
        """
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

    def test_transition_to_logo_success(self):
        """
        Переход из личного кабинета на главную
        :return:
        """
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
