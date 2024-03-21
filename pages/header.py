import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderHelper(BasePage):

    @allure.step('Открываем форму авторизации')
    def click_button_auth(self):
        return self.find_element(locator=HeaderLocators.auth_link, wait_time=3).click()

    @allure.step('Переходим в ЛК')
    def click_link_personal_account(self):
        return self.find_element(locator=HeaderLocators.link_personal_account, wait_time=3).click()
