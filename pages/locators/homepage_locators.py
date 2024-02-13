from selenium.webdriver.common.by import By
from pages.locators.base_locators import BaseLocators


class HomePageLocators(BaseLocators):

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

    FIRST_POLL_ANSWER = (By.CSS_SELECTOR,
                         "li.answer input[value='1']")

    POLL_BUTTON = (By.CSS_SELECTOR,
                   "div.buttons input[value='Vote']")

    POLL_ERROR = (By.ID,
                  "block-poll-vote-error-1")

    RECENTLY_VIEWED_ITEM = (
        By.CSS_SELECTOR,
        "div.block-recently-viewed-products a.product-name")
