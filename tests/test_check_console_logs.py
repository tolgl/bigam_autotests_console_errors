import time

from pages.base_page import BasePage
from pages.form_authorization import FormAuthorizationHelper
from pages.header import HeaderHelper
from pages.personal_page import PersonalPageHelper


class TestCheckConsoleLogs:

    def test_check_console_errors_from_file(self, driver, test_input):
        base_page = BasePage(driver)
        base_page.go_to_page(path=test_input)
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')

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
        header.click_link_personal_account()
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')

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
        header.click_link_personal_account()
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_my_order()
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')

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
        header.click_link_personal_account()
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_favorites()
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')

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
        header.click_link_personal_account()
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_history_product()
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')

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
        header.click_link_personal_account()
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_repairs()
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')

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
        header.click_link_personal_account()
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_reviews()
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')

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
        header.click_link_personal_account()
        personal_page = PersonalPageHelper(driver)
        personal_page.click_link_settings()
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')
