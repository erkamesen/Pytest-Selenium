from selenium.webdriver.common.by import By
from pages.locators.base_locators import BaseLocators


class DetailPageLocators(BaseLocators):

    ADD_QUANTITY = (By.ID,
                    "addtocart_31_EnteredQuantity")

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button-31")

    PRODUCT_PRICE = (By.CSS_SELECTOR,
                     "span.price-value-2")

    PRODUCT_TEXT = (By.CSS_SELECTOR,
                    "div.product-name > h1")
