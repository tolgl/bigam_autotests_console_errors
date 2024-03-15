from selenium.webdriver.common.by import By


class FormAuthLocators:
    button_login_with_pass = (By.XPATH, ".//button[@title='Вход по паролю']")
    field_phone = (By.XPATH, ".//input[@type='tel']")
    field_password = (By.XPATH, ".//input[@autocomplete='new-password']")
    button_login = (By.XPATH, ".//span[text()='Войти']")
