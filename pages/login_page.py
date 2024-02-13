import time
from pages.locators import LoginPageLocators
from pages.basepage import BasePage


class LoginPage(BasePage, LoginPageLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_links(self) -> list[str]:
        return list(map(lambda x: x.text,
                        self.driver.find_elements(*self.HEADER_LINKS)))

    def navigate_to_login_page(self):
        self.driver.find_element(*self.HEADER_LOGIN).click()

    def fill_email_password_fields(self, email, password):
        email_field = self.driver.find_element(*self.EMAIL_INPUT)
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)

        email_field.send_keys(email)
        password_field.send_keys(password)

    def click_the_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(1)
