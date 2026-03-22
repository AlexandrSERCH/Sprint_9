import allure

from data.users.user_builder import UserBuilder


@allure.epic("Пользователи")
@allure.feature("Создание пользователя")
class TestCreateAccount:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "smoke", "regress", "Пользователи")
    @allure.title("Успешное создание пользователя")
    def test_succes_create_account(self, login_page, header_component, register_page):
        user_data = UserBuilder().build()

        login_page.open()
        header_component.click_create_account()
        register_page.send_keys_first_name(user_data.first_name)
        register_page.send_keys_last_name(user_data.last_name)
        register_page.send_keys_username(user_data.login)
        register_page.send_keys_email(user_data.email)
        register_page.send_keys_password(user_data.password)
        register_page.click_create_account()

        with allure.step("Проверить переход на страницу авторизации"):
            login_page.assert_auth_form_is_visible()

            with allure.step("Проверить, что в URL содержится '/signin'"):
                assert "/signin" in login_page.get_current_url()
