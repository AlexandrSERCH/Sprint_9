import allure
from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    @allure.step("Открыть страницу авторизации")
    def open(self):
        self._open_page(constants.login_page_url())

    @allure.step("Заполнить поле 'Электронная почта' значением {email}")
    def send_keys_email(self, email: str):
        self._send_keys(self.EMAIL_FIELD, email)

    @allure.step("Заполнить поле 'Пароль' значением {password}")
    def send_keys_password(self, password: str):
        self._send_keys(self.PASSWORD_FIELD, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self._click(self.LOGIN_BUTTON)

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        return self._get_current_url()

    @allure.step("Проверить отображение формы авторизации")
    def assert_auth_form_is_visible(self):
        self._is_visible(self.EMAIL_FIELD)
        self._is_visible(self.PASSWORD_FIELD)
        self._is_visible(self.LOGIN_BUTTON)
