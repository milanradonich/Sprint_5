BTN_ENTER_IN_ACC = '//button[text()="Войти в аккаунт"]'  # кнопка входа в аккаунт на главной
REGISTRATION_LINK = '//a[text()="Зарегистрироваться"]'  # кнопка регистрации
INPUT_NAME = '//label[text()="Имя"]/following-sibling::input'  # поле ввода имени
INPUT_EMAIL = '//label[text()="Email"]/following-sibling::input'  # поле ввода почты
INPUT_PASSWORD = '//label[text()="Пароль"]/following-sibling::input'  # поле ввода пароля
BTN_REGISTRATION_SUBMIT = '//button[text()="Зарегистрироваться"]'  # кнопка подтверждения регистрации
ERROR_MESSAGE = '//*[@class="input__error text_type_main-default"]'  # сообщение при невалидном пароле при регистрации
BTN_LOGIN = '//button[text()="Войти"]'  # кнопка войти при авторизации
BTN_PERSONAL_ACCOUNT = '//a[contains(@class, "AppHeader_header__link__3D_hX") and @href="/account"]' # кнопка личный кабинет на главной
BTN_LOGIN_IN_REGISTRATION = '//a[text()="Войти"]'  # кнопка войти на странице регистрации
# и на странице восстановления пароля
LINK_FORGOT_PASSWORD = '//a[text()="Восстановить пароль"]'  # ссылка восстановить пароль
BTN_LOGOUT = '//button[text()="Выход"]'  # кнопка выйти в ЛК
LINK_CONSTRACTION = "//a[@class='AppHeader_header__link__3D_hX']"  # ссылка на конструктор
LINK_LOGO = '//div[contains(@class, "AppHeader_header__logo__2D0X2")]/a'  # логотип стелларбургер
LINK_HEADER_MENU_BUNS = "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]"  # булки
LINK_HEADER_MENU_SAUCES = "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]"  # соусы
LINK_HEADER_MENU_FILLINGS = "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]"  # начинки
CLASS_LOCATOR = 'tab_tab_type_current__2BEPc'
