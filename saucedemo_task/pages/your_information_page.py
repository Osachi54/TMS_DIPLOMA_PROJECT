from saucedemo_task.base_pagee import BasePage
from saucedemo_task.locators import your_information_page_locators


class YOUR_INFORMATION_PAGE(BasePage):

    def enter_first_name(self, name):
        elem = self.find_element(your_information_page_locators.FIRST_NAME)
        elem.send_keys(name)
    def enter_last_name(self, name):
        elem = self.find_element(your_information_page_locators.LAST_NAME)
        elem.send_keys(name)
    def enter_postal_code(self, code):
        elem = self.find_element(your_information_page_locators.POSTAL_CODE)
        elem.send_keys(code)
    def click_on_continue_button(self):
        self.find_element(your_information_page_locators.CONTINUE_BUTTON).click()
