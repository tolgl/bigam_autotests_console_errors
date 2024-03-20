from selenium.webdriver.common.by import By


class BasePageLocators:
    modal_geo = (By.CLASS_NAME, "a-confirm-city-modal-content")
    miss_click = (By.CLASS_NAME, "vm--overlay")
    loader = (By.CLASS_NAME, "a-local-loader")
