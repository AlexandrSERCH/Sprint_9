import allure
from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class RecipesPage(BasePage):
    RECEPT_NAME_FIELD = (By.XPATH, "//div[text()='Название рецепта']/../input")
    INGRIDIENT_FIELD = (By.XPATH, "//input[contains(@class, 'ingredientsInput')]")
    INGRIDIENT_AMOUNT_VALUE = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    INGRIDIENT_ADD_BUTTON = (By.XPATH, "//div[contains(@class, 'ingredientAdd')]")
    COOKING_TIME_FIELD = (By.XPATH, "//div[text()='Время приготовления']/../input")
    RECEPT_DESCRIPTION_TEXTAREA = (By.XPATH, "//div[text()='Описание рецепта']/../textarea")
    SELECT_FILE_INPUT = (By.XPATH, "//input[contains(@class, 'fileInput')]")
    CREATE_RECEPT_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")

    @staticmethod
    def get_ingridient_item_locator(ingridient: str):
        return By.XPATH, f"//div[text()='{ingridient}']"

    @allure.step("Открыть страницу 'Рецепты'")
    def open(self):
        self._open_page(constants.recipes_page_url())

    @allure.step("Заполнить поле 'Название рецепта' значением {recept_name}")
    def send_keys_recept_name(self, recept_name: str):
        self._send_keys(self.RECEPT_NAME_FIELD, recept_name)

    @allure.step("Выбрать 'Ингредиент': {ingridient}")
    def select_ingridient(self, ingridient: str):
        self._send_keys_ingridient(ingridient)
        self._select_ingredient_with_dropdown(ingridient)

    @allure.step("Ввести в поле 'Ингредиент' значение {ingridient}")
    def _send_keys_ingridient(self, ingridient: str):
        self._send_keys(self.INGRIDIENT_FIELD, ingridient)

    @allure.step("Выбрать из дропдауна ингридиент: '{ingridient}'")
    def _select_ingredient_with_dropdown(self, ingridient: str):
        locator = self.get_ingridient_item_locator(ingridient)
        self._click(locator)

    @allure.step("Ввести в поле 'Вес' кол-во: '{amount}'")
    def send_keys_amount_value_ingridient(self, amount: int):
        self._send_keys(self.INGRIDIENT_AMOUNT_VALUE, amount)

    @allure.step("Нажать кнопку 'Добавить игридиент'")
    def click_add_ingridient_button(self):
        self._click(self.INGRIDIENT_ADD_BUTTON)

    @allure.step("Заполнить поле 'Время приготовления' значением: '{time}'")
    def send_keys_cooking_time(self, time: int):
        self._send_keys(self.COOKING_TIME_FIELD, time)

    @allure.step("Заполнить поле 'Описание рецепта' значением {description}")
    def send_keys_description_recept(self, description: str):
        self._send_keys(self.RECEPT_DESCRIPTION_TEXTAREA, description)

    @allure.step("Загрузить фото рецепта")
    def upload_recept_image(self, path_iamge: str):
        self._upload_photo(self.SELECT_FILE_INPUT, path_iamge)

    @allure.step("Нажать на кнопку 'Создать рецепт'")
    def click_create_recept(self):
        self._click(self.CREATE_RECEPT_BUTTON)

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        return self._get_current_url()
