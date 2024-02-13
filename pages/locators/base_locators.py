from selenium.webdriver.common.by import By


class BaseLocators:

    CART_QUANTITY = (By.CSS_SELECTOR,
                     "span.cart-qty")
