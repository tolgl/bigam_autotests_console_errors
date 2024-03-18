import allure

from locators.personal_page_locators import PersonalPageLocators
from pages.base_page import BasePage


class PersonalPageHelper(BasePage):

    @allure.step('Переходим в "Мои заказы"')
    def click_link_my_order(self):
        return self.find_element(locator=PersonalPageLocators.link_my_order, wait_time=3).click()

    @allure.step('Переходим в избранное в ЛК')
    def click_link_favorites(self):
        return self.find_element(locator=PersonalPageLocators.link_favorites, wait_time=3).click()

    @allure.step('Переходим на страницу "Вы смотрели" в ЛК')
    def click_link_history_product(self):
        return self.find_element(locator=PersonalPageLocators.link_history_product, wait_time=3).click()

    @allure.step('Переходим на страницу "Заявки на ремонт"')
    def click_link_repairs(self):
        return self.find_element(locator=PersonalPageLocators.link_repairs, wait_time=3).click()

    @allure.step('Переходим на страницу "Мои отзывы"')
    def click_link_reviews(self):
        return self.find_element(locator=PersonalPageLocators.link_reviews, wait_time=3).click()

    @allure.step('Переходим на страницу "Профиль и настройки"')
    def click_link_settings(self):
        return self.find_element(locator=PersonalPageLocators.link_settings, wait_time=3).click()

    @allure.step('Переходим на страницу "Мои организации"')
    def click_link_my_organizations(self):
        return self.find_element(locator=PersonalPageLocators.link_my_organizations, wait_time=3).click()
