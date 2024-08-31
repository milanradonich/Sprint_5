import faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import get_user_data
from locators import *


def get_sing_up_data():
    fake = faker.Faker()
    email = fake.email()

    return email


def login_execution(self):
    """
    метод стандартного входа в ЛК
    :return:
    """
    email_data, password_data = get_user_data()
    self.driver.find_element(By.XPATH, INPUT_EMAIL_LOGIN).send_keys(email_data)
    self.driver.find_element(By.XPATH, INPUT_PASSWORD_LOGIN).send_keys(password_data)
    self.driver.find_element(By.XPATH, BTN_LOGIN).click()
    WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(
        (By.CLASS_NAME, 'BurgerConstructor_basket__container__2fUl3')
    ))

