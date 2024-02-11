from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class HomePage(BasePage):
    MENU_ITEMS = [
        "BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES",
        "DIGITAL DOWNLOADS", "JEWELRY", "GIFT CARDS"
    ]

    TOP_MENU_ITEMS = (By.CSS_SELECTOR,
                      "ul.top-menu > li > a")
    FIRST_PRODUCT_LINK = (By.CSS_SELECTOR,
                          "h2.product-title > a")

    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR,
                           "span.actual-price")

    FIRST_PRODUCT_THAT_IS_NOT_GIFT_CARD = (
        By.XPATH,
        "//div[@class='item-box']//h2/a[not(contains(text(), \
                'Gift Card'))]"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_top_menu_items(self) -> list:
        return self.driver.find_elements(*self.TOP_MENU_ITEMS)

    def click_the_product_that_is_not_gift_card(self):
        profuct_that_is_not_gift_card = self.wait_element_visibility(
            self.FIRST_PRODUCT_THAT_IS_NOT_GIFT_CARD
        )
        profuct_that_is_not_gift_card.click()

    def get_first_product_link(self) -> object:
        return self.driver.find_element(
            *self.FIRST_PRODUCT_LINK)

    def get_first_product_text(self) -> str:
        return self.get_first_product_link().text

    def get_first_product_price(self) -> str:
        return self.driver.find_element(
            *self.FIRST_PRODUCT_PRICE).text

    def click_first_product_link(self):
        first_product = self.wait_element_visibility(
            self.FIRST_PRODUCT_LINK
        )
        first_product.click()
