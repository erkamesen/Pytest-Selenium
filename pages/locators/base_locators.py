from selenium.webdriver.common.by import By


class BaseLocators:

    CART_QUANTITY = (By.CSS_SELECTOR,
                     "span.cart-qty")

    HEADER_LINKS = (By.CSS_SELECTOR,
                    "div.header-links a")
