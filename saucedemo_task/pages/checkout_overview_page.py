from saucedemo_task.base_pagee import BasePage
from saucedemo_task.locators.checkout_overview_page_locators import FINISH_BUTTON


class Checkout_page(BasePage):

    def click_finish_button(self):
        self.find_element(FINISH_BUTTON).click()
