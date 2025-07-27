from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента с ожиданием видимости")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Ввод текста в элемент")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Форматирование локатора с подстановкой")
    def format_locator(self, locator, num):
        method, locator_str = locator
        locator_str = locator_str.format(num)
        return method, locator_str

    @allure.step("Клик по элементу, если он кликабельный")
    def click_when_clickable(self, locator):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Клик по элементу с использованием js")
    def click_with_js(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )

    @allure.step("Перетаскивание элемента")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)

        script = """
            const [source, target] = arguments;
            const createEvent = (type) => {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: new DataTransfer()
                });
                return event;
            };

            source.dispatchEvent(createEvent('dragstart'));
            target.dispatchEvent(createEvent('dragenter'));
            target.dispatchEvent(createEvent('dragover'));
            target.dispatchEvent(createEvent('drop'));
            source.dispatchEvent(createEvent('dragend'));
        """

        self.driver.execute_script(script, source, target)

    @allure.step("Проверка наличия отображения элемента")
    def is_element_displayed(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step("Переход на страницу")
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step("Ожидание выполнения условия")
    def wait_until_condition(self, condition, timeout=30):
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Ожидание изменения текста элемента")
    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=30):
        self.wait_until_condition(
            lambda _: self.get_text_from_element(locator) != initial_text, timeout
        )
        return self.find_element_with_wait(locator)

    @allure.step("Поиск элемента с динамическим значением")
    def find_and_format_locator(self, locator, dynamic_value):
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.find_element_with_wait(formatted_locator)

    @allure.step("Получение значения атрибута элемента")
    def get_element_attribute(self, locator, attribute_name):
        element = self.find_element_with_wait(locator)
        return element.get_attribute(attribute_name)

    @allure.step("Проверка наличия элемента")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step("Проверка отсутствия элемента")
    def is_element_present(self, locator, timeout=7):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False