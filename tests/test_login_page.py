import pytest
from pages.homepage import HomePage
from pages.login_page import LoginPage
from ddt import (ddt,
                 data,
                 unpack)
import unittest
from utils.utils import (get_negative_datas,
                         get_positive_datas)

LOGIN_DATA_PATH = "./testdatas/login_datas.csv"


@pytest.mark.usefixtures("setUp")
@ddt
class TestLoginPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setUp(self):
        self.homepage = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.driver.get(self.BASE_URL)
        self.login_page.navigate_to_login_page()

    @data(*get_negative_datas(LOGIN_DATA_PATH))
    @unpack
    def test_invalid_data_login(self, scenario, email, password, expected):
        print(f"Tested User:\nEmail: {email}\nPassword: {password}")
        self.login_page.fill_email_password_fields(email, password)
        self.login_page.click_the_login_button()
        self.assertIn(expected, self.login_page.get_header_links())

    @data(*get_positive_datas(LOGIN_DATA_PATH))
    @unpack
    def test_valid_data_login(self, scenario, email, password, expected):
        print(f"Tested User:\nEmail: {email}\nPassword: {password}")
        self.login_page.fill_email_password_fields(email, password)
        self.login_page.click_the_login_button()
        self.assertIn(expected, self.login_page.get_header_links())
