from saucedemo_task.base_pagee import BasePage
from saucedemo_task.locators import finished_order_page_locators

class Finished_order_page(BasePage):
    def get_checkout_header_text(self):
        text = self.find_element(finished_order_page_locators.CHECKOUT_HEADER).text
        return text
    def click_back_home_button(self):
        self.find_element(finished_order_page_locators.BACK_HOME_BUTTON).click()