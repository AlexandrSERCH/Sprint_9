from selenium.webdriver.common.by import By

EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
