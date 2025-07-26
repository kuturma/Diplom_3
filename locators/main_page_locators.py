from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    
    # Секция "Соберите бургер"
    SECTION_BURGER_CONSTRUCTOR = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")
    
    # Кнопка "Лента заказов"
    BUTTON_ORDER_FEED = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    # Заголовок "Готовы:"
    COMPLETED_ORDERS = (By.XPATH, "//p[contains(text(),'Готовы:')]")

    # Счетчик готовых заказов за все время
    COMPLETED_ORDERS_COUNTER = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ")[0]

    # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_R2D3_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

    # Заголовок "Детали ингредиента"
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")

    # Кнопка "Закрыть"
    BUTTON_CLOSE_INGREDIENT_DETAILS = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")

    # Поле конструктора "Перетяните булочку сюда (верх)"
    ORDER_TARGET_TOP = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")

    # Счетчик ингредиентов
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    # Кнопка "Оформить заказ"
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    # Сообщение "Ваш заказ начали готовить"
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']")

    # Номер заказа который в работе
    ORDER_IN_PROGRESS_LOCATOR = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li[1]//*[contains(text(), '{0}')]")
