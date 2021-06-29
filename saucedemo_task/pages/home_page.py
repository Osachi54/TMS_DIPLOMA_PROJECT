from saucedemo_task.base_pagee import BasePage
from saucedemo_task.locators import home_page_locators
class Home_page(BasePage):
    def enter_login_and_password(self, login: str, password: str):
        login_element = self.find_element(home_page_locators.LOGIN)
        login_element.click()
        login_element.send_keys(login)
        password_element = self.find_element(home_page_locators.PASSWORD)
        password_element.click()
        password_element.send_keys(password)

    def click_to_LoginButton(self):
        element = self.find_element(home_page_locators.LOGIN_BUTTON)
        element.click()