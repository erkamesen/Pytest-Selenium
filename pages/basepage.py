from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    BASE_URL = "https://demowebshop.tricentis.com/"

    def __init__(self, driver):
        self.driver = driver

    def wait_element_visibility(self, locator) -> object:
        """Wait for given locator element s visibility and return it."""
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_element_presence(self, locator) -> object:
        """Wait for given locator element s presence and return it."""
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(locator))

    def wait_alert_presence(self, locator) -> object:
        """Wait for alert"""
        WebDriverWait(self.driver, 20).until(
            expected_conditions.alert_is_present()
        )

    def get_cart_items_count(self):
        return int(self.driver.find_element(*self.CART_QUANTITY
                                            ).text[1:-1])
