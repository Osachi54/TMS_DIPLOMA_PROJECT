from saucedemo_task.base_pagee import BasePage
from saucedemo_task.locators import cart_page_locators
class Cart_page(BasePage):

    def first_item_in_cart(self):
        elements = self.find_elements(cart_page_locators.CART_ITEMS_NAMES)
        return elements[0]
    def second_item_in_cart(self):
        elements = self.find_elements(cart_page_locators.CART_ITEMS_NAMES)
        return elements[1]
    def remove_product_from_cart(self, name_of_product):
        elem = self.find_element(cart_page_locators.remove_button_of_selected_item(name_of_product=name_of_product))
        elem.click()
    def list_of_items(self):
        elements = self.find_elements(cart_page_locators.CART_ITEMS_NAMES)
        return elements
    def click_checkout_button(self):
        self.find_element(cart_page_locators.CHECKOUT_BUTTON).click()