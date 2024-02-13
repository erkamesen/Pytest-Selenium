import pytest
from pages.homepage import HomePage
from pages.detail_page import DetailPage
import softest


@pytest.mark.usefixtures("setUp")
class TestHomePage(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setUp(self):
        self.homepage = HomePage(self.driver)
        self.detail_page = DetailPage(self.driver)
        self.driver.get(self.BASE_URL)

    def test_community_poll_without_login(self):
        self.driver.get(self.BASE_URL)
        self.homepage.make_poll()
        text = self.homepage.get_poll_warning_text()
        assert text == "Only registered users can vote."

    def test_recently_viewed_products(self):
        self.homepage.click_first_product_link()
        self.driver.get(self.BASE_URL)
        text = self.homepage.get_recently_viewed_product_text()
        assert text == "$25 Virtual Gift Card"

    def test_top_menu_items(self):
        top_menu_items = self.homepage.get_top_menu_items()
        for item in top_menu_items:
            item_text = item.text
            self.soft_assert(self.assertIn,
                             item_text,
                             self.homepage.MENU_ITEMS,
                             "There is no valid item in menu items..!"
                             )

        self.assert_all()

    def test_product_detail_page(self):
        homepage_product_text = self.homepage.get_first_product_text()
        homepage_product_price = self.homepage.get_first_product_price()

        self.homepage.click_first_product_link()

        detail_page_product_text = self.detail_page.\
            get_detail_page_product_text()
        detail_page_product_price = self.detail_page.\
            get_detail_page_product_price()

        self.soft_assert(self.assertEqual,
                         homepage_product_text, detail_page_product_text,
                         "Something different in detail page it must be text")
        self.soft_assert(self.assertEqual,
                         homepage_product_price, detail_page_product_price,
                         "Something different in detail page it must be price")

        self.assert_all()
