from pages.locators import DetailPageLocators
import time
from pages.basepage import BasePage


class DetailPage(BasePage, DetailPageLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def get_quantity(self):
        return int(self.driver.find_element(
            *self.ADD_QUANTITY).get_attribute("value"))

    def click_add_to_cart_button(self):
        add_to_cart_button = self.wait_element_visibility(
            self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        time.sleep(1.5)  # wait for cart increase

    def get_detail_page_product_price(self) -> str:
        return self.driver.find_element(
            *self.PRODUCT_PRICE
        ).text

    def get_detail_page_product_text(self) -> str:
        return self.driver.find_element(
            *self.PRODUCT_TEXT
        ).text
