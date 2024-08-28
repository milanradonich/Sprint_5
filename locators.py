from selenium.webdriver.common.by import By

BTN_ENTER_IN_ACC = '//*[@id="root"]/div/main/section[2]/div/button'  # кнопка входа в аккаунт на главной
REGISTRATION_LINK = (By.CLASS_NAME, 'Auth_link__1fOlj')  # кнопка регистрации
INPUT_NAME = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'  #поле ввода имени
INPUT_EMAIL = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'  # поле ввода почты
INPUT_PASSWORD = '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'  # поле ввода пароля
BTN_REGISTRATION_SUBMIT = '//*[@id="root"]/div/main/div/form/button'  # кнопка подтверждения регистрации
ERROR_MESSAGE = '//*[@class="input__error text_type_main-default"]'  # сообщение при невалидном пароле при регистрации



