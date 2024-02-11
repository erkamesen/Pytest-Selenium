from selenium.webdriver.common.by import By


class HomePage:
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
        self.driver = driver

    def get_top_menu_items(self) -> list:
        return self.driver.find_elements(*self.TOP_MENU_ITEMS)

    def click_the_product_that_is_not_gift_card(self):
        self.driver.find_element(
            *self.FIRST_PRODUCT_THAT_IS_NOT_GIFT_CARD
        ).click()

    def get_first_product_link(self) -> object:
        return self.driver.find_element(
            *self.FIRST_PRODUCT_LINK)

    def get_first_product_text(self) -> str:
        return self.get_first_product_link().text

    def get_first_product_price(self) -> str:
        return self.driver.find_element(
            *self.FIRST_PRODUCT_PRICE).text

    def click_first_product_link(self):
        self.get_first_product_link().click()
