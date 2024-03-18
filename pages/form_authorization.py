import allure
from locators.form_authorization_locators import FormAuthLocators
from pages.base_page import BasePage


class FormAuthorizationHelper(BasePage):

    @allure.step('Нажимаем на кнопку "Вход по паролю"')
    def click_button_login_with_password(self):
        self.find_element(FormAuthLocators.button_login_with_pass, wait_time=3).click()

    @allure.step('Заполняем поле "Номер телефона"')
    def filing_field_phone(self, phone):
        self.find_element(FormAuthLocators.field_phone, wait_time=3).send_keys(phone)

    @allure.step('Заполняем поле "Код или пароль"')
    def filing_field_password(self, password):
        self.find_element(FormAuthLocators.field_password, wait_time=3).send_keys(password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_button_login(self):
        self.find_element(FormAuthLocators.button_login, wait_time=3).click()

    @allure.step('Нажимаем на кнопку "Вход" для юр лиц')
    def click_button_login_b2b(self):
        self.find_element(FormAuthLocators.button_login_b2b, wait_time=3).click()

    @allure.step('Заполняем форму авторизации б2б пользователя')
    def filing_form_auth_b2b_user(self, email, password):
        self.find_element(FormAuthLocators.field_email, wait_time=3).send_keys(email)
        self.find_element(FormAuthLocators.field_password_b2b, wait_time=3).send_keys(password)
        self.find_element(FormAuthLocators.button_login, wait_time=3).click()
