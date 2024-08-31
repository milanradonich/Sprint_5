import pytest
import helper

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class TestLogout:
    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        """
        фикстура получения двайвера
        :param driver_setup:
        :return:
        """
        self.driver = driver_setup
        yield self.driver

    def test_logout_personal_account_btn_success(self):
        """
        выход по кнопке «Выйти» в личном кабинете
        :return:
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_PERSONAL_ACCOUNT))
        ).click()
        helper.login_execution(self)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/')
        )
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_PERSONAL_ACCOUNT))
        ).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_LOGOUT))
        ).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login')
        )
