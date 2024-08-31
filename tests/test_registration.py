import time
import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import get_sing_up_data
from locators import *


class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        self.driver = driver_setup
        yield self.driver

    @pytest.mark.parametrize("password, should_fail", [
        ('123', True),  # Неправильный пароль
        ('Qwerty1000!', False)  # Правильный пароль
    ])
    def test_registration_with_correct_password_and_incorrect(self, password, should_fail):
        """
        тест на успешную регистраицию и регистрацию с некорректным паролем
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BTN_ENTER_IN_ACC))
        ).click()
        register_button = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_LINK))
        )
        register_button.click()
        email_data = get_sing_up_data()
        self.driver.find_element(By.XPATH, INPUT_NAME).send_keys('milan')
        time.sleep(1)
        self.driver.find_element(By.XPATH, INPUT_EMAIL).send_keys(email_data)
        time.sleep(1)
        self.driver.find_element(By.XPATH, INPUT_PASSWORD).send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, BTN_REGISTRATION_SUBMIT).click()
        time.sleep(1)

        if should_fail:
            error_message = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((
                By.XPATH, ERROR_MESSAGE))
            )
            assert "Некорректный пароль" in error_message.text
        else:
            WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(
                "https://stellarburgers.nomoreparties.site/login")
            )


