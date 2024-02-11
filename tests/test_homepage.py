import pytest
from pages.homepage import HomePage
from pages.product_detail_page import DetailPage


@pytest.mark.usefixtures("setUp")
class TestHomePage:
    BASE_URL = "https://demowebshop.tricentis.com/"

    @pytest.fixture(autouse=True)
    def class_setUp(self):
        self.homepage = HomePage(self.driver)
        self.product_detail_page = DetailPage(self.driver)

    def test_top_menu_items(self):
        self.driver.get(self.BASE_URL)
        top_menu_items = self.homepage.get_top_menu_items()
        for item in top_menu_items:
            item_text = item.text
            assert item_text in self.homepage.MENU_ITEMS

    def test_product_detail_page(self):
        self.driver.get(self.BASE_URL)

        homepage_product_text = self.homepage.get_first_product_text()
        homepage_product_price = self.homepage.get_first_product_price()

        self.homepage.click_first_product_link()

        detail_page_product_text = self.product_detail_page.\
            get_detail_page_product_text()
        detail_page_product_price = self.product_detail_page.\
            get_detail_page_product_price()

        assert homepage_product_text == detail_page_product_text
        assert homepage_product_price == detail_page_product_price
