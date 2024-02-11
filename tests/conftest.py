import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


@pytest.fixture(scope="class")
def setUp(request, browser, headless_mode):
    match browser:
        case "chrome":
            options = webdriver.ChromeOptions()
            if headless_mode:
                options.add_argument("--headless")
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
        case "firefox":
            options = webdriver.FirefoxOptions()
            if headless_mode:
                options.add_argument("--headless")
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        case _:
            options = webdriver.ChromeOptions()
            if headless_mode:
                options.add_argument("--headless")
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

    driver.maximize_window()
    request.cls.driver = driver
    request.cls.BASE_URL = "https://demowebshop.tricentis.com/"
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", help="Please enter chrome or firefox")
    parser.addoption("--headless", action="store_true",
                     help="Run tests in headless mode")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def headless_mode(request):
    return request.config.getoption("--headless")
