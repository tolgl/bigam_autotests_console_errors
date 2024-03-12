import time

from pages.base_page import BasePage


class TestCheckConsoleLogs:

    def test_check_console_errors_from_file(self, driver, test_input):
        base_page = BasePage(driver)
        base_page.go_to_page(path=test_input)
        time.sleep(3)
        log = driver.get_log('browser')

        assert (log == []) or (log[0]['level'] != 'SEVERE')
