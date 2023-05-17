from selenium.webdriver.common.by import By
import pytest
import time
from pages.homepage import HomePage
from pages.productpage import ProductPage


@pytest.mark.usefixtures("setup")
class TestProduct:

    def test_add_to_cart_button_adds_product_to_cart(self):
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        self.driver.get("https://demowebshop.tricentis.com/")
        home_page.click_to_laptop_product()
        first_shopping_cart_count = product_page.get_shopping_cart_count()
        quantity = product_page.get_quantity_from_value()
        product_page.click_add_to_cart_button()
        time.sleep(1)

        secondary_shopping_cart_count = product_page.get_shopping_cart_count()

        assert secondary_shopping_cart_count == (
            first_shopping_cart_count + quantity)

        """
        $ pytest -v test_product.py

        platform linux -- Python 3.10.6, pytest-7.3.1, pluggy-0.13.1 -- /usr/bin/python3
        cachedir: .pytest_cache
        rootdir: /home/erkam/Files/Test/pytest-selenium-project/tests_webshop
        plugins: Faker-18.7.0, anyio-3.6.2
        collected 1 item                                                                                                                                                                         

        test_product.py::TestProduct::test_add_to_cart_button_adds_product_to_cart PASSED                                                                                                  [100%]

        """
