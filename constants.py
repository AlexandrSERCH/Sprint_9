BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru"
BASE_URL_API = "https://foodgram-backend-1.prakticum-team.ru"

URLS = {
    "base_page": f"{BASE_URL}",
    "register_page": f"{BASE_URL}/signup",
    "login_page": f"{BASE_URL}/signin",
    "recipes_page": f"{BASE_URL}/recipes",
}

API_ENDPOINTS = {
    "register_user": f"{BASE_URL_API}/api/users/",
    "auth_user": f"{BASE_URL_API}/api/auth/token/login/"
}


def base_page_url():
    return URLS["base_page"]


def register_page_url():
    return URLS["register_page"]


def login_page_url():
    return URLS["login_page"]


def recipes_page_url():
    return URLS["recipes_page"]


def register_user_endpoint():
    return API_ENDPOINTS["register_user"]


def auth_user_endpoint():
    return API_ENDPOINTS["auth_user"]
