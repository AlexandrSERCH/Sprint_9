from selenium.webdriver.common.by import By

RECEPT_NAME_FIELD = (By.XPATH, "//div[text()='Название рецепта']/../input")
INGRIDIENT_FIELD = (By.XPATH, "//input[contains(@class, 'ingredientsInput')]")
INGRIDIENT_AMOUNT_VALUE = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
INGRIDIENT_ADD_BUTTON = (By.XPATH, "//div[contains(@class, 'ingredientAdd')]")
COOKING_TIME_FIELD = (By.XPATH, "//div[text()='Время приготовления']/../input")
RECEPT_DESCRIPTION_TEXTAREA = (By.XPATH, "//div[text()='Описание рецепта']/../textarea")
SELECT_FILE_INPUT = (By.XPATH, "//input[contains(@class, 'fileInput')]")
CREATE_RECEPT_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
