import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helper import get_sing_up_data
from locators import *


@pytest.fixture(autouse=True)
def setup(driver_setup):
    driver = driver_setup
    yield driver


@pytest.mark.parametrize("password, should_fail", [
    ('123', True),  # Неправильный пароль
    ('Qwerty1000!', False)  # Правильный пароль
])
def test_registration_with_correct_password_and_incorrect(setup, password, should_fail):
    setup.find_element(By.XPATH, BTN_ENTER_IN_ACC).click()
    time.sleep(2)
    register_button = WebDriverWait(setup, 3).until(
        expected_conditions.visibility_of_element_located(REGISTRATION_LINK)
    )
    register_button.click()
    time.sleep(2)
    email_data = get_sing_up_data()
    # Выполняем регистрацию
    setup.find_element(By.XPATH, INPUT_NAME).send_keys('milan')
    time.sleep(1)
    setup.find_element(By.XPATH, INPUT_EMAIL).send_keys(email_data)
    time.sleep(1)
    setup.find_element(By.XPATH, INPUT_PASSWORD).send_keys(password)
    time.sleep(1)
    setup.find_element(By.XPATH, BTN_REGISTRATION_SUBMIT).click()
    time.sleep(1)

    if should_fail:
        error_message = WebDriverWait(setup, 3).until(expected_conditions.visibility_of_element_located((
            By.XPATH, ERROR_MESSAGE))
        )
        assert "Некорректный пароль" in error_message.text


#milan_radonich13@yandex.ru
#Qwerty1000!
