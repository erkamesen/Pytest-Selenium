from selenium.webdriver.common.by import By
import time
from pages.basepage import BasePage


class DetailPage(BasePage):

    CART_QUANTITY = (By.CSS_SELECTOR,
                     "span.cart-qty")

    ADD_QUANTITY = (By.ID,
                    "addtocart_31_EnteredQuantity")

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button-31")

    PRODUCT_PRICE = (By.CSS_SELECTOR,
                     "span.price-value-2")

    PRODUCT_TEXT = (By.CSS_SELECTOR,
                    "div.product-name > h1")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_cart_items_count(self):
        return int(self.driver.find_element(*self.CART_QUANTITY
                                            ).text[1:-1])

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
