from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class PageBase:

    def __init__(self, driver):
        self.driver = driver

    TOP_MENU_ELEMENTS = (By.CSS_SELECTOR, "ul.top-menu > li > a")

    def get_menu_elements_with_text(self) -> list:
        return self.driver.find_elements(*PageBase.TOP_MENU_ELEMENTS)     

    def wait_element_visibility(self, locator):
        elem = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator=locator))
        return elem
    

    def wait_element_presence(self, locator):
        elem = WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator=locator))
        return elem
    

    def wait_alert_presence(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())