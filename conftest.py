import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import constants
from data.users.user_builder import UserBuilder
from helpers.api_client import ApiClient
from pages.components.header_component import HeaderComponent
from pages.login_page import LoginPage
from pages.recept_page import ReceptPage
from pages.recipes_page import RecipesPage
from pages.register_page import RegisterPage
from utils.attach import attach_screenshot


@pytest.fixture(autouse=True)
def browser():
    selenoid_url = os.getenv("SELENOID_URL")

    if selenoid_url:
        options = Options()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability("selenoid:options", {
            "enableVideo": True,  # запись видео
            "enableVNC": True,  # просмотр в реальном времени
            "screenResolution": "1920x1080x24"
        })
        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    attach_screenshot(driver)
    driver.quit()


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture
def register_page(browser):
    return RegisterPage(browser)


@pytest.fixture
def recipes_page(browser):
    return RecipesPage(browser)


@pytest.fixture
def recept_page(browser):
    return ReceptPage(browser)


@pytest.fixture
def header_component(browser):
    return HeaderComponent(browser)


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def registered_user(api_client):
    user_data = UserBuilder().build()

    user = {
        "email": user_data.email,
        "password": user_data.password,
        "username": user_data.login,
        "first_name": user_data.first_name,
        "last_name": user_data.last_name
    }

    response = api_client.register_user(user)
    if response.status_code != 201:
        pytest.fail(
            f"Пользователь не зарегестрирован. Код ответа: {response.status_code}. Тело ответа: {response.json()}")

    yield user_data


@pytest.fixture
def auth_user(browser, api_client, registered_user):
    user = {"email": registered_user.login, "password": registered_user.password}

    response = api_client.auth_user(user)
    if response.status_code != 200:
        pytest.fail(
            f"Пользователь не авторизовался. Код ответа: {response.status_code}. Тело ответа: {response.json()}")

    browser.get(constants.base_page_url())
    body = response.json()
    browser.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", 'token', body['auth_token'])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук, который отлавливает момент падения теста и делает скриншот.
    Необходим, чтобы успеть сделать скриншот, если на экране, к примеру
    помешал поп-ап, на странице не видно необходимый элемент или элемент не отобразился и т.п.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            with allure.step("Скриншот при падении"):
                attach_screenshot(driver)
