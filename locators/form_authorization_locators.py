from selenium.webdriver.common.by import By


class FormAuthLocators:
    button_login_with_pass = (By.XPATH, ".//button[@title='Вход по паролю']")
    field_phone = (By.XPATH, ".//input[@type='tel']")
    field_password = (By.XPATH, ".//input[@autocomplete='new-password']")
    button_login = (By.XPATH, ".//span[text()='Войти']")
    button_login_b2b = (By.XPATH, ".//div/div[2]/div/div[2]/div/div/div/div[3]/button[1]")
    field_email = (By.XPATH, ".//input[@placeholder='E-mail']")
    field_password_b2b = (By.XPATH, ".//input[@type='password']")
