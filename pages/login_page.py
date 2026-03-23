import allure

import constants
from locators.login_page_locators import EMAIL_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from pages.base_page import BasePage


class LoginPage(BasePage):


    @allure.step("Открыть страницу авторизации")
    def open(self):
        self._open_page(constants.login_page_url())

    @allure.step("Заполнить поле 'Электронная почта' значением {email}")
    def send_keys_email(self, email: str):
        self._send_keys(EMAIL_FIELD, email)

    @allure.step("Заполнить поле 'Пароль' значением {password}")
    def send_keys_password(self, password: str):
        self._send_keys(PASSWORD_FIELD, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self._click(LOGIN_BUTTON)

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        return self._get_current_url()

    @allure.step("Проверить отображение формы авторизации")
    def assert_auth_form_is_visible(self):
        self._is_visible(EMAIL_FIELD)
        self._is_visible(PASSWORD_FIELD)
        self._is_visible(LOGIN_BUTTON)
