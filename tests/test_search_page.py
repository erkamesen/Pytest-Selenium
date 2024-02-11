import pytest
from pages.search_page import SearchPage
from pages.homepage import HomePage
from ddt import (ddt,
                 data,
                 unpack)
import unittest
from utils.utils import (get_negative_datas,
                         get_positive_datas)


SEARCH_DATA_PATH = "./testdatas/search_datas.csv"


@pytest.mark.usefixtures("setUp")
@ddt
class TestSearchPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setUp(self):
        self.homepage = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.driver.get(self.BASE_URL)

    @data(*get_negative_datas(SEARCH_DATA_PATH))
    @unpack
    def test_negative_scenario_search(self, scenario, word, expected_message):
        self.search_page.make_search(word=word)
        self.search_page.click_to_search_button()

        warning = self.search_page.get_search_warning_text()

        assert warning == expected_message

    @data(*get_positive_datas(SEARCH_DATA_PATH))
    @unpack
    def test_positive_scenario_search(self, scenario, word, expected_message):
        self.search_page.make_search(word=word)
        self.search_page.click_to_search_button()

        result_list = self.search_page.get_searched_product_list()

        for result in result_list:
            self.assertIn(word.lower(), result)
