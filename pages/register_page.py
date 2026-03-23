import allure

import constants
from locators.register_page_locators import FIRST_NAME_FIELD, LAST_NAME_FIELD, USERNAME_FIELD, EMAIL_FIELD, \
    PASSWORD_FIELD, CREATE_ACCOUNT_BUTTON
from pages.base_page import BasePage


class RegisterPage(BasePage):


    @allure.step("Открыть страницу регистрации")
    def open(self):
        self._open_page(constants.register_page_url())

    @allure.step("Заполнить поле 'Имя' значением: '{first_name}'")
    def send_keys_first_name(self, first_name: str):
        self._send_keys(FIRST_NAME_FIELD, first_name)

    @allure.step("Заполнить поле 'Фамилия' значением: '{last_name}'")
    def send_keys_last_name(self, last_name: str):
        self._send_keys(LAST_NAME_FIELD, last_name)

    @allure.step("Заполнить поле 'Имя пользователя' значением: '{username}'")
    def send_keys_username(self, username: str):
        self._send_keys(USERNAME_FIELD, username)

    @allure.step("Заполнить поле 'Адрес электронной почты' значением: '{email}'")
    def send_keys_email(self, email: str):
        self._send_keys(EMAIL_FIELD, email)

    @allure.step("Заполнить поле 'Пароль' значением: '{password}'")
    def send_keys_password(self, password: str):
        self._send_keys(PASSWORD_FIELD, password)

    @allure.step("Нажать кнопку 'Создать аккаунт'")
    def click_create_account(self):
        self._click(CREATE_ACCOUNT_BUTTON)
