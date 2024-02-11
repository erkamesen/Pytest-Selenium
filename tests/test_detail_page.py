"""
Test product detail page
"""
import pytest
from pages.homepage import HomePage
from pages.product_detail_page import DetailPage


@pytest.mark.usefixtures("setUp")
class TestProductDetailPage:

    BASE_URL = "https://demowebshop.tricentis.com/"

    def test_add_to_cart_button_adds_product_to_cart(self):
        self.driver.get(self.BASE_URL)
        homepage = HomePage(driver=self.driver)
        product_detail_page = DetailPage(driver=self.driver)
        homepage.click_the_product_that_is_not_gift_card()
        quantity = product_detail_page.get_quantity()
        first_cart_items_count = product_detail_page.get_cart_items_count()

        product_detail_page.click_add_to_cart_button()
        last_cart_items_count = product_detail_page.get_cart_items_count()

        assert (first_cart_items_count +
                quantity) == last_cart_items_count
