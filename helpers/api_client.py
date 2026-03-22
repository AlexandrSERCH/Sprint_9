import allure
import requests

from constants import register_user_endpoint, auth_user_endpoint


class ApiClient:

    def __init__(self):
        self.register_user_endpoint = register_user_endpoint()
        self.auth_user_endpoint = auth_user_endpoint()

    @allure.step("Зарегистрировать пользователя")
    def register_user(self, user_data: dict) -> requests.Response:
        return requests.post(self.register_user_endpoint, json=user_data)

    @allure.step("Авторизоваться")
    def auth_user(self, user_data: dict) -> requests.Response:
        return requests.post(self.auth_user_endpoint, json=user_data)
