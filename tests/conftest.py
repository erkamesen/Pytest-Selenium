from pathlib import Path
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import datetime
# import getpass


@pytest.fixture(scope="class")
def setUp(request, browser, headless_mode, environment):
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

    if not environment:
        base_url = "https://demowebshop.tricentis.com/"  # Change Here
    elif environment == "dev":
        base_url = "https://dev-demowebshop.tricentis.com/"

    elif environment == "qa":
        base_url = "https://qa-demowebshop.tricentis.com/"

    elif environment == "test":
        base_url = "https://test-demowebshop.tricentis.com/"

    elif environment == "prod":
        base_url = "https://demowebshop.tricentis.com/"

    driver.maximize_window()
    request.cls.driver = driver
    request.cls.BASE_URL = base_url
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", help="Please enter chrome or firefox")
    parser.addoption("--headless", action="store_true",
                     help="Run tests in headless mode")
    parser.addoption("--env", help="Please enter chrome or firefox")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def headless_mode(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="session", autouse=True)
def environment(request):
    return request.config.getoption("--env")


def pytest_html_report_title(report):
    report.title = "Test Automation Report"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.datetime.now()

    report_folder = Path('reports', today.strftime("%Y-%m-%d"))  # Foldername
    report_folder.mkdir(parents=True, exist_ok=True)

    report = report_folder / \
        f"report_{today.strftime('%H-%M')}.html"  # Filename
    config.option.htmlpath = report
    config.option.self_contained_html = True


# @pytest.fixture(scope="session", autouse=True)
# def configure_html_report_env(request, environment, browser):
#     request.config._metadata.update(
#         {
#             "user": getpass.getuser(),
#             "environment": environment,
#             "browser": browser,
#         }
#     )
