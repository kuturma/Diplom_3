from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    # Заголовок страницы "Лента заказов"
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    # Список готовых заказов
    LAST_ORDER = (By.XPATH, "(//ul[contains(@class,'OrderFeed_orderList')]//li)[last()]")
    # Списик заказов в работе
    ORDER_IN_PROGRESS_LOCATOR = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList__cByyi')]//li[contains(., '{}')]")

    # Счетчик выполненных заказов за все время
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за все время:']]")
    # Счетчик выполненных заказов за сегодня
    TODAY_COMPLETED_COUNTER = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за сегодня:']]")

    # Окно с деталями заказа
    ORDER_DETAILS_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    # Закрыть окно с деталями заказа
    BUTTON_CLOSE_ORDER_DETAILS = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button[@type='button']")

    # Номера заказа в сплывающем окне
    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    # Номер заказа в работе
    ORDER_ID_IN_FEED = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]//li//*[contains(text(), '{0}')]")

    # Кнопка "Лента заказов"
    BUTTON_ORDER_FEED = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    # Кнопка "Личный кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка "История заказов"
    BUTTON_ORDER_HISTORY = (By.XPATH, "//a[@href='/account/order-history']")
    # Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    # Кнопка "Оформить заказ"
    PLACE_AN_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")