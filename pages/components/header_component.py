import allure

from locators.header_component_locators import CREATE_ACCOUNT_BUTTON, LOGIN_BUTTON, CREATE_RECEPT_BUTTON, LOGOUT_BUTTON
from pages.base_page import BasePage


class HeaderComponent(BasePage):


    @allure.step("Нажать в хедере кнопку 'Создать аккаунт'")
    def click_create_account(self):
        self._click(CREATE_ACCOUNT_BUTTON)

    @allure.step("Нажать в хедере кнопку 'Войти'")
    def click_login_button(self):
        self._click(LOGIN_BUTTON)

    @allure.step("Нажать в хедере кнопку 'Создать рецепт'")
    def click_create_recept(self):
        self._click(CREATE_RECEPT_BUTTON)

    @allure.step("Проверить отображение кнопки 'Выйти'")
    def assert_logout_button_is_visible(self):
        self._is_visible(LOGOUT_BUTTON)
