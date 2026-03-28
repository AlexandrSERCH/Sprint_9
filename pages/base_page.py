import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    @allure.step("Открыть страницу по ссылке: {url}")
    def _open_page(self, url):
        return self.driver.get(url)

    @allure.step("Проверить видимость элемента по локатору: '{locator}'")
    def _is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элемент не отображается: {locator}")

    @allure.step("Нажать на элемент по локатору: {locator}")
    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести текст: {text} в поле, по локатору: {locator}")
    def _send_keys(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Загрузить фото из пути: '{path}' по локатору: '{locator}'")
    def _upload_photo(self, locator, path: str):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(path)

    @allure.step("Получить текст по локатору: {locator}")
    def _get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Получить текущую ссылку")
    def _get_current_url(self):
        return self.driver.current_url
