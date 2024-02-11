import pytest
from pages.homepage import HomePage
from pages.product_detail_page import DetailPage


@pytest.mark.usefixtures("setUp")
class TestHomePage:
    BASE_URL = "https://demowebshop.tricentis.com/"

    def test_top_menu_items(self):
        self.driver.get(self.BASE_URL)
        homepage = HomePage(driver=self.driver)
        top_menu_items = homepage.get_top_menu_items()

        for item in top_menu_items:
            item_text = item.text
            assert item_text in homepage.MENU_ITEMS

    def test_product_detail_page(self):
        self.driver.get(self.BASE_URL)
        homepage = HomePage(driver=self.driver)
        product_detail_page = DetailPage(driver=self.driver)

        homepage_product_text = homepage.get_first_product_text()
        homepage_product_price = homepage.get_first_product_price()

        homepage.click_first_product_link()

        detail_page_product_text = product_detail_page.\
            get_detail_page_product_text()
        detail_page_product_price = product_detail_page.\
            get_detail_page_product_price()

        assert homepage_product_text == detail_page_product_text
        assert homepage_product_price == detail_page_product_price
