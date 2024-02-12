from pages.basepage import BasePage
from pages.locators import SearchPageLocators


class SearchPage(BasePage, SearchPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def make_search(self, word):
        search_box = self.driver.find_element(*self.SEARCH_BOX_INPUT)
        search_box.send_keys(word)

    def click_to_search_button(self):
        self.driver.find_element(*self.SERACH_BUTTON).click()

    def get_search_warning_text(self):
        elem = self.wait_element_visibility(self.SEARCH_RESULT)
        return elem.text.strip()

    def get_searched_product_list(self) -> list:
        return list(map(lambda x: x.text.strip().lower(),
                        self.driver.find_elements(*self.RESULTS)))
