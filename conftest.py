import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


@pytest.fixture(scope="function")
def driver_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]'))
    )
    yield driver
    driver.quit()


