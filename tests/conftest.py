from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.BASE_URL = "https://demowebshop.tricentis.com/"
    yield driver
    driver.quit()
