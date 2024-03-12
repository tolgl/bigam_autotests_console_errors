import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.bigam.ru'

    @allure.step('Открываем страницу')
    def go_to_page(self, path):
        return self.driver.get(self.base_url + path)
