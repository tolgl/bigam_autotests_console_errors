from selenium.webdriver.common.by import By


class HeaderLocators:
    auth_link = (By.XPATH, ".//span[text()='Профиль']")
    link_personal_account = (By.XPATH, ".//a[@href='/personal/']")
