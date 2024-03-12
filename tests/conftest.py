import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# костыль для параметризации с тестовыми данными из файла
def pytest_generate_tests(metafunc):
    # Пропускаем все функции, у которых нет аргумента test_input
    if 'test_input' not in metafunc.fixturenames:
        return
    # Читаем файл
    url = open('urls.txt', 'r').read().splitlines()

    return metafunc.parametrize("test_input", url)
