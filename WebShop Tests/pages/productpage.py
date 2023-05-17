from selenium.webdriver.common.by import By
from pages.PageBase import PageBase
import re


class ProductPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    SHOPPING_CART_COUNT = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[3]/a/span[2]")
    QUANTITY_TAG = (By.XPATH, '//*[@id="addtocart_31_EnteredQuantity"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button-31")
    GIFT_CARD_NAME = (By.CSS_SELECTOR, "div.product-name > h1")
    GIFT_CARD_PRICE = (By.CSS_SELECTOR, ".price-value-2")

    def get_shopping_cart_count(self):
        shopping_cart_count = self.driver.find_element(*ProductPage.SHOPPING_CART_COUNT).text
        return int(re.findall(r'\d+', shopping_cart_count)[0])

    def get_quantity_from_value(self):
        return int(self.driver.find_element(*ProductPage.QUANTITY_TAG).get_attribute("value"))

    def click_add_to_cart_button(self):
        elem = self.wait_element_visibility(locator=ProductPage.ADD_TO_CART_BUTTON)
        elem.click()
        
    def get_fetched_url_for_gift_card(self):
        return self.driver.current_url

    def get_fetched_product_name_for_gift_card(self):
        return self.driver.find_element(*ProductPage.GIFT_CARD_NAME).text

    def get_fetched_product_price_for_gift_card(self):
        return self.driver.find_element(*ProductPage.GIFT_CARD_PRICE).text
