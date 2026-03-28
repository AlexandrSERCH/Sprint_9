import re

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ReceptPage(BasePage):
    TITLE_H1 = (By.XPATH, "//div[contains(@class, 'header-info')]/h1")

    @allure.step("Получить заголовок на странице рецета")
    def get_title_in_recept_page(self):
        return self._get_text(self.TITLE_H1)

    @allure.step("Проверить наличие ID рецепта в URL страницы")
    def assert_url_contains_recipe_id(self):
        actual_url = self._get_current_url()
        assert re.search(r"/recipes/\d+", actual_url)
