from saucedemo_task.base_pagee import BasePage
from saucedemo_task.locators import product_page_locators


class Product_page(BasePage):

    def add_last_two_items_to_cart(self):
        elements = self.find_elements(product_page_locators.LIST_OF_PRODUCTS_ADD_BUTTONS)
        elements[-1].click()
        elements[-2].click()

    def click_on_curt_button(self):
        self.find_element(product_page_locators.CART_BUTTON).click()

    def name_of_lust_product(self):
        elements = self.find_elements(product_page_locators.LIST_OF_PRODUCTS_NAMES)
        return elements[-1].text
    def name_of_penultimate_product(self):
        elements = self.find_elements(product_page_locators.LIST_OF_PRODUCTS_NAMES)
        return elements[-2].text
