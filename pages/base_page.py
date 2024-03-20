import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://bigam:12345@php8.bigam-dev.ru'

    @allure.step('Открываем страницу')
    def go_to_page(self, path):
        return self.driver.get(self.base_url + path)

    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(
            expected_conditions.visibility_of_element_located(locator))

    def miss_click_on_selection_city(self):
        self.find_element(BasePageLocators.modal_geo, wait_time=5)
        return self.find_element(BasePageLocators.miss_click, wait_time=5).click()

    def wait_invisibility_element(self, locator, wait_time=15):
        return WebDriverWait(self.driver, wait_time).until(
            expected_conditions.invisibility_of_element(locator))
