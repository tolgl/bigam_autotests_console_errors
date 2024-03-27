import time

from locators.form_authorization_locators import FormAuthLocators
from pages.base_page import BasePage
from pages.form_authorization import FormAuthorizationHelper
from pages.header import HeaderHelper
from pages.personal_page import PersonalPageHelper


class TestCheckConsoleLogs:

    def test_check_console_errors_from_file_by_physical_person(self, driver, test_input):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_with_password()
        form_auth.filing_field_phone(phone='9201494057')
        form_auth.filing_field_password(password='123456')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_physical_user)
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        base_page.go_to_page(path=test_input)
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])
        print(level_error)
        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_from_file_by_b2b_user(self, driver, test_input):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        base_page.go_to_page(path=test_input)
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_main_personal_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_with_password()
        form_auth.filing_field_phone(phone='9201494057')
        form_auth.filing_field_password(password='123456')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_physical_user)
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        header.click_link_personal_account()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_my_orders_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_with_password()
        form_auth.filing_field_phone(phone='9201494057')
        form_auth.filing_field_password(password='123456')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_physical_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_my_order()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_favorites_personal_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_with_password()
        form_auth.filing_field_phone(phone='9201494057')
        form_auth.filing_field_password(password='123456')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_physical_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_favorites()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_history_product_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_with_password()
        form_auth.filing_field_phone(phone='9201494057')
        form_auth.filing_field_password(password='123456')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_physical_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_history_product()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_repairs_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_with_password()
        form_auth.filing_field_phone(phone='9201494057')
        form_auth.filing_field_password(password='123456')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_physical_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_repairs()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_reviews_personal_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_with_password()
        form_auth.filing_field_phone(phone='9201494057')
        form_auth.filing_field_password(password='123456')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_physical_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_reviews()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_settings_personal_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_with_password()
        form_auth.filing_field_phone(phone='9201494057')
        form_auth.filing_field_password(password='123456')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_physical_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_settings()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_main_personal_page_by_b2b(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        header.click_link_personal_account()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_my_organisation_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_my_organizations()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_my_orders_page_by_b2b(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_my_order()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_favorites_personal_page_by_b2b(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_favorites()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_history_product_page_by_b2b(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_history_product()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_repairs_page_by_b2b(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_repairs()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_reviews_personal_page_by_b2b(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_reviews()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)

    def test_check_console_errors_settings_personal_page_by_b2b(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page(path='')
        base_page.miss_click_on_selection_city()
        header = HeaderHelper(driver)
        header.click_button_auth()
        form_auth = FormAuthorizationHelper(driver)
        form_auth.click_button_login_b2b()
        form_auth.filing_form_auth_b2b_user(email='test_d@test.ru', password='87654321')
        form_auth.click_button_login()
        base_page.wait_invisibility_element(locator=FormAuthLocators.h3_form_auth_b2b_user)
        header.click_link_personal_account()
        # возвращает лог и очищает консоль
        driver.get_log('browser')
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_settings()
        time.sleep(3)
        log = driver.get_log('browser')
        level_error = []
        for error in log:
            level_error.append(error['level'])

        assert (log == []) or ('SEVERE' not in level_error)
