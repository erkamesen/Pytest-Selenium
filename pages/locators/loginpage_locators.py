from selenium.webdriver.common.by import By
from pages.locators.base_locators import BaseLocators


class LoginPageLocators(BaseLocators):

    HEADER_LOGIN = (
        By.CSS_SELECTOR,
        "a.ico-login"
    )

    HEADER_LOGOUT = (
        By.CSS_SELECTOR,
        "a.ico-logout"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input.login-button"
    )

    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "input[name='Email']"
    )

    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "input[name='Password']"
    )
