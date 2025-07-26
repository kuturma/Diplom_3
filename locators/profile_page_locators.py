from selenium.webdriver.common.by import By

class ProfilePageLocators:

    # Кнопка "Личный кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    # Поле ввода почты
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  

    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  

    # Кнопка "Войти"
    BUTTON_LOGIN = (By.CSS_SELECTOR, '.button_button__33qZ0')  

    # Кнопка "Выход"
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]") 

    # Кнопка "История заказов"
    BUTTON_ORDER_HISTORY = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']") 

    # Выполненные заказы в "Историях заказов"
    ORDER_COMPLETED = (By.XPATH, "//p[@class='OrderHistory_visible__19YMB text text_type_main-small mb-7']")

    # Локатор успешного выхода из личного кабинет, кнопка "Вход"
    LOGIN_AFTER_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]")

    # Локатор успешной авторизации
    LOGIN_AFTER_LOGOUT_BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")