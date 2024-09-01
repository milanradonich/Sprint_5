import pytest
from selenium.webdriver.common.by import By

import helper

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class TestLogout:
    def test_logout_personal_account_btn_success(self, driver_setup):
        """
        выход по кнопке «Выйти» в личном кабинете
        :return:
        """
        self.driver = driver_setup
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
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

