import allure
from selenium.webdriver.common.by import By

import constants
from locators.recipes_page_locators import RECEPT_NAME_FIELD, INGRIDIENT_FIELD, INGRIDIENT_AMOUNT_VALUE, \
    INGRIDIENT_ADD_BUTTON, COOKING_TIME_FIELD, RECEPT_DESCRIPTION_TEXTAREA, SELECT_FILE_INPUT, CREATE_RECEPT_BUTTON
from pages.base_page import BasePage


class RecipesPage(BasePage):


    @staticmethod
    def get_ingridient_item_locator(ingridient: str):
        return By.XPATH, f"//div[text()='{ingridient}']"

    @allure.step("Открыть страницу 'Рецепты'")
    def open(self):
        self._open_page(constants.recipes_page_url())

    @allure.step("Заполнить поле 'Название рецепта' значением {recept_name}")
    def send_keys_recept_name(self, recept_name: str):
        self._send_keys(RECEPT_NAME_FIELD, recept_name)

    @allure.step("Выбрать 'Ингредиент': {ingridient}")
    def select_ingridient(self, ingridient: str):
        self._send_keys_ingridient(ingridient)
        self._select_ingredient_with_dropdown(ingridient)

    @allure.step("Ввести в поле 'Ингредиент' значение {ingridient}")
    def _send_keys_ingridient(self, ingridient: str):
        self._send_keys(INGRIDIENT_FIELD, ingridient)

    @allure.step("Выбрать из дропдауна ингридиент: '{ingridient}'")
    def _select_ingredient_with_dropdown(self, ingridient: str):
        locator = self.get_ingridient_item_locator(ingridient)
        self._click(locator)

    @allure.step("Ввести в поле 'Вес' кол-во: '{amount}'")
    def send_keys_amount_value_ingridient(self, amount: int):
        self._send_keys(INGRIDIENT_AMOUNT_VALUE, amount)

    @allure.step("Нажать кнопку 'Добавить игридиент'")
    def click_add_ingridient_button(self):
        self._click(INGRIDIENT_ADD_BUTTON)

    @allure.step("Заполнить поле 'Время приготовления' значением: '{time}'")
    def send_keys_cooking_time(self, time: int):
        self._send_keys(COOKING_TIME_FIELD, time)

    @allure.step("Заполнить поле 'Описание рецепта' значением {description}")
    def send_keys_description_recept(self, description: str):
        self._send_keys(RECEPT_DESCRIPTION_TEXTAREA, description)

    @allure.step("Загрузить фото рецепта")
    def upload_recept_image(self, path_iamge: str):
        self._upload_photo(SELECT_FILE_INPUT, path_iamge)

    @allure.step("Нажать на кнопку 'Создать рецепт'")
    def click_create_recept(self):
        self._click(CREATE_RECEPT_BUTTON)

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        return self._get_current_url()
