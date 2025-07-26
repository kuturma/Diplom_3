import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликаем кнопку 'Конструктор'")
    def click_constructor(self):
        self.click_to_element(MainPageLocators.BUTTON_CONSTRUCTOR)


    @allure.step("Кликаем кнопку 'Оформить заказ'")
    def click_place_an_order(self):
        self.click_to_element(MainPageLocators.BUTTON_MAKE_ORDER)


    @allure.step("Проверяем, что секция 'Cобери бургер' отображается")
    def is_burger_constructor_visible(self):
        return self.find_element_with_wait(MainPageLocators.SECTION_BURGER_CONSTRUCTOR).is_displayed()


    @allure.step("Нажимаем на кнопку 'Лента заказов'")
    def click_order_feed(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_FEED)


    @allure.step("Проверяем, что отображается cчетчик заказов")
    def is_order_feed_counter_visible(self):
        return self.find_element_with_wait(MainPageLocators.COMPLETED_ORDERS).is_displayed()


    @allure.step("Кликаем по ингредиенту R2D3")
    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_R2D3_BUN)


    @allure.step("Проверяем, что открыто окно деталей ингредиента")
    def is_ingredient_details_visible(self):
        return self.is_element_displayed(MainPageLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)


    @allure.step("Закрываем окно c деталями ингредиента")
    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)


    @allure.step("Получаем текущее значение cчётчика ингредиента")
    def get_ingredient_counter(self):
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))


    @allure.step("Перетаскиваем ингредиент в заказ")
    def drag_and_drop_ingredient(self):
        ingredient_locator = MainPageLocators.INGREDIENT_R2D3_BUN
        target_locator = MainPageLocators.ORDER_TARGET_TOP
        self.drag_and_drop(ingredient_locator, target_locator)


    @allure.step("Cообщение о успешном заказе")
    def get_order_success_message(self):
        return self.get_text_from_element(MainPageLocators.ORDER_SUCCESS_MESSAGE)