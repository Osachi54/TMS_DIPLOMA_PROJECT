from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Tuple
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: Tuple, time: int = 10) -> WebElement:
        ignored_exceptions = (StaleElementReferenceException,)
        return WebDriverWait(self.driver, time, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: Tuple, time: int = 10) -> List:
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def switch_to_frame(self, locator: Tuple):
        iframe = self.find_element(locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_current_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def move_to_element(self, web_elem: WebElement) -> None:
        ActionChains(self.driver).move_to_element(web_elem).perform()

    def check_absence_element(self, locator, time=5) -> None:
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def click_with_javascript(self, web_element: WebElement) -> None:
        self.driver.execute_script("arguments[0].click();", web_element)

    def move_to_element_vs_JS(self, web_element: WebElement, locator: Tuple) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

