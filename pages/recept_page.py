import re

import allure

from locators.recept_page_locators import TITLE_H1
from pages.base_page import BasePage


class ReceptPage(BasePage):

    @allure.step("Получить заголовок на странице рецета")
    def get_title_in_recept_page(self):
        return self._get_text(TITLE_H1)

    @allure.step("Проверить наличие ID рецепта в URL страницы")
    def assert_url_contains_recipe_id(self):
        actual_url = self._get_current_url()
        assert re.search(r"/recipes/\d+", actual_url)
