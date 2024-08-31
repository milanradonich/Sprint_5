import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import login_execution
from locators import *


class TestLoginPortal:
    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        """
        фикстура получения двайвера
        :param driver_setup:
        :return:
        """
        self.driver = driver_setup
        yield self.driver

    def test_login_on_home_page_success(self):
        """
        вход по кнопке «Войти в аккаунт» на главной
        :return:
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_ENTER_IN_ACC))
        ).click()
        login_execution(self)

    def test_login_personal_account_btn_success(self):
        """
        вход через кнопку «Личный кабинет»
        :return:
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_PERSONAL_ACCOUNT))
        ).click()
        login_execution(self)

    def test_login_form_registration_btn_success(self):
        """
        вход через кнопку в форме регистрации
        :return:
        """
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_ENTER_IN_ACC))
        ).click()
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, REGISTRATION_LINK))
        ).click()
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_LOGIN_IN_REGISTRATION))
        ).click()
        login_execution(self)

    def test_login_recovery_form_btn_success(self):
        """
        вход через кнопку в форме восстановления пароля
        :return:
        """
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_ENTER_IN_ACC))
        ).click()
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LINK_FORGOT_PASSWORD))
        ).click()
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_LOGIN_IN_REGISTRATION))
        ).click()
        login_execution(self)

