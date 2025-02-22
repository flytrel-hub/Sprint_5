from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка входа на главной
    PERSONAL_ACCOUNT_LINK = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Ссылка на личный кабинет
    CONSTRUCTOR_LINK = (By.XPATH, '//p[text()="Конструктор"]')  # Ссылка на конструктор
    LOGO = (By.XPATH,  '//div[contains(@class, "AppHeader_header__logo")]')  # Логотип Stellar Burgers
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]/parent::div')  # Раздел булок
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]/parent::div')  # Раздел соусов
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]/parent::div')  # Раздел начинок
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')  # Кнопка оформить заказ на главной
    ORDER_HISTORY_LINK = (By.XPATH, '//a[text()="История заказов"]')  # Ссылка на историю заказов

    LOGIN_TITLE = (By.XPATH, '//h2[text()="Вход"]')  # Название авторизации "Вход"
    EMAIL_LOGIN_INPUT = (By.XPATH, '//input[@name="name"]')  # Поле ввода email
    PASSWORD_LOGIN_INPUT = (By.XPATH, '//input[@name="Пароль"]')  # Поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Кнопка подтверждения входа
    REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться"]')  # Ссылка на регистрацию
    RECOVER_PASSWORD_LINK = (By.XPATH,  '//a[text()="Восстановить пароль"]')  # Ссылка на восстановление

    NAME_REGISTRATION_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')  # Поле имени
    EMAIL_REGISTRATION_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле email
    PASSWORD_REGISTRATION_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Поле пароля
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка регистрации
    ERROR_MESSAGE = (By.XPATH, '//p[contains(@class, "input__error")]')  # Сообщение об ошибке
    LOGIN_LINK = (By.XPATH,  '//a[text()="Войти"]')  # Ссылка на вход

    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # Кнопка выхода