from selenium.webdriver.common.by import By
from pages.locators.base_locators import BaseLocators


class SearchPageLocators(BaseLocators):

    SEARCH_BOX_INPUT = (By.CSS_SELECTOR,
                        "input[name='q']")
    SERACH_BUTTON = (By.CSS_SELECTOR,
                     "input.button-1.search-box-button")

    SEARCH_RESULT = (By.CSS_SELECTOR,
                     "div.search-results")

    RESULTS = (By.CSS_SELECTOR,
               "div.product-item h2 a")
