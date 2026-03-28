import allure
from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class RegisterPage(BasePage):
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='first_name']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='last_name']")
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[name='username']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")

    @allure.step("Открыть страницу регистрации")
    def open(self):
        self._open_page(constants.register_page_url())

    @allure.step("Заполнить поле 'Имя' значением: '{first_name}'")
    def send_keys_first_name(self, first_name: str):
        self._send_keys(self.FIRST_NAME_FIELD, first_name)

    @allure.step("Заполнить поле 'Фамилия' значением: '{last_name}'")
    def send_keys_last_name(self, last_name: str):
        self._send_keys(self.LAST_NAME_FIELD, last_name)

    @allure.step("Заполнить поле 'Имя пользователя' значением: '{username}'")
    def send_keys_username(self, username: str):
        self._send_keys(self.USERNAME_FIELD, username)

    @allure.step("Заполнить поле 'Адрес электронной почты' значением: '{email}'")
    def send_keys_email(self, email: str):
        self._send_keys(self.EMAIL_FIELD, email)

    @allure.step("Заполнить поле 'Пароль' значением: '{password}'")
    def send_keys_password(self, password: str):
        self._send_keys(self.PASSWORD_FIELD, password)

    @allure.step("Нажать кнопку 'Создать аккаунт'")
    def click_create_account(self):
        self._click(self.CREATE_ACCOUNT_BUTTON)
