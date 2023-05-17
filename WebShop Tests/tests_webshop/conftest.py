from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    # Adds the driver attribute to the class that uses this fixture
    request.cls.driver = driver
    yield
    driver.quit()
