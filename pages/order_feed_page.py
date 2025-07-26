import allure
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from data.urls import FEED_URL
from selenium.webdriver.common.by import By


class OrderFeedPage(BasePage):

    @allure.step("Клик на последний заказ в ленте")
    def click_last_order(self):
        self.click_to_element(OrderFeedPageLocators.LAST_ORDER)

    @allure.step("Получаем содержимое деталей заказа")
    def get_order_details_content(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    @allure.step("Получаем общее количество выполненных заказов")
    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получаем количество заказов, выполненных сегодня")
    def get_today_completed_counter(self):
        element = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip())

    @allure.step("Открываем страницу ленты заказов")
    def open_feed_page(self):
        self.navigate_to(FEED_URL)
        self.wait_for_element_visible(OrderFeedPageLocators.FEED_TITLE)

    @allure.step("Клик на кнопку 'Конструктор'")
    def click_constructor(self):
        self.click_to_element(OrderFeedPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Клик на кнопку 'Лента заказов'")
    def click_feed(self):
        self.click_when_clickable(OrderFeedPageLocators.BUTTON_ORDER_FEED)

    @allure.step("Клик на кнопку 'Оформить заказ'")
    def click_place_an_order(self):
        self.click_to_element(OrderFeedPageLocators.PLACE_AN_ORDER)

    @allure.step("Клик на кнопку 'Личный кабинет'")
    def click_account_button(self):
        self.click_when_clickable(OrderFeedPageLocators.BUTTON_ACCOUNT)

    @allure.step("Клик на кнопку 'История заказов'")
    def click_order_history_button(self):
        self.click_to_element(OrderFeedPageLocators.BUTTON_ORDER_HISTORY)

    @allure.step("Закрываем всплывающее окно деталей заказа")
    def click_close_order_details(self):
        self.click_when_clickable(OrderFeedPageLocators.BUTTON_CLOSE_ORDER_DETAILS)

    @allure.step("Получаем номер последнего оформленнoго заказа")
    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_ID)

    @allure.step("Проверяем, что заказ с номером {order_id} отображается в ленте")
    def is_order_number_displayed_anywhere(self, order_id: str) -> bool:
        id_str = str(order_id).lstrip('#').lstrip('0')
        locators = [
            (By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderList__cByyi')]//li[contains(., '{id_str}')]"),
            (By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(., '{id_str}')]"),
        ]
        for locator in locators:
            if self.is_element_present(locator):
                return True
        return False