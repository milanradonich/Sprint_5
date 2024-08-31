from selenium.webdriver.common.by import By

BTN_ENTER_IN_ACC = '//*[@id="root"]/div/main/section[2]/div/button'  # кнопка входа в аккаунт на главной
REGISTRATION_LINK = '//*[@id="root"]/div/main/div/div/p[1]/a'  # кнопка регистрации
INPUT_NAME = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'  # поле ввода имени
INPUT_EMAIL = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'  # поле ввода почты
INPUT_EMAIL_LOGIN = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'  # поле ввода почты на
# странице логин
INPUT_PASSWORD = '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'  # поле ввода пароля
INPUT_PASSWORD_LOGIN = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'  # поле ввода пароля на
# странице логин
BTN_REGISTRATION_SUBMIT = '//*[@id="root"]/div/main/div/form/button'  # кнопка подтверждения регистрации
ERROR_MESSAGE = '//*[@class="input__error text_type_main-default"]'  # сообщение при невалидном пароле при регистрации
BTN_LOGIN = '//*[@id="root"]/div/main/div/form/button'  # кнопка войти при авторизации
BTN_PERSONAL_ACCOUNT = '//*[@id="root"]/div/header/nav/a' # кнопка личный кабинет на главной
BTN_LOGIN_IN_REGISTRATION = '//*[@id="root"]/div/main/div/div/p/a'  # кнопка войти на странице регистрации
# и на странице восстановления пароля
LINK_FORGOT_PASSWORD = '//*[@id="root"]/div/main/div/div/p[2]/a'  # ссылка восстановить пароль
BTN_LOGOUT = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'  # кнопка выйти в ЛК
LINK_CONSTRACTION = '//*[@id="root"]/div/header/nav/ul/li[1]/a'  # ссылка на конструктор
LINK_LOGO = '//*[@id="root"]/div/header/nav/div/a'  # логотип стелларбургер
LINK_HEADER_MENU_BUNS = '//*[@id="root"]/div/main/section[1]/div[1]/div[1]'  # булки
LINK_HEADER_MENU_SAUCES = '//*[@id="root"]/div/main/section[1]/div[1]/div[2]'  # соусы
LINK_HEADER_MENU_FILLINGS = '//*[@id="root"]/div/main/section[1]/div[1]/div[3]'  # начинки
