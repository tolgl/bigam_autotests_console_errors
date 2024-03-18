from selenium.webdriver.common.by import By


class PersonalPageLocators:
    link_my_order = (By.XPATH, ".//a[@href='/personal/orders/']")
    link_favorites = (By.XPATH, ".//a[@href='/personal/favorites/']")
    link_history_product = (By.XPATH, ".//a[@href='/personal/history/']")
    link_repairs = (By.XPATH, ".//a[@href='/personal/repairs/']")
    link_reviews = (By.XPATH, ".//a[@href='/personal/reviews/']")
    link_settings = (By.XPATH, ".//a[@href='/personal/settings/']")
    link_my_organizations = (By.XPATH, ".//a[@href='/personal/organizations/']")
