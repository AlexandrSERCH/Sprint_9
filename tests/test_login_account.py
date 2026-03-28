import allure

from utils.mark import mark_tag


@allure.epic("Пользователи")
@allure.feature("Авторизация пользователя")
class TestLoginAccount:

    @allure.severity(allure.severity_level.CRITICAL)
    @mark_tag("UI", "smoke", "regress", "users")
    @allure.title("Успешная авторизация пользователя")
    def test_succes_login_account(self, registered_user, login_page, register_page, header_component, recipes_page):
        register_page.open()
        header_component.click_login_button()
        login_page.send_keys_email(registered_user.login)
        login_page.send_keys_password(registered_user.password)
        login_page.click_login_button()

        with allure.step("Проверить переход на главную страницу"):
            header_component.assert_logout_button_is_visible()

            with allure.step("Проверить, что в URL содержится '/recipes"):
                assert "/recipes" in recipes_page.get_current_url()
