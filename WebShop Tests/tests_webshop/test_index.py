from selenium.webdriver.common.by import By 
from pages.homepage import HomePage
from pages.productpage import ProductPage
import pytest

@pytest.mark.usefixtures("setup")
class TestHomePage:


    def test_top_menu_items(self):
        home_page = HomePage(self.driver)
        expected_menu_items = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS", "JEWELRY", "GIFT CARDS"]  
        elements = home_page.get_menu_elements_with_text()
        for element in elements:
            assert element.text in expected_menu_items


        """ 
        platform linux -- Python 3.10.6, pytest-7.3.1, pluggy-0.13.1 -- /usr/bin/python3
        cachedir: .pytest_cache
        rootdir: /home/erkam/Files/Test/pytest-selenium-project/tests_webshop
        plugins: Faker-18.7.0, anyio-3.6.2
        collected 1 item                                                                                                                                                 

        [WDM] - Downloading: 19.2kB [00:00, 9.30MB/s]                                                                                                                     
        PASSED
        """


    def test_click_to_product(self):

        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        expected_URL = home_page.get_expected_url_for_gift_card()
        expected_name = home_page.get_expected_name_for_gift_card()
        expected_price = home_page.get_expected_price_for_gift_card()
        home_page.click_to_gift_card()
        
        fetched_url= product_page.get_fetched_url_for_gift_card()
        fetched_product_name = product_page.get_fetched_product_name_for_gift_card()
        fetched_product_price = product_page.get_fetched_product_price_for_gift_card()

        assert expected_URL == fetched_url 
        assert expected_name == fetched_product_name
        assert expected_price == fetched_product_price


        """
        [WDM] - Downloading: 19.2kB [00:00, 8.45MB/s]                                                                                                                                             
        PASSED
        [WDM] - Downloading: 19.2kB [00:00, 11.4MB/s]                                                                                                                                             
        https://demowebshop.tricentis.com/25-virtual-gift-card $25 Virtual Gift Card 25.00
        PASSED
        """






    