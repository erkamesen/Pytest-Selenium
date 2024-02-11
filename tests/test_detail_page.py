"""
Test product detail page
"""
import pytest
from pages.homepage import HomePage
from pages.product_detail_page import DetailPage


@pytest.mark.usefixtures("setUp")
class TestProductDetailPage:

    @pytest.fixture(autouse=True)
    def class_setUp(self):
        self.homepage = HomePage(self.driver)
        self.product_detail_page = DetailPage(self.driver)

    def test_add_to_cart_button_add_products_to_cart(self):
        self.driver.get(self.BASE_URL)

        self.homepage.click_the_product_that_is_not_gift_card()
        quantity = self.product_detail_page.get_quantity()
        first_cart_items_count = self.product_detail_page.\
            get_cart_items_count()

        self.product_detail_page.click_add_to_cart_button()
        last_cart_items_count = self.product_detail_page.get_cart_items_count()

        assert (first_cart_items_count +
                quantity) == last_cart_items_count
