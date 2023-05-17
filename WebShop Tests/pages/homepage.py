from selenium.webdriver.common.by import By
from pages.PageBase import PageBase

class HomePage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    GIFT_CARD_NAME = (By.CSS_SELECTOR, "div.product-item h2 a")
    GIFT_CARD_PRICE = ( By.CSS_SELECTOR, "span.price.actual-price")
    GIFT_CARD_URL = "https://demowebshop.tricentis.com/25-virtual-gift-card"
    LAPTOP_NAME = (By.CSS_SELECTOR, "div.item-box:nth-child(3) > div:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)")


    def click_to_laptop_product(self):
        elem = self.wait_element_visibility(locator=HomePage.LAPTOP_NAME)
        elem.click()

    def get_expected_url_for_gift_card(self):
        return HomePage.GIFT_CARD_URL

    def get_expected_name_for_gift_card(self):
        return self.driver.find_element(*HomePage.GIFT_CARD_NAME).text

    def get_expected_price_for_gift_card(self):
        return self.driver.find_element(*HomePage.GIFT_CARD_PRICE).text

    def click_to_gift_card(self):
        elem = self.wait_element_visibility(locator=HomePage.GIFT_CARD_NAME)
        elem.click()

  
