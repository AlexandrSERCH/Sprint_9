import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderComponent(BasePage):
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[text()='Создать аккаунт']")
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    CREATE_RECEPT_BUTTON = (By.XPATH, "//a[text()='Создать рецепт']")

    @allure.step("Нажать в хедере кнопку 'Создать аккаунт'")
    def click_create_account(self):
        self._click(self.CREATE_ACCOUNT_BUTTON)

    @allure.step("Нажать в хедере кнопку 'Войти'")
    def click_login_button(self):
        self._click(self.LOGIN_BUTTON)

    @allure.step("Нажать в хедере кнопку 'Создать рецепт'")
    def click_create_recept(self):
        self._click(self.CREATE_RECEPT_BUTTON)

    @allure.step("Проверить отображение кнопки 'Выйти'")
    def assert_logout_button_is_visible(self):
        self._is_visible(self.LOGOUT_BUTTON)
