import allure

from data.recipes.recept_builder import build_recipt
from utils.mark import mark_tag


@allure.epic("Рецепты")
@allure.feature("Создание рецепта")
class TestCreateRecept:

    @allure.severity(allure.severity_level.CRITICAL)
    @mark_tag("UI", "smoke", "regress", "recipes")
    @allure.title("Успешное создание рецепта")
    def test_succes_create_recept(self, recipes_page, auth_user, header_component, recept_page):
        recept_data = build_recipt()

        recipes_page.open()
        header_component.click_create_recept()
        recipes_page.send_keys_recept_name(recept_data.recept_name)
        recipes_page.select_ingridient(recept_data.ingredient_name)
        recipes_page.send_keys_amount_value_ingridient(recept_data.ingredient_amount_value)
        recipes_page.click_add_ingridient_button()
        recipes_page.send_keys_cooking_time(recept_data.cooking_time)
        recipes_page.send_keys_description_recept(recept_data.recept_description)
        recipes_page.upload_recept_image(recept_data.path_image)
        recipes_page.click_create_recept()

        with allure.step("Проверить создание карточки рецепта"):
            actual_title = recept_page.get_title_in_recept_page()

            with allure.step(
                    f"Проверить соответствие текущего заголовка '{recept_data.recept_name}'"
                    f" с созданным '{actual_title}'"):
                assert recept_data.recept_name == actual_title

            recept_page.assert_url_contains_recipe_id()
